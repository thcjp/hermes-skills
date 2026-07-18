---
slug: volcengine-dns-tool-free
name: volcengine-dns-tool-free
version: "1.0.0"
displayName: 火山引擎DNS免费版
summary: 火山引擎DNS记录管理，支持域名区查询、记录增删改与传播验证，适合个人开发者日常运维。
license: MIT
edition: free
description: |-
  火山引擎DNS管理工具免费版，面向个人开发者的轻量级DNS记录管理工具。

  核心能力:
  - 域名区记录查询
  - DNS记录增删改操作
  - TTL 约束与回滚值保留
  - 传播验证（权威与递归检查）

  适用场景:
  - 个人域名的DNS记录维护
  - 服务迁移时的DNS切换
  - DNS记录的日常查询与验证

  差异化: 免费版聚焦核心DNS记录管理能力，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手。

  触发关键词: DNS管理, 火山引擎, 域名解析, 记录增删改, TTL, 传播验证, 权威查询, 递归查询
tags:
- DNS管理
- 火山引擎
- 域名运维
- 免费版
tools:
- read
- exec
---

# 火山引擎DNS管理（免费版）

## 概述

火山引擎DNS管理工具免费版帮助你管理火山引擎网络服务上的 DNS 记录。提供域名区查询、记录增删改、TTL 约束与传播验证能力，遵循严格变更范围控制与验证步骤。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 记录查询 | 查询指定域名区的现有记录 |
| 记录新增 | 添加 A/AAAA/CNAME/MX/TXT 等记录 |
| 记录修改 | 更新现有记录，保留回滚值 |
| 记录删除 | 删除指定记录，保留回滚值 |
| TTL 约束 | 支持自定义 TTL，迁移窗口前最小化 |
| 传播验证 | 权威查询 + 递归查询双重验证 |

## 使用场景

### 场景一：新增 A 记录

为新增服务添加 A 记录。

```bash
# 新增 A 记录
volcengine-dns add \
  --zone "example.com" \
  --record "api.example.com" \
  --type A \
  --value "192.168.1.100" \
  --ttl 300

# 输出
# ✅ 记录已添加
# 区: example.com
# 记录: api.example.com
# 类型: A
# 值: 192.168.1.100
# TTL: 300s
```

### 场景二：服务迁移时的 DNS 切换

服务迁移至新 IP，需要更新 DNS 记录。

```bash
# 1. 迁移前最小化 TTL
volcengine-dns update \
  --zone "example.com" \
  --record "api.example.com" \
  --type A \
  --ttl 60 \
  --comment "迁移前最小化TTL"

# 2. 等待原 TTL 过期后切换值
volcengine-dns update \
  --zone "example.com" \
  --record "api.example.com" \
  --type A \
  --value "192.168.2.100" \
  --ttl 60

# 输出（保留回滚值）
# ✅ 记录已更新
# 旧值: 192.168.1.100
# 新值: 192.168.2.100
# 回滚命令: volcengine-dns update --record api.example.com --type A --value 192.168.1.100
```

### 场景三：传播验证

DNS 切换后验证传播情况。

```bash
# 权威查询
volcengine-dns verify \
  --record "api.example.com" \
  --type A \
  --source authoritative

# 递归查询
volcengine-dns verify \
  --record "api.example.com" \
  --type A \
  --source recursive

# 输出
# 🔍 传播验证
# 权威查询: 192.168.2.100 ✅
# 递归查询:
#   - 8.8.8.8: 192.168.2.100 ✅
#   - 114.114.114.114: 192.168.1.100 ⚠️ (尚未传播)
# 建议等待原 TTL 过期后再次验证
```

## 快速开始

```bash
# 1. 查询现有记录
volcengine-dns list --zone "example.com"

# 2. 新增记录
volcengine-dns add --zone "example.com" --record "www" --type A --value "192.168.1.1" --ttl 300

# 3. 修改记录
volcengine-dns update --zone "example.com" --record "www" --type A --value "192.168.1.2"

# 4. 验证传播
volcengine-dns verify --record "www.example.com" --type A

# 5. 删除记录
volcengine-dns delete --zone "example.com" --record "old.example.com" --type A
```

## 配置示例

```bash
# 环境变量配置
export VOLCENGINE_ACCESS_KEY="your-access-key"
export VOLCENGINE_SECRET_KEY="your-secret-key"
export VOLCENGINE_REGION="cn-beijing"

# 安全规则
# 1. 修改前先查询现有记录，diff 对比
# 2. 避免盲覆盖，保留回滚值
# 3. 迁移窗口前最小化 TTL
# 4. 变更后执行传播验证
```

## 最佳实践

* 修改前先查询现有记录，避免盲覆盖。
* 所有修改操作保留回滚值，便于快速回滚。
* 迁移窗口前最小化 TTL（建议 60s），加速传播。
* 变更后执行权威与递归双重验证。
* 批量变更时分批次执行，每批验证后再继续。
* 删除操作前确认记录无依赖，避免误删导致服务中断。
* API 密钥仅从环境变量读取，不硬编码。

## 常见问题

**Q：免费版支持批量记录操作吗？**
A：免费版仅支持单条记录操作。如需批量操作与变更计划，请考虑 PRO 版本。

**Q：免费版支持变更回滚吗？**
A：免费版保留回滚值并输出回滚命令，但需手动执行。如需自动回滚，请使用 PRO 版本。

**Q：支持哪些记录类型？**
A：支持 A、AAAA、CNAME、MX、TXT、NS、SRV 等常见记录类型。

**Q：传播验证需要多长时间？**
A：取决于原 TTL 设置。TTL 60s 时通常 5-10 分钟内全球传播完成。

**Q：可以查询多个域名区吗？**
A：免费版支持查询多个域名区，但每次操作针对单个区。如需跨区批量，请使用 PRO 版本。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 可访问火山引擎 API

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 火山引擎 SDK | 库 | 必需 | pip/npm 安装 |
| dig/nslookup | 工具 | 可选（验证） | 系统自带 |

### API Key 配置
- `VOLCENGINE_ACCESS_KEY` - 火山引擎访问密钥
- `VOLCENGINE_SECRET_KEY` - 火山引擎秘密密钥
- `VOLCENGINE_REGION` - 火山引擎地域
- API 密钥仅从环境变量读取，不硬编码

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过命令行工具管理火山引擎DNS记录
