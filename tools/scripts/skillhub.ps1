# SkillHub CLI 便捷运行器 (PowerShell 包装)
# 用法: .\skillhub.ps1 <command...>
# 示例:
#   .\skillhub.ps1 --version
#   .\skillhub.ps1 auth whoami
#   .\skillhub.ps1 publish .\my-skill --dry-run
#   .\skillhub.ps1 publish .\my-skill --changelog "首次发布"
#   .\skillhub.ps1 search calendar

$GitBash = "C:\Program Files\Git\bin\bash.exe"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RunScript = Join-Path $ScriptDir "run-skillhub.sh"
$OutputFile = Join-Path $ScriptDir ".skillhub-credentials\last-output.txt"

if (-not (Test-Path $GitBash)) {
    Write-Error "Git Bash not found at $GitBash. Please install Git for Windows."
    exit 1
}

# Ensure output file directory exists
$outDir = Split-Path -Parent $OutputFile
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

# Convert all arguments - escape for bash
$argString = $args -join " "

# Execute via Git Bash (output goes to file due to Bad file descriptor issue)
& $GitBash $RunScript $args

# Read and display the output file
if (Test-Path $OutputFile) {
    $content = Get-Content $OutputFile -Raw
    # Extract exit code from last line
    if ($content -match '(?s)\[EXIT_CODE:(\d+)\]$') {
        $exitCode = $matches[1]
        $content = $content -replace '\n?\[EXIT_CODE:\d+\]$', ''
    }
    if ($content.Trim()) { Write-Output $content.Trim() }
}

exit $exitCode
