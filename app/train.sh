#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -d "/app/code" ]; then
  APP_ROOT="/app"
else
  APP_ROOT="${SCRIPT_DIR}"
fi
CODE_ROOT="${APP_ROOT}/code"
DATA_DIR="${APP_ROOT}/data"
TEMP_DIR="${APP_ROOT}/temp"
MODEL_DIR="${APP_ROOT}/model"
SRC_ROOT="${CODE_ROOT}/src"
PYTHON_BIN="${PYTHON_BIN:-python}"
FEATURE_SET="${FEATURE_SET:-base_alpha_v3_rs_crowding_mini4}"
TARGET_MODE="${TARGET_MODE:-cross_section_rank}"
SEQUENCE_LENGTH="${SEQUENCE_LENGTH:-10}"
HIDDEN_SIZE="${HIDDEN_SIZE:-64}"
NUM_LAYERS="${NUM_LAYERS:-1}"
DROPOUT="${DROPOUT:-0.0}"
LEARNING_RATE="${LEARNING_RATE:-0.001}"
BATCH_SIZE="${BATCH_SIZE:-256}"
EPOCHS="${EPOCHS:-8}"
PATIENCE="${PATIENCE:-2}"

bash "${APP_ROOT}/init.sh"

cd "${CODE_ROOT}"

"${PYTHON_BIN}" "${SRC_ROOT}/featurework.py" \
  --mode train \
  --data_dir "${DATA_DIR}" \
  --temp_dir "${TEMP_DIR}"

"${PYTHON_BIN}" "${SRC_ROOT}/train_lstm.py" \
  --feature_path "${TEMP_DIR}/train_features.csv" \
  --model_dir "${MODEL_DIR}" \
  --feature_set "${FEATURE_SET}" \
  --target_mode "${TARGET_MODE}" \
  --sequence_length "${SEQUENCE_LENGTH}" \
  --hidden_size "${HIDDEN_SIZE}" \
  --num_layers "${NUM_LAYERS}" \
  --dropout "${DROPOUT}" \
  --learning_rate "${LEARNING_RATE}" \
  --batch_size "${BATCH_SIZE}" \
  --epochs "${EPOCHS}" \
  --patience "${PATIENCE}"

echo "[train.sh] training pipeline completed."
