$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$appRoot = $scriptDir
$codeRoot = Join-Path $appRoot "code"
$dataDir = Join-Path $appRoot "data"
$tempDir = Join-Path $appRoot "temp"
$modelDir = Join-Path $appRoot "model"
$srcRoot = Join-Path $codeRoot "src"
$pythonBin = if ($env:PYTHON_BIN) { $env:PYTHON_BIN } else { "python" }

$featureSet = if ($env:FEATURE_SET) { $env:FEATURE_SET } else { "base_alpha_v3_rs_crowding_mini4" }
$targetMode = if ($env:TARGET_MODE) { $env:TARGET_MODE } else { "cross_section_rank" }
$sequenceLength = if ($env:SEQUENCE_LENGTH) { $env:SEQUENCE_LENGTH } else { "10" }
$hiddenSize = if ($env:HIDDEN_SIZE) { $env:HIDDEN_SIZE } else { "64" }
$numLayers = if ($env:NUM_LAYERS) { $env:NUM_LAYERS } else { "1" }
$dropout = if ($env:DROPOUT) { $env:DROPOUT } else { "0.0" }
$learningRate = if ($env:LEARNING_RATE) { $env:LEARNING_RATE } else { "0.001" }
$batchSize = if ($env:BATCH_SIZE) { $env:BATCH_SIZE } else { "256" }
$epochs = if ($env:EPOCHS) { $env:EPOCHS } else { "8" }
$patience = if ($env:PATIENCE) { $env:PATIENCE } else { "2" }

& (Join-Path $appRoot "init.ps1")

Push-Location $codeRoot
try {
    & $pythonBin (Join-Path $srcRoot "featurework.py") `
        --mode train `
        --data_dir $dataDir `
        --temp_dir $tempDir

    & $pythonBin (Join-Path $srcRoot "train_lstm.py") `
        --feature_path (Join-Path $tempDir "train_features.csv") `
        --model_dir $modelDir `
        --feature_set $featureSet `
        --target_mode $targetMode `
        --sequence_length $sequenceLength `
        --hidden_size $hiddenSize `
        --num_layers $numLayers `
        --dropout $dropout `
        --learning_rate $learningRate `
        --batch_size $batchSize `
        --epochs $epochs `
        --patience $patience
} finally {
    Pop-Location
}

Write-Host "[train.ps1] training pipeline completed."
