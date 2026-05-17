import argparse
from pathlib import Path

import pandas as pd


RAW_TO_STD = {
    "股票代码": "stock_id",
    "日期": "date",
    "开盘": "open",
    "收盘": "close",
    "最高": "high",
    "最低": "low",
    "成交量": "volume",
    "成交额": "amount",
    "振幅": "amplitude",
    "涨跌额": "change_amount",
    "换手率": "turnover_rate",
    "涨跌幅": "pct_change",
}

NUMERIC_COLUMNS = [
    "open",
    "close",
    "high",
    "low",
    "volume",
    "amount",
    "amplitude",
    "change_amount",
    "turnover_rate",
    "pct_change",
]

FEATURE_COLUMNS = [
    "ret_1d",
    "ret_3d",
    "ret_5d",
    "ret_10d",
    "mom_5d",
    "mom_10d",
    "intraday_return",
    "range_pct",
    "close_to_high",
    "close_to_low",
    "close_to_ma_5d",
    "close_to_ma_10d",
    "close_to_ma_20d",
    "volatility_5d",
    "volatility_10d",
    "volatility_20d",
    "volatility_ratio_5_10",
    "volatility_ratio_10_20",
    "volume_change_1d",
    "volume_change_5d",
    "volume_ratio_5d",
    "volume_ratio_10d",
    "amount_change_1d",
    "amount_ratio_5d",
    "turnover_mean_5d",
    "turnover_mean_10d",
    "turnover_mean_20d",
    "turnover_change_1d",
    "turnover_ratio_5d",
    "turnover_ratio_10d",
    "amplitude_mean_5d",
    "amplitude_mean_10d",
    "amplitude_ratio_5d",
    "amplitude_change_1d",
    "risk_adjusted_mom_5d",
    "risk_adjusted_mom_10d",
    "rank_ret_1d",
    "rank_ret_5d",
    "rank_mom_5d",
    "rank_close_to_ma_10d",
    "rank_turnover_rate",
    "rank_volume_change_1d",
    "rank_volatility_5d",
    "rank_volatility_20d",
    "rank_amount_ratio_5d",
    "rel_ret_1d",
    "rel_ret_5d",
    "rel_mom_10d",
    "rank_rel_ret_5d",
    "consecutive_up_days",
    "consecutive_down_days",
    "positive_day_ratio_10d",
    "negative_day_ratio_10d",
    "volatility_ratio_5_20",
    "volatility_state_change_5d",
    "volatility_regime_rank",
    "rel_hs300_mean_ret_1d",
    "rel_hs300_mean_ret_5d",
    "rel_hs300_mean_mom_10d",
    "rel_cs_mean_close_to_ma_10d",
    "distance_to_20d_high",
    "rebound_from_10d_low",
    "breakout_streak_20d",
    "drawdown_recovery_ratio_10d",
    "turnover_spike_5d",
    "rank_volume_change_5d",
    "volume_price_divergence_5d",
    "crowding_risk_5d",
    "volatility_switch_signal",
    "volatility_switch_rank",
    "rel_strength_accel_5d",
    "rel_strength_accel_5d_v2",
    "rel_strength_accel_5d_v3a",
    "rel_strength_accel_5d_v3b",
    "rel_strength_accel_5d_v3c",
    "trend_persistence_score_10d",
    "trend_persistence_score_10d_v2",
    "volatility_compression_breakout_20d",
    "crowding_reversal_risk_5d",
]


def compute_signed_streak(series: pd.Series, positive: bool = True) -> pd.Series:
    values = series.fillna(0.0).to_numpy()
    streak = []
    running = 0
    for value in values:
        condition = value > 0 if positive else value < 0
        if condition:
            running += 1
        else:
            running = 0
        streak.append(running)
    return pd.Series(streak, index=series.index, dtype="float64")


