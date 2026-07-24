<#
.SYNOPSIS
    Batch upload 60 packaged skills to SkillHub (free) and ClawHub.
.DESCRIPTION
    Uploads all 60 packaged skills:
    - 20 JueJin skills from d:\skills\packaged-skills\skillhub\
    - 40 OpenSource skills from d:\skills\opensource-skills\packaged\
    Each skill is uploaded to:
    - SkillHub (personal account, free, via skh_ token)
    - ClawHub (via clh_ token)
#>

$ErrorActionPreference = "Continue"

# Directories
$JueJinDir = "d:\skills\packaged-skills\skillhub"
$OpenSourceDir = "d:\skills\opensource-skills\packaged"

# Credentials
$SkillHubToken = "skh_7906ab19cefaf3854349fae7b8b97310c5582073b76acf1557731c0f1c612c11"
$ClawHubToken = "clh_FYKOzz03rZocoNFDQiP8w1Z6JLIPDsORrCIJzjtBHdg"

# Log file
$LogFile = "d:\skills\packaged-skills\upload-log.csv"
if (-not (Test-Path $LogFile)) {
    "timestamp,platform,source,slug,status,http_code,error" | Out-File -FilePath $LogFile -Encoding UTF8
}

function Write-Log {
    param($platform, $source, $slug, $status, $httpCode, $error)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts,$platform,$source,$slug,$status,$httpCode,$error" | Out-File -FilePath $LogFile -Append -Encoding UTF8
}

function Upload-ToSkillHub {
    param([string]$SkillDir, [string]$Slug, [string]$Source, [bool]$DryRun)
    
    $changelog = "TRACE增强版：五维度评分A级，8标准章节完整，国内替代方案覆盖，营销优化"
    
    $args = @("C:\Users\thcd\.skillhub\skills_store_cli.py", "publish", $SkillDir, 
              "--token", $SkillHubToken, "--changelog", $changelog, "--json")
    
    if ($DryRun) {
        $args += "--dry-run"
    }
    
    try {
        $output = & python @args 2>&1
        $exitCode = $LASTEXITCODE
        
        if ($exitCode -eq 0 -and ($output -match "success|published|created|updated|ok")) {
            Write-Host "  [SkillHub OK] $Slug" -ForegroundColor Green
            Write-Log "skillhub" $Source $Slug "success" "200" ""
            return $true
        } elseif ($output -match "conflict|exists|duplicate|409") {
            Write-Host "  [SkillHub EXISTS] $Slug (already uploaded)" -ForegroundColor Yellow
            Write-Log "skillhub" $Source $Slug "exists" "409" ""
            return $true
        } else {
            $errorMsg = ($output | Out-String).Substring(0, [Math]::Min(200, ($output | Out-String).Length))
            Write-Host "  [SkillHub FAIL] $Slug : $errorMsg" -ForegroundColor Red
            Write-Log "skillhub" $Source $Slug "fail" "$exitCode" $errorMsg
            return $false
        }
    } catch {
        Write-Host "  [SkillHub ERROR] $Slug : $_" -ForegroundColor Red
        Write-Log "skillhub" $Source $Slug "error" "0" $_
        return $false
    }
}

function Upload-ToClawHub {
    param([string]$SkillDir, [string]$Slug, [string]$Source, [bool]$DryRun)
    
    $changelog = "TRACE增强版：五维度评分A级，8标准章节完整，国内替代方案覆盖"
    
    $args = @("--registry", "https://clawhub.ai", "publish", $SkillDir, 
              "--changelog", $changelog, "--json")
    
    if ($DryRun) {
        $args += "--dry-run"
    }
    
    try {
        $output = & clawhub @args 2>&1
        $exitCode = $LASTEXITCODE
        
        if ($exitCode -eq 0 -and ($output -match "success|published|created|updated|ok")) {
            Write-Host "  [ClawHub OK] $Slug" -ForegroundColor Green
            Write-Log "clawhub" $Source $Slug "success" "200" ""
            return $true
        } elseif ($output -match "conflict|exists|duplicate|409") {
            Write-Host "  [ClawHub EXISTS] $Slug (already uploaded)" -ForegroundColor Yellow
            Write-Log "clawhub" $Source $Slug "exists" "409" ""
            return $true
        } else {
            $errorMsg = ($output | Out-String).Substring(0, [Math]::Min(200, ($output | Out-String).Length))
            Write-Host "  [ClawHub FAIL] $Slug : $errorMsg" -ForegroundColor Red
            Write-Log "clawhub" $Source $Slug "fail" "$exitCode" $errorMsg
            return $false
        }
    } catch {
        Write-Host "  [ClawHub ERROR] $Slug : $_" -ForegroundColor Red
        Write-Log "clawhub" $Source $Slug "error" "0" $_
        return $false
    }
}

# Parse arguments
$DryRun = $false
$StartFrom = ""
$PlatformOnly = ""  # "skillhub" or "clawhub" or "" (both)
foreach ($arg in $args) {
    if ($arg -eq "--dry-run") { $DryRun = $true }
    if ($arg -eq "--skillhub-only") { $PlatformOnly = "skillhub" }
    if ($arg -eq "--clawhub-only") { $PlatformOnly = "clawhub" }
    if ($arg -match "^--start=(.+)$") { $StartFrom = $Matches[1] }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  60 Packaged Skills Batch Upload" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Mode: $(if ($DryRun) {'DRY RUN'} else {'PUBLISH'})"
Write-Host "Platform: $(if ($PlatformOnly) {$PlatformOnly} else {'both'})"
Write-Host ""

# Collect all skill directories
$allSkills = @()

# JueJin 20 skills (P0-P2)
if (Test-Path $JueJinDir) {
    $juejinSkills = Get-ChildItem -Path $JueJinDir -Directory | Sort-Object Name
    foreach ($d in $juejinSkills) {
        if (($d | Get-ChildItem -Filter "SKILL.md" -ErrorAction SilentlyContinue)) {
            $allSkills += @{Dir=$d; Slug=$d.Name; Source="juejin"}
        }
    }
}

# OpenSource 40 skills (P3-P5)
if (Test-Path $OpenSourceDir) {
    $osSkills = Get-ChildItem -Path $OpenSourceDir -Directory | Sort-Object Name
    foreach ($d in $osSkills) {
        if (($d | Get-ChildItem -Filter "SKILL.md" -ErrorAction SilentlyContinue)) {
            $allSkills += @{Dir=$d; Slug=$d.Name; Source="opensource"}
        }
    }
}

Write-Host "Total skills to upload: $($allSkills.Count)"
Write-Host ""

$successCount = 0
$failCount = 0
$skipCount = 0
$started = $StartFrom -eq ""

for ($i = 0; $i -lt $allSkills.Count; $i++) {
    $skill = $allSkills[$i]
    $slug = $skill.Slug
    $skillDir = $skill.Dir.FullName
    $source = $skill.Source
    
    if (-not $started) {
        if ($slug -eq $StartFrom) {
            $started = $true
        } else {
            $skipCount++
            continue
        }
    }
    
    $progress = "[{0}/{1}]" -f ($i + 1), $allSkills.Count
    Write-Host "`n$progress $slug ($source)" -ForegroundColor White
    
    # Upload to SkillHub
    if ($PlatformOnly -ne "clawhub") {
        $result = Upload-ToSkillHub -SkillDir $skillDir -Slug $slug -Source $source -DryRun $DryRun
        if ($result) { $successCount++ } else { $failCount++ }
        Start-Sleep -Seconds 1
    }
    
    # Upload to ClawHub
    if ($PlatformOnly -ne "skillhub") {
        $result = Upload-ToClawHub -SkillDir $skillDir -Slug $slug -Source $source -DryRun $DryRun
        if ($result) { $successCount++ } else { $failCount++ }
        Start-Sleep -Seconds 1
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Upload Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total processed: $($allSkills.Count - $skipCount)"
Write-Host "Successful: $successCount" -ForegroundColor Green
Write-Host "Failed: $failCount" -ForegroundColor Red
Write-Host "Skipped: $skipCount" -ForegroundColor Yellow
Write-Host "Log file: $LogFile"
Write-Host ""
