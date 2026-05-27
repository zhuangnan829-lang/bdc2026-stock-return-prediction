# Misranked Sample Diagnostics

Definitions: `missed_winners` = true Top5 but not model Top5; `false_positives` = model Top5 but not true Top5.

## Required Answers

1. 漏选赢家有什么共同特征？
- `volatility_5d` is higher than fold baseline (mean 0.0420 vs 0.0213, z-gap 1.24).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.1296 vs 0.0534, z-gap 1.10).
- `volatility_20d` is higher than fold baseline (mean 0.0273 vs 0.0175, z-gap 1.03).
- `volatility_20d` is higher than fold baseline (mean 0.0272 vs 0.0179, z-gap 0.95).
- `volatility_20d` is higher than fold baseline (mean 0.0353 vs 0.0228, z-gap 0.95).
- `rel_hs300_mean_ret_5d` is higher than fold baseline (mean 0.0482 vs 0.0000, z-gap 0.92).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.1278 vs 0.0596, z-gap 0.91).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.0850 vs 0.0409, z-gap 0.90).

2. 误选输家是否存在短期过热、放量、换手异常、高波动、长上影等特征？
- 过热/放量/高波动综合 z-gap 均值为 0.13；未形成单一强证据，但仍需结合 Fold 分组观察。
- 反转/位置风险相关 z-gap 均值为 -0.15。

3. 是否应该加入反转保护特征？
- 建议小步验证：false positives 中高波动、换手或位置风险信号偏强时，反转保护有助于抑制追高误选。

4. 是否应该调整 risk penalty 或 candidate filter？
- 建议先保持 candidate filter，优先用诊断特征做排序侧修正；不能直接推翻当前主线。

5. 哪些特征最值得在下一轮加入 base_alpha_v4_medium？
- `volatility_20d`
- `volatility_5d`
- `rebound_from_10d_low`
- `turnover_rate`
- `distance_to_20d_high`
- `rel_hs300_mean_ret_5d`
- `ret_5d`
- `reversal_risk_score`
- `ret_3d`
- `close_position_20d`

## Missing Requested Features

- `volume_ratio`
- `turnover_spike`
- `rel_hs300_ret_5d`

建议新增缺失特征，尤其是 `overheat_score`、`reversal_risk_score`、`close_position_20d` 这类显式风险保护字段。

## Alias Features Used

- volume_ratio -> volume_ratio_5d
- turnover_spike -> turnover_spike_5d
- rel_hs300_ret_5d -> rel_hs300_mean_ret_5d

## Fold Overview

| fold | dates | model_top_ret | true_top_ret | hit_rate | missed | false_pos | poor_false_pos |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 20 | 0.004075 | 0.128325 | 0.020 | 98 | 98 | 45 |
| 2 | 20 | 0.015189 | 0.223324 | 0.020 | 98 | 98 | 39 |
| 3 | 20 | 0.003244 | 0.182866 | 0.030 | 97 | 97 | 48 |

## Fold 1 Feature Gaps

### Missed Winners
- `volatility_20d` is higher than fold baseline (mean 0.0273 vs 0.0175, z-gap 1.03).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.0850 vs 0.0409, z-gap 0.90).
- `volatility_5d` is higher than fold baseline (mean 0.0257 vs 0.0161, z-gap 0.88).
- `turnover_rate` is higher than fold baseline (mean 2.1327 vs 1.1374, z-gap 0.75).
- `reversal_risk_score` is higher than fold baseline (mean 0.6232 vs 0.4445, z-gap 0.57).
- `rel_hs300_mean_ret_5d` is higher than fold baseline (mean 0.0135 vs 0.0000, z-gap 0.35).

### False Positives
- `turnover_rate` is higher than fold baseline (mean 2.5036 vs 1.1374, z-gap 1.04).
- `distance_to_20d_high` is lower than fold baseline (mean -0.1243 vs -0.0716, z-gap -1.01).
- `volatility_20d` is higher than fold baseline (mean 0.0254 vs 0.0175, z-gap 0.82).
- `ret_3d` is lower than fold baseline (mean -0.0099 vs 0.0036, z-gap -0.44).
- `turnover_ratio_10d` is lower than fold baseline (mean -0.1681 vs -0.0091, z-gap -0.41).
- `volume_ratio_10d` is lower than fold baseline (mean -0.1672 vs -0.0086, z-gap -0.41).

