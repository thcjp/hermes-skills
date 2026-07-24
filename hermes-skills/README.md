# Hermes Skills

> AI 智能体技能库 · 分类索引

[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-TW.md)

## 关于

本仓库收录 **1218** 个 AI 智能体技能（759 个免费 + 459 个付费），采用 [agentskills.io](https://agentskills.io) 标准格式，兼容 Claude Code / Cursor / Codex / Gemini CLI 等主流 Agent 平台。技能按以下 14 个分类组织，每个分类下分为 `free/`（免费）与 `paid/`（付费）两个子目录。

> **付费技能说明**：付费技能保留 Proprietary 许可证，与 ClawHub 付费版本保持一致，未完全开源。如需购买或了解更多，请访问 [SkillHub](https://www.skillhub.cn)。

## 分类总览

| 分类 | 免费技能数 | 付费技能数 | 合计 | 说明 |
|---|---|---|---|---|
| [Agents](Agents/README.md) | 20 | 27 | 47 | 智能体 — AI 智能体框架、编排与多智能体协作工具。 |
| [Automation](Automation/README.md) | 20 | 238 | 258 | 自动化 — 工作流自动化、定时任务与流程编排工具。 |
| [Communication](Communication/README.md) | 56 | 12 | 68 | 通讯协作 — 即时通讯、邮件、通知与社交通信工具。 |
| [Creative](Creative/README.md) | 124 | 47 | 171 | 创意设计 — 内容创作、图像/音乐生成、写作与视觉设计工具。 |
| [Development](Development/README.md) | 194 | 35 | 229 | 开发工具 — 编程、代码质量、数据库、前端与 DevOps 工具。 |
| [Finance](Finance/README.md) | 34 | 10 | 44 | 财务金融 — 财务分析、投资、税务与加密货币工具。 |
| [Integrations](Integrations/README.md) | 5 | 0 | 5 | 集成工具 — 第三方平台与 API 集成连接器。 |
| [Knowledge](Knowledge/README.md) | 50 | 49 | 99 | 知识管理 — 笔记、知识库、知识图谱与文档管理工具。 |
| [Lifestyle](Lifestyle/README.md) | 12 | 0 | 12 | 生活助手 — 天气、出行、健康、智能家居与日常生活工具。 |
| [Operations](Operations/README.md) | 41 | 17 | 58 | 运维监控 — 云计算、基础设施、网络与系统监控运维工具。 |
| [Other](Other/README.md) | 0 | 0 | 0 | 其他 — 未归入上述分类的各类专用工具。 |
| [Productivity](Productivity/README.md) | 69 | 2 | 71 | 生产力 — 任务管理、日程、办公与个人效率工具。 |
| [Research](Research/README.md) | 87 | 3 | 90 | 研究分析 — 信息检索、数据分析、新闻资讯与学术研究工具。 |
| [Security](Security/README.md) | 47 | 19 | 66 | 安全合规 — 安全审计、漏洞扫描、隐私保护与合规工具。 |
| **合计** | **759** | **459** | **1218** | — |

## 目录结构

```
hermes-skills/
├── README.md            # 主索引（简体中文）
├── README.zh-CN.md      # 简体中文
├── README.zh-TW.md      # 繁體中文
├── README.en.md         # English
├── Agents/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 20
│   └── paid/            # 27
├── Automation/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 20
│   └── paid/            # 238
├── Communication/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 56
│   └── paid/            # 12
├── Creative/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 124
│   └── paid/            # 47
├── Development/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 194
│   └── paid/            # 35
├── Finance/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 34
│   └── paid/            # 10
├── Integrations/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 5
│   └── paid/            # 0
├── Knowledge/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 50
│   └── paid/            # 49
├── Lifestyle/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 12
│   └── paid/            # 0
├── Operations/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 41
│   └── paid/            # 17
├── Other/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 0
│   └── paid/            # 0
├── Productivity/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 69
│   └── paid/            # 2
├── Research/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 87
│   └── paid/            # 3
├── Security/
│   ├── README.md        # 分类说明（三语）
│   ├── free/            # 47
│   └── paid/            # 19
```

## 使用方法

1. 克隆本仓库。
2. 将所需技能目录（如 `Development/free/git-cli-tool-free/`）复制到对应 Agent 的技能目录：
   - **Claude Code**: `.claude/skills/`
   - **Cursor**: `.cursor/skills/`
   - **Codex**: 在配置中引用技能路径
   - **Gemini CLI**: 添加到技能搜索路径
3. 免费技能可直接使用；付费技能请前往 [SkillHub](https://www.skillhub.cn) 获取授权。
4. 技能将在 Agent 会话中自动可用。

---

开源协议：免费技能 MIT | 付费技能 Proprietary

最后更新：2026 年 7 月 25 日
