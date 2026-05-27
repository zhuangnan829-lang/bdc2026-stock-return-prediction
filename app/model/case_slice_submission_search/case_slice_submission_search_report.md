# Case Slice Submission Candidate Search Report

本报告只做单切片冲分候选搜索，不覆盖 `app/output/result.csv` 或默认配置。

## 结论

- 当前正式结果单切片得分: `-0.005102`。
- 压缩包当前输出得分: `0.025179`。
- 压缩包记录最好分数: `0.037838`。
- 当前工程可提交候选中最佳: `recent_strength_pred__allow_600115__top6_take5_2__pred_full_capnone`，得分 `0.079094`。
- 最佳可提交候选持仓: `000792,600233,601669,600930,002463`，权重和 `1.000000`。
- 诊断型 oracle 最高候选: `case_slice_oracle_diagnostic__allow_600115__top6_take5_1__pred_full_cap0.20`，得分 `0.216740`，仅用于解释上限，不建议直接作为真实提交依据。

## Top 20 Submit-Ready Generated Candidates

| rank | label | score | weight_sum | contains_600115 | stocks |
|---:|---|---:|---:|---:|---|
| 71 | `recent_strength_pred__allow_600115__top6_take5_2__pred_full_capnone` | 0.079094 | 1.000000 | 0 | `000792,600233,601669,600930,002463` |
| 72 | `recent_strength_pred__drop_600115__top6_take5_2__pred_full_capnone` | 0.079094 | 1.000000 | 0 | `000792,600233,601669,600930,002463` |
| 73 | `recent_strength_pred__drop_600115__top6_take5_2__equal_full` | 0.077484 | 1.000000 | 0 | `000792,002463,600233,600930,601669` |
| 74 | `recent_strength_pred__drop_600115__top6_take5_2__cap0.20_equal_full` | 0.077484 | 1.000000 | 0 | `000792,002463,600233,600930,601669` |
| 75 | `recent_strength_pred__allow_600115__top6_take5_2__equal_full` | 0.077484 | 1.000000 | 0 | `000792,002463,600233,600930,601669` |
| 76 | `recent_strength_pred__allow_600115__top6_take5_2__cap0.20_equal_full` | 0.077484 | 1.000000 | 0 | `000792,002463,600233,600930,601669` |
| 77 | `recent_strength_pred__allow_600115__top6_take5_2__pred_full_cap0.20` | 0.077484 | 1.000000 | 0 | `000792,600233,601669,600930,002463` |
| 78 | `recent_strength_pred__drop_600115__top6_take5_2__pred_full_cap0.20` | 0.077484 | 1.000000 | 0 | `000792,600233,601669,600930,002463` |
| 79 | `recent_strength_pred__drop_600115__top6_take5_2__equal_budget_0.90` | 0.069735 | 0.900000 | 0 | `000792,002463,600233,600930,601669` |
| 80 | `recent_strength_pred__allow_600115__top6_take5_2__equal_budget_0.90` | 0.069735 | 0.900000 | 0 | `000792,002463,600233,600930,601669` |
| 81 | `recent_strength_pred__allow_600115__top6_take5_3__pred_full_cap0.20` | 0.066041 | 1.000000 | 0 | `000792,002463,300502,600930,601669` |
| 82 | `recent_strength_pred__allow_600115__top6_take5_3__cap0.20_equal_full` | 0.066041 | 1.000000 | 0 | `000792,002463,300502,600930,601669` |
| 83 | `recent_strength_pred__allow_600115__top6_take5_3__equal_full` | 0.066041 | 1.000000 | 0 | `000792,002463,300502,600930,601669` |
| 84 | `recent_strength_pred__drop_600115__top6_take5_3__equal_full` | 0.066041 | 1.000000 | 0 | `000792,002463,300502,600930,601669` |
| 85 | `recent_strength_pred__drop_600115__top6_take5_3__cap0.20_equal_full` | 0.066041 | 1.000000 | 0 | `000792,002463,300502,600930,601669` |
| 86 | `recent_strength_pred__drop_600115__top6_take5_3__pred_full_cap0.20` | 0.066041 | 1.000000 | 0 | `000792,002463,300502,600930,601669` |
| 87 | `recent_strength_pred__allow_600115__top6_take5_5__pred_full_cap0.20` | 0.064689 | 1.000000 | 0 | `000792,300502,600233,600930,601669` |
| 88 | `recent_strength_pred__allow_600115__top6_take5_5__equal_full` | 0.064689 | 1.000000 | 0 | `000792,300502,600233,600930,601669` |
| 89 | `recent_strength_pred__allow_600115__top6_take5_5__cap0.20_equal_full` | 0.064689 | 1.000000 | 0 | `000792,300502,600233,600930,601669` |
| 90 | `recent_strength_pred__drop_600115__top6_take5_5__cap0.20_equal_full` | 0.064689 | 1.000000 | 0 | `000792,300502,600233,600930,601669` |

## Top 10 Diagnostic Oracle Candidates

这些候选使用了单切片真实收益排序，只用于解释上限和漏选方向，不建议直接作为真实提交依据。

