# Hermes Skills

> AI 智能體技能庫 · 分類索引

[English](README.en.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

## 關於

本倉庫收錄 **759** 個免費 AI 智能體技能，採用 [agentskills.io](https://agentskills.io) 標準格式，相容於 Claude Code / Cursor / Codex / Gemini CLI 等主流 Agent 平台。技能按以下 14 個分類組織，每個分類下分為 `free/`（免費）與 `paid/`（付費，待新增）兩個子目錄。

## 分類總覽

| 分類 | 免費技能數 | 付費技能數 | 說明 |
|---|---|---|---|
| [Agents](Agents/README.md) | 20 | 0 | 智慧型代理人 — AI 智慧型代理人框架、編排與多代理人協作工具。 |
| [Automation](Automation/README.md) | 20 | 0 | 自動化 — 工作流程自動化、定時任務與流程編排工具。 |
| [Communication](Communication/README.md) | 56 | 0 | 通訊協作 — 即時通訊、郵件、通知與社群通訊工具。 |
| [Creative](Creative/README.md) | 124 | 0 | 創意設計 — 內容創作、圖像/音樂生成、寫作與視覺設計工具。 |
| [Development](Development/README.md) | 194 | 0 | 開發工具 — 程式設計、程式碼品質、資料庫、前端與 DevOps 工具。 |
| [Finance](Finance/README.md) | 34 | 0 | 財務金融 — 財務分析、投資、稅務與加密貨幣工具。 |
| [Integrations](Integrations/README.md) | 5 | 0 | 整合工具 — 第三方平台與 API 整合連接器。 |
| [Knowledge](Knowledge/README.md) | 50 | 0 | 知識管理 — 筆記、知識庫、知識圖譜與文件管理工具。 |
| [Lifestyle](Lifestyle/README.md) | 12 | 0 | 生活助手 — 天氣、出行、健康、智慧家庭與日常生活工具。 |
| [Operations](Operations/README.md) | 41 | 0 | 運維監控 — 雲端運算、基礎設施、網路與系統監控運維工具。 |
| [Other](Other/README.md) | 0 | 0 | 其他 — 未歸入上述分類的各類專用工具。 |
| [Productivity](Productivity/README.md) | 69 | 0 | 生產力 — 任務管理、行事曆、辦公與個人效率工具。 |
| [Research](Research/README.md) | 87 | 0 | 研究分析 — 資訊檢索、資料分析、新聞資訊與學術研究工具。 |
| [Security](Security/README.md) | 47 | 0 | 安全合規 — 安全稽核、弱點掃描、隱私保護與合規工具。 |
| **合計** | **759** | **0** | — |

## 目錄結構

```
hermes-skills/
├── README.md            # 主索引（簡體中文）
├── README.zh-CN.md      # 简体中文
├── README.zh-TW.md      # 繁體中文
├── README.en.md         # English
├── Agents/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 20
│   └── paid/            # 0
├── Automation/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 20
│   └── paid/            # 0
├── Communication/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 56
│   └── paid/            # 0
├── Creative/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 124
│   └── paid/            # 0
├── Development/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 194
│   └── paid/            # 0
├── Finance/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 34
│   └── paid/            # 0
├── Integrations/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 5
│   └── paid/            # 0
├── Knowledge/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 50
│   └── paid/            # 0
├── Lifestyle/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 12
│   └── paid/            # 0
├── Operations/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 41
│   └── paid/            # 0
├── Other/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 0
│   └── paid/            # 0
├── Productivity/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 69
│   └── paid/            # 0
├── Research/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 87
│   └── paid/            # 0
├── Security/
│   ├── README.md        # 分類說明（三語）
│   ├── free/            # 47
│   └── paid/            # 0
```

## 使用方法

1. 克隆本倉庫。
2. 將所需技能目錄（如 `Development/free/git-cli-tool-free/`）複製到對應 Agent 的技能目錄：
   - **Claude Code**: `.claude/skills/`
   - **Cursor**: `.cursor/skills/`
   - **Codex**: 在設定中引用技能路徑
   - **Gemini CLI**: 加入到技能搜尋路徑
3. 技能將在 Agent 工作階段中自動可用。

---

開源協議：MIT

最後更新：2026 年 7 月