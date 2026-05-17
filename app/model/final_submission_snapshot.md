# 最终提交快照

## 当前冻结默认方案

- 配置名称：`lstm_sl20_base_alpha_v3_rs_crowding_mini4__risk_adjusted_sort__pred_weight__cs180_v2086_v5100_rp-30_mt100`
- 配置状态：`frozen_best_config`
- 主模型：`LSTM`
- 特征集：`base_alpha_v3_rs_crowding_mini4`
- 特征数：`20`
- 训练目标：`cross_section_rank`
- 序列窗口长度：`20`
- 排序策略：`risk_adjusted`
- 权重策略：`pred`
- 选股数量：`5`
- 候选池大小：`180`
- `max_volatility_20d_pct = 0.86`
- `max_volatility_5d_pct = 1.00`
- `turnover_rate_lower_pct = 0.03`
- `turnover_rate_upper_pct = 0.97`
- `turnover_ratio_upper_pct = 0.95`
- `risk_penalty_weight = -0.30`
- `max_turnover = 1.00`
- `transaction_cost = 0.001`
- `AUTO_USE_PREVIOUS_RESULT = 0`

配置来源：
- [best_config.json](D:/Desktop/股票分析预测代码/app/model/best_config.json:1)
- [default_submission_config.json](D:/Desktop/股票分析预测代码/app/model/default_submission_config.json:1)
- [model_meta.json](D:/Desktop/股票分析预测代码/app/model/model_meta.json:1)

## 当前提交文件

- [result.csv](D:/Desktop/股票分析预测代码/app/output/result.csv:1)

当前持仓如下：

| stock_id | weight |
|---|---:|
| `300316` | `0.211841` |
| `600183` | `0.201978` |
| `600584` | `0.201300` |
| `688396` | `0.197701` |
| `601877` | `0.187179` |

当前 `result.csv` 权重和为：`1.000000`

说明：
- 当前 `result.csv` 已按正式默认口径重新生成
- 当前正式提交路径默认不自动复用上一版 `result.csv`

## 当前默认方案本地回测指标

- 成本后累计收益：`1.171246`
- 成本后 Sharpe：`4.019488`
- 成本后最大回撤：`-0.090067`
- 平均换手率：`0.956671`
- walk-forward `rank_ic_mean`：`0.027982`
- walk-forward `top5_mean_return_mean`：`0.007502`

指标来源：
- [backtest_summary.csv](app/model/default_profile_backtest/backtest_summary.csv:1)

## 与压缩包程序的当前对比结论

- 我方当前单切片分数：`0.032984`
- 压缩包当前可见分数：`0.025179`
- 压缩包公开最佳分数：`0.037838`

这说明：
- 当前正式默认已经超过压缩包当前结果
- 当前正式默认也超过压缩包公开最佳分数

对应文件：
- [case_program_comparison_summary.csv](D:/Desktop/股票分析预测代码/app/model/case_program_comparison/case_program_comparison_summary.csv:1)
- [case_program_comparison_report.md](D:/Desktop/股票分析预测代码/app/model/case_program_comparison/case_program_comparison_report.md:1)

## 提交校验状态

- 正式默认脚本参数与配置快照一致
- `result.csv` 符合提交格式要求
- `pre_submit_check.py` 一致性检查应通过
