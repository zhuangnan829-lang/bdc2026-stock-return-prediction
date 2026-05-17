# Alpha v3 子特征细粒度消融报告

## 目标

- 找出既能抬高压缩包单切片自测分数，又不明显打坏本地累计收益的小组合。
- 所有实验统一使用当前 refined 默认执行参数，不借用压缩包建模逻辑。

## 实验结论

- 当前 refined 默认方案本地成本后累计收益最高，仍为 `0.844155`。
- 单切片自测分数最好的子特征组合是 `alpha_v3_crowding_risk`，分数为 `-0.012411`。
- 本地多期回测表现最好的子特征组合是 `alpha_v3_relative_strength`，成本后累计收益为 `0.835635`。
- 如果某个子特征组合只改善单切片分数，却明显牺牲本地累计收益或回撤控制，就不应替换当前默认方案。

## 正式对比表

| 方案 | 特征集 | 特征数 | rank_ic_mean | top5_mean_return_mean | cumulative_return_after_cost | sharpe_after_cost | max_drawdown_after_cost | avg_turnover | 压缩包单切片自测分数 | 说明 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| current_refined_default | base | 16 | 0.008584 | 0.017534 | 0.844155 | 3.308486 | -0.043533 | 0.702415 | -0.038739 | 当前正式默认方案基线。 |
| alpha_v3_relative_strength | base_alpha_v3_relative_strength | 20 | 0.021914 | 0.008333 | 0.835635 | 2.743791 | -0.112865 | 0.743815 | -0.034037 | 只测试相对强弱子特征。 |
| alpha_v3_trend_persistence | base_alpha_v3_trend_persistence | 20 | 0.029424 | 0.008574 | 0.449291 | 3.098484 | -0.065094 | 0.736659 | -0.028199 | 只测试趋势持续子特征。 |
| alpha_v3_crowding_risk | base_alpha_v3_crowding_risk | 22 | 0.021014 | 0.012679 | 0.481846 | 2.645177 | -0.088724 | 0.775322 | -0.012411 | 只测试拥挤风险子特征。 |
| alpha_v3_selected5 | base_alpha_v3_selected5 | 21 | 0.034153 | 0.012775 | 0.253516 | 1.683318 | -0.082068 | 0.780641 | -0.023243 | 优先押注的 5 个 alpha v3 子特征组合。 |

## 建议

- 优先保留那些 `压缩包单切片自测分数` 明显改善，同时 `cumulative_return_after_cost` 没有大幅掉队的子特征组合。
- 下一步不要再整包堆 alpha，而是从这轮最有希望的 1 到 2 组子特征里再做更小范围组合试验。
