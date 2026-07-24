﻿﻿<#
.SYNOPSIS
    Retry failed SkillHub uploads with longer delays.
#>

$ErrorActionPreference = "Continue"
$SkillHubScript = "d:\skills\skillhub.ps1"
$token = Get-Content "d:\skills\.skillhub-credentials\api-key.txt" -Raw
$token = $token.Trim()
$LogFile = "d:\skills\differentiated-skills\retry-skillhub-log.csv"
$delaySeconds = 180  # 3 minutes between each skill

if (-not (Test-Path $LogFile)) {
    "timestamp,slug,status,error" | Out-File -FilePath $LogFile -Encoding UTF8
}

# Known failed skills from the upload output
# Conflicts (4): slug already exists - need renaming
# Server errors (3): 566 server error - retry
# Rate-limited (14+): rate limit exhausted - retry with longer delay
$failedSkills = @(
    @{slug="evolution-engine"; path="d:\skills\differentiated-skills\Agents\evolution-engine"; conflict=$true},
    @{slug="memory-distiller"; path="d:\skills\differentiated-skills\Agents\memory-distiller"; conflict=$true},
    @{slug="memory-orchestrator"; path="d:\skills\differentiated-skills\Agents\memory-orchestrator"; conflict=$true},
    @{slug="multi-agent-dev"; path="d:\skills\differentiated-skills\Agents\multi-agent-dev"; conflict=$true},
    @{slug="cdp-browser-master"; path="d:\skills\differentiated-skills\Automation\cdp-browser-master"; conflict=$false},
    @{slug="cron-guard"; path="d:\skills\differentiated-skills\Automation\cron-guard"; conflict=$false},
    @{slug="linear-workflow-bot"; path="d:\skills\differentiated-skills\Automation\linear-workflow-bot"; conflict=$false},
    @{slug="cad-insight-pro"; path="d:\skills\differentiated-skills\Automation\cad-insight-pro"; conflict=$false},
    @{slug="cloud-ops-orchestrator"; path="d:\skills\differentiated-skills\Automation\cloud-ops-orchestrator"; conflict=$false},
    @{slug="cron-assist"; path="d:\skills\differentiated-skills\Automation\cron-assist"; conflict=$false},
    @{slug="cron-master-pro"; path="d:\skills\differentiated-skills\Automation\cron-master-pro"; conflict=$false},
    @{slug="cron-scheduler-pro"; path="d:\skills\differentiated-skills\Automation\cron-scheduler-pro"; conflict=$false},
    @{slug="desktop-autopilot"; path="d:\skills\differentiated-skills\Automation\desktop-autopilot"; conflict=$false},
    @{slug="excel-maestro"; path="d:\skills\differentiated-skills\Automation\excel-maestro"; conflict=$false},
    @{slug="flow-architect"; path="d:\skills\differentiated-skills\Automation\flow-architect"; conflict=$false},
    @{slug="flow-editor-pro"; path="d:\skills\differentiated-skills\Automation\flow-editor-pro"; conflict=$false},
    @{slug="linear-cli-pro"; path="d:\skills\differentiated-skills\Automation\linear-cli-pro"; conflict=$false},
    @{slug="macro-pulse"; path="d:\skills\differentiated-skills\Automation\macro-pulse"; conflict=$false},
    @{slug="notes-cli-toolkit"; path="d:\skills\differentiated-skills\Automation\notes-cli-toolkit"; conflict=$false},
    @{slug="office-productivity-hub"; path="d:\skills\differentiated-skills\Automation\office-productivity-hub"; conflict=$false},
    @{slug="pcb-design-assistant"; path="d:\skills\differentiated-skills\Automation\pcb-design-assistant"; conflict=$false},
    @{slug="security-radar"; path="d:\skills\differentiated-skills\Automation\security-radar"; conflict=$false},
    @{slug="system-controller"; path="d:\skills\differentiated-skills\Automation\system-controller"; conflict=$false},
    @{slug="update-guardian"; path="d:\skills\differentiated-skills\Automation\update-guardian"; conflict=$false},
    @{slug="vault-master-pro"; path="d:\skills\differentiated-skills\Automation\vault-master-pro"; conflict=$false},
    @{slug="vault-sync-engine"; path="d:\skills\differentiated-skills\Automation\vault-sync-engine"; conflict=$false},
    @{slug="workflow-lite"; path="d:\skills\differentiated-skills\Automation\workflow-lite"; conflict=$false},
    @{slug="workflow-symphony"; path="d:\skills\differentiated-skills\Automation\workflow-symphony"; conflict=$false}
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SkillHub Retry Script ($($failedSkills.Count) skills)" -ForegroundColor Cyan
Write-Host "  Delay: ${delaySeconds}s between skills" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

$successCount = 0
$failCount = 0

for ($i = 0; $i -lt $failedSkills.Count; $i++) {
    $skill = $failedSkills[$i]
    $slug = $skill.slug
    $path = $skill.path
    $isConflict = $skill.conflict

    Write-Host "`n[$($i+1)/$($failedSkills.Count)] Processing: $slug (conflict: $isConflict)" -ForegroundColor White

    # For conflicts, try with -v2 suffix
    $actualSlug = $slug
    if ($isConflict) {
        $actualSlug = "$slug-v2"
        # Update the SKILL.md slug field
        $skillFile = Join-Path $path "SKILL.md"
        $content = Get-Content $skillFile -Raw -Encoding UTF8
        $newContent = $content -replace "^slug:\s*$slug", "slug: $actualSlug"
        Set-Content -Path $skillFile -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "  Renamed slug: $slug -> $actualSlug" -ForegroundColor Yellow
    }

    $changelog = "深度差异化版重试上传：基于用户痛点研究完全重写"

    try {
        & $SkillHubScript publish $path --changelog $changelog --token $token --json 2>&1 | Out-Null

        $outputFile = "d:\skills\.skillhub-credentials\last-output.txt"
        $outputContent = ""
        if (Test-Path $outputFile) {
            $outputContent = Get-Content $outputFile -Raw
        }

        $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

        if ($outputContent -match "EXIT_CODE:0" -and $outputContent -match "success|published|created|ok|version") {
            Write-Host "  [OK] $actualSlug" -ForegroundColor Green
            "$ts,$actualSlug,success," | Out-File -FilePath $LogFile -Append -Encoding UTF8
            $successCount++
        } elseif ($outputContent -match "conflict|exists|duplicate|already|occupied|已被") {
            Write-Host "  [CONFLICT] $actualSlug - slug already exists" -ForegroundColor Yellow
            "$ts,$actualSlug,conflict,$($outputContent.Substring(0, [Math]::Min(200, $outputContent.Length)))" | Out-File -FilePath $LogFile -Append -Encoding UTF8
            $failCount++
        } else {
            $errorMsg = $outputContent.Substring(0, [Math]::Min(200, $outputContent.Length))
            Write-Host "  [FAIL] ${actualSlug}: $errorMsg" -ForegroundColor Red
            "$ts,$actualSlug,fail,$errorMsg" | Out-File -FilePath $LogFile -Append -Encoding UTF8
            $failCount++
        }
    } catch {
        Write-Host "  [ERROR] $actualSlug : $_" -ForegroundColor Red
        $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        "$ts,$actualSlug,error,$_" | Out-File -FilePath $LogFile -Append -Encoding UTF8
        $failCount++
    }

    # Delay between skills
    if ($i -lt $failedSkills.Count - 1) {
        Write-Host "  Waiting ${delaySeconds}s before next skill..." -ForegroundColor DarkGray
        Start-Sleep -Seconds $delaySeconds
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Retry Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total: $($failedSkills.Count)"
Write-Host "Successful: $successCount" -ForegroundColor Green
Write-Host "Failed: $failCount" -ForegroundColor Red
Write-Host "Log: $LogFile"
