# Case Zip Hybrid Candidate Search Report

本报告生成 `当前模型 TopN + 压缩包 Top5 + aggressive score` 的 hybrid 候选，并按压缩包同口径复算单切片分数。

## Top Hybrid Candidates

| rank | label | score | weight_sum | stocks |
|---:|---|---:|---:|---|
| 1 | `result_hybrid_aggressive4_case_fill_equal` | 0.075957 | 1.000000 | `000792,600233,601669,600930,600023` |
| 2 | `result_hybrid_aggressive3_case_fill_equal` | 0.068807 | 1.000000 | `000792,600233,601669,600023,601668` |
| 3 | `result_hybrid_rankblend_cur0p25_case0p20_aggr0p55_predcap20` | 0.063966 | 1.000000 | `000792,600233,601668,601018,601669` |
| 4 | `result_hybrid_rankblend_cur0p25_case0p20_aggr0p55` | 0.063966 | 1.000000 | `000792,600233,601668,601018,601669` |
| 5 | `result_hybrid_aggressive2_case_fill_equal` | 0.038813 | 1.000000 | `000792,600233,600023,601668,601018` |
| 6 | `result_hybrid_rankblend_cur0p25_case0p50_aggr0p25_predcap20` | 0.036532 | 1.000000 | `601668,600023,601018,601818,000792` |
| 7 | `result_hybrid_rankblend_cur0p25_case0p50_aggr0p25` | 0.036532 | 1.000000 | `601668,600023,601018,601818,000792` |
| 8 | `result_hybrid_rankblend_cur0p25_case0p35_aggr0p40` | 0.036532 | 1.000000 | `601668,601018,000792,600023,601818` |
| 9 | `result_hybrid_aggressive1_case_fill_equal` | 0.036532 | 1.000000 | `000792,600023,601668,601018,601818` |
| 10 | `result_hybrid_rankblend_cur0p25_case0p35_aggr0p40_predcap20` | 0.036532 | 1.000000 | `601668,601018,000792,600023,601818` |
| 11 | `result_hybrid_rankblend_cur0p40_case0p20_aggr0p40` | 0.030895 | 1.000000 | `601668,601018,601818,000792,688396` |
| 12 | `result_hybrid_rankblend_cur0p40_case0p20_aggr0p40_predcap20` | 0.030895 | 1.000000 | `601668,601018,601818,000792,688396` |
| 13 | `result_hybrid_hybrid_current0_case5_equal` | 0.025179 | 1.000000 | `600023,601668,601018,601818,601186` |
| 14 | `result_hybrid_hybrid_current1_case4_equal` | 0.022511 | 1.000000 | `688396,600023,601668,601018,601818` |
| 15 | `result_hybrid_case_first4_fill_current_equal` | 0.022511 | 1.000000 | `600023,601668,601018,601818,688396` |
| 16 | `result_hybrid_rankblend_cur0p40_case0p35_aggr0p25` | 0.022511 | 1.000000 | `601668,601018,601818,600023,688396` |
| 17 | `result_hybrid_rankblend_cur0p40_case0p35_aggr0p25_predcap20` | 0.022511 | 1.000000 | `601668,601018,601818,600023,688396` |
| 18 | `result_hybrid_case_first3_fill_current_equal` | 0.018274 | 1.000000 | `600023,601668,601018,688396,600183` |
| 19 | `result_hybrid_hybrid_current2_case3_equal` | 0.018274 | 1.000000 | `688396,600183,600023,601668,601018` |
| 20 | `result_hybrid_case_first2_fill_current_equal` | 0.016594 | 1.000000 | `600023,601668,688396,600183,300316` |

## Best Candidate Detail

| stock_id | weight | case_slice_return | contribution |
|---|---:|---:|---:|
| `000792` | 0.200000 | 0.080310 | 0.016062 |
| `600233` | 0.200000 | 0.039267 | 0.007853 |
| `601669` | 0.200000 | 0.164154 | 0.032831 |
| `600930` | 0.200000 | 0.057661 | 0.011532 |
| `600023` | 0.200000 | 0.038391 | 0.007678 |

## Interpretation

- 若 hybrid 低于 aggressive score 候选，说明当前最强冲分来自最新单切片强势股，而不是压缩包 Top5。
- 若 hybrid 高于 zip current 但低于 aggressive score，可作为备选冲分包，不建议替换已同步的 aggressive result。
- 本脚本只生成候选和报告，不覆盖 `app/output/result.csv`。
