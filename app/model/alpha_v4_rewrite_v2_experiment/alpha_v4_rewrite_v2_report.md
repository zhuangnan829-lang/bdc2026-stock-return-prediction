# rs_accel v2 / trend_persist v2 重写实验

## 目标

- 将 `rs_accel` 和 `trend_persist` 重写为更温和、更收敛的 v2 版本；
- 继续比较压缩包单切片分数与本地多期收益；
- 观察是否比原版 alpha_v4_micro 子特征更适合保留。

## 基线

- 基线切片分数：`-0.015835`
- 基线成本后累计收益：`0.935572`
- 基线夏普：`3.629525`
- 基线最大回撤：`-0.042894`

## 结论

- 切片分数提升最明显的是 `rs_accel_v2`，提升 `0.024410`。
- 对本地累计收益伤害最小的是 `rs_accel_v2`，变化 `-0.139226`。
- 若仍没有组合通过保留门槛，说明这两个方向值得继续做，但当前 v2 还不够。

## 对比表

| 方案 | slice分数 | Δslice | 累计收益 | Δ累计收益 | 夏普 | Δ夏普 | 最大回撤 | Δ回撤 | 保留 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| current_mini4_default | -0.015835 | 0.000000 | 0.935572 | 0.000000 | 3.629525 | 0.000000 | -0.042894 | 0.000000 | baseline |
| rs_accel_v2 | 0.008575 | 0.024410 | 0.796346 | -0.139226 | 3.852958 | 0.223433 | -0.041241 | 0.001653 | local_cumulative_not_worse |
| trend_persist_v2 | -0.008354 | 0.007481 | 0.711294 | -0.224278 | 3.158888 | -0.470637 | -0.053896 | -0.011002 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |
| rs_accel_v2__trend_persist_v2 | 0.000098 | 0.015933 | 0.388743 | -0.546829 | 2.998924 | -0.630601 | -0.058379 | -0.015486 | local_cumulative_not_worse / local_sharpe_not_worse / drawdown_not_materially_worse |