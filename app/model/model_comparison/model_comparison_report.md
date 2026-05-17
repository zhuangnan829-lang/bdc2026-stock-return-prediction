# 统一模型对比报告

## 对比口径

- 特征集：`base_technical_risk`
- 训练目标：`cross_section_rank`
- 选股逻辑：`risk_adjusted sort + pred weight + max_turnover=0.70`
- 回测口径：统一使用当前正式默认风险过滤与执行约束

## 总结论

- 当前同口径下综合表现最优模型：`LSTM`
- 成本后累计收益：`0.256650`
- 成本后夏普：`2.143554`
- 成本后最大回撤：`-0.046309`
- 平均换手率：`0.690485`

## 模型排序

| 排名 | 模型 | rank_ic_mean | top5_mean_return_mean | cumulative_return_after_cost | sharpe_after_cost | max_drawdown_after_cost | avg_turnover | 是否最优 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | LSTM | 0.027738 | 0.005160 | 0.256650 | 2.143554 | -0.046309 | 0.690485 | 是 |
| 2 | LightGBM | -0.028080 | -0.000944 | 0.125348 | 1.578308 | -0.070621 | 0.700000 | 否 |
| 3 | Transformer | 0.008137 | 0.003885 | 0.123012 | 0.887265 | -0.126046 | 0.683027 | 否 |
| 4 | XGBoost | -0.024164 | -0.005002 | -0.028796 | -0.387174 | -0.105148 | 0.700000 | 否 |

## 结果解读

- `rank_ic_mean` 和 `top5_mean_return_mean` 反映 walk-forward 预测排序能力。
- `cumulative_return_after_cost`、`sharpe_after_cost`、`max_drawdown_after_cost`、`avg_turnover` 反映同一执行逻辑下的真实组合表现。
- 如果某个模型回归误差不差，但成本后收益明显弱，通常说明它在 Top-K 排序稳定性上不如更优模型。
