# alpha_v4_micro 实验报告

## 实验目的

- 在当前 mini4 默认方案上追加一组小特征 `alpha_v4_micro`；
- 同时比较压缩包单切片分数与本地多期回测表现；
- 只保留“切片分数上升且本地收益不坏”的组合。

## 特征定义

- `rel_strength_accel_5d`：相对沪深 300 强弱加速度
- `trend_persistence_score_10d`：趋势持续性综合分数
- `volatility_compression_breakout_20d`：低波动压缩下的突破状态
- `crowding_reversal_risk_5d`：拥挤交易后的反转风险

## 对比结果

| 方案 | 特征集 | 特征数 | rank_ic_mean | top5_mean_return_mean | cumulative_return_after_cost | sharpe_after_cost | max_drawdown_after_cost | avg_turnover | case_slice_score |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| current_mini4_default | base_alpha_v3_rs_crowding_mini4 | 20 | 0.011680 | 0.010119 | 0.935572 | 3.629525 | -0.042894 | 0.761281 | -0.015835 |
| mini4_plus_alpha_v4_micro | base_alpha_v3_rs_crowding_mini4_alpha_v4_micro | 24 | 0.044142 | 0.013770 | 0.601434 | 3.948667 | -0.054270 | 0.777670 | 0.006276 |

## 关键差值

- 切片分数变化：`0.022111`
- 成本后累计收益变化：`-0.334137`
- 成本后夏普变化：`0.319142`
- 成本后最大回撤变化：`-0.011377`

## 保留判断

- retain_candidate: `False`
- retain_reason: `local_cumulative_not_worse / drawdown_not_materially_worse`

结论：

- 这组 alpha_v4_micro 没有同时满足双目标门槛。
- 当前正式默认方案保持不变，候选结果仅保留为实验记录。