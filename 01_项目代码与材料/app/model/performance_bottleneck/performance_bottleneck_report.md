# Performance Bottleneck Report

- pred_path: `D:\Desktop\股票分析预测代码\app\model\walk_forward_predictions.csv`
- data_path: `D:\Desktop\股票分析预测代码\app\temp\train_features.csv`
- result_path: `D:\Desktop\股票分析预测代码\app\output\result.csv`

## Summary Averages

- true_top5_return: `0.178172`
- candidate_pool_true_top5_return: `0.137993`
- model_top5_equal_return: `0.016264`
- model_top5_weighted_return: `0.014637`
- model_top5_hit_rate: `0.016667`
- model_top10_hit_rate: `0.040000`
- weight_strategy_gain: `-0.001626`
- max_single_contribution_ratio: `0.460994`

## Diagnosis

- 候选池是否漏掉真实高收益股票？是。candidate gap = `0.040179`。
- 模型排序是否把候选池中的高收益股票排到前面？仍有明显不足。ranking gap = `0.121729`。
- 当前权重策略是否优于等权？否。平均增益 = `-0.001626`。
- 当前收益是否过度依赖单只股票？否。平均最大单票贡献占比 = `0.460994`。
- 下一步更应该改候选池、排序模型还是权重？建议优先看 `ranking`。

## Bottleneck Gap Metrics

| metric | value |
|---|---:|
| candidate_gap | 0.040179 |
| ranking_gap | 0.121729 |
| weighting_loss | 0.002065 |
| concentration | 0.460994 |

## Result Slice Contribution

- result.csv contribution uses latest analyzable date 2026-02-27; missing_true_return_rows=0.

Final judgment: `ranking`
