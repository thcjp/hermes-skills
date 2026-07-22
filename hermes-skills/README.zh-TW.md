# Hermes Skills

> 759 個免費 AI 智能體技能，採用 [agentskills.io](https://agentskills.io) 標準格式

[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-TW.md)

## 關於

本倉庫包含 759 個精心整理的免費 AI 智能體技能，每個技能均採用 agentskills.io 標準格式打包。這些技能相容於主流 AI 程式智能體：

- **Claude Code** (Anthropic)
- **Cursor** (Anysphere)
- **Codex** (OpenAI)
- **Gemini CLI** (Google)
- 任何支援 SKILL.md 標準的智能體平台

## 目錄結構

每個技能是一個獨立的目錄，包含一個 `SKILL.md` 檔案：

```
hermes-skills/
├── ad-creative-intel-free/
│   └── SKILL.md
├── aws-agent-orchestrator-free/
│   └── SKILL.md
├── ...
└── README.md
```

## 技能格式

每個 `SKILL.md` 檔案遵循 agentskills.io 標準：

```yaml
---
name: skill-name-free
description: 技能的簡要描述
license: MIT
allowed-tools: read write
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
metadata:
  version: 1.0.0
  category: productivity
  tags: [automation, workflow]
---

# 技能名稱

## 描述
技能功能的詳細說明...

## 用法
如何使用此技能...
```

## 分類

技能按多個類別組織：

| 類別 | 數量 | 範例 |
|------|------|------|
| 自動化與工作流程 | ~60 | cron-scheduler, task-queue-manager, workflow-orchestrator |
| 通訊 | ~50 | discord-toolkit, slack-hub-tool, telegram-chat-tool |
| 創意與設計 | ~80 | logo-design-tool, ui-ux-toolkit, video-producer-tool |
| 開發工具 | ~70 | git-cli-tool, docker-essentials, code-analysis-toolkit |
| 記憶與上下文 | ~25 | context-compressor, memory-fortress, neural-context-engine |
| 生產力 | ~50 | excel-ninja, notes-sync-cli, schedule-manager |
| 安全 | ~15 | encryption-tool, ssl-toolkit, aegis-security |
| 資料與分析 | ~30 | data-analysis-toolkit, knowledge-graph-builder |
| AI 與 LLM | ~40 | llm-provider-tool, prompt-architect, ai-image-gen-tool |
| 其他 | ~339 | 各類專用工具 |

## 使用方法

### Claude Code
1. 複製本倉庫
2. 將任意技能目錄複製到 `.claude/skills/` 資料夾
3. 技能將自動在 Claude Code 工作階段中可用

### Cursor
1. 複製本倉庫
2. 將任意技能目錄複製到 `.cursor/skills/` 資料夾
3. 重新啟動 Cursor 以載入技能

### Codex
1. 複製本倉庫
2. 在 Codex 設定中引用技能路徑

### Gemini CLI
1. 複製本倉庫
2. 將技能目錄新增到 Gemini CLI 的技能搜尋路徑中

## 品質保證

所有技能均通過 6 層品質稽核：
- **第 1-3 層**：格式驗證（YAML 前置中繼資料、必填欄位、結構）
- **第 4 層**：功能驗證（任務定義、輸入/輸出、錯誤處理）
- **第 5 層**：可銷售性評估（市場價值、目標受眾、差異化）
- **第 6 層**：內容真實性（無模板填充、真實可執行程式碼）

## 開源協議

MIT 協議 - 詳情見 [LICENSE](LICENSE)

## 相關平台

這些技能同時發布於：
- **SkillHub** - 中文 AI 技能市場（商業化變現）
- **ClawHub** - 國際開源技能生態

## 最後更新

2026 年 7 月
