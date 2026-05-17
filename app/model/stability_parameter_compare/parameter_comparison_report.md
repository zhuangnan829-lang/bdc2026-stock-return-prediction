# Stability Parameter Comparison

## Overview

- This report compares sequence length, risk penalty, sort strategy, and primary candidate size.
- Ranking priority emphasizes worst-fold stability first, then overall rank_ic_mean and backtest quality.

## Ranked Table

| profile_name | sequence_length | sort_strategy | primary_candidate_size | risk_penalty_weight | worst_fold_rank_ic | rank_ic_mean | avg_negative_day_ratio | cum_after_cost | sharpe_after_cost | max_dd_after_cost |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sl20__risk_adjusted__cs150__rp-30 | 20 | risk_adjusted | 150 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 1.087389 | 3.803308 | -0.076012 |
| sl20__pure_prediction__cs150__rp-30 | 20 | pure_prediction | 150 | -0.30 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs150__rp-60 | 20 | pure_prediction | 150 | -0.60 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__pure_prediction__cs150__rp-90 | 20 | pure_prediction | 150 | -0.90 | -0.033492 | 0.027982 | 0.400000 | 0.880322 | 3.842787 | -0.043068 |
| sl20__risk_adjusted__cs150__rp-90 | 20 | risk_adjusted | 150 | -0.90 | -0.033492 | 0.027982 | 0.400000 | 0.791009 | 3.008920 | -0.093423 |
| sl20__risk_adjusted__cs150__rp-60 | 20 | risk_adjusted | 150 | -0.60 | -0.033492 | 0.027982 | 0.400000 | 0.784486 | 3.015071 | -0.103152 |
| sl10__pure_prediction__cs150__rp-30 | 10 | pure_prediction | 150 | -0.30 | -0.060918 | 0.011680 | 0.450000 | 0.946900 | 3.456369 | -0.053180 |
| sl10__pure_prediction__cs150__rp-60 | 10 | pure_prediction | 150 | -0.60 | -0.060918 | 0.011680 | 0.450000 | 0.946900 | 3.456369 | -0.053180 |
| sl10__pure_prediction__cs150__rp-90 | 10 | pure_prediction | 150 | -0.90 | -0.060918 | 0.011680 | 0.450000 | 0.946900 | 3.456369 | -0.053180 |
| sl10__risk_adjusted__cs150__rp-90 | 10 | risk_adjusted | 150 | -0.90 | -0.060918 | 0.011680 | 0.450000 | 0.827100 | 2.789765 | -0.123647 |
| sl10__risk_adjusted__cs150__rp-30 | 10 | risk_adjusted | 150 | -0.30 | -0.060918 | 0.011680 | 0.450000 | 0.773533 | 2.654261 | -0.101649 |
| sl10__risk_adjusted__cs150__rp-60 | 10 | risk_adjusted | 150 | -0.60 | -0.060918 | 0.011680 | 0.450000 | 0.671142 | 2.416302 | -0.099168 |

## Suggested Focus

- Current top candidate: `sl20__risk_adjusted__cs150__rp-30`
- Sequence length: `20`
- Sort strategy: `risk_adjusted`
- Primary candidate size: `150`
- Risk penalty weight: `-0.30`
- Worst fold rank_ic: `-0.033492`
