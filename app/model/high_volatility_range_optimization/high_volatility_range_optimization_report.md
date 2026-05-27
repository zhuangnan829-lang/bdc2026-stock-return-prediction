# High Volatility Range Optimization Report

目标：只针对高波动震荡阶段做专项优化，不推翻 LSTM sl20 主线。

## Current Regime Decision

- latest_date: `2026-03-13`
- latest_regime: `normal_or_low_volatility`
- selected_config_by_rule: `aggressive`
- source: `predict_features_latest_date`

## Profile Comparison

| profile | rule | total_return | sharpe | max_dd | avg_turnover | hvr_return | hvr_max_dd | hvr_avg_return | return_loss_vs_mainline | next_step |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mainline_static | current_default_submission_config | 1.085936 | 3.977455 | -0.087064 | 0.931137 | 0.437007 | 0.000000 | 0.026529 | 0.000000 | hold |
| aggressive_static | submission_aggressive_static | 1.165010 | 4.002179 | -0.090852 | 0.956291 | 0.469572 | 0.000000 | 0.028202 | -0.079074 | hold |
| robust_static | submission_robust_static | 0.653410 | 4.053580 | -0.048990 | 0.500000 | 0.283646 | -0.000539 | 0.018135 | 0.432526 | hold |
| regime_switch | robust_if_high_volatility_range_else_aggressive | 0.900501 | 3.825155 | -0.090852 | 0.858719 | 0.290028 | -0.000338 | 0.018496 | 0.185435 | hold |

## Decision

- recommend_regime_switch: `false`
- recommend_robust_observation: `true`
- switch_return_loss_vs_mainline: `0.185435`
- aggressive_return_delta_vs_mainline: `0.079074`
- final: 暂不采用 regime_switch；robust_static 可作为风险观察配置，但收益损失需要继续压缩。

## Next Step

如果继续推进，下一步应该做阈值网格：volatility quantile 0.60/0.65/0.70/0.75，range quantile 0.25/0.30/0.35/0.40，并要求收益损失不超过 0.05、换手下降、HVR 回撤不恶化。
