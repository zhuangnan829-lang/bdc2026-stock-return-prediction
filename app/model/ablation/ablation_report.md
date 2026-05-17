# 消融实验报告

## 各组优胜项

| 消融类型 | 方案 | 成本后累计收益 | 成本后夏普 | 平均换手率 | 是否优胜 |
|---|---|---:|---:|---:|---|
| feature | base_technical_risk | 0.040137 | 0.701162 | 0.500000 | 是 |
| feature | base_technical | 0.017975 | 0.304523 | 0.500000 | 否 |
| feature | base | 0.011810 | 0.222492 | 0.500000 | 否 |
| sort_strategy | risk_adjusted | 0.040137 | 0.701162 | 0.500000 | 是 |
| sort_strategy | pure_prediction | 0.030436 | 0.509515 | 0.500000 | 否 |
| turnover | max_turnover_0.5 | 0.040137 | 0.701162 | 0.500000 | 是 |
| turnover | max_turnover_0.75 | 0.035876 | 0.478671 | 0.750000 | 否 |
| turnover | max_turnover_1.0 | 0.022662 | 0.272979 | 0.997530 | 否 |
| weighting | risk_adjusted | 0.040137 | 0.701162 | 0.500000 | 是 |
| weighting | pred | 0.036308 | 0.614244 | 0.500000 | 否 |
| weighting | equal | 0.034326 | 0.591450 | 0.500000 | 否 |
