#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -d "/app/code" ]; then
  APP_ROOT="/app"
else
  APP_ROOT="${SCRIPT_DIR}"
fi
CODE_ROOT="${APP_ROOT}/code"
SRC_ROOT="${CODE_ROOT}/src"
PYTHON_BIN="${PYTHON_BIN:-python}"

echo "[freeze_submission.sh] sync submission config..."
"${PYTHON_BIN}" "${SRC_ROOT}/sync_submission_config.py"

echo "[freeze_submission.sh] run inference..."
bash "${APP_ROOT}/test.sh"

echo "[freeze_submission.sh] validate result.csv..."
"${PYTHON_BIN}" "${SRC_ROOT}/result_validator.py" \
  --result_path "${APP_ROOT}/output/result.csv"

echo "[freeze_submission.sh] run pre-submit check..."
"${PYTHON_BIN}" "${SRC_ROOT}/pre_submit_check.py" \
  --root_dir / \
  --result_path app/output/result.csv

echo "[freeze_submission.sh] refresh case comparison..."
"${PYTHON_BIN}" "${SRC_ROOT}/build_case_program_comparison.py"

echo "[freeze_submission.sh] submission freeze pipeline completed."
