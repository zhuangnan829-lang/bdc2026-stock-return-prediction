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
OUTPUT_PATH="${APP_ROOT}/output/result.csv"
SRC_ROOT="${CODE_ROOT}/src"
PREVIOUS_RESULT_PATH="${PREVIOUS_RESULT_PATH:-}"
AUTO_USE_PREVIOUS_RESULT="${AUTO_USE_PREVIOUS_RESULT:-0}"
TOP_K="${TOP_K:-5}"
PRIMARY_CANDIDATE_SIZE="${PRIMARY_CANDIDATE_SIZE:-180}"
MAX_VOLATILITY_20D_PCT="${MAX_VOLATILITY_20D_PCT:-0.86}"
MAX_VOLATILITY_5D_PCT="${MAX_VOLATILITY_5D_PCT:-1.0}"
TURNOVER_RATE_LOWER_PCT="${TURNOVER_RATE_LOWER_PCT:-0.03}"
TURNOVER_RATE_UPPER_PCT="${TURNOVER_RATE_UPPER_PCT:-0.97}"
TURNOVER_RATIO_UPPER_PCT="${TURNOVER_RATIO_UPPER_PCT:-0.95}"
RISK_PENALTY_WEIGHT="${RISK_PENALTY_WEIGHT:--0.30}"
SORT_STRATEGY="${SORT_STRATEGY:-risk_adjusted}"
WEIGHTING_SCHEME="${WEIGHTING_SCHEME:-pred}"
MAX_TURNOVER="${MAX_TURNOVER:-1.0}"
SCORE_OUTPUT_PATH="${SCORE_OUTPUT_PATH:-${APP_ROOT}/output/predict_scores.csv}"
DEBUG_CANDIDATES_PATH="${DEBUG_CANDIDATES_PATH:-${APP_ROOT}/output/debug_candidates.csv}"
PYTHON_BIN="${PYTHON_BIN:-python}"

bash "${APP_ROOT}/init.sh"

cd "${CODE_ROOT}"

if [ "${AUTO_USE_PREVIOUS_RESULT}" = "1" ] && [ -z "${PREVIOUS_RESULT_PATH}" ] && [ -f "${OUTPUT_PATH}" ]; then
  PREVIOUS_RESULT_PATH="${OUTPUT_PATH}"
  echo "[test.sh] auto-detected previous result: ${PREVIOUS_RESULT_PATH}"
fi

"${PYTHON_BIN}" "${SRC_ROOT}/featurework.py" \
  --mode predict \
  --data_dir "${DATA_DIR}" \
  --temp_dir "${TEMP_DIR}"

"${PYTHON_BIN}" "${SRC_ROOT}/test_lstm.py" \
  --feature_path "${TEMP_DIR}/predict_features.csv" \
  --model_dir "${MODEL_DIR}" \
  --output_path "${OUTPUT_PATH}" \
  --score_output_path "${SCORE_OUTPUT_PATH}" \
  --debug_candidates_path "${DEBUG_CANDIDATES_PATH}" \
  --top_k "${TOP_K}" \
  --primary_candidate_size "${PRIMARY_CANDIDATE_SIZE}" \
  --max_volatility_20d_pct "${MAX_VOLATILITY_20D_PCT}" \
  --max_volatility_5d_pct "${MAX_VOLATILITY_5D_PCT}" \
  --turnover_rate_lower_pct "${TURNOVER_RATE_LOWER_PCT}" \
  --turnover_rate_upper_pct "${TURNOVER_RATE_UPPER_PCT}" \
  --turnover_ratio_upper_pct "${TURNOVER_RATIO_UPPER_PCT}" \
  --risk_penalty_weight "${RISK_PENALTY_WEIGHT}" \
  --sort_strategy "${SORT_STRATEGY}" \
  --weighting_scheme "${WEIGHTING_SCHEME}" \
  --max_turnover "${MAX_TURNOVER}" \
  ${PREVIOUS_RESULT_PATH:+--previous_result_path "${PREVIOUS_RESULT_PATH}"}

echo "[test.sh] inference pipeline completed."
