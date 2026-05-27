# BDC2026 股票收益预测提交包

本包是 `aggressive_score_submission` 版本，目标是让正式入口和包内已有结果都产出同一份 aggressive 满仓提交结果。

## 提交结果

核心提交文件：

- `app/output/result.csv`

当前结果：

```csv
stock_id,weight
000792,0.2
600233,0.2
601669,0.2
600930,0.19999999999999998
002463,0.19999999999999996
```

- 权重和：`1.000000`
- 可见 case-slice score：`0.077484`
- 变体说明：`PACKAGE_VARIANT.md`
- 机器可读变体信息：`app/model/package_variant.json`
- 答辩展示统一口径：`app/docs/final_presentation_alignment.md`

## 运行入口

本包实际包含以下入口：

- `app/data/run.sh`：Docker/评测容器默认入口。
- `app/run_submission.sh`：正式提交入口。
- `app/test.sh` / `app/test.ps1`：本地推理与校验入口。
- `app/train.sh` / `app/train.ps1`：重新训练入口。

`run_submission.sh`、`test.sh` 和 `test.ps1` 会先跑默认冻结推理，再检测 `app/model/package_variant.json`。当变体为 `aggressive_score_submission` 时，会把 `app/model/aggressive_score_submission_candidate/result_aggressive_score.csv` 同步回 `app/output/result.csv`，因此最终输出会保持为上面的 5 只股票。

## 校验

只校验结果格式：

```bash
python app/code/src/result_validator.py --result_path app/output/result.csv
```

提交前检查：

```bash
python app/code/src/pre_submit_check.py --root_dir . --result_path app/output/result.csv
```

Windows 本地推理链路：

```powershell
powershell -ExecutionPolicy Bypass -File .\app\test.ps1
```

Docker 构建：

```bash
docker build -t bdc2026 .
```

本提交包不包含 `app/docs/`、`app/demo/` 或 `app/run_research_pipeline.sh`；这些属于完整研发仓库内容，不作为本精简提交包入口。
