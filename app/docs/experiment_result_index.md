# 实验结果索引

本文档用于把“实验脚本、结果文件、结论用途”串起来，方便查找每项结论的证据来源。

## 1. 正式主线与模型对比

| 实验主题 | 主要脚本 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| 正式模型对比表 | `app/code/src/build_formal_model_comparison.py` | `app/model/formal_model_comparison/formal_model_comparison.csv`、`app/model/formal_model_comparison/formal_model_comparison.md` | 支撑“为什么正式方案选 LSTM sl20”。 |
| 综合模型比较 | `app/code/src/run_model_comparison.py` | `app/model/model_comparison/model_comparison_summary.csv`、`app/model/model_comparison/model_comparison_report.md` | 支撑“除正式候选外还做过哪些模型对照”。 |
| 最终冻结方案说明 | `app/code/src/sync_submission_config.py`、`app/freeze_submission.sh` | `app/model/final_submission_snapshot.md`、`app/model/submission_artifacts/` | 支撑“当前正式默认配置是什么”。 |

## 2. 训练、walk-forward 与预测产物

| 实验主题 | 主要脚本 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| LSTM 训练 | `app/train.sh`、`app/code/src/train_lstm.py` | `app/model/lstm_model.pt`、`app/model/model_meta.json` | 支撑主线模型已完成训练。 |
| walk-forward 预测 | `app/code/src/train_lstm.py` | `app/model/walk_forward_predictions.csv`、`app/model/walk_forward_metrics.csv` | 支撑主线模型排序能力评估。 |
| 冻结推理 | `app/test.sh`、`app/code/src/test_lstm.py` | `app/output/result.csv`、`app/output/predict_scores.csv`、`app/output/debug_candidates.csv` | 支撑正式提交结果生成链路。 |

## 3. 本地回测与风险收益分析

| 实验主题 | 主要脚本 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| 默认回测与配置比较 | `app/code/src/backtest.py` | `app/model/backtest_summary.csv`、`app/model/backtest_report.md`、`app/model/backtest_config_comparison.csv` | 支撑“正式方案收益、Sharpe、回撤表现”。 |
| 回测净值与回撤图 | `app/code/src/generate_midterm_report_figures.py` 或报告图生成链路 | `app/docs/figures/midterm/fig3_equity_curve.png`、`app/docs/figures/midterm/fig4_drawdown_curve.png` | 用于展示收益曲线和回撤曲线。 |
| 日频持仓与回测明细 | `app/code/src/backtest.py` | `app/model/backtest_daily_results.csv`、`app/model/backtest_holdings.csv` | 支撑更细粒度的组合回放分析。 |

## 4. 稳定性、分折与阶段分析

| 实验主题 | 主要脚本 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| 折次诊断 | `app/run_research_pipeline.sh` 内嵌 diagnostics 流程 | `app/model/fold_diagnostics.csv`、`app/model/fold_daily_diagnostics.csv`、`app/model/fold_1_predictions.csv` | 支撑“第一折表现退化与稳定性分析”。 |
| 市场阶段分析 | `app/code/src/build_market_regime_analysis.py` | `app/model/market_regime_analysis/fold_stage_performance.csv`、`app/model/market_regime_analysis/` 下相关 md/csv | 支撑“不同市场阶段下模型表现不同”。 |
| report 补充图资产 | `app/code/src/build_report_supplement_assets.py` | `app/docs/report_supplement_assets/market_regime_analysis_chart.png` | 用于中期/答辩图示。 |

## 5. 特征消融与解释性分析

| 实验主题 | 主要脚本/目录 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| 短期特征诊断 | 相关分析脚本已沉淀为结果文件 | `app/model/fold1_short_term_ticket_summary.csv`、`app/model/fold1_short_term_ticket_diagnostics.csv` | 支撑“哪些股票/短期因子导致错排”。 |
| 特征消融汇总 | 多个 `ablation_*` 目录与相关构建脚本 | `app/model/ablation/ablation_summary.csv`、`app/model/fine_short_term_ablation_comparison.csv`、`app/model/ret3d_interaction_ablation_comparison.csv` | 支撑“当前特征集是如何收敛出来的”。 |
| Alpha 特征升级 | `alpha_*_experiment` 系列实验 | `app/model/alpha_feature_upgrade/`、`app/model/alpha_rs_crowding_mini4_experiment/` 等 | 支撑“为什么最终选择 base_alpha_v3_rs_crowding_mini4”。 |

## 6. 基线与备选模型实验

| 实验主题 | 主要结果目录 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| LightGBM 基线 | `app/model/baseline_lightgbm_same_protocol/` | `model_meta.json`、`walk_forward_predictions.csv` | 支撑机器学习基线对照。 |
| XGBoost 基线 | `app/model/xgboost_baseline/` | `model_meta.json`、`walk_forward_predictions.csv` | 支撑树模型基线对照。 |
| 线性回归基线 | `app/model/baseline_linear_same_protocol/` | 相关 baseline 结果文件 | 支撑线性模型对照。 |
| Transformer 基线 | `app/model/transformer_baseline/` | `walk_forward_metrics.csv`、`walk_forward_predictions.csv`、`backtest/backtest_summary.csv` | 支撑“做过 Transformer，但未纳入正式方案”。 |

## 7. Demo 与展示材料

| 展示主题 | 主要脚本 | 主要结果文件 | 用途/支撑结论 |
|---|---|---|---|
| Streamlit Demo | `app/demo/streamlit_app.py` | 读取 `app/model/` 与 `app/docs/` 下现有结果文件 | 支撑答辩现场展示。 |
| Demo 流程图与说明图 | `app/code/src/build_report_supplement_assets.py` | `app/docs/report_supplement_assets/demo_flowchart.png`、`demo_key_commands.png`、`demo_result_files.png` | 支撑“项目不是一堆脚本，而是一条完整流程”。 |

## 8. 建议优先引用的证据文件

如果只允许快速给老师看少量文件，优先顺序建议是：

1. `app/model/final_submission_snapshot.md`
2. `app/model/formal_model_comparison/formal_model_comparison.csv`
3. `app/model/backtest_summary.csv`
4. `app/model/market_regime_analysis/fold_stage_performance.csv`
5. `app/model/fold1_short_term_ticket_diagnostics.csv`
6. `app/demo/streamlit_app.py`
