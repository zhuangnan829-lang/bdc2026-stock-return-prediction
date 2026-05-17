# BDC2026 股票收益预测项目 README

本项目面向沪深300股票收益预测任务，目标是基于历史行情与特征工程结果，训练横截面排序模型，生成符合提交要求的 `result.csv`，并提供研究复现链路、正式提交链路与答辩 Demo 链路。

## Quick Start

### 1. 安装依赖

在项目根目录执行：

```bash
pip install -r requirements.txt
```

### 2. 最快看正式结果

如果你只想复现当前冻结的正式提交结果，优先执行：

```bash
bash /app/run_submission.sh
```

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File .\app\test.ps1
```

核心输出：

- `app/output/result.csv`
- `app/output/predict_scores.csv`
- `app/output/debug_candidates.csv`

### 3. 最快看完整研究闭环

如果你想一次性跑完训练、walk-forward、回测和诊断：

```bash
bash /app/run_research_pipeline.sh
```

### 4. 最快打开展示 Demo

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File .\app\demo\run_demo.ps1
```

Linux/macOS：

```bash
bash /app/demo/run_demo.sh
```

注意：

- Demo 端口**不保证固定是 `8501`**
- 若 `8501` 被占用，`run_demo.ps1` 会自动尝试 `8502 / 8503 / 8510 / 8601`
- 以终端最终打印出的 URL 为准，例如 `http://127.0.0.1:8502`

## 当前正式默认方案

当前冻结的正式默认方案来自：

- [best_config.json](/d:/Desktop/股票分析预测代码/app/model/best_config.json)
- [default_submission_config.json](/d:/Desktop/股票分析预测代码/app/model/default_submission_config.json)
- [final_submission_snapshot.md](/d:/Desktop/股票分析预测代码/app/model/final_submission_snapshot.md)

默认方案配置如下：

- 模型：`LSTM`
- 主线名称：`LSTM sl20`
- 特征集：`base_alpha_v3_rs_crowding_mini4`
- 训练目标：`cross_section_rank`
- 序列长度：`20`
- 排序策略：`risk_adjusted`
- 权重策略：`pred`
- `top_k`：`5`
- 候选池大小：`180`
- 风险惩罚：`-0.30`
- 最大换手：`1.00`
- 交易成本：`0.001`

冻结 profile 名称：

`lstm_sl20_base_alpha_v3_rs_crowding_mini4__risk_adjusted_sort__pred_weight__cs180_v2086_v5100_rp-30_mt100`

### 为什么最后选 `LSTM sl20`

根据正式模型对比结果：

- `app/model/formal_model_comparison/formal_model_comparison.csv`
- `app/model/formal_model_comparison/formal_model_comparison.md`

`LSTM sl20` 在当前统一口径下同时取得了更优的：

- `RankIC`
- `Top5平均收益`
- 回测累计收益
- `Sharpe`

因此它被冻结为正式默认方案，而不是继续使用历史参考主线 `sl10`。

更完整的答辩说明见：

- [opening_report_alignment.md](/d:/Desktop/股票分析预测代码/app/docs/opening_report_alignment.md)

## Demo 启动方式

### Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\app\demo\run_demo.ps1
```

### Linux/macOS

```bash
bash /app/demo/run_demo.sh
```

### Demo 页面内容

当前 Demo 主要展示：

1. 项目简介与正式默认方案
2. 正式模型对比表
3. Walk-forward 分折结果
4. 回测净值与回撤
5. 第 1 折错排股票诊断

对应实现文件：

- [streamlit_app.py](/d:/Desktop/股票分析预测代码/app/demo/streamlit_app.py)

## 关键结果入口

如果你只看最重要的结果文件，优先从下面这些开始：

### 正式方案快照

- [final_submission_snapshot.md](/d:/Desktop/股票分析预测代码/app/model/final_submission_snapshot.md)
- [best_config.json](/d:/Desktop/股票分析预测代码/app/model/best_config.json)
- [default_submission_config.json](/d:/Desktop/股票分析预测代码/app/model/default_submission_config.json)

### 正式模型对比

- [formal_model_comparison.csv](/d:/Desktop/股票分析预测代码/app/model/formal_model_comparison/formal_model_comparison.csv)
- [formal_model_comparison.md](/d:/Desktop/股票分析预测代码/app/model/formal_model_comparison/formal_model_comparison.md)
- [formal_model_comparison_chart.png](/d:/Desktop/股票分析预测代码/app/docs/report_supplement_assets/formal_model_comparison_chart.png)

### 回测结果

- [backtest_summary.csv](/d:/Desktop/股票分析预测代码/app/model/backtest_summary.csv)
- [backtest_report.md](/d:/Desktop/股票分析预测代码/app/model/backtest_report.md)
- [fig3_equity_curve.png](/d:/Desktop/股票分析预测代码/app/docs/figures/midterm/fig3_equity_curve.png)
- [fig4_drawdown_curve.png](/d:/Desktop/股票分析预测代码/app/docs/figures/midterm/fig4_drawdown_curve.png)

### 稳定性与阶段分析

- [fold_stage_performance.csv](/d:/Desktop/股票分析预测代码/app/model/market_regime_analysis/fold_stage_performance.csv)
- [fold_diagnostics.csv](/d:/Desktop/股票分析预测代码/app/model/fold_diagnostics.csv)
- [fold_daily_diagnostics.csv](/d:/Desktop/股票分析预测代码/app/model/fold_daily_diagnostics.csv)
- [fig2_fold_rankic.png](/d:/Desktop/股票分析预测代码/app/docs/figures/midterm/fig2_fold_rankic.png)

### 个股诊断与解释性分析

- [fold_1_predictions.csv](/d:/Desktop/股票分析预测代码/app/model/fold_1_predictions.csv)
- [fold1_short_term_ticket_summary.csv](/d:/Desktop/股票分析预测代码/app/model/fold1_short_term_ticket_summary.csv)
- [fold1_short_term_ticket_diagnostics.csv](/d:/Desktop/股票分析预测代码/app/model/fold1_short_term_ticket_diagnostics.csv)
- [fig6_ticket_diagnostics.png](/d:/Desktop/股票分析预测代码/app/docs/figures/midterm/fig6_ticket_diagnostics.png)

### 正式提交输出

- [result.csv](/d:/Desktop/股票分析预测代码/app/output/result.csv)
- [predict_scores.csv](/d:/Desktop/股票分析预测代码/app/output/predict_scores.csv)
- [debug_candidates.csv](/d:/Desktop/股票分析预测代码/app/output/debug_candidates.csv)

## 开题承诺说明

为避免“开题写得很宽，仓库落地状态不清楚”的问题，当前项目已经单独整理：

- [opening_report_alignment.md](/d:/Desktop/股票分析预测代码/app/docs/opening_report_alignment.md)

该文档明确区分了：

- 已完成并纳入正式链路的内容
- 已有实验但未纳入正式方案的内容
- 仍处于调研/后续计划阶段的内容

当前口径可以概括为：

- 已完成：`LSTM / LightGBM / XGBoost / 动量基线 / Linear Regression / Streamlit Demo`
- 已有实验但未纳入正式方案：`Transformer`
- 未形成统一可复现实验链路：`ARIMA / TFT / N-HiTS / TSFM / Qlib / FinRL`

## 复现路径入口

项目当前分三条主路径：

### 1. 研究链路

入口：

- `app/run_research_pipeline.sh`

作用：

- 训练
- walk-forward 验证
- 本地回测
- fold 诊断

说明文档：

- [reproducibility_guide.md](/d:/Desktop/股票分析预测代码/app/docs/reproducibility_guide.md)

### 2. 正式提交链路

入口：

- `app/run_submission.sh`
- `app/freeze_submission.sh`

作用：

- 冻结配置
- 正式推理
- 结果校验
- 提交前彩排

### 3. Demo 链路

入口：

- `app/demo/run_demo.ps1`
- `app/demo/run_demo.sh`

作用：

- 答辩展示
- 结果讲解
- 现场演示

## 目录结构

```text
app/
  code/src/                  核心源码
  data/                      输入数据
  demo/                      Streamlit Demo
  docs/                      文档、图表索引、答辩材料
  model/                     模型、对比结果、回测结果、冻结快照
  output/                    正式推理输出
  temp/                      中间特征文件
```

## Docker 入口

### 构建镜像

```bash
docker build -t bdc2026 .
```

### 本地彩排

```bash
docker compose up
```

当前容器默认入口：

- `app/data/run.sh`

该入口最终会调用：

- `app/run_submission.sh`

## 文档导航

如果你在整理报告、PPT 或答辩，建议优先看这些文档：

- [opening_report_alignment.md](/d:/Desktop/股票分析预测代码/app/docs/opening_report_alignment.md)
- [reproducibility_guide.md](/d:/Desktop/股票分析预测代码/app/docs/reproducibility_guide.md)
- [environment_snapshot.md](/d:/Desktop/股票分析预测代码/app/docs/environment_snapshot.md)
- [experiment_result_index.md](/d:/Desktop/股票分析预测代码/app/docs/experiment_result_index.md)
- [report_figure_table_index.md](/d:/Desktop/股票分析预测代码/app/docs/report_figure_table_index.md)
- [final_delivery_checklist.md](/d:/Desktop/股票分析预测代码/app/docs/final_delivery_checklist.md)
- [demo_3min_main_flow.md](/d:/Desktop/股票分析预测代码/app/docs/demo_3min_main_flow.md)

## 提交前建议顺序

推荐你在最终提交或答辩前按这个顺序彩排：

1. 执行 `bash /app/freeze_submission.sh`
2. 检查 `app/output/result.csv`
3. 打开 `app/model/final_submission_snapshot.md`
4. 启动 `app/demo/run_demo.ps1`
5. 按 Demo 页面讲一遍完整流程
