# Aggressive Score Candidate Stability Review

本报告复核单切片冲分候选是否只是偶然命中，并给出是否同步默认配置的建议。脚本不会覆盖默认配置。

## Candidate

- candidate label: `recent_strength_pred__allow_600115__top6_take5_2__pred_full_cap0.20`
- candidate result: `app\model\case_slice_submission_search\generated_results\recent_strength_pred__allow_600115__top6_take5_2__pred_full_cap0.20.csv`
- stocks: `000792,600233,601669,600930,002463`
- weight sum: `1.000000`
- same-protocol single-slice score: `0.077484`

## Decision

- decision: `aggressive_package_ok; default_sync_requires_manual_confirmation`
- reason: 历史稳定性可接受，但该候选仍是单切片冲分导向，默认配置需要人工确认后再同步。
- default sync: `不建议自动同步 default_submission_config.json`
- current default: 保留已人工确认的 HV rerank/sl20 主线，除非用户明确选择比赛冲分。
- aggressive score package result: `app\model\aggressive_score_submission_candidate\result_aggressive_score.csv`

## Walk-Forward Basket Check

- days: `60`
- cumulative return: `0.604956`
- mean daily return: `0.008225`
- positive rate: `0.633333`
- sharpe: `5.165172`
- max drawdown: `-0.190947`
- worst fold cumulative return: `0.067532`

## Per-Stock Evidence

| stock_id | weight | case_return | case_contribution | wf_mean | wf_positive_rate | wf_min | latest_vol20_pctile | latest_turnover_pctile | false_positive | risk_flags |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `000792` | 0.200000 | 0.080310 | 0.016062 | 0.023894 | 0.650000 | -0.094663 | 0.816667 | 0.670000 | 3 | `large_single_period_loss` |
| `002463` | 0.200000 | 0.046027 | 0.009205 | 0.008299 | 0.516667 | -0.086106 | 0.876667 | 0.853333 | 0 | `large_single_period_loss;latest_volatility_high` |
| `600233` | 0.200000 | 0.039267 | 0.007853 | 0.007742 | 0.566667 | -0.068054 | 0.556667 | 0.343333 | 0 | `ok` |
| `600930` | 0.200000 | 0.057661 | 0.011532 | -0.002971 | 0.416667 | -0.056213 | 0.016667 | 0.906667 | 0 | `wf_mean_nonpositive;wf_positive_rate_low;latest_turnover_high` |
| `601669` | 0.200000 | 0.164154 | 0.032831 | 0.004160 | 0.483333 | -0.055184 | 0.420000 | 0.983333 | 0 | `latest_turnover_high` |

## Fold Basket Evidence

| fold_id | days | mean_return | cumulative_return | positive_rate | max_drawdown |
|---:|---:|---:|---:|---:|---:|
| 1 | 20 | 0.003338 | 0.067532 | 0.600000 | -0.043153 |
| 2 | 20 | 0.012438 | 0.276077 | 0.800000 | -0.054708 |
| 3 | 20 | 0.008899 | 0.178163 | 0.500000 | -0.106790 |

## Regime Evidence

| regime | days | mean_return | cumulative_return | positive_rate | max_drawdown |
|---|---:|---:|---:|---:|---:|
| `high_volatility_range` | 18 | 0.012774 | 0.241973 | 0.555556 | -0.058413 |
| `low_volatility_trend` | 9 | 0.012027 | 0.112154 | 0.666667 | -0.017216 |
| `low_volatility_range` | 31 | 0.006686 | 0.224878 | 0.709677 | -0.040837 |
| `high_volatility_trend` | 2 | -0.025978 | -0.051378 | 0.000000 | -0.016138 |

## Misrank Diagnostic Counts

| stock_id | file | count | poor_return_count | bad_pred_top5_count | mean_target_return |
|---|---|---:|---:|---:|---:|
| `000792` | `false_positives` | 3 | 1 | 0 | 0.057146 |
| `000792` | `misrank_samples` | 2 | 0 | 1 | 0.035353 |
| `000792` | `missed_winners` | 2 | 0 | 0 | 0.126566 |
| `002463` | `false_positives` | 0 | 0 | 0 |  |
| `002463` | `misrank_samples` | 3 | 0 | 0 | 0.170807 |
| `002463` | `missed_winners` | 3 | 0 | 0 | 0.170807 |
| `600233` | `false_positives` | 0 | 0 | 0 |  |
| `600233` | `misrank_samples` | 0 | 0 | 0 |  |
| `600233` | `missed_winners` | 0 | 0 | 0 |  |
| `600930` | `false_positives` | 0 | 0 | 0 |  |
| `600930` | `misrank_samples` | 0 | 0 | 0 |  |
| `600930` | `missed_winners` | 0 | 0 | 0 |  |
| `601669` | `false_positives` | 0 | 0 | 0 |  |
| `601669` | `misrank_samples` | 0 | 0 | 0 |  |
| `601669` | `missed_winners` | 0 | 0 | 0 |  |

## Submit/Sync Rule

- 比赛冲分：可人工选择 aggressive score 包，但要接受它不是默认稳健主线。
- 稳定策略：继续使用当前 HV rerank/sl20 默认结果。
- 默认同步：本轮不自动同步；只有用户明确确认后才可替换 `app/output/result.csv` 和默认配置。
