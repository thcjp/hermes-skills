---
slug: mac-system-tool-pro
name: mac-system-tool-pro
version: "1.0.0"
displayName: Mac 系统工具专业版
summary: 面向团队的多设备远程管理、自动化策略与合规审计工具。
license: MIT
edition: pro
description: |-
  面向团队的多 Mac 设备远程管理与自动化策略专业工具。

  核心能力:
  - 多设备远程批量管理与执行
  - 定时任务与自动化策略
  - 系统合规审计与基线检查
  - 资产清单与变更追踪

  适用场景:
  - 团队多台 Mac 统一管理
  - 定时维护与自动化策略
  - 合规审计与资产追踪

  差异化: 专业版在免费版单机控制上扩展多设备远程、自动化策略、合规审计与资产追踪，兼容免费版命令。

  触发关键词: 多设备管理, 远程执行, 自动化策略, 合规审计, 资产清单, mac pro, fleet, compliance
tags:
- macOS
- 企业级
- 设备管理
- 合规
- 其他工具
tools:
- read
- exec
---

# Mac 系统工具（专业版）

## 概述

专业版面向团队与企业，在免费版单机控制基础上，扩展多设备远程批量管理、定时任务与自动化策略、系统合规审计与资产清单。命令与免费版兼容，已有命令可直接纳入自动化策略。

## 核心能力

| 能力 | 说明 | 专业版增强 |
|:-----|:-----|:-----------|
| 多设备管理 | 批量远程执行与汇总 | 设备分组 |
| 自动化策略 | 定时任务与条件触发 | 规则引擎 |
| 合规审计 | 基线检查与违规告警 | 全量报告 |
| 资产清单 | 硬件/软件清单与变更 | 追踪历史 |

## 使用场景

### 场景一：多设备批量执行

```bash
# 批量查询设备状态（专业版）
{baseDir}/scripts/fleet.sh exec --group dev-team --cmd "pmset -g batt"
```

```text
设备 dev-mac-01: 电池 82% 充电中
设备 dev-mac-02: 电池 15% 未充电 ⚠️
设备 dev-mac-03: 电池 95% 已充满
```

### 场景二：自动化策略

```json
{
  "policies": [
    {"schedule": "0 2 * * 6", "cmd": "softwareupdate -ia", "group": "all"},
    {"trigger": "disk_full > 90%", "cmd": "清空废纸篓并告警"},
    {"schedule": "0 9 * * 1", "cmd": "生成资产清单报告"}
  ]
}
```

### 场景三：合规审计

```text
合规审计报告:
  全盘加密: 12/12 通过 ✓
  防火墙: 11/12 通过（1 台未开）⚠️
  系统更新: 10/12 通过（2 台滞后）⚠️
  螺丝锁: 8/12 通过
  建议: 立即处理 dev-mac-05 防火墙
```

## 快速开始

1. 将免费版命令纳入设备分组与策略。
2. 配置多设备清单与 SSH/MDM 接入。
3. 设定自动化策略与合规基线。
4. 启用资产清单与变更追踪。

## 配置示例

设备清单与策略（`fleet.json`）：

```json
{
  "groups": {
    "dev-team": ["dev-mac-01", "dev-mac-02", "dev-mac-03"],
    "design-team": ["des-mac-01", "des-mac-02"]
  },
  "compliance": {
    "baseline": ["full_disk_encryption", "firewall_on", "updates_current"],
    "alert_on_fail": true
  },
  "asset_tracking": {"refresh": "weekly", "diff": true}
}
```

## 最佳实践

- **设备先分组**：按团队/角色分组，批量操作不误伤。
- **策略先试跑**：新策略先单设备验证再批量推。
- **合规定期跑**：每周合规扫描，违规即时告警。
- **资产留变更**：硬件软件变更留历史，便于追踪。
- **破坏性分级**：批量关机重启需多签确认。

## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 命令 | 相同 | 相同（可编排） |
| 范围 | 单机 | 多设备 |
| 自动化 | 不支持 | 策略引擎 |
| 合规 | 不支持 | 基线审计 |

## 常见问题

**Q1：多设备怎么接入？**
A：通过 SSH 或 MDM（如 Jamf）接入，专业版提供对接模板。

**Q2：自动化策略安全吗？**
A：破坏性操作需多签确认，普通维护策略可自动执行。

**Q3：合规基线能定制吗？**
A：能。按企业安全要求定义基线项与阈值。

**Q4：资产变更怎么追踪？**
A：每周扫描清单并 diff，变更自动记录历史。

**Q5：专业版有优先支持吗？**
A：有。专业版享设备管理策略与合规设计咨询。

## 进阶用法

### 多设备批量执行

```bash
# 批量查询设备状态
{baseDir}/scripts/fleet.sh exec --group dev-team --cmd "pmset -g batt"

# 批量更新软件
{baseDir}/scripts/fleet.sh exec --group all --cmd "softwareupdate -ia"

# 批量收集资产清单
{baseDir}/scripts/fleet.sh inventory --group all --out assets.json
```

```text
执行结果汇总:
  dev-mac-01: ✓ 成功
  dev-mac-02: ✓ 成功
  dev-mac-03: ✗ 超时（设备离线）
  成功: 2 / 失败: 1
```

### 自动化策略示例

```json
{
  "policies": [
    {
      "name": "周末自动更新",
      "schedule": "0 2 * * 6",
      "group": "all",
      "cmd": "softwareupdate -ia",
      "reboot": false
    },
    {
      "name": "磁盘告警",
      "trigger": "disk_full > 90%",
      "cmd": "清理废纸篓并通知",
      "notify": "ops-team"
    },
    {
      "name": "周资产报告",
      "schedule": "0 9 * * 1",
      "cmd": "generate_inventory_report"
    }
  ]
}
```

### 合规基线检查

```bash
# 合规扫描
{baseDir}/scripts/fleet.sh compliance --baseline baseline.json

# 输出报告
{baseDir}/scripts/fleet.sh compliance --report compliance.json
```

```text
合规基线项:
  full_disk_encryption: 全盘加密
  firewall_on: 防火墙开启
  screen_lock: 屏幕锁定
  updates_current: 系统更新
  filevault_on: FileVault 开启
  ssh_disabled: SSH 关闭（或限白名单）
```

## 设备分组治理

- **按团队分组**：dev-team / design-team / ops-team。
- **按角色分组**：developer / designer / admin。
- **按状态分组**：在线 / 离线 / 维护中。
- **策略按组下发**：不同组不同策略，避免一刀切。

## 资产变更追踪

```text
资产清单字段:
  设备 ID / 型号 / 序列号
  macOS 版本 / CPU / 内存 / 磁盘
  已装软件清单
  最近变更时间

变更追踪:
  每周扫描 diff，记录:
  - 新增/卸载软件
  - 硬件变更（内存升级等）
  - 系统版本升级
```

## 安全与合规

- **破坏性多签**：批量关机重启需多签确认，避免误操作。
- **合规定期扫**：每周合规扫描，违规即时告警。
- **资产留变更**：硬件软件变更留历史，便于追踪。
- **SSH 限白名单**：远程 SSH 限制白名单或关闭。
- **加密全开**：全盘加密与 FileVault 强制开启。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: macOS（控制端与被控端）
- **网络**: 设备间可达（SSH/MDM）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| SSH | 远程执行 | 多设备必需 | macOS 自带 |
| MDM（Jamf 等） | 设备管理 | 可选 | 企业 MDM 平台 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令，无需额外 API Key
- 多设备 SSH 需配置密钥或密码，建议密钥 + 密码库
- MDM 接入需配置 MDM 平台访问凭证

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成多设备管理与合规审计
