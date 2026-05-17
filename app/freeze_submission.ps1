$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$appRoot = $scriptDir
$codeRoot = Join-Path $appRoot "code"
$srcRoot = Join-Path $codeRoot "src"
$pythonBin = if ($env:PYTHON_BIN) { $env:PYTHON_BIN } else { "python" }
$resultPath = Join-Path $appRoot "output\result.csv"

Write-Host "[freeze_submission.ps1] sync submission config..."
& $pythonBin (Join-Path $srcRoot "sync_submission_config.py")

Write-Host "[freeze_submission.ps1] run inference..."
& powershell -ExecutionPolicy Bypass -File (Join-Path $appRoot "test.ps1")

Write-Host "[freeze_submission.ps1] validate result.csv..."
& $pythonBin (Join-Path $srcRoot "result_validator.py") `
    --result_path $resultPath

Write-Host "[freeze_submission.ps1] run pre-submit check..."
& $pythonBin (Join-Path $srcRoot "pre_submit_check.py") `
    --root_dir . `
    --result_path "app/output/result.csv"

Write-Host "[freeze_submission.ps1] refresh case comparison..."
& $pythonBin (Join-Path $srcRoot "build_case_program_comparison.py")

Write-Host "[freeze_submission.ps1] submission freeze pipeline completed."
