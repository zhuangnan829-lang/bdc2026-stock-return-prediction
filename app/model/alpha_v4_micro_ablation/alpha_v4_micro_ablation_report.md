# alpha_v4_micro 子特征细粒度消融报告

## 实验目标

- 在当前 mini4 默认方案上，拆开 `alpha_v4_micro` 的 4 个子特征；
- 系统测试单特征与两两组合；
- 只保留“压缩包单切片分数提升，且本地收益不坏”的候选。

## 基线

- 基线方案：`base_alpha_v3_rs_crowding_mini4`
- 基线切片分数：`-0.015835`
- 基线成本后累计收益：`0.935572`
- 基线夏普：`3.629525`
- 基线最大回撤：`-0.042894`

## 关键结论

- 这轮单特征/两两组合里，没有组合同时满足保留门槛。
- 说明 `alpha_v4_micro` 的切片提升信号是真存在的，但当前写法仍偏激进。
- 切片分数提升最大的组合：`rs_accel__vol_compress_breakout`，提升 ` 0.034422`。
- 但它的本地累计收益变化为 `-0.729361`，需要结合保留门槛一起看。

## 完整对比表

| 方案 | 新增特征 | slice分数 | Δslice | 累计收益 | Δ累计收益 | 夏普 | Δ夏普 | 最大回撤 | Δ回撤 | 保留 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| current_mini4_default | N/A | -0.015835 | 0.000000 | 0.935572 | 0.000000 | 3.629525 | 0.000000 | -0.042894 | 0.000000 | baseline |
| rs_accel | rel_strength_accel_5d | -0.001094 | 0.014741 | 0.863539 | -0.072033 | 3.725782 | 0.096257 | -0.036925 | 0.005968 | local_cumulative_not_worse |
| trend_persist | trend_persistence_score_10d | 0.001382 | 0.017217 | 0.854836 | -0.080735 | 3.479930 | -0.149595 | -0.066724 | -0.023831 | local_cumulative_not_worse / drawdown_not_materially_worse |
| vol_compress_breakout | volatility_compression_breakout_20d | -0.018037 | -0.002202 | 0.823321 | -0.112251 | 3.731990 | 0.102464 | -0.068804 | -0.025911 | case_slice_score_up / local_cumulative_not_worse / drawdown_not_materially_worse |
| crowding_reversal | crowding_reversal_risk_5d | -0.002646 | 0.013189 | 0.752000 | -0.183571 | 3.683397 | 0.053872 | -0.059979 | -0.017085 | local_cumulative_not_worse / drawdown_not_materially_worse |
| rs_accel__trend_persist | rel_strength_accel_5d|trend_persistence_score_10d | 0.009024 | 0.024859 | 0.335272 | -0.600299 | 2.569288 | -1.060238 | -0.074078 | -0.031184 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| rs_accel__vol_compress_breakout | rel_strength_accel_5d|volatility_compression_breakout_20d | 0.018587 | 0.034422 | 0.206211 | -0.729361 | 1.406750 | -2.222775 | -0.091658 | -0.048764 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| rs_accel__crowding_reversal | rel_strength_accel_5d|crowding_reversal_risk_5d | 0.001374 | 0.017209 | 0.518725 | -0.416846 | 3.120808 | -0.508718 | -0.040582 | 0.002312 | local_cumulative_not_worse / local_sharpe_not_worse |
| trend_persist__vol_compress_breakout | trend_persistence_score_10d|volatility_compression_breakout_20d | 0.008486 | 0.024321 | 0.356778 | -0.578794 | 2.443875 | -1.185650 | -0.081611 | -0.038718 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| trend_persist__crowding_reversal | trend_persistence_score_10d|crowding_reversal_risk_5d | -0.000760 | 0.015075 | 0.531472 | -0.404100 | 3.305282 | -0.324243 | -0.035764 | 0.007130 | local_cumulative_not_worse / local_sharpe_not_worse |
| vol_compress_breakout__crowding_reversal | volatility_compression_breakout_20d|crowding_reversal_risk_5d | 0.008363 | 0.024198 | 0.510727 | -0.424845 | 3.006210 | -0.623315 | -0.055252 | -0.012359 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| alpha_v4_micro_full | rel_strength_accel_5d|trend_persistence_score_10d|volatility_compression_breakout_20d|crowding_reversal_risk_5d | 0.006276 | 0.022111 | 0.601434 | -0.334137 | 3.948667 | 0.319142 | -0.054270 | -0.011377 | local_cumulative_not_worse / drawdown_not_materially_worse |

## 建议

- 下一步优先围绕通过门槛的组合继续做更小范围微调；
- 如果没有组合通过，就从切片提升明显但本地损伤较小的那 1 到 2 组继续改写特征定义，而不是直接保留现版本。