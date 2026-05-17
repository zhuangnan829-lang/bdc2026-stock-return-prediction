$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$appRoot = $scriptDir
$codeRoot = Join-Path $appRoot "code"
$dataDir = Join-Path $appRoot "data"
$tempDir = Join-Path $appRoot "temp"
$modelDir = Join-Path $appRoot "model"
$outputPath = Join-Path $appRoot "output\result.csv"
$srcRoot = Join-Path $codeRoot "src"
$pythonBin = if ($env:PYTHON_BIN) { $env:PYTHON_BIN } else { "python" }

$previousResultPath = if ($env:PREVIOUS_RESULT_PATH) { $env:PREVIOUS_RESULT_PATH } else { "" }
$autoUsePreviousResult = if ($env:AUTO_USE_PREVIOUS_RESULT) { $env:AUTO_USE_PREVIOUS_RESULT } else { "0" }
$topK = if ($env:TOP_K) { $env:TOP_K } else { "5" }
$primaryCandidateSize = if ($env:PRIMARY_CANDIDATE_SIZE) { $env:PRIMARY_CANDIDATE_SIZE } else { "180" }
$maxVolatility20dPct = if ($env:MAX_VOLATILITY_20D_PCT) { $env:MAX_VOLATILITY_20D_PCT } else { "0.86" }
$maxVolatility5dPct = if ($env:MAX_VOLATILITY_5D_PCT) { $env:MAX_VOLATILITY_5D_PCT } else { "1.0" }
$turnoverRateLowerPct = if ($env:TURNOVER_RATE_LOWER_PCT) { $env:TURNOVER_RATE_LOWER_PCT } else { "0.03" }
$turnoverRateUpperPct = if ($env:TURNOVER_RATE_UPPER_PCT) { $env:TURNOVER_RATE_UPPER_PCT } else { "0.97" }
$turnoverRatioUpperPct = if ($env:TURNOVER_RATIO_UPPER_PCT) { $env:TURNOVER_RATIO_UPPER_PCT } else { "0.95" }
$riskPenaltyWeight = if ($env:RISK_PENALTY_WEIGHT) { $env:RISK_PENALTY_WEIGHT } else { "-0.30" }
$sortStrategy = if ($env:SORT_STRATEGY) { $env:SORT_STRATEGY } else { "risk_adjusted" }
$weightingScheme = if ($env:WEIGHTING_SCHEME) { $env:WEIGHTING_SCHEME } else { "pred" }
$maxTurnover = if ($env:MAX_TURNOVER) { $env:MAX_TURNOVER } else { "1.0" }
$scoreOutputPath = if ($env:SCORE_OUTPUT_PATH) { $env:SCORE_OUTPUT_PATH } else { (Join-Path $appRoot "output\predict_scores.csv") }
$debugCandidatesPath = if ($env:DEBUG_CANDIDATES_PATH) { $env:DEBUG_CANDIDATES_PATH } else { (Join-Path $appRoot "output\debug_candidates.csv") }

& (Join-Path $appRoot "init.ps1")

Push-Location $codeRoot
try {
    if ($autoUsePreviousResult -eq "1" -and [string]::IsNullOrWhiteSpace($previousResultPath) -and (Test-Path -LiteralPath $outputPath)) {
        $previousResultPath = $outputPath
        Write-Host "[test.ps1] auto-detected previous result: $previousResultPath"
    }

    & $pythonBin (Join-Path $srcRoot "featurework.py") `
        --mode predict `
        --data_dir $dataDir `
        --temp_dir $tempDir

    $argsList = @(
        (Join-Path $srcRoot "test_lstm.py"),
        "--feature_path", (Join-Path $tempDir "predict_features.csv"),
        "--model_dir", $modelDir,
        "--output_path", $outputPath,
        "--score_output_path", $scoreOutputPath,
        "--debug_candidates_path", $debugCandidatesPath,
        "--top_k", $topK,
        "--primary_candidate_size", $primaryCandidateSize,
        "--max_volatility_20d_pct", $maxVolatility20dPct,
        "--max_volatility_5d_pct", $maxVolatility5dPct,
        "--turnover_rate_lower_pct", $turnoverRateLowerPct,
        "--turnover_rate_upper_pct", $turnoverRateUpperPct,
        "--turnover_ratio_upper_pct", $turnoverRatioUpperPct,
        "--risk_penalty_weight", $riskPenaltyWeight,
        "--sort_strategy", $sortStrategy,
        "--weighting_scheme", $weightingScheme,
        "--max_turnover", $maxTurnover
    )

    if (-not [string]::IsNullOrWhiteSpace($previousResultPath)) {
        $argsList += @("--previous_result_path", $previousResultPath)
    }

    & $pythonBin @argsList
} finally {
    Pop-Location
}

Write-Host "[test.ps1] inference pipeline completed."
