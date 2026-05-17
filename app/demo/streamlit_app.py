from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st


APP_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = APP_DIR / "model"
DOCS_DIR = APP_DIR / "docs"
FIGURE_DIR = DOCS_DIR / "figures" / "midterm"

BEST_CONFIG_PATH = MODEL_DIR / "best_config.json"
FORMAL_COMPARISON_PATH = MODEL_DIR / "formal_model_comparison" / "formal_model_comparison.csv"
FOLD_STAGE_PATH = MODEL_DIR / "market_regime_analysis" / "fold_stage_performance.csv"
BACKTEST_SUMMARY_PATH = MODEL_DIR / "backtest_summary.csv"
FOLD1_PREDICTIONS_PATH = MODEL_DIR / "fold_1_predictions.csv"
TICKET_SUMMARY_PATH = MODEL_DIR / "fold1_short_term_ticket_summary.csv"
TICKET_DIAGNOSTICS_PATH = MODEL_DIR / "fold1_short_term_ticket_diagnostics.csv"
MODEL_CHART_PATH = DOCS_DIR / "report_supplement_assets" / "formal_model_comparison_chart.png"
FOLD_RANKIC_PATH = FIGURE_DIR / "fig2_fold_rankic.png"
EQUITY_PATH = FIGURE_DIR / "fig3_equity_curve.png"
DRAWDOWN_PATH = FIGURE_DIR / "fig4_drawdown_curve.png"
DIAG_CHART_PATH = FIGURE_DIR / "fig6_ticket_diagnostics.png"