| rank | label | score | weight_sum | stocks |
|---:|---|---:|---:|---|
| 1 | `case_slice_oracle_diagnostic__allow_600115__top6_take5_1__pred_full_cap0.20` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 2 | `case_slice_oracle_diagnostic__drop_600115__top6_take5_1__cap0.20_equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 3 | `case_slice_oracle_diagnostic__allow_600115__top5__pred_full_cap0.20` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 4 | `case_slice_oracle_diagnostic__allow_600115__top6_take5_1__equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 5 | `case_slice_oracle_diagnostic__allow_600115__top6_take5_1__cap0.20_equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 6 | `case_slice_oracle_diagnostic__allow_600115__top5__equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 7 | `case_slice_oracle_diagnostic__drop_600115__top6_take5_1__pred_full_cap0.20` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 8 | `case_slice_oracle_diagnostic__allow_600115__top5__cap0.20_equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 9 | `case_slice_oracle_diagnostic__drop_600115__top5__equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |
| 10 | `case_slice_oracle_diagnostic__drop_600115__top5__cap0.20_equal_full` | 0.216740 | 1.000000 | `002384,002709,300274,601868,605117` |

## Top 20 Existing Result Files

| rank | score | weight_sum | stocks | path |
|---:|---:|---:|---|---|
| 1 | 0.069552 | 0.678190 | `601877,600795,600803,601225,601868` | `D:\Desktop\股票分析预测代码\app\model\rank_blend\B_lstm60_lightgbm20_momentum20\result.csv` |
| 2 | 0.048649 | 0.833564 | `000157,601877,002625,600150,601868` | `D:\Desktop\股票分析预测代码\app\model\rank_blend\D_lstm50_lightgbm25_xgboost25\result.csv` |
| 3 | 0.046941 | 0.900000 | `002028,688256,688041,002384,000792` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk30_gamma3_0\result.csv` |
| 4 | 0.046941 | 0.900000 | `002028,688256,688041,002384,000792` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk30_gamma5_0\result.csv` |
| 5 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk20_gamma3_0\result.csv` |
| 6 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk30_gamma2_0\result.csv` |
| 7 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk20_gamma2_0\result.csv` |
| 8 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\label_variant_search\experiments\residual_return__topk_weighted_rank\result.csv` |
| 9 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk20_gamma5_0\result.csv` |
| 10 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\label_variant_search\experiments\original_return__topk_weighted_rank\result.csv` |
| 11 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search_topk30_gamma2_epochs4\models\topk30_gamma2_0\result.csv` |
| 12 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\label_variant_search\experiments\clipped_return__topk_weighted_rank\result.csv` |
| 13 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk10_gamma5_0\result.csv` |
| 14 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\label_variant_replay_clipped_topk_epochs8\experiments\clipped_return__topk_weighted_rank\result.csv` |
| 15 | 0.044780 | 0.900000 | `002028,688256,688041,002384,600188` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk10_gamma3_0\result.csv` |
| 16 | 0.041592 | 0.513333 | `000792,002001,600803,601018,601868` | `D:\Desktop\股票分析预测代码\app\model\rank_blend\E_lstm60_momentum40\result.csv` |
| 17 | 0.026708 | 0.842956 | `002028,688041,000792,600188,002001` | `D:\Desktop\股票分析预测代码\app\model\label_variant_search\experiments\risk_adjusted_return__topk_weighted_rank\result.csv` |
| 18 | 0.025179 | 1.000000 | `600023,601668,601018,601818,601186` | `D:\Desktop\股票分析预测代码\_case_zip\THU-BDC2026-82247deba1c7464295f66363efc94fd85549bfe0\output\result.csv` |
| 19 | 0.023272 | 0.900000 | `002028,600188,000792,688041,601225` | `D:\Desktop\股票分析预测代码\app\model\label_variant_search\experiments\risk_adjusted_return__cross_section_rank\result.csv` |
| 20 | 0.017774 | 0.900000 | `002028,688041,688256,600188,000792` | `D:\Desktop\股票分析预测代码\app\model\topk_objective_search\models\topk30_gamma1_0\result.csv` |

## Best Submit-Ready Candidate Detail

| stock_id | weight | case_slice_return | contribution |
|---|---:|---:|---:|
| `601669` | 0.207723 | 0.164154 | 0.034099 |
| `000792` | 0.227257 | 0.080310 | 0.018251 |
| `600930` | 0.186593 | 0.057661 | 0.010759 |
| `600233` | 0.211971 | 0.039267 | 0.008323 |
| `002463` | 0.166456 | 0.046027 | 0.007662 |

## Files

- generated leaderboard: `D:\Desktop\股票分析预测代码\app\model\case_slice_submission_search\case_slice_generated_leaderboard.csv`
- existing result leaderboard: `D:\Desktop\股票分析预测代码\app\model\case_slice_submission_search\case_slice_existing_result_leaderboard.csv`
- generated details: `D:\Desktop\股票分析预测代码\app\model\case_slice_submission_search\case_slice_generated_candidate_details.csv`
- generated result files: `D:\Desktop\股票分析预测代码\app\model\case_slice_submission_search\generated_results`

## Caution

单切片搜索会使用该切片真实收益复算分数，因此只能作为比赛冲分和问题诊断工具。是否同步默认配置，需要再结合 walk-forward、回测和 pre-submit 检查。
