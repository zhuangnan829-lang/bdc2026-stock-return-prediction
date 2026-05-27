# feature_set_search

This directory records same-protocol comparisons for feature-set changes.

## Candidate

- Baseline 20-feature set: `base_alpha_v3_rs_crowding_mini4`
- Medium candidate: `base_alpha_v4_medium`
- Expected medium feature count: 40-60 columns
- Adoption rule: do not adopt the medium set if it only improves fit/training metrics and does not improve Walk-forward metrics.

## Same-Protocol Commands

Rebuild features:

```powershell
python app/code/src/featurework.py --mode train --data_dir app/data --temp_dir app/temp
```

Train the 20-feature baseline:

```powershell
python app/code/src/train_lstm.py --feature_path app/temp/train_features.csv --model_dir app/model/feature_set_search/base20 --feature_set base_alpha_v3_rs_crowding_mini4
```

Train the medium candidate:

```powershell
python app/code/src/train_lstm.py --feature_path app/temp/train_features.csv --model_dir app/model/feature_set_search/base_alpha_v4_medium --feature_set base_alpha_v4_medium
```

Compare `model_meta.json`, `walk_forward_metrics.csv`, `fold_diagnostics.csv`, and downstream backtest summaries under the same selection and execution configuration.