st.set_page_config(
    page_title="沪深300收益预测 Demo",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data(show_spinner=False)
def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def must_load_csv(path: Path, label: str) -> pd.DataFrame:
    if not path.exists():
        st.error(f"缺少文件：{label} - {path}")
        st.stop()
    return load_csv(path)


def must_load_json(path: Path, label: str) -> dict:
    if not path.exists():
        st.error(f"缺少文件：{label} - {path}")
        st.stop()
    return load_json(path)


def format_percent(value: float, digits: int = 2) -> str:
    return f"{value * 100:.{digits}f}%"


def format_number(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def inject_style() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(180deg, #fff8f1 0%, #fff3e8 45%, #fdf7f2 100%);
        }
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
            max-width: 1380px;
        }
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #fff4ea 0%, #ffe7d6 55%, #ffd8bd 100%);
            min-width: 360px !important;
            max-width: 360px !important;
            border-right: 1px solid rgba(217, 119, 6, 0.12);
        }
        section[data-testid="stSidebar"] * {
            color: #6b3f1d !important;
        }
        section[data-testid="stSidebar"] .stCodeBlock,
        section[data-testid="stSidebar"] pre,
        section[data-testid="stSidebar"] code {
            white-space: pre-wrap !important;
            word-break: break-word !important;
            overflow-wrap: anywhere !important;
        }
        section[data-testid="stSidebar"] [data-testid="stCodeBlock"] {
            background: rgba(255, 250, 245, 0.92) !important;
            border: 1px solid rgba(217, 119, 6, 0.16) !important;
            border-radius: 14px !important;
        }
        section[data-testid="stSidebar"] ul {
            padding-left: 1.2rem;
        }
        section[data-testid="stSidebar"] li {
            margin-bottom: 0.45rem;
        }
        .hero {
            padding: 1.6rem 1.8rem;
            border-radius: 18px;
            background: linear-gradient(135deg, #fff2df 0%, #ffd6ae 50%, #ffb77d 100%);
            color: #6b3f1d;
            box-shadow: 0 18px 40px rgba(180, 83, 9, 0.12);
            margin-bottom: 1rem;
            border: 1px solid rgba(217, 119, 6, 0.12);
        }
        .hero h1 {
            margin: 0 0 0.4rem 0;
            font-size: 2rem;
            color: #8a3b12;
        }
        .hero p {
            margin: 0;
            font-size: 1rem;
            line-height: 1.6;
            color: #7c4a24;
        }
        .section-card {
            background: rgba(255, 251, 247, 0.96);
            border: 1px solid rgba(234, 179, 8, 0.14);
            border-radius: 16px;
            padding: 1rem 1rem 0.7rem 1rem;
            box-shadow: 0 10px 28px rgba(180, 83, 9, 0.06);
            margin-bottom: 1rem;
        }
        .section-card h3 {
            color: #8a3b12;
        }
        .mini-note {
            color: #7c5a3b;
            font-size: 0.92rem;
            line-height: 1.6;
        }
        div[data-testid="metric-container"] {
            background: rgba(255, 250, 245, 0.96);
            border: 1px solid rgba(245, 158, 11, 0.18);
            border-radius: 14px;
            padding: 0.75rem 0.85rem;
            box-shadow: 0 8px 24px rgba(180, 83, 9, 0.05);
        }
        .config-chip {
            display: inline-block;
            padding: 0.35rem 0.6rem;
            margin: 0.18rem 0.24rem 0.18rem 0;
            border-radius: 999px;
            background: #ffe8cc;
            color: #9a3412;
            font-size: 0.88rem;
            font-weight: 600;
        }
        .sidebar-card {
            background: rgba(255, 250, 245, 0.88);
            border: 1px solid rgba(217, 119, 6, 0.16);
            border-radius: 14px;
            padding: 0.85rem 0.95rem;
            margin: 0.5rem 0 1rem 0;
            color: #744210;
            line-height: 1.6;
            word-break: break-word;
            overflow-wrap: anywhere;
        }
        .sidebar-kv {
            margin: 0.35rem 0;
            color: #6b3f1d;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.35rem;
        }
        .stTabs [data-baseweb="tab"] {
            background: #fff1e4;
            border-radius: 12px 12px 0 0;
            color: #8a3b12;
            padding: 0.55rem 0.95rem;
        }
        .stTabs [aria-selected="true"] {
            background: #ffd8b4 !important;
            color: #7c2d12 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def normalize_model_table(formal_df: pd.DataFrame) -> pd.DataFrame:
    table = formal_df.copy()
    numeric_cols = [
        "MAE",
        "RMSE",
        "RankIC",
        "NDCG@5",
        "NDCG@10",
        "NDCG@20",
        "HitRate@5",
        "HitRate@10",
        "HitRate@20",
        "Top5平均收益",
        "回测累计收益",
        "Sharpe",
        "最大回撤",
    ]
    for col in numeric_cols:
        if col in table.columns:
            table[col] = pd.to_numeric(table[col], errors="coerce")
    return table


def build_model_table(formal_df: pd.DataFrame) -> pd.DataFrame:
    table = normalize_model_table(formal_df)
    cols = [
        "模型名",
        "模型族",
        "特征集",
        "sequence_length",
        "MAE",
        "RMSE",
        "RankIC",
        "Top5平均收益",
        "回测累计收益",
        "Sharpe",
        "最大回撤",
        "是否正式候选",
        "说明",
    ]
    available = [col for col in cols if col in table.columns]
    return table[available].sort_values(["是否正式候选", "回测累计收益"], ascending=[False, False])


def build_intro_metrics(best_config: dict, formal_df: pd.DataFrame) -> list[tuple[str, str]]:
    table = normalize_model_table(formal_df)
    formal_row = table.loc[table["是否正式候选"] == "是"].iloc[0]
    return [
        ("正式主线", "LSTM sl20"),
        ("特征集", best_config["training"]["feature_set"]),
        ("序列长度", str(best_config["training"]["sequence_length"])),
        ("候选池", str(best_config["selection"]["primary_candidate_size"])),
        ("Top-K", str(best_config["selection"]["top_k"])),
        ("风险惩罚", format_number(float(best_config["risk_filter_thresholds"]["risk_penalty_weight"]), 2)),
        ("正式 RankIC", format_number(float(formal_row["RankIC"]), 4)),
        ("正式回测累计收益", format_percent(float(formal_row["回测累计收益"]), 2)),
    ]


def build_fold_error_table(fold_pred_df: pd.DataFrame) -> pd.DataFrame:
    table = fold_pred_df.copy()
    table["rank_error"] = (table["rank_pred"] - table["rank_true"]).abs()
    grouped = (
        table.groupby("stock_id", as_index=False)
        .agg(
            交易天数=("trade_date", "count"),
            平均真实收益=("y_true", "mean"),
            平均预测值=("y_pred", "mean"),
            平均真实排序=("rank_true", "mean"),
            平均预测排序=("rank_pred", "mean"),
            平均错排幅度=("rank_error", "mean"),
            最大错排幅度=("rank_error", "max"),
        )
        .sort_values(["平均错排幅度", "最大错排幅度"], ascending=[False, False])
    )
    return grouped.head(20)


def render_image(path: Path, caption: str) -> None:
    if path.exists():
        st.image(str(path), caption=caption, use_column_width=True)


def render_sidebar(best_config: dict) -> None:
    with st.sidebar:
        st.markdown("## 展示导航")
        st.markdown(
            "\n".join(
                [
                    "- 项目简介与正式默认方案",
                    "- 模型对比表",
                    "- Walk-forward 分折结果",
                    "- 回测净值与回撤",
                    "- 第 1 折错排股票诊断",
                ]
            )
        )
        st.markdown("---")
        st.markdown("## 正式默认配置")
        st.markdown(
            f'<div class="sidebar-card">{best_config["profile_name"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown("### 关键参数")
        st.markdown(
            f"""
            <div class="sidebar-card">
                <div class="sidebar-kv"><strong>模型：</strong>{best_config["training"]["model_family"]}</div>
                <div class="sidebar-kv"><strong>序列长度：</strong>{best_config["training"]["sequence_length"]}</div>
                <div class="sidebar-kv"><strong>排序策略：</strong>{best_config["selection"]["sort_strategy"]}</div>
                <div class="sidebar-kv"><strong>权重策略：</strong>{best_config["selection"]["weighting_scheme"]}</div>
                <div class="sidebar-kv"><strong>交易成本：</strong>{best_config["execution"]["transaction_cost"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def main() -> None:
    inject_style()

    best_config = must_load_json(BEST_CONFIG_PATH, "正式默认配置")
    formal_df = must_load_csv(FORMAL_COMPARISON_PATH, "正式模型对比表")
    fold_stage_df = must_load_csv(FOLD_STAGE_PATH, "分折阶段分析表")
    backtest_df = must_load_csv(BACKTEST_SUMMARY_PATH, "回测汇总表")
    fold1_df = must_load_csv(FOLD1_PREDICTIONS_PATH, "第一折预测结果")

    render_sidebar(best_config)

    st.markdown(
        """
        <div class="hero">
            <h1>沪深300收益预测与组合推荐演示系统</h1>
            <p>
                面向汇报展示的轻量交互页。当前页面只读取已经完成的模型对比、分折验证、回测结果与诊断产物，
                不现场训练模型，重点呈现正式默认方案的效果、稳定性与可解释分析。
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metrics = build_intro_metrics(best_config, formal_df)
    row1 = st.columns(4)
    row2 = st.columns(4)
    for col, (label, value) in zip(row1, metrics[:4]):
        col.metric(label, value)
    for col, (label, value) in zip(row2, metrics[4:]):
        col.metric(label, value)

    st.markdown(
        """
        <div class="section-card">
            <h3>项目简介与正式默认方案</h3>
            <div class="mini-note">
                当前正式默认方案采用 LSTM sl20 主线，结合 base_alpha_v3_rs_crowding_mini4 特征集，
                以横截面收益排序为目标，通过 risk_adjusted 排序策略和 pred 权重分配生成 Top-K 推荐组合。
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.4, 1])
    with left:
        st.markdown(
            """
            - 任务目标：预测未来一周收益排序并生成 Top-K 推荐组合
            - 正式模型：`LSTM sl20`
            - 训练目标：`cross_section_rank`
            - 排序策略：`risk_adjusted`
            - 权重策略：`pred`
            - 候选池大小：`180`
            - 风险惩罚系数：`-0.30`
            """
        )
        chips = [
            "沪深300",
            "横截面排序",
            "Walk-forward",
            "低换手执行",
            "冻结提交链路",
            "Docker 复现",
        ]
        st.markdown("".join([f'<span class="config-chip">{chip}</span>' for chip in chips]), unsafe_allow_html=True)
    with right:
        st.json(
            {
                "feature_set": best_config["training"]["feature_set"],
                "sequence_length": best_config["training"]["sequence_length"],
                "candidate_size": best_config["selection"]["primary_candidate_size"],
                "top_k": best_config["selection"]["top_k"],
                "risk_penalty_weight": best_config["risk_filter_thresholds"]["risk_penalty_weight"],
                "transaction_cost": best_config["execution"]["transaction_cost"],
            },
            expanded=False,
        )

    tab1, tab2, tab3, tab4 = st.tabs(["模型对比", "分折结果", "回测表现", "错排诊断"])

    with tab1:
        st.markdown("### 正式模型对比")
        st.dataframe(build_model_table(formal_df), use_container_width=True, hide_index=True)
        render_image(MODEL_CHART_PATH, "正式模型对比图")

    with tab2:
        st.markdown("### Walk-forward 分折表现")
        fold_view = fold_stage_df.copy()
        for col in ["RankIC", "Top5平均收益", "回测收益", "胜率", "平均换手"]:
            if col in fold_view.columns:
                fold_view[col] = pd.to_numeric(fold_view[col], errors="coerce")
        st.dataframe(fold_view, use_container_width=True, hide_index=True)
        render_image(FOLD_RANKIC_PATH, "Walk-forward 分折 RankIC")

    with tab3:
        st.markdown("### 回测净值与回撤")
        default_row = backtest_df.loc[backtest_df["profile_name"] == "risk_adjusted"]
        if default_row.empty:
            default_row = backtest_df.head(1)
        default_row = default_row.iloc[0]

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("成本后累计收益", format_percent(float(default_row["cumulative_return_after_cost"])))
        m2.metric("成本后 Sharpe", format_number(float(default_row["sharpe_after_cost"]), 3))
        m3.metric("成本后最大回撤", format_percent(float(default_row["max_drawdown_after_cost"])))
        m4.metric("平均换手", format_number(float(default_row["avg_turnover"]), 3))

        with st.expander("展开查看完整回测汇总表", expanded=False):
            st.dataframe(backtest_df, use_container_width=True, hide_index=True)

        chart_left, chart_right = st.columns(2)
        with chart_left:
            render_image(EQUITY_PATH, "净值曲线")
        with chart_right:
            render_image(DRAWDOWN_PATH, "回撤曲线")

    with tab4:
        st.markdown("### 第 1 折错排股票诊断")
        diag_left, diag_right = st.columns([1.15, 1])
        with diag_left:
            st.markdown("#### 原始错排统计 Top20")
            st.dataframe(build_fold_error_table(fold1_df), use_container_width=True, hide_index=True)
        with diag_right:
            if TICKET_SUMMARY_PATH.exists():
                ticket_summary_df = load_csv(TICKET_SUMMARY_PATH)
                st.markdown("#### 短期特征消融后重点股票摘要")
                st.dataframe(ticket_summary_df, use_container_width=True, hide_index=True)
            else:
                st.info("未找到 fold1_short_term_ticket_summary.csv。")

        if TICKET_DIAGNOSTICS_PATH.exists():
            st.markdown("#### 重点股票逐日诊断")
            ticket_diag_df = load_csv(TICKET_DIAGNOSTICS_PATH)
            stock_options = sorted(ticket_diag_df["stock_id"].astype(str).unique().tolist())
            selected_stock = st.selectbox("选择诊断股票", stock_options, index=0)
            stock_df = ticket_diag_df.loc[ticket_diag_df["stock_id"].astype(str) == selected_stock].copy()
            st.dataframe(stock_df, use_container_width=True, hide_index=True)

        render_image(DIAG_CHART_PATH, "小票诊断图")


if __name__ == "__main__":
    main()
