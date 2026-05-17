# 特征升级消融报告

## 各组优胜项

| 消融类型 | 方案 | 成本后累计收益 | 成本后夏普 | 平均换手率 | 是否优胜 |
|---|---|---:|---:|---:|---|
| feature | base_technical_risk | 0.115561 | 1.615013 | 0.650000 | 是 |
| feature | base | 0.060902 | 0.783112 | 0.650000 | 否 |
| feature | base_technical_risk_alpha | 0.050444 | 0.720224 | 0.650000 | 否 |
| feature | base_technical | 0.000280 | 0.037761 | 0.650000 | 否 |
| sort_strategy | risk_adjusted | 0.115561 | 1.615013 | 0.650000 | 是 |
| sort_strategy | pure_prediction | 0.105669 | 1.458343 | 0.650000 | 否 |
| turnover | max_turnover_0.75 | 0.117397 | 1.469242 | 0.750000 | 是 |
| turnover | max_turnover_0.65 | 0.115561 | 1.615013 | 0.650000 | 否 |
| turnover | max_turnover_1.0 | 0.108761 | 1.112465 | 0.993590 | 否 |
| turnover | max_turnover_0.5 | 0.106534 | 1.839981 | 0.500000 | 否 |
| weighting | pred | 0.124083 | 1.653794 | 0.650000 | 是 |
| weighting | equal | 0.120367 | 1.623529 | 0.650000 | 否 |
| weighting | risk_adjusted | 0.115561 | 1.615013 | 0.650000 | 否 |
