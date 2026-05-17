# LSTM Dual Objective Search Report

## Objective

- Optimize for both zip-case visible slice score and local walk-forward stability.
- zip current slice score: `0.025179`
- zip reported best score: `0.037838`
- local baseline cumulative_return_after_cost: `0.935572`
- local baseline sharpe_after_cost: `3.629525`
- local baseline max_drawdown_after_cost: `-0.042894`

## Guardrails

- case_slice_score >= `0.037838`
- cumulative_return_after_cost >= `0.608122`
- sharpe_after_cost >= `2.359191`
- max_drawdown_after_cost >= `-0.102894`
- used max_drawdown_slack = `0.060000`
- attempted drawdown slack schedule = `0.02, 0.04, 0.06, 0.08`

## Best Single-Objective Rows

- best case slice row: `dual_cs180_v2086_v5100_rp-80_risk_adjusted_pred_mt100` with case score `0.040557`
- best local row: `dual_cs180_v2086_v5100_rp-80_risk_adjusted_pred_mt100` with cumulative `0.902891` and sharpe `2.952606`

## Recommended Default

- recommended profile: `dual_cs150_v2086_v5100_rp-60_risk_adjusted_pred_mt100`
- recommendation score: `0.694500`
- case slice score: `0.040557`
- cumulative_return_after_cost: `0.671142`
- sharpe_after_cost: `2.416302`
- max_drawdown_after_cost: `-0.099168`
- rationale: case score first, then cumulative return, then sharpe, and finally drawdown stability within the shortlist.

## Shortlist

| profile_name | case_slice_score | cumulative_return_after_cost | sharpe_after_cost | max_drawdown_after_cost |
|---|---:|---:|---:|---:|
| dual_cs150_v2086_v5100_rp-60_risk_adjusted_pred_mt100 | 0.040557 | 0.671142 | 2.416302 | -0.099168 |
| dual_cs120_v2086_v5100_rp-60_risk_adjusted_pred_mt100 | 0.040557 | 0.644852 | 2.422266 | -0.090062 |
| dual_cs150_v2086_v5100_rp-60_risk_adjusted_risk_adjusted_mt100 | 0.038537 | 0.681338 | 2.467104 | -0.095237 |
| dual_cs120_v2086_v5100_rp-60_risk_adjusted_risk_adjusted_mt100 | 0.038835 | 0.647683 | 2.439666 | -0.087975 |
| dual_cs120_v2086_v5100_rp-80_risk_adjusted_risk_adjusted_mt100 | 0.038835 | 0.649135 | 2.399281 | -0.095828 |
| dual_cs150_v2086_v5100_rp-50_risk_adjusted_risk_adjusted_mt100 | 0.038537 | 0.631934 | 2.396343 | -0.087079 |