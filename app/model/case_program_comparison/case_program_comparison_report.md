# 当前程序 vs 压缩包程序对比总结

## 结论

- 当前刚跑出的 `app/output/result.csv` 在压缩包单切片打分口径下得分为 `-0.005102`。
- 压缩包当前公开切片结果得分为 `0.025179`，因此当前版本 **仍低于** 压缩包当前结果。
- 压缩包公开最好分数为 `0.037838`，因此当前版本 **仍低于** 压缩包公开最好分数。
- 相比上一版默认方案 `-0.038739`，当前版本已经进一步提高了 `0.033637`。
- 在我方统一本地回测口径下，当前默认方案仍保持：累计收益 `0.935572`，夏普 `3.629525`，最大回撤 `-0.042894`。

## 判断口径

- `current_live_case_slice_score`：当前实时 `result.csv` 按压缩包 `test/data` 单切片公式复算得到。
- `case_current_slice_score`：压缩包目录里当前保存的切片结果。
- `case_reported_best_score`：压缩包公开材料中的最好单次成绩。
- `local_*` 指标：我方统一 walk-forward + 成本后回测指标，不与压缩包构成同口径直接对打，但反映策略稳定性。

## 结构化对比表

| 维度 | 我方 | 压缩包 | 判断 |
|---|---|---|---|
| our_current_default_feature_set | base_alpha_v3_rs_crowding_mini4 | not_disclosed_as_clean_feature_bundle | different_design |
| our_feature_count | 20 | reported_large_mixed_bundle_approx_197 | different_design |
| current_live_case_slice_score | -0.005101713484383047 | 0.0251794912169185 | case_stronger |
| current_live_vs_case_reported_best | -0.005101713484383047 | 0.037838 | case_stronger |
| previous_default_case_slice_score | -0.0387391261901916 | 0.0251794912169185 | case_stronger |
| frozen_mini4_case_slice_score | -0.0158350415650904 | 0.0251794912169185 | case_stronger |
| local_cumulative_return_after_cost | 0.935571619432464 | N/A | our_stronger_but_not_same_protocol |
| local_sharpe_after_cost | 3.6295252848094974 | N/A | our_stronger_but_not_same_protocol |
| local_max_drawdown_after_cost | -0.0428936280873258 | N/A | our_stronger_but_not_same_protocol |
| local_avg_turnover | 0.7612811507926904 | N/A | our_stronger_but_not_same_protocol |
| reproducibility_and_pipeline_completeness | full_train_test_backtest_validator_snapshot | partial_public_artifacts | our_stronger |
| ablation_and_iteration_evidence | feature_execution_model_ablation_complete | not_publicly_complete | our_stronger |
| engineering_controllability | high | medium_unknown | our_stronger |
| baseline_vs_other_our_models | mini4 beats lightgbm=0.295839, xgboost=0.137837, transformer=0.243178 | N/A | our_stronger_internal_evidence |