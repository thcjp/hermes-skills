$ErrorActionPreference = "Continue"
$SkillHubScript = "d:\skills\skillhub.ps1"
$token = Get-Content "d:\skills\.skillhub-credentials\api-key.txt" -Raw
$token = $token.Trim()
$LogFile = "d:\skills\differentiated-skills\retry-skillhub-log.csv"
$delaySeconds = 180

if (-not (Test-Path $LogFile)) {
    "timestamp,slug,status,error" | Out-File -FilePath $LogFile -Encoding UTF8
}

$failedSkills = @(
    @{slug="evolution-engine-v2"; path="d:\skills\differentiated-skills\Agents\evolution-engine"},
    @{slug="memory-distiller-v2"; path="d:\skills\differentiated-skills\Agents\memory-distiller"},
    @{slug="memory-orchestrator-v2"; path="d:\skills\differentiated-skills\Agents\memory-orchestrator"},
    @{slug="multi-agent-dev-v2"; path="d:\skills\differentiated-skills\Agents\multi-agent-dev"},
    @{slug="cdp-browser-master"; path="d:\skills\differentiated-skills\Automation\cdp-browser-master"},
    @{slug="cron-guard"; path="d:\skills\differentiated-skills\Automation\cron-guard"},
    @{slug="linear-workflow-bot"; path="d:\skills\differentiated-skills\Automation\linear-workflow-bot"},
    @{slug="cad-insight-pro"; path="d:\skills\differentiated-skills\Automation\cad-insight-pro"},
    @{slug="cloud-ops-orchestrator"; path="d:\skills\differentiated-skills\Automation\cloud-ops-orchestrator"},
    @{slug="cron-assist"; path="d:\skills\differentiated-skills\Automation\cron-assist"},
    @{slug="cron-master-pro"; path="d:\skills\differentiated-skills\Automation\cron-master-pro"},
    @{slug="cron-scheduler-pro"; path="d:\skills\differentiated-skills\Automation\cron-scheduler-pro"},
    @{slug="desktop-autopilot"; path="d:\skills\differentiated-skills\Automation\desktop-autopilot"},
    @{slug="excel-maestro"; path="d:\skills\differentiated-skills\Automation\excel-maestro"},
    @{slug="flow-architect"; path="d:\skills\differentiated-skills\Automation\flow-architect"},
    @{slug="flow-editor-pro"; path="d:\skills\differentiated-skills\Automation\flow-editor-pro"},
    @{slug="linear-cli-pro"; path="d:\skills\differentiated-skills\Automation\linear-cli-pro"},
    @{slug="macro-pulse"; path="d:\skills\differentiated-skills\Automation\macro-pulse"},
    @{slug="notes-cli-toolkit"; path="d:\skills\differentiated-skills\Automation\notes-cli-toolkit"},
    @{slug="office-productivity-hub"; path="d:\skills\differentiated-skills\Automation\office-productivity-hub"},
    @{slug="pcb-design-assistant"; path="d:\skills\differentiated-skills\Automation\pcb-design-assistant"},
    @{slug="security-radar"; path="d:\skills\differentiated-skills\Automation\security-radar"},
    @{slug="system-controller"; path="d:\skills\differentiated-skills\Automation\system-controller"},
    @{slug="update-guardian"; path="d:\skills\differentiated-skills\Automation\update-guardian"},
    @{slug="vault-master-pro"; path="d:\skills\differentiated-skills\Automation\vault-master-pro"},
    @{slug="vault-sync-engine"; path="d:\skills\differentiated-skills\Automation\vault-sync-engine"},
    @{slug="workflow-lite"; path="d:\skills\differentiated-skills\Automation\workflow-lite"},
    @{slug="workflow-symphony"; path="d:\skills\differentiated-skills\Automation\workflow-symphony"}
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

    Write-Host ""
    Write-Host "[$($i+1)/$($failedSkills.Count)] Processing: $slug" -ForegroundColor White

    $changelog = "深度差异化版重试上传"

    try {
        & $SkillHubScript publish $path --changelog $changelog --token $token --json 2>&1 | Out-Null

        $outputFile = "d:\skills\.skillhub-credentials\last-output.txt"
        $outputContent = ""
        if (Test-Path $outputFile) {
            $outputContent = Get-Content $outputFile -Raw
        }

        $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

        if ($outputContent -match "EXIT_CODE:0" -and $outputContent -match "success|published|created|ok|version") {
            Write-Host "  [OK] $slug" -ForegroundColor Green
            "$ts,$slug,success," | Out-File -FilePath $LogFile -Append -Encoding UTF8
            $successCount++
        } elseif ($outputContent -match "conflict|exists|duplicate|already|occupied|已被") {
            Write-Host "  [CONFLICT] $slug - slug already exists" -ForegroundColor Yellow
            "$ts,$slug,conflict,slug exists" | Out-File -FilePath $LogFile -Append -Encoding UTF8
            $failCount++
        } else {
            $errorMsg = $outputContent.Substring(0, [Math]::Min(200, $outputContent.Length))
            Write-Host "  [FAIL] ${slug}: $errorMsg" -ForegroundColor Red
            "$ts,$slug,fail,$errorMsg" | Out-File -FilePath $LogFile -Append -Encoding UTF8
            $failCount++
        }
    } catch {
        Write-Host "  [ERROR] $slug : $_" -ForegroundColor Red
        $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        "$ts,$slug,error,$_" | Out-File -FilePath $LogFile -Append -Encoding UTF8
        $failCount++
    }

    if ($i -lt $failedSkills.Count - 1) {
        Write-Host "  Waiting ${delaySeconds}s..." -ForegroundColor DarkGray
        Start-Sleep -Seconds $delaySeconds
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Retry Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total: $($failedSkills.Count)"
Write-Host "Successful: $successCount" -ForegroundColor Green
Write-Host "Failed: $failCount" -ForegroundColor Red
Write-Host "Log: $LogFile"
