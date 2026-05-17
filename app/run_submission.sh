#!/bin/bash
set -euo pipefail

echo "[run_submission] starting formal submission entrypoint..."

RUN_TRAIN="${RUN_TRAIN:-0}"
RUN_VALIDATION="${RUN_VALIDATION:-0}"

bash /app/init.sh

if [ "${RUN_TRAIN}" = "1" ]; then
  echo "[run_submission] training enabled for this run"
  bash /app/train.sh
else
  echo "[run_submission] using frozen submission artifacts because RUN_TRAIN=${RUN_TRAIN}"
fi

echo "[run_submission] running frozen inference"
bash /app/test.sh

if [ "${RUN_VALIDATION}" = "1" ]; then
  echo "[run_submission] running result validation"
  python /app/code/src/result_validator.py --result_path /app/output/result.csv
fi

echo "[run_submission] final result.csv"
cat /app/output/result.csv
echo "[run_submission] submission entrypoint completed"
