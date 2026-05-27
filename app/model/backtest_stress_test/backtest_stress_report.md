# Backtest Stress Test

- current_default_profile: `lstm_sl20_base_alpha_v3_rs_crowding_mini4__risk_adjusted_sort__pred_weight__cs180_v2086_v5100_rp-30_mt100`
- transaction_cost_grid: `0.000, 0.001, 0.002, 0.003, 0.005`
- max_turnover_grid: `0.50, 0.75, 1.00`
- weight_cap_grid: `0.16, 0.18, 0.20`
- total_profiles: `45`

## Cost Robustness Answer

- At transaction_cost `0.005`, at least one stressed profile remains positive: `0.725022` after cost.

## Best Profile By Cost

| transaction_cost | profile_name | max_turnover | weight_cap | return | Sharpe | max_drawdown | win_rate |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0.000 | tc0000_mt100_wc20 | 1.00 | 0.20 | 1.291222 | 4.295018 | -0.086348 | 0.733333 |
| 0.001 | tc0010_mt100_wc20 | 1.00 | 0.20 | 1.165010 | 4.002179 | -0.090852 | 0.716667 |
| 0.002 | tc0020_mt100_wc20 | 1.00 | 0.20 | 1.045639 | 3.709768 | -0.095339 | 0.666667 |
| 0.003 | tc0030_mt100_wc20 | 1.00 | 0.20 | 0.932745 | 3.417798 | -0.099808 | 0.650000 |
| 0.005 | tc0050_mt100_wc20 | 1.00 | 0.20 | 0.725022 | 2.835247 | -0.108694 | 0.600000 |

Reference CSV: `backtest_stress_summary.csv`
