# Stability Parameter Comparison

## Overview

- This report compares sequence length, risk penalty, sort strategy, and primary candidate size.
- Ranking priority emphasizes worst-fold stability first, then overall rank_ic_mean and backtest quality.

## Ranked Table

| profile_name | sequence_length | sort_strategy | primary_candidate_size | risk_penalty_weight | worst_fold_rank_ic | rank_ic_mean | avg_negative_day_ratio | cum_after_cost | sharpe_after_cost | max_dd_after_cost |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sl20__risk_adjusted__cs180__rp-30 | 20 | risk_adjusted | 180 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 1.171246 | 4.019488 | -0.090067 |
| sl20__risk_adjusted__cs160__rp-30 | 20 | risk_adjusted | 160 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 1.153215 | 3.973338 | -0.070057 |
| sl20__risk_adjusted__cs160__rp-35 | 20 | risk_adjusted | 160 | -0.35 | -0.033492 | 0.027982 | 0.400000 | 1.141300 | 3.918804 | -0.090067 |
| sl20__risk_adjusted__cs200__rp-25 | 20 | risk_adjusted | 200 | -0.25 | -0.033492 | 0.027982 | 0.400000 | 1.121087 | 3.926588 | -0.090067 |
| sl20__risk_adjusted__cs180__rp-25 | 20 | risk_adjusted | 180 | -0.25 | -0.033492 | 0.027982 | 0.400000 | 1.093771 | 3.841741 | -0.076012 |
| sl20__risk_adjusted__cs200__rp-30 | 20 | risk_adjusted | 200 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 1.090150 | 3.716836 | -0.102938 |
| sl20__risk_adjusted__cs200__rp-35 | 20 | risk_adjusted | 200 | -0.35 | -0.033492 | 0.027982 | 0.400000 | 1.058198 | 3.721711 | -0.102936 |
| sl20__risk_adjusted__cs180__rp-35 | 20 | risk_adjusted | 180 | -0.35 | -0.033492 | 0.027982 | 0.400000 | 1.054132 | 3.698658 | -0.102938 |
| sl20__risk_adjusted__cs160__rp-25 | 20 | risk_adjusted | 160 | -0.25 | -0.033492 | 0.027982 | 0.400000 | 1.018591 | 3.666002 | -0.076012 |

## Suggested Focus

- Current top candidate: `sl20__risk_adjusted__cs180__rp-30`
- Sequence length: `20`
- Sort strategy: `risk_adjusted`
- Primary candidate size: `180`
- Risk penalty weight: `-0.30`
- Worst fold rank_ic: `-0.033492`
