# LSTM TopK Weighted Rank 实验

- 训练目标从 `cross_section_rank` 升级为 `topk_weighted_rank`。
- 标签仍为横截面排序标签，但训练损失对当日收益排名前 5 和前 10 的样本给予更高权重。

| 方案 | target_mode | sample_weight_mode | rank_ic_mean | top5_mean_return_mean | cumulative_return_after_cost | sharpe_after_cost | max_drawdown_after_cost | avg_turnover |
|---|---|---|---:|---:|---:|---:|---:|---:|
| baseline_cross_section_rank | cross_section_rank | uniform | 0.011680 | 0.010119 | 0.935572 | 3.629525 | -0.042894 | 0.761281 |
| candidate_topk_weighted_rank | topk_weighted_rank | topk_head_weighted | 0.026322 | 0.004903 | 0.921115 | 3.112451 | -0.082337 | 0.760873 |

## 变化

- rank_ic_mean 变化：`0.014642`
- top5_mean_return_mean 变化：`-0.005216`
- 成本后累计收益变化：`-0.014456`
- 成本后夏普变化：`-0.517075`
- 最大回撤变化：`-0.039444`
