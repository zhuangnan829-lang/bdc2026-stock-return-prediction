# Feature Set Same-Protocol Comparison

## Required Answers

1. v4_medium 是否真的提升 Top5 收益？否。同协议 `top5_return_mean` 对比见下表。
2. 是否只提升单切片但降低 Walk-forward 稳定性？否。
3. 是否存在明显过拟合？有迹象。判断依据是 RankIC 改善但 after-cost/Sharpe 转化不足。
4. 哪些新增特征可能有效？见 `Potential Feature Signals`，按与真实收益的绝对 Spearman 相关排序。
5. 是否建议 v4_medium 进入下一轮主线或只作为候选？只作为候选继续拆解，不进入主线。

## Adoption Rule

Only retain v4 if at least two of `top5_return_mean`, `worst_fold_rank_ic`, and `sharpe` are not worse than v3, without materially increasing drawdown or turnover.

## Summary

| label | status | rank_ic_mean | worst_fold | top5_mean | top5_min_fold | cost_after | sharpe | mdd | turnover | slice | neg_day_ic | adopt |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| v3_mini4_lstm_sl20 | ok | 0.027982 | -0.033492 | 0.007502 | 0.003244 | 1.085936 | 3.977455 | -0.087064 | 0.931137 | 0.024596 | 0.400000 | False |
| v4_medium_lstm_sl20 | ok | 0.035370 | 0.009668 | 0.006252 | 0.001906 | 0.320973 | 1.980195 | -0.130310 | 0.920797 | 0.025958 | 0.433333 | False |
| v4_medium_lstm_sl40 | missing | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | False |
| v4_medium_lstm_sl60 | missing | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | False |
| v4_medium_lightgbm | missing | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | False |

## Potential Feature Signals

| feature | spearman_to_target | spearman_to_prediction |
|---|---:|---:|
| `reversal_risk_score` | 0.037614 | -0.178877 |
| `amount_ratio_10d` | -0.028454 | -0.106648 |
| `close_position_20d` | 0.026587 | 0.201340 |
| `ret_20d` | 0.021731 | 0.139800 |
| `ret_3d_zscore_cross_section` | 0.020306 | -0.060298 |
| `ret_15d` | 0.014395 | 0.171503 |
| `relative_to_market_10d` | 0.009513 | 0.044967 |
| `volume_spike_zscore` | -0.009466 | -0.089176 |
| `turnover_spike_zscore` | -0.008794 | -0.088188 |
| `ret_2d` | 0.006273 | -0.017364 |
| `close_position_10d` | 0.006192 | 0.108012 |
| `ret_7d` | -0.005660 | 0.022502 |

## Missing Artifacts

- `v4_medium_lstm_sl40`: no_existing_artifact_found
- `v4_medium_lstm_sl60`: no_existing_artifact_found
- `v4_medium_lightgbm`: no_existing_artifact_found
