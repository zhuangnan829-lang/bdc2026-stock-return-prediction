# Regime Switch Submission Report

Rule: use robust config only when the recent market state is high-volatility range; otherwise use aggressive config.

## Current Regime

- latest_date: `2026-03-13`
- latest_regime: `normal_or_low_volatility`
- selected_config: `aggressive`
- source: `predict_features_latest_date`
- volatility_threshold_70q: `0.022595`
- range_abs_return_20d_threshold_30q: `0.018578`

## Required Answers

1. Regime switching 是否提升稳定性: no, worst_fold_rank_ic `-0.033492` vs aggressive `-0.033492`.
2. 是否降低高波动震荡阶段回撤: no, high_vol_range_max_drawdown `-0.000850` vs aggressive `0.000000`.
3. 是否牺牲过多收益: yes, cost_after_return loss `0.275039`.
4. 阈值是否简单可解释: yes, volatility_20d uses the training 70% quantile and range uses the 30% quantile of abs(market_return_20d).
5. 是否建议用于最终提交: no, recommendation is `research_only`.

## Summary

| profile | rule | slice | cost_after | sharpe | mdd | turnover | rank_ic | worst_fold | hvr_cost | hvr_mdd | hvr_avg | robust_days | adopted |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| aggressive_static | aggressive_static | 0.025274 | 1.171246 | 4.019488 | -0.090067 | 0.956671 | 0.027982 | -0.033492 | 0.468210 | 0.000000 | 0.028132 | 14 | false |
| robust_static | robust_static | 0.013605 | 0.608495 | 3.824835 | -0.051176 | 0.500000 | 0.027982 | -0.033492 | 0.275864 | -0.001048 | 0.017693 | 14 | false |
| regime_switch | robust_if_high_volatility_range_else_aggressive | 0.013608 | 0.896208 | 3.814060 | -0.090067 | 0.858766 | 0.027982 | -0.033492 | 0.282227 | -0.000850 | 0.018055 | 14 | false |

## Decision

This switch uses the turnover-stress robust candidate, not the earlier rerank robust candidate. If the switch does not beat the aggressive walk-forward profile, keep it as research evidence only.