## Fold 2 Feature Gaps

### Missed Winners
- `volatility_20d` is higher than fold baseline (mean 0.0272 vs 0.0179, z-gap 0.95).
- `rel_hs300_mean_ret_5d` is higher than fold baseline (mean 0.0482 vs 0.0000, z-gap 0.92).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.1278 vs 0.0596, z-gap 0.91).
- `ret_5d` is higher than fold baseline (mean 0.0607 vs 0.0124, z-gap 0.89).
- `turnover_rate` is higher than fold baseline (mean 3.1063 vs 1.6062, z-gap 0.84).
- `reversal_risk_score` is higher than fold baseline (mean 0.6973 vs 0.4437, z-gap 0.80).

### False Positives
- `volatility_20d` is higher than fold baseline (mean 0.0370 vs 0.0179, z-gap 1.95).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.1312 vs 0.0596, z-gap 0.95).
- `distance_to_20d_high` is lower than fold baseline (mean -0.0817 vs -0.0457, z-gap -0.83).
- `turnover_rate` is higher than fold baseline (mean 3.0771 vs 1.6062, z-gap 0.82).
- `volatility_5d` is higher than fold baseline (mean 0.0287 vs 0.0177, z-gap 0.82).
- `rel_hs300_mean_ret_5d` is lower than fold baseline (mean -0.0350 vs 0.0000, z-gap -0.67).

## Fold 3 Feature Gaps

### Missed Winners
- `volatility_5d` is higher than fold baseline (mean 0.0420 vs 0.0213, z-gap 1.24).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.1296 vs 0.0534, z-gap 1.10).
- `volatility_20d` is higher than fold baseline (mean 0.0353 vs 0.0228, z-gap 0.95).
- `turnover_rate` is higher than fold baseline (mean 2.8544 vs 1.5496, z-gap 0.81).
- `reversal_risk_score` is higher than fold baseline (mean 0.6813 vs 0.4436, z-gap 0.77).
- `close_position_20d` is higher than fold baseline (mean 0.5951 vs 0.4014, z-gap 0.68).

### False Positives
- `volatility_20d` is higher than fold baseline (mean 0.0390 vs 0.0228, z-gap 1.23).
- `volatility_5d` is higher than fold baseline (mean 0.0392 vs 0.0213, z-gap 1.07).
- `distance_to_20d_high` is lower than fold baseline (mean -0.1369 vs -0.0796, z-gap -0.97).
- `turnover_rate` is higher than fold baseline (mean 2.7581 vs 1.5496, z-gap 0.75).
- `rebound_from_10d_low` is higher than fold baseline (mean 0.1046 vs 0.0534, z-gap 0.74).
- `reversal_risk_score` is higher than fold baseline (mean 0.6060 vs 0.4436, z-gap 0.52).

## Weakest Dates

| fold | date | model_top_ret | true_top_ret | hit_rate | missed | false_pos |
|---:|---|---:|---:|---:|---:|---:|
| 3 | 2026-02-25 | -0.049647 | 0.251580 | 0.000 | 5 | 5 |
| 3 | 2026-01-27 | -0.044556 | 0.113146 | 0.000 | 5 | 5 |
| 2 | 2026-01-06 | -0.040822 | 0.336918 | 0.000 | 5 | 5 |
| 2 | 2026-01-15 | -0.035797 | 0.245273 | 0.000 | 5 | 5 |
| 1 | 2025-11-28 | -0.034995 | 0.120847 | 0.000 | 5 | 5 |
| 2 | 2026-01-07 | -0.033440 | 0.280876 | 0.000 | 5 | 5 |
| 1 | 2025-12-01 | -0.031982 | 0.136380 | 0.000 | 5 | 5 |
| 1 | 2025-12-17 | -0.020161 | 0.125049 | 0.000 | 5 | 5 |
| 1 | 2025-11-27 | -0.019612 | 0.139344 | 0.000 | 5 | 5 |
| 3 | 2026-02-06 | -0.013923 | 0.190273 | 0.000 | 5 | 5 |

Diagnostic note: missed rebound/momentum gap=0.80.