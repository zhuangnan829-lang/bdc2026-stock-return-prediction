# rs_accel v3 保守化实验

- 切片提升最强：`rs_accel_v2`，`0.024410`
- 本地收益损伤最小：`rs_accel_v2`，`-0.139226`

| 方案 | slice | Δslice | cum_after | Δcum | sharpe | Δsharpe | max_dd | Δdd | retain |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| current_mini4_default | -0.015835 | 0.000000 | 0.935572 | 0.000000 | 3.629525 | 0.000000 | -0.042894 | 0.000000 | baseline |
| rs_accel_v2 | 0.008575 | 0.024410 | 0.796346 | -0.139226 | 3.852958 | 0.223433 | -0.041241 | 0.001653 | local_cumulative_not_worse |
| rs_accel_v3a | -0.005390 | 0.010445 | 0.773783 | -0.161788 | 3.426785 | -0.202740 | -0.054704 | -0.011810 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| rs_accel_v3b | -0.006463 | 0.009372 | 0.694095 | -0.241477 | 3.224866 | -0.404659 | -0.061572 | -0.018678 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| rs_accel_v3c | -0.001270 | 0.014565 | 0.758507 | -0.177065 | 3.394433 | -0.235093 | -0.054231 | -0.011337 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |