<#
.SYNOPSIS
    Batch upload 51 differentiated skills to both SkillHub and ClawHub.
.DESCRIPTION
    Reads differentiated skills from d:\skills\differentiated-skills
    Uploads to both platforms with new slugs to avoid conflicts.
.PARAMETER Platform
    "skillhub", "clawhub", or "both" (default: both)
.PARAMETER DryRun
    Preview without actually publishing
#>

param(
    [string]$Platform = "both",
    [switch]$DryRun = $false,
    [int]$DelaySeconds = 3,
    [int]$RateLimitWaitSeconds = 90
)

$ErrorActionPreference = "Continue"
$SkillsDir = "d:\skills\differentiated-skills"
$LogFile = "d:\skills\differentiated-skills\upload-log.csv"
$SkillHubScript = "d:\skills\skillhub.ps1"

# Category mapping for clawhub publish --categories
$CategoryMap = @{
    "Agents"        = "agents"
    "Automation"    = "automation"
    "Creative"      = "creative"
    "Development"   = "development"
    "Productivity"  = "productivity"
    "Communication" = "communication"
    "Knowledge"     = "knowledge"
    "Security"      = "security"
    "Integrations"  = "integrations"
    "Lifestyle"     = "lifestyle"
    "Operations"    = "operations"
    "Finance"       = "finance"
    "Research"      = "research"
    "Other"         = "other"
}

# Initialize log
if (-not (Test-Path $LogFile)) {
    "timestamp,platform,category,slug,status,http_code,error" | Out-File -FilePath $LogFile -Encoding UTF8
}

function Write-Log {
    param($platform, $category, $slug, $status, $httpCode, $error)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts,$platform,$category,$slug,$status,$httpCode,$error" | Out-File -FilePath $LogFile -Append -Encoding UTF8
}

function Get-SkillMetadata {
    param([string]$SkillDir)

    $skillFile = Join-Path $SkillDir "SKILL.md"
    if (-not (Test-Path $skillFile)) {
        return $null
    }

    $content = Get-Content $skillFile -Raw -Encoding UTF8
    $metadata = @{}

    # Extract frontmatter between --- markers
    if ($content -match "(?s)^---\r?\n(.*?)\r?\n---") {
        $frontmatter = $matches[1]

        # Parse each field
        $lines = $frontmatter -split "`r?`n"
        $currentField = $null
        $currentValue = @()

        foreach ($line in $lines) {
            if ($line -match "^(\w+):\s*(.*)$") {
                if ($currentField) {
                    $metadata[$currentField] = ($currentValue -join "`n").Trim()
                }
                $currentField = $matches[1]
                $currentValue = @()
                if ($matches[2] -and $matches[2] -ne "|-" -and $matches[2] -ne "|") {
                    $val = $matches[2].Trim('"').Trim("'")
                    if ($val) {
                        $currentValue = @($val)
                    }
                }
            } elseif ($line -match "^  -\s+(.*)$" -and $currentField) {
                # Array item
                if ($metadata[$currentField] -is [string]) {
                    $metadata[$currentField] = @($metadata[$currentField])
                }
                if ($metadata[$currentField] -isnot [array]) {
                    $metadata[$currentField] = @()
                }
                $metadata[$currentField] += $matches[1].Trim()
                $currentField = $null  # Array field, don't accumulate
            } elseif ($line -match "^  (.+)$" -and $currentField) {
                $currentValue += $matches[1]
            }
        }
        if ($currentField) {
            $metadata[$currentField] = ($currentValue -join "`n").Trim()
        }
    }

    return $metadata
}

function Test-ClawhubLogin {
    Write-Host "Checking clawhub login status..." -ForegroundColor Cyan
    $result = clawhub --registry https://clawhub.ai whoami 2>&1
    if ($LASTEXITCODE -ne 0 -or $result -match "not.*logged|error|fail") {
        Write-Host "Not logged in to ClawHub. Starting login..." -ForegroundColor Yellow
        $clawhubToken = Get-Content "d:\skills\.skillhub-credentials\clawhub-token.txt" -Raw
        $clawhubToken = $clawhubToken.Trim()
        clawhub --registry https://clawhub.ai login --token $clawhubToken 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Login failed. Please run 'clawhub login' manually." -ForegroundColor Red
            return $false
        }
    }
    Write-Host "Logged in to ClawHub successfully." -ForegroundColor Green
    return $true
}

function Test-SkillHubLogin {
    Write-Host "Checking SkillHub login status..." -ForegroundColor Cyan
    $result = & $SkillHubScript "whoami" 2>&1
    $outputFile = "d:\skills\.skillhub-credentials\last-output.txt"
    if (Test-Path $outputFile) {
        $output = Get-Content $outputFile -Raw
        if ($output -match "userId" -and $output -match "EXIT_CODE:0") {
            Write-Host "Logged in to SkillHub successfully." -ForegroundColor Green
            return $true
        }
    }
    Write-Host "SkillHub login check failed." -ForegroundColor Yellow
    return $true  # Continue anyway, the API key is hardcoded in wrapper
}

function Publish-ToClawhub {
    param(
        [string]$SkillDir,
        [string]$Slug,
        [string]$DisplayName,
        [string]$CategorySlug,
        [string]$CategoryCN,
        [bool]$IsDryRun
    )

    $changelog = "深度差异化版：基于用户痛点研究完全重写，新增FAQ、故障排查、场景化指南，${CategoryCN}分类"

    $publishArgs = @(
        "--registry", "https://clawhub.ai",
        "publish", $SkillDir,
        "--slug", $Slug,
        "--name", $DisplayName,
        "--changelog", $changelog,
        "--categories", $CategorySlug,
        "--json"
    )

    if ($IsDryRun) {
        $publishArgs += "--dry-run"
    }

    $maxRetries = 3
    $retryCount = 0

    while ($retryCount -lt $maxRetries) {
        try {
            $output = & clawhub @publishArgs 2>&1
            $exitCode = $LASTEXITCODE

            if ($exitCode -eq 0 -and ($output -match "success|published|created|updated" -or $IsDryRun)) {
                Write-Host "  [clawhub OK] $Slug" -ForegroundColor Green
                Write-Log "clawhub" $CategoryCN $Slug "success" "200" ""
                return $true
            }

            # Check for rate limit (429)
            if ($output -match "429|rate.*limit|too.*many") {
                $retryCount++
                Write-Host "  [clawhub RATE LIMIT] $Slug - waiting ${RateLimitWaitSeconds}s (retry $retryCount/$maxRetries)" -ForegroundColor Yellow
                Start-Sleep -Seconds $RateLimitWaitSeconds
                continue
            }

            # Check for slug conflict
            if ($output -match "conflict|exists|duplicate|already") {
                Write-Host "  [clawhub CONFLICT] $Slug - slug already exists, skipping" -ForegroundColor Yellow
                Write-Log "clawhub" $CategoryCN $Slug "conflict" "409" $output
                return $false
            }

            # Other error
            $retryCount++
            $errorMsg = ($output | Out-String).Substring(0, [Math]::Min(200, ($output | Out-String).Length))
            Write-Host "  [clawhub FAIL] $Slug (attempt $retryCount): $errorMsg" -ForegroundColor Red
            Write-Log "clawhub" $CategoryCN $Slug "fail" "$exitCode" $errorMsg
            Start-Sleep -Seconds 5
        } catch {
            $retryCount++
            Write-Host "  [clawhub ERROR] $Slug : $_" -ForegroundColor Red
            Write-Log "clawhub" $CategoryCN $Slug "error" "0" $_
            Start-Sleep -Seconds 5
        }
    }

    return $false
}

function Publish-ToSkillhub {
    param(
        [string]$SkillDir,
        [string]$Slug,
        [string]$DisplayName,
        [string]$CategoryCN,
        [bool]$IsDryRun
    )

    $changelog = "深度差异化版：基于用户痛点研究完全重写，新增FAQ、故障排查、场景化指南，${CategoryCN}分类"
    $token = Get-Content "d:\skills\.skillhub-credentials\api-key.txt" -Raw
    $token = $token.Trim()

    $publishArgs = @("publish", $SkillDir, "--changelog", $changelog, "--token", $token, "--json")
    if ($IsDryRun) {
        $publishArgs += "--dry-run"
    }

    $maxRetries = 3
    $retryCount = 0

    while ($retryCount -lt $maxRetries) {
        try {
            # Use the skillhub.ps1 wrapper to publish
            & $SkillHubScript @publishArgs 2>&1 | Out-Null

            # Read the output file
            $outputFile = "d:\skills\.skillhub-credentials\last-output.txt"
            $outputContent = ""
            if (Test-Path $outputFile) {
                $outputContent = Get-Content $outputFile -Raw
            }

            if ($outputContent -match "EXIT_CODE:0") {
                if ($outputContent -match "success|published|created|ok|version" -or $IsDryRun) {
                    Write-Host "  [skillhub OK] $Slug" -ForegroundColor Green
                    Write-Log "skillhub" $CategoryCN $Slug "success" "200" ""
                    return $true
                }
            }

            # Check for rate limit
            if ($outputContent -match "429|rate.*limit|too.*many") {
                $retryCount++
                Write-Host "  [skillhub RATE LIMIT] $Slug - waiting ${RateLimitWaitSeconds}s (retry $retryCount/$maxRetries)" -ForegroundColor Yellow
                Start-Sleep -Seconds $RateLimitWaitSeconds
                continue
            }

            # Check for slug conflict
            if ($outputContent -match "conflict|exists|duplicate|already|occupied|已被") {
                Write-Host "  [skillhub CONFLICT] $Slug - slug already exists, skipping" -ForegroundColor Yellow
                Write-Log "skillhub" $CategoryCN $Slug "conflict" "409" $outputContent
                return $false
            }

            # Other error
            $retryCount++
            $errorMsg = $outputContent.Substring(0, [Math]::Min(200, $outputContent.Length))
            Write-Host "  [skillhub FAIL] $Slug (attempt $retryCount): $errorMsg" -ForegroundColor Red
            Write-Log "skillhub" $CategoryCN $Slug "fail" "1" $errorMsg
            Start-Sleep -Seconds 5
        } catch {
            $retryCount++
            Write-Host "  [skillhub ERROR] $Slug : $_" -ForegroundColor Red
            Write-Log "skillhub" $CategoryCN $Slug "error" "0" $_
            Start-Sleep -Seconds 5
        }
    }

    return $false
}

