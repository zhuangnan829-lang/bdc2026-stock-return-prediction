# 环境快照

本文档记录当前项目在本地整理文档时的环境与依赖快照，用于减少“能跑但说不清在哪个环境跑”的问题。

## 1. 本地 Python 环境

- Python：`3.12.7`
- 平台：`Windows-11-10.0.26200-SP0`

## 2. requirements.txt 快照

当前 `requirements.txt` 包含：

- `pandas==2.2.3`
- `numpy==2.1.3`
- `scikit-learn==1.5.2`
- `joblib==1.4.2`
- `lightgbm==4.5.0`
- `matplotlib==3.9.2`
- `torch==2.11.0`
- `streamlit==1.37.1`

## 3. Docker 环境快照

Dockerfile 当前基础镜像：

- `python:3.12-slim`

Dockerfile 额外安装：

- `libgomp1`

默认容器工作目录：

- `/app`

默认 CMD：

- `/bin/bash /app/data/run.sh`

## 4. 关键脚本快照

当前核心链路脚本：

- `app/init.sh`
- `app/train.sh`
- `app/test.sh`
- `app/run_research_pipeline.sh`
- `app/run_submission.sh`
- `app/freeze_submission.sh`
- `app/demo/run_demo.ps1`
- `app/demo/run_demo.sh`

## 5. 关键配置快照

当前正式默认方案相关快照文件：

- `app/model/best_config.json`
- `app/model/default_submission_config.json`
- `app/model/model_meta.json`
- `app/model/final_submission_snapshot.md`
- `app/model/submission_artifacts/manifest.json`

## 6. 关键输出目录快照

### 6.1 研究/模型产物

- `app/model/`

### 6.2 正式推理输出

- `app/output/result.csv`
- `app/output/predict_scores.csv`
- `app/output/debug_candidates.csv`

### 6.3 Demo 与报告图片

- `app/docs/report_supplement_assets/`
- `app/docs/figures/midterm/`

## 7. 说明

- 本文档是“项目整理阶段”的环境快照，不等同于比赛官方评测环境。
- 若后续切换 Python、依赖版本或 Docker 基础镜像，建议同步更新本文件。