def compute_binary_streak(series: pd.Series) -> pd.Series:
    values = series.fillna(0.0).to_numpy()
    streak = []
    running = 0
    for value in values:
        if value > 0:
            running += 1
        else:
            running = 0
        streak.append(running)
    return pd.Series(streak, index=series.index, dtype="float64")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Feature engineering and label construction entrypoint.")
    parser.add_argument("--mode", choices=["train", "predict"], required=True)
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--temp_dir", required=True)
    return parser.parse_args()


def load_and_standardize(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    missing_columns = [column for column in RAW_TO_STD if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns in {csv_path}: {missing_columns}")

    df = df.rename(columns=RAW_TO_STD).copy()
    df["stock_id"] = df["stock_id"].astype(str).str.zfill(6)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isna().any():
        bad_rows = int(df["date"].isna().sum())
        raise ValueError(f"Found {bad_rows} rows with invalid dates in {csv_path}")

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.sort_values(["stock_id", "date"]).reset_index(drop=True)
    return df


def fill_basic_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    filled = df.copy()
    grouped = filled.groupby("stock_id", group_keys=False)

    # Use within-stock forward/back fill first so we preserve each stock's own scale.
    for column in NUMERIC_COLUMNS:
        filled[column] = grouped[column].transform(lambda s: s.ffill().bfill())

    # Remaining missing values are filled conservatively.
    zero_fill_columns = ["volume", "amount", "turnover_rate", "pct_change", "change_amount", "amplitude"]
    price_fill_columns = ["open", "close", "high", "low"]

    for column in zero_fill_columns:
        filled[column] = filled[column].fillna(0.0)

    for column in price_fill_columns:
        filled[column] = filled[column].ffill().bfill()

    return filled


def build_train_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    grouped = out.groupby("stock_id", group_keys=False)
    out["future_open_1"] = grouped["open"].shift(-1)
    out["future_open_5"] = grouped["open"].shift(-5)
    out["target_return"] = (out["future_open_5"] - out["future_open_1"]) / out["future_open_1"]
    return out


def build_predict_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["prediction_date"] = out["date"]
    return out


def add_v2_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    grouped = out.groupby("stock_id", group_keys=False)

    out["ret_1d"] = grouped["close"].pct_change(1)
    out["ret_3d"] = grouped["close"].pct_change(3)
    out["ret_5d"] = grouped["close"].pct_change(5)
    out["ret_10d"] = grouped["close"].pct_change(10)

    out["mom_5d"] = grouped["close"].pct_change(5)
    out["mom_10d"] = grouped["close"].pct_change(10)
    out["intraday_return"] = out["close"] / out["open"] - 1.0
    out["range_pct"] = out["high"] / out["low"] - 1.0
    out["close_to_high"] = out["close"] / out["high"] - 1.0
    out["close_to_low"] = out["close"] / out["low"] - 1.0

    grouped = out.groupby("stock_id", group_keys=False)

    ma_5d = grouped["close"].transform(lambda s: s.rolling(5, min_periods=5).mean())
    ma_10d = grouped["close"].transform(lambda s: s.rolling(10, min_periods=10).mean())
    ma_20d = grouped["close"].transform(lambda s: s.rolling(20, min_periods=20).mean())
    out["close_to_ma_5d"] = out["close"] / ma_5d - 1.0
    out["close_to_ma_10d"] = out["close"] / ma_10d - 1.0
    out["close_to_ma_20d"] = out["close"] / ma_20d - 1.0

    out["volatility_5d"] = grouped["ret_1d"].transform(lambda s: s.rolling(5, min_periods=5).std())
    out["volatility_10d"] = grouped["ret_1d"].transform(lambda s: s.rolling(10, min_periods=10).std())
    out["volatility_20d"] = grouped["ret_1d"].transform(lambda s: s.rolling(20, min_periods=20).std())
    out["volatility_ratio_5_10"] = out["volatility_5d"] / out["volatility_10d"]
    out["volatility_ratio_10_20"] = out["volatility_10d"] / out["volatility_20d"]

    out["volume_change_1d"] = grouped["volume"].pct_change(1)
    out["volume_change_5d"] = grouped["volume"].pct_change(5)
    volume_mean_5d = grouped["volume"].transform(lambda s: s.rolling(5, min_periods=5).mean())
    volume_mean_10d = grouped["volume"].transform(lambda s: s.rolling(10, min_periods=10).mean())
    out["volume_ratio_5d"] = out["volume"] / volume_mean_5d - 1.0
    out["volume_ratio_10d"] = out["volume"] / volume_mean_10d - 1.0
    out["amount_change_1d"] = grouped["amount"].pct_change(1)
    amount_mean_5d = grouped["amount"].transform(lambda s: s.rolling(5, min_periods=5).mean())
    out["amount_ratio_5d"] = out["amount"] / amount_mean_5d - 1.0

    out["turnover_mean_5d"] = grouped["turnover_rate"].transform(lambda s: s.rolling(5, min_periods=5).mean())
    out["turnover_mean_10d"] = grouped["turnover_rate"].transform(lambda s: s.rolling(10, min_periods=10).mean())
    out["turnover_mean_20d"] = grouped["turnover_rate"].transform(lambda s: s.rolling(20, min_periods=20).mean())
    out["turnover_change_1d"] = grouped["turnover_rate"].pct_change(1)
    out["turnover_ratio_5d"] = out["turnover_rate"] / out["turnover_mean_5d"] - 1.0
    out["turnover_ratio_10d"] = out["turnover_rate"] / out["turnover_mean_10d"] - 1.0

    out["amplitude_mean_5d"] = grouped["amplitude"].transform(lambda s: s.rolling(5, min_periods=5).mean())
    out["amplitude_mean_10d"] = grouped["amplitude"].transform(lambda s: s.rolling(10, min_periods=10).mean())
    out["amplitude_ratio_5d"] = out["amplitude"] / out["amplitude_mean_5d"] - 1.0
    out["amplitude_change_1d"] = grouped["amplitude"].pct_change(1)

    out["risk_adjusted_mom_5d"] = out["mom_5d"] / (out["volatility_5d"] + 1e-12)
    out["risk_adjusted_mom_10d"] = out["mom_10d"] / (out["volatility_10d"] + 1e-12)

    market_ret_1d = out.groupby("date")["ret_1d"].transform("median")
    market_ret_5d = out.groupby("date")["ret_5d"].transform("median")
    market_mom_10d = out.groupby("date")["mom_10d"].transform("median")
    out["rel_ret_1d"] = out["ret_1d"] - market_ret_1d
    out["rel_ret_5d"] = out["ret_5d"] - market_ret_5d
    out["rel_mom_10d"] = out["mom_10d"] - market_mom_10d

    out["consecutive_up_days"] = grouped["ret_1d"].transform(lambda s: compute_signed_streak(s, positive=True))
    out["consecutive_down_days"] = grouped["ret_1d"].transform(lambda s: compute_signed_streak(s, positive=False))
    out["positive_day_ratio_10d"] = grouped["ret_1d"].transform(
        lambda s: s.gt(0).rolling(10, min_periods=10).mean()
    )
    out["negative_day_ratio_10d"] = grouped["ret_1d"].transform(
        lambda s: s.lt(0).rolling(10, min_periods=10).mean()
    )

    out["volatility_ratio_5_20"] = out["volatility_5d"] / out["volatility_20d"]
    volatility_state_baseline = grouped["volatility_5d"].transform(lambda s: s.rolling(5, min_periods=5).mean())
    out["volatility_state_change_5d"] = out["volatility_5d"] / volatility_state_baseline - 1.0

    out["rank_ret_1d"] = out.groupby("date")["ret_1d"].rank(pct=True)
    out["rank_ret_5d"] = out.groupby("date")["ret_5d"].rank(pct=True)
    out["rank_mom_5d"] = out.groupby("date")["mom_5d"].rank(pct=True)
    out["rank_close_to_ma_10d"] = out.groupby("date")["close_to_ma_10d"].rank(pct=True)
    out["rank_turnover_rate"] = out.groupby("date")["turnover_rate"].rank(pct=True)
    out["rank_volume_change_1d"] = out.groupby("date")["volume_change_1d"].rank(pct=True)
    out["rank_volume_change_5d"] = out.groupby("date")["volume_change_5d"].rank(pct=True)
    out["rank_volatility_5d"] = out.groupby("date")["volatility_5d"].rank(pct=True)
    out["rank_volatility_20d"] = out.groupby("date")["volatility_20d"].rank(pct=True)
    out["rank_amount_ratio_5d"] = out.groupby("date")["amount_ratio_5d"].rank(pct=True)
    out["rank_rel_ret_5d"] = out.groupby("date")["rel_ret_5d"].rank(pct=True)
    out["volatility_regime_rank"] = out.groupby("date")["volatility_ratio_5_20"].rank(pct=True)

    # Alpha v3: relative strength vs HS300 basket proxy, trend persistence, and crowding/risk state.
    hs300_mean_ret_1d = out.groupby("date")["ret_1d"].transform("mean")
    hs300_mean_ret_5d = out.groupby("date")["ret_5d"].transform("mean")
    hs300_mean_mom_10d = out.groupby("date")["mom_10d"].transform("mean")
    cs_mean_close_to_ma_10d = out.groupby("date")["close_to_ma_10d"].transform("mean")
    prev_high_20d = grouped["high"].transform(lambda s: s.shift(1).rolling(20, min_periods=20).max())
    prev_low_10d = grouped["low"].transform(lambda s: s.shift(1).rolling(10, min_periods=10).min())

    out["rel_hs300_mean_ret_1d"] = out["ret_1d"] - hs300_mean_ret_1d
    out["rel_hs300_mean_ret_5d"] = out["ret_5d"] - hs300_mean_ret_5d
    out["rel_hs300_mean_mom_10d"] = out["mom_10d"] - hs300_mean_mom_10d
    out["rel_cs_mean_close_to_ma_10d"] = out["close_to_ma_10d"] - cs_mean_close_to_ma_10d

    out["distance_to_20d_high"] = out["close"] / prev_high_20d - 1.0
    out["rebound_from_10d_low"] = out["close"] / prev_low_10d - 1.0
    breakout_flag_20d = (out["close"] >= prev_high_20d).astype("float64")
    out["breakout_streak_20d"] = breakout_flag_20d.groupby(out["stock_id"]).transform(compute_binary_streak)
    out["drawdown_recovery_ratio_10d"] = out["rebound_from_10d_low"] / (out["distance_to_20d_high"].abs() + 1e-12)

    out["turnover_spike_5d"] = out["turnover_rate"] / (out["turnover_mean_5d"] + 1e-12)
    out["volume_price_divergence_5d"] = out["rank_ret_5d"] - out["rank_volume_change_5d"]
    out["crowding_risk_5d"] = out["turnover_spike_5d"] * (1.0 + out["amplitude_ratio_5d"].clip(lower=0.0))
    out["volatility_switch_signal"] = out["volatility_5d"] - out["volatility_20d"]
    out["volatility_switch_rank"] = out.groupby("date")["volatility_switch_signal"].rank(pct=True)

    # Alpha v4 micro: a compact follow-up bundle aimed at improving slice score
    # without breaking multi-period local return stability.
    rank_rel_hs300_mean_ret_1d = out.groupby("date")["rel_hs300_mean_ret_1d"].rank(pct=True)
    out["rel_strength_accel_5d"] = out["rel_hs300_mean_ret_1d"] - (out["rel_hs300_mean_ret_5d"] / 5.0)
    out["rel_strength_accel_5d_v2"] = (
        0.50 * (rank_rel_hs300_mean_ret_1d - 0.5)
        + 0.30 * (out["rank_rel_ret_5d"] - 0.5)
        + 0.20 * (out["rank_mom_5d"] - 0.5)
    )
    out["rel_strength_accel_5d_v3a"] = (
        0.60 * (out["rank_rel_ret_5d"] - 0.5)
        + 0.25 * (out["rank_mom_5d"] - 0.5)
        + 0.15 * (rank_rel_hs300_mean_ret_1d - 0.5)
    )
    out["rel_strength_accel_5d_v3b"] = (
        0.55 * (out["rank_rel_ret_5d"] - 0.5)
        + 0.25 * (out["rank_mom_5d"] - 0.5)
        + 0.20 * (out["rank_close_to_ma_10d"] - 0.5)
    )
    out["rel_strength_accel_5d_v3c"] = (
        0.45 * out["rel_strength_accel_5d_v2"]
        + 0.35 * (out["rank_rel_ret_5d"] - 0.5)
        + 0.20 * (out["rank_close_to_ma_10d"] - 0.5)
    )
    out["trend_persistence_score_10d"] = (
        out["positive_day_ratio_10d"]
        - out["negative_day_ratio_10d"]
        + 0.05 * (out["consecutive_up_days"] - out["consecutive_down_days"])
    )
    clipped_up = out["consecutive_up_days"].clip(lower=0.0, upper=5.0)
    clipped_down = out["consecutive_down_days"].clip(lower=0.0, upper=5.0)
    out["trend_persistence_score_10d_v2"] = (
        0.50 * (out["positive_day_ratio_10d"] - out["negative_day_ratio_10d"])
        + 0.30 * ((clipped_up - clipped_down) / 5.0)
        + 0.20 * (out["rank_close_to_ma_10d"] - 0.5)
    )
    out["volatility_compression_breakout_20d"] = (
        (1.0 - out["volatility_switch_rank"]) * out["distance_to_20d_high"]
    )
    out["crowding_reversal_risk_5d"] = out["crowding_risk_5d"] * (1.0 - out["rank_ret_5d"])

    cleaned_features = out[FEATURE_COLUMNS].replace([pd.NA, float("inf"), float("-inf")], pd.NA)
    with pd.option_context("future.no_silent_downcasting", True):
        cleaned_features = cleaned_features.fillna(0.0)
    cleaned_features = cleaned_features.infer_objects(copy=False)
    out[FEATURE_COLUMNS] = cleaned_features
    return out


def save_features(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")


def main() -> None:
    args = parse_args()
    data_dir = Path(args.data_dir)
    temp_dir = Path(args.temp_dir)
    temp_dir.mkdir(parents=True, exist_ok=True)

    if args.mode == "train":
        input_path = data_dir / "train.csv"
        output_path = temp_dir / "train_features.csv"

        df = load_and_standardize(input_path)
        df = fill_basic_missing_values(df)
        df = add_v2_features(df)
        features = build_train_features(df)
        usable_rows = int(features["target_return"].notna().sum())
        print(f"[featurework] constructed labels for {usable_rows} train rows")
    else:
        test_path = data_dir / "test.csv"
        output_path = temp_dir / "predict_features.csv"

        # Use the full raw history as feature context when available so long-window
        # features remain meaningful in prediction mode. Only the test-period rows
        # are kept in the final prediction feature file.
        context_path = data_dir / "stock_data.csv"
        input_path = context_path if context_path.exists() else test_path

        context_df = load_and_standardize(input_path)
        context_df = fill_basic_missing_values(context_df)
        context_df = add_v2_features(context_df)

        test_df = load_and_standardize(test_path)
        test_dates = set(test_df["date"].drop_duplicates())
        features = context_df[context_df["date"].isin(test_dates)].copy()
        features = build_predict_features(features)
        features = features.sort_values(["stock_id", "date"]).reset_index(drop=True)
        print(f"[featurework] prepared {len(features)} prediction rows")

    save_features(features, output_path)

    print(f"[featurework] mode={args.mode}")
    print(f"[featurework] input={input_path}")
    print(f"[featurework] output={output_path}")
    print(f"[featurework] rows={len(features)} stocks={features['stock_id'].nunique()}")
    print(
        f"[featurework] date_range={features['date'].min().date()}~"
        f"{features['date'].max().date()}"
    )
    print(f"[featurework] feature_count={len(FEATURE_COLUMNS)}")


if __name__ == "__main__":
    main()