# Main execution
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Differentiated Skills Upload Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Platform: $Platform"
Write-Host "Mode: $(if ($DryRun) {'DRY RUN'} else {'PUBLISH'})"
Write-Host "Delay: ${DelaySeconds}s between skills"
Write-Host ""

# Check login
if (-not $DryRun) {
    if ($Platform -eq "both" -or $Platform -eq "clawhub") {
        if (-not (Test-ClawhubLogin)) {
            Write-Host "Cannot continue without clawhub login. Exiting clawhub upload." -ForegroundColor Red
            if ($Platform -eq "clawhub") { exit 1 }
        }
    }
    if ($Platform -eq "both" -or $Platform -eq "skillhub") {
        Test-SkillHubLogin | Out-Null
    }
}

# Get all category directories
$categories = Get-ChildItem -Path $SkillsDir -Directory | Sort-Object Name

$totalSkills = 0
$clawhubSuccess = 0
$clawhubFail = 0
$skillhubSuccess = 0
$skillhubFail = 0

foreach ($catDir in $categories) {
    $category = $catDir.Name
    $categorySlug = $CategoryMap[$category]
    if (-not $categorySlug) { $categorySlug = "other" }

    $categoryCN = switch ($category) {
        "Agents" { "智能代理" }
        "Automation" { "效率工具" }
        "Creative" { "创意设计" }
        "Development" { "开发工具" }
        "Productivity" { "商业工具" }
        "Communication" { "沟通协作" }
        "Knowledge" { "知识管理" }
        "Security" { "安全工具" }
        "Integrations" { "集成工具" }
        "Lifestyle" { "生活工具" }
        "Operations" { "运维工具" }
        "Finance" { "金融工具" }
        "Research" { "研究工具" }
        default { "其他工具" }
    }

    # Get all skill directories in this category
    $skillDirs = Get-ChildItem -Path $catDir.FullName -Directory | Sort-Object Name
    $catCount = $skillDirs.Count

    Write-Host "`n--- Category: $category ($categoryCN) - $catCount skills ---" -ForegroundColor Cyan

    foreach ($skillDir in $skillDirs) {
        $totalSkills++
        $skillPath = $skillDir.FullName

        # Read metadata from SKILL.md frontmatter
        $metadata = Get-SkillMetadata -SkillDir $skillPath
        if (-not $metadata -or -not $metadata.slug) {
            Write-Host "[$totalSkills/51] SKIP $($skillDir.Name) - no valid SKILL.md frontmatter" -ForegroundColor Red
            continue
        }

        $slug = $metadata.slug
        $displayName = if ($metadata.displayName) { $metadata.displayName } else { $slug }
        $summary = if ($metadata.summary) { $metadata.summary } else { "" }

        Write-Host "`n[$totalSkills/51] Processing: $slug ($displayName)" -ForegroundColor White

        # Upload to clawhub
        if ($Platform -eq "both" -or $Platform -eq "clawhub") {
            $result = Publish-ToClawhub -SkillDir $skillPath -Slug $slug -DisplayName $displayName -CategorySlug $categorySlug -CategoryCN $categoryCN -IsDryRun $DryRun
            if ($result) { $clawhubSuccess++ } else { $clawhubFail++ }
        }

        # Upload to skillhub
        if ($Platform -eq "both" -or $Platform -eq "skillhub") {
            $result = Publish-ToSkillhub -SkillDir $skillPath -Slug $slug -DisplayName $displayName -CategoryCN $categoryCN -IsDryRun $DryRun
            if ($result) { $skillhubSuccess++ } else { $skillhubFail++ }
        }

        # Delay between skills
        if (-not $DryRun) {
            Start-Sleep -Seconds $DelaySeconds
        }
    }
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Upload Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total skills processed: $totalSkills"
if ($Platform -eq "both" -or $Platform -eq "clawhub") {
    Write-Host "ClawHub - Successful: $clawhubSuccess, Failed: $clawhubFail" -ForegroundColor $(if ($clawhubFail -eq 0) {'Green'} else {'Yellow'})
}
if ($Platform -eq "both" -or $Platform -eq "skillhub") {
    Write-Host "SkillHub - Successful: $skillhubSuccess, Failed: $skillhubFail" -ForegroundColor $(if ($skillhubFail -eq 0) {'Green'} else {'Yellow'})
}
Write-Host "Log file: $LogFile"
Write-Host ""
