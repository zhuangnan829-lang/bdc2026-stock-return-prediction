# HV Rerank Submission Candidate Report

本报告只生成候选建议，不覆盖 `app/output/result.csv`，也不覆盖 `app/model/default_submission_config.json`。

## 候选配置

- config: `D:\Desktop\股票分析预测代码\app\model\configs\submission_hv_rerank_candidate.json`
- profile: `lstm_sl20_base_alpha_v3_rs_crowding_mini4__hv_close_position_rerank`
- result: `D:\Desktop\股票分析预测代码\app\model\hv_rerank_submission_candidate\result_hv_rerank.csv`
- comparison: `D:\Desktop\股票分析预测代码\app\model\hv_rerank_submission_candidate\result_hv_rerank_vs_current.csv`
- top_k: `5`
- candidate_size: `180`
- weighting_scheme: `pred`
- max_single_weight: `0.18`
- regime_rerank: enabled=`True`, flag=`is_high_volatility`, signal=`close_position_20d`, weight=`-0.05`

## 执行状态

| step | status | seconds | error |
|---|---|---:|---|
| featurework_predict | PASS | 6.9 |  |
| test_lstm_hv_rerank | PASS | 13.1 |  |
| result_validator_hv_rerank | PASS | 0.6 |  |
| pre_submit_check_hv_rerank_result | PASS | 0.6 |  |

## 与当前正式结果对比

- 当前正式结果: `D:\Desktop\股票分析预测代码\app\output\result.csv`
- 当前行数: `5`, 当前权重和: `0.900000`
- 候选行数: `5`, 候选权重和: `0.900000`
- 共同股票数: `4`
- 新增股票: `600115`
- 移除股票: `601877`
- 相对当前结果的切换换手: `0.360000`

| stock_id | current_weight | candidate_weight | weight_delta | action |
| --- | --- | --- | --- | --- |
| 600115 | 0.000000 | 0.180000 | 0.180000 | added |
| 601877 | 0.180000 | 0.000000 | -0.180000 | dropped |
| 300316 | 0.180000 | 0.180000 | 0.000000 | kept |
| 600183 | 0.180000 | 0.180000 | 0.000000 | kept |
| 600584 | 0.180000 | 0.180000 | 0.000000 | kept |
| 688396 | 0.180000 | 0.180000 | 0.000000 | kept |

## 判断

- 手动确认前，继续把当前 LSTM sl20 默认结果作为权威提交结果。
- 这份 HV rerank 结果可以作为独立候选进入人工复核。
- 只有当换入/换出的股票可接受，并且与完整验证结论一致时，才考虑升级为正式默认配置。
