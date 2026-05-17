# Stability Parameter Comparison

## Overview

- This report compares sequence length, risk penalty, sort strategy, and primary candidate size.
- Ranking priority emphasizes worst-fold stability first, then overall rank_ic_mean and backtest quality.

## Ranked Table

| profile_name | sequence_length | sort_strategy | primary_candidate_size | risk_penalty_weight | worst_fold_rank_ic | rank_ic_mean | avg_negative_day_ratio | cum_after_cost | sharpe_after_cost | max_dd_after_cost |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sl20__risk_adjusted__cs180__rp-30 | 20 | risk_adjusted | 180 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 1.171246 | 4.019488 | -0.090067 |
| sl20__risk_adjusted__cs120__rp-40 | 20 | risk_adjusted | 120 | -0.40 | -0.033492 | 0.027982 | 0.400000 | 1.108458 | 3.929769 | -0.070057 |
| sl20__risk_adjusted__cs150__rp-40 | 20 | risk_adjusted | 150 | -0.40 | -0.033492 | 0.027982 | 0.400000 | 1.092644 | 3.724493 | -0.102938 |
| sl20__risk_adjusted__cs150__rp-30 | 20 | risk_adjusted | 150 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 1.087389 | 3.803308 | -0.076012 |
| sl20__risk_adjusted__cs180__rp-40 | 20 | risk_adjusted | 180 | -0.40 | -0.033492 | 0.027982 | 0.400000 | 1.047878 | 3.678156 | -0.102936 |
| sl20__risk_adjusted__cs180__rp-20 | 20 | risk_adjusted | 180 | -0.20 | -0.033492 | 0.027982 | 0.400000 | 0.981468 | 3.535922 | -0.076012 |
| sl20__risk_adjusted__cs120__rp-30 | 20 | risk_adjusted | 120 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 0.978859 | 3.590073 | -0.065930 |
| sl20__risk_adjusted__cs150__rp-20 | 20 | risk_adjusted | 150 | -0.20 | -0.033492 | 0.027982 | 0.400000 | 0.934878 | 3.446948 | -0.070847 |
| sl20__risk_adjusted__cs120__rp-20 | 20 | risk_adjusted | 120 | -0.20 | -0.033492 | 0.027982 | 0.400000 | 0.885059 | 3.462659 | -0.059219 |
| sl20__pure_prediction__cs120__rp-20 | 20 | pure_prediction | 120 | -0.20 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs150__rp-20 | 20 | pure_prediction | 150 | -0.20 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs180__rp-20 | 20 | pure_prediction | 180 | -0.20 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs120__rp-30 | 20 | pure_prediction | 120 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs150__rp-30 | 20 | pure_prediction | 150 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs180__rp-30 | 20 | pure_prediction | 180 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs120__rp-40 | 20 | pure_prediction | 120 | -0.40 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs150__rp-40 | 20 | pure_prediction | 150 | -0.40 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs180__rp-40 | 20 | pure_prediction | 180 | -0.40 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |

## Suggested Focus

- Current top candidate: `sl20__risk_adjusted__cs180__rp-30`
- Sequence length: `20`
- Sort strategy: `risk_adjusted`
- Primary candidate size: `180`
- Risk penalty weight: `-0.30`
- Worst fold rank_ic: `-0.033492`
