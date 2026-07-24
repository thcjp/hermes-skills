<#
.SYNOPSIS
    Batch upload 600 optimized ClawHub skills to SkillHub via clawhub CLI.
.DESCRIPTION
    Iterates through all skill directories by category and publishes each skill.
    Handles rate limits (429), slug conflicts, and supports resuming.
.PARAMETER StartCategory
    Category to start from (default: all categories)
.PARAMETER DryRun
    Preview without actually publishing
.EXAMPLE
    .\upload-to-skillhub.ps1 -DryRun
    .\upload-to-skillhub.ps1 -StartCategory "Security"
    .\upload-to-skillhub.ps1
#>

param(
    [string]$StartCategory = "",
    [switch]$DryRun = $false,
    [int]$DelaySeconds = 2,
    [int]$RateLimitWaitSeconds = 90
)

$ErrorActionPreference = "Continue"
$SkillsDir = "d:\skills\clawhub-skills\downloaded"
$LogFile = "d:\skills\clawhub-skills\upload-log.csv"

# Category mapping for clawhub publish --categories
$CategoryMap = @{
    "Agents"        = "agents"
    "Creative"      = "creative"
    "Development"   = "development"
    "Automation"    = "automation"
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

# Category display names for changelog
$CategoryCN = @{
    "Agents"        = "智能代理"
    "Creative"      = "创意设计"
    "Development"   = "开发工具"
    "Automation"    = "效率工具"
    "Productivity"  = "商业工具"
    "Communication" = "沟通协作"
    "Knowledge"     = "知识管理"
    "Security"      = "安全工具"
    "Integrations"  = "集成工具"
    "Lifestyle"     = "生活工具"
    "Operations"    = "运维工具"
    "Finance"       = "金融工具"
    "Research"      = "研究工具"
    "Other"         = "其他工具"
}

# Initialize log
if (-not (Test-Path $LogFile)) {
    "timestamp,category,slug,status,http_code,error" | Out-File -FilePath $LogFile -Encoding UTF8
}

function Write-Log {
    param($category, $slug, $status, $httpCode, $error)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts,$category,$slug,$status,$httpCode,$error" | Out-File -FilePath $LogFile -Append -Encoding UTF8
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
    Write-Host "Logged in successfully as $result." -ForegroundColor Green
    return $true
}

function Publish-Skill {
    param(
        [string]$SkillDir,
        [string]$Slug,
        [string]$Category,
        [string]$CategorySlug,
        [string]$CategoryCN,
        [bool]$IsDryRun
    )
    
    $displayName = $Slug -replace '-', ' '
    $displayName = (Get-Culture).TextInfo.ToTitleCase($displayName)
    $changelog = "深度优化版：修复代码块、清除外部引用、移除风险代码、增强元数据，${CategoryCN}分类"
    
    $args = @("--registry", "https://clawhub.ai", "publish", $SkillDir, "--slug", $Slug, "--name", $displayName, "--changelog", $changelog, "--categories", $CategorySlug, "--json")
    
    if ($IsDryRun) {
        $args += "--dry-run"
    }
    
    $maxRetries = 3
    $retryCount = 0
    $success = $false
    
    while ($retryCount -lt $maxRetries -and -not $success) {
        try {
            $output = & clawhub @args 2>&1
            $exitCode = $LASTEXITCODE
            
            if ($exitCode -eq 0) {
                # Check for success in output
                if ($output -match "success|published|created|updated" -or $IsDryRun) {
                    Write-Host "  [OK] $Slug" -ForegroundColor Green
                    Write-Log $Category $Slug "success" "200" ""
                    $success = $true
                } elseif ($output -match "conflict|exists|duplicate") {
                    # Slug conflict - try with suffix
                    $newSlug = "$Slug-pro"
                    Write-Host "  [CONFLICT] $Slug -> trying $newSlug" -ForegroundColor Yellow
                    $args = @("--registry", "https://clawhub.ai", "publish", $SkillDir, "--slug", $newSlug, "--name", $displayName, "--changelog", $changelog, "--categories", $CategorySlug, "--json")
                    if ($IsDryRun) { $args += "--dry-run" }
                    $output = & clawhub @args 2>&1
                    $exitCode = $LASTEXITCODE
                    if ($exitCode -eq 0) {
                        Write-Host "  [OK] $newSlug (renamed)" -ForegroundColor Green
                        Write-Log $Category $Slug "success_renamed" "200" "renamed to $newSlug"
                        $success = $true
                    }
                }
            }
            
            if (-not $success) {
                # Check for rate limit (429)
                if ($output -match "429|rate.*limit|too.*many") {
                    $retryCount++
                    Write-Host "  [RATE LIMIT] $Slug - waiting ${RateLimitWaitSeconds}s (retry $retryCount/$maxRetries)" -ForegroundColor Yellow
                    Start-Sleep -Seconds $RateLimitWaitSeconds
                } elseif ($output -match "auth|unauthorized|401|403") {
                    Write-Host "  [AUTH ERROR] $Slug - please login again" -ForegroundColor Red
                    Write-Log $Category $Slug "auth_error" "401" $output
                    return $false
                } else {
                    $retryCount++
                    $errorMsg = ($output | Select-String -Pattern "error|fail" | Select-Object -First 1).ToString()
                    Write-Host "  [FAIL] $Slug (attempt $retryCount): $errorMsg" -ForegroundColor Red
                    Write-Log $Category $Slug "fail" "$exitCode" $errorMsg
                    Start-Sleep -Seconds 5
                }
            }
        } catch {
            $retryCount++
            Write-Host "  [ERROR] $Slug : $_" -ForegroundColor Red
            Write-Log $Category $Slug "error" "0" $_
            Start-Sleep -Seconds 5
        }
    }
    
    return $success
}

# Main execution
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  SkillHub Batch Upload Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Mode: $(if ($DryRun) {'DRY RUN'} else {'PUBLISH'})"
Write-Host "Delay: ${DelaySeconds}s between skills"
Write-Host "Rate limit wait: ${RateLimitWaitSeconds}s"
Write-Host ""

# Check login
if (-not $DryRun) {
    if (-not (Test-ClawhubLogin)) {
        Write-Host "Cannot continue without login. Exiting." -ForegroundColor Red
        exit 1
    }
}

# Get all category directories
$categories = Get-ChildItem -Path $SkillsDir -Directory | Sort-Object Name

$totalSkills = 0
$successCount = 0
$failCount = 0
$skipCount = 0

foreach ($catDir in $categories) {
    $category = $catDir.Name
    
    # Skip if StartCategory is specified and we haven't reached it
    if ($StartCategory -and $category -lt $StartCategory) {
        continue
    }
    
    $categorySlug = $CategoryMap[$category]
    $categoryCN = $CategoryCN[$category]
    
    if (-not $categorySlug) {
        $categorySlug = "other"
        $categoryCN = "其他工具"
    }
    
    # Get all skill directories in this category
    $skillDirs = Get-ChildItem -Path $catDir.FullName -Directory | Sort-Object Name
    $catCount = $skillDirs.Count
    
    Write-Host "`n--- Category: $category ($categoryCN) - $catCount skills ---" -ForegroundColor Cyan
    
    for ($i = 0; $i -lt $skillDirs.Count; $i++) {
        $skillDir = $skillDirs[$i]
        $slug = $skillDir.Name
        $skillPath = $skillDir.FullName
        
        $progress = "[{0}/{1}] [{2}/{3}]" -f ($i + 1), $catCount, ($totalSkills + 1), 600
        Write-Host "`n$progress Processing: $slug" -ForegroundColor White
        
        $result = Publish-Skill -SkillDir $skillPath -Slug $slug -Category $category -CategorySlug $categorySlug -CategoryCN $categoryCN -IsDryRun $DryRun
        
        if ($result) {
            $successCount++
        } else {
            $failCount++
        }
        
        $totalSkills++
        
        # Delay between skills
        if (-not $DryRun -and $i -lt $skillDirs.Count - 1) {
            Start-Sleep -Seconds $DelaySeconds
        }
    }
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Upload Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total skills processed: $totalSkills"
Write-Host "Successful: $successCount" -ForegroundColor Green
Write-Host "Failed: $failCount" -ForegroundColor Red
Write-Host "Log file: $LogFile"
Write-Host ""
