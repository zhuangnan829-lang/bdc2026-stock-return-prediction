# Alpha 特征升级对比报告

## 对比对象

- `current_refined_default`：当前正式默认方案，`LSTM + base + refined 执行参数`
- `lstm_alpha_v3_base`：`base + alpha_v3`
- `lstm_alpha_v3_full`：`base_technical_risk_alpha_v3`
- `case_zip_program`：压缩包内自带程序的可见结果口径

## 核心结论

- 当前 refined 默认方案的本地成本后累计收益最高：`0.844155`，夏普为 `3.308486`。
- `alpha_v3_base` 的单切片自测分数从当前默认版的 `-0.038739` 提升到 `-0.014386`，但本地多期回测下降到 `0.364367`。
- `alpha_v3_full` 的单切片自测分数也高于当前默认版，为 `-0.013416`，但本地多期回测进一步降到 `0.260622`。
- 压缩包程序当前可见单切片自测分数为 `0.025179`，仍高于我方当前默认版和两组 alpha 候选。
- 这说明新 alpha 特征在某个局部测试切片上有帮助，但还没有转化为更稳定的多期收益优势；当前默认方案暂时不应被替换。

## 正式对比表

| 方案 | 特征集 | 特征数 | rank_ic_mean | top5_mean_return_mean | cumulative_return_after_cost | sharpe_after_cost | max_drawdown_after_cost | avg_turnover | 压缩包单切片自测分数 | 压缩包公布最佳分数 | 说明 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| current_refined_default | base | 16 | 0.008584 | 0.017534 | 0.844155 | 3.308486 | -0.043533 | 0.702415 | -0.038739 | N/A | 当前正式默认方案，作为所有新实验的基线。 |
| lstm_alpha_v3_base | base_alpha_v3 | 30 | 0.033931 | 0.009103 | 0.364367 | 2.336069 | -0.050804 | 0.746010 | -0.014386 | N/A | base 特征上新增 alpha_v3，单切片改善，但本地多期回测明显弱于当前默认版。 |
| lstm_alpha_v3_full | base_technical_risk_alpha_v3 | 70 | 0.054215 | 0.007765 | 0.260622 | 2.505064 | -0.079145 | 0.797846 | -0.013416 | N/A | 全量技术/风险/alpha_v3 特征，单切片优于当前默认版，但本地回测仍弱。 |
| case_zip_program | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 0.025179 | 0.037838 | 压缩包程序可见结果。未提供完整滚动预测或统一回测轨迹，因此本地多期指标记为 N/A。 |

## 如何解读

- `cumulative_return_after_cost / sharpe_after_cost / max_drawdown_after_cost / avg_turnover` 是我方统一本地回测口径，最能反映策略是否真的更赚钱、更稳。
- `压缩包单切片自测分数` 来自压缩包自带 `score_self.py` 的单次测试切片，只能反映一个局部窗口。
- 当前最好的下一步不是直接替换默认方案，而是保留 refined 默认版，继续沿着 alpha 方向做更小步的筛选和组合适配。
