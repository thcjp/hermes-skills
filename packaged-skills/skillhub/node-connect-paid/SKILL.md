---
slug: "node-connect-paid"
name: "node-connect-paid"
version: 1.0.1
displayName: "节点连接工具(专业版)"
summary: "全拓扑节点连接诊断,含尾网/公网/远程网关、批量配对、审计日志与自动修复。。节点连接工具(专业版)面向团队与运维,提供全拓扑节点连接诊断、批量配对、连接审计日志与一键自动修复能力。核心能力:"
license: "MIT"
edition: "pro"
description: |-
  节点连接工具(专业版)面向团队与运维,提供全拓扑节点连接诊断、批量配对、连接审计日志与一键自动修复能力。核心能力:
  - 全拓扑支持:同机器/局域网/Tailscale尾网/公网反代/远程网关
  - 批量设备配对与状态管理
  - 连接审计日志与回溯
  - 一键诊断与自动修复脚本
  - 远程网关与多网关节点管理
  - 高级鉴权配置(Tailscale Serve/Funnel)

  适用场景:
  - 跨网络团队节点协作
  - 远程网关与多区域部署
  - 大规模设备配对与运维
  - 安全合规要求的连接审计

  差异化:
  - ...
tags:
  - Development
  - 网络
  - 诊断
  - 企业级
  - 运维
  - 安全
  - 工具
  - 效率
  - 自动化
  - 工作流
  - 写作
  - 电商
  - 研究
  - skill-platform
  - gateway
  - tailscale
  - config
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# 节点连接工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
|:-----|:-----|:-----|
| 本地/局域网诊断 | 同机器、同Wi-Fi拓扑诊断 | 与免费版一致 |
| 尾网诊断 | Tailscale Serve/Funnel 配置与排查 | 免费版无 |
| 公网反代 | 公共URL与反向代理配置诊断 | 免费版无 |
| 远程网关 | 远程模式与多网关节点管理 | 免费版无 |
| 批量配对 | 多设备同时配对与状态管理 | 免费版仅单设备 |
| 审计日志 | 连接事件记录与回溯 | 免费版无 |
| 自动修复 | 一键诊断并应用修复脚本 | 免费版仅建议 |
| 鉴权高级 | Tailscale鉴权、令牌轮换 | 免费版基础鉴权 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 本地/局域网诊断

针对本地/局域网诊断,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供本地/局域网诊断相关的配置参数、输入数据和处理选项.
**输出**: 返回本地/局域网诊断的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`本地/局域网诊断`的配置文档进行参数调优
### 尾网诊断

针对尾网诊断,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供尾网诊断相关的配置参数、输入数据和处理选项.
**输出**: 返回尾网诊断的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`尾网诊断`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:Tailscale尾网跨网络协作

团队成员分布在不同网络,通过Tailscale尾网连接节点.
```bash
# 标准检查 + 尾网检查
skill-platform config get gateway.bind
skill-platform config get gateway.tailscale.mode
skill-platform config get gateway.auth.allowTailscale
skill-platform qr --json
tailscale status --json
```

常见根因:

- `gateway.bind=tailnet set, but no tailnet IP was found`:网关主机未实际加入Tailscale
  - 修复:在网关主机运行 `tailscale up`,确认 `tailscale status` 显示在线
- 应用提示 `unauthorized`:`gateway.auth.allowTailscale` 与预期流程不匹配
  - 修复:对Tailscale Serve流程,设置 `gateway.auth.allowTailscale=true`

### 场景二:公网反代部署

团队通过公网URL与反向代理暴露节点网关.
```bash
# 检查公共URL配置
skill-platform config get plugins.entries.device-pair.config.publicUrl
skill-platform config get gateway.remote.url
# ...
# 远程模式QR
skill-platform qr --remote --json
```

常见根因:

- `qr --remote requires gateway.remote.url`:远程模式配置不完整
  - 修复:设置 `gateway.remote.url=https://gateway.example.com`
- 公共URL已设但QR仍广播其他地址:检查 `urlSource`,配置并非你以为的那样
  - 修复:确认 `publicUrl` 配置项的优先级,或重启网关使配置生效

### 场景三:批量设备配对与运维

团队一次性接入大量设备,需要批量配对与状态管理.
```bash
# 批量查看所有待配对设备
skill-platform devices list --state pending
# ...
# 批量批准
skill-platform devices approve --all
# ...
# 按设备类型筛选
skill-platform devices list --type ios
skill-platform devices list --type android
# ...
# 查看节点状态概览
skill-platform nodes status --summary
```

工具输出设备状态看板:

```text
# ...
## 使用流程
# ...
### 1. 全拓扑诊断脚本
# ...
```bash
# diagnose.sh 全拓扑一键诊断
#!/usr/bin/env bash
set -euo pipefail

echo "=== 拓扑识别 ==="
echo "gateway.mode: $(skill-platform config get gateway.mode)"
echo "gateway.bind: $(skill-platform config get gateway.bind)"
echo "tailscale.mode: $(skill-platform config get gateway.tailscale.mode)"
echo "remote.url: $(skill-platform config get gateway.remote.url)"
echo "publicUrl: $(skill-platform config get plugins.entries.device-pair.config.publicUrl)"

echo ""
echo "=== QR载荷 ==="
skill-platform qr --json

echo ""
echo "=== 设备列表 ==="
skill-platform devices list

echo ""
echo "=== 节点状态 ==="
skill-platform nodes status

# 若涉及Tailscale
if [ "$(skill-platform config get gateway.tailscale.mode)" != "off" ]; then
  echo ""
  echo "=== Tailscale状态 ==="
  tailscale status --json
fi

# 若涉及远程
if [ -n "$(skill-platform config get gateway.remote.url)" ]; then
  echo ""
  echo "=== 远程QR ==="
  skill-platform qr --remote --json
fi
```
# ...
### 2. 自动修复脚本
# ...
```bash
# auto-fix.sh 自动诊断并应用修复
#!/usr/bin/env bash
set -euo pipefail

DIAGNOSE=$(skill-platform qr --json)
URL_SOURCE=$(echo "$DIAGNOSE" | jq -r '.urlSource // empty')

case "$URL_SOURCE" in
  loopback)
    echo "检测到:网关仅绑定到回环地址"
    echo "修复:设置 gateway.bind=lan"
    skill-platform config set gateway.bind lan
    skill-platform gateway restart
    skill-platform qr --json
    ;;
  tailnet)
    TS_STATUS=$(tailscale status --json 2>/dev/null || echo '{}')
    if [ "$(echo "$TS_STATUS" | jq -r '.Self.Online // false')" != "true" ]; then
      echo "检测到:尾网模式但主机未加入Tailscale"
      echo "修复:运行 tailscale up"
      tailscale up
    fi
    ;;
  *)
    echo "当前urlSource: $URL_SOURCE"
    echo "请人工审查配置"
    ;;
esac
```
# ...
### 3. 批量配对工作流
# ...
```bash
# 批量配对新设备
skill-platform devices list --state pending --format json | jq '.[].id' | while read id; do
  echo "批准设备: $id"
  skill-platform devices approve --id "$id"
done
```
# ...
#
## 输入格式
# ...
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | node-connect处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```
# ...
## 异常处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 
# ...
## 依赖说明
# ...
### 运行环境
# ...
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络环境**: 视拓扑而定,可能需要Tailscale或公网可达
- **Tailscale版本**: 建议 1.50 及以上(用于尾网拓扑)
# ...
### 依赖说明(补充)
# ...
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| skill-platform CLI | 命令行工具 | 必需 | 随技能平台安装 |
| Tailscale | VPN工具 | 视拓扑而定 | tailscale.com 下载(尾网场景) |
| jq | JSON处理 | 推荐 | 系统包管理器安装 |
| 网络诊断工具 | 命令行工具 | 推荐 | ping / traceroute / nc 等 |
# ...
### API Key 配置
# ...
- 本Skill基于指令驱动,无需额外API Key.
- `skill-platform` CLI 鉴权由所在平台处理.
- Tailscale 通过 `tailscale up` 完成OAuth认证,凭据存储在系统钥匙串.
- 远程网关若使用反向代理,需按代理服务文档配置SSL证书与访问控制.
# ...
### 可用性分类
# ...
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。PRO版面向团队与运维,提供全拓扑诊断、批量配对、审计日志与自动修复能力,完全兼容免费版本地与局域网诊断流程.
# ...
## 案例展示
# ...
### 全拓扑配置矩阵
# ...
| 拓扑 | 关键配置 | QR命令 |
|---:|:---|---:|
| 同机器 | `gateway.bind=loopback` | `qr --json` |
| 同局域网 | `gateway.bind=lan` | `qr --json` |
| Tailscale尾网 | `gateway.tailscale.mode=serve` | `qr --json` |
| Tailscale公网 | `gateway.tailscale.mode=funnel` | `qr --json` |
| 公网反代 | `plugins.entries.device-pair.config.publicUrl` | `qr --json` |
| 远程网关 | `gateway.remote.url` | `qr --remote --json` |
# ...
### 鉴权配置参考
# ...
| 鉴权模式 | 配置 | 适用场景 |
|:------:|--------|:-------|
| 令牌 | `gateway.auth.mode=token` | 通用 |
| 密码 | `gateway.auth.mode=password` | 简单场景 |
| Tailscale | `gateway.auth.allowTailscale=true` | 尾网内信任 |
| 混合 | token + allowTailscale | 兼容多场景 |
# ...
## 常见问题
# ...
### Q1:PRO版与免费版如何共存?
# ...
两者本地与局域网诊断流程完全兼容,PRO版包含免费版全部能力。团队升级时直接替换Skill文件,已有诊断脚本与根因映射无需改造.
# ...
### Q2:Tailscale Funnel与Serve有何区别?
# ...
- Serve:仅尾网内可访问(需Tailscale客户端)
- Funnel:公网可访问(无需Tailscale客户端),但安全性较低,建议额外启用令牌鉴权
# ...
### Q3:远程网关与公网反代有何区别?
# ...
- 远程网关:节点连接到独立的远程网关实例,通过 `gateway.remote.url` 配置
- 公网反代:本地网关通过反向代理暴露到公网,通过 `publicUrl` 配置
- 两者可共存,但通常二选一以简化运维
# ...
### Q4:批量配对会触发限流吗?
# ...
不会触发API限流,但建议分批进行(每批10-20台),便于观察异常。批量批准后立即运行 `nodes status` 确认全部在线,失败的设备单独处理.
# ...
### Q5:审计日志保留多久?
# ...
默认保留90天。可在配置中调整:
# ...
```bash
skill-platform config set audit.retention-days 180
```
# ...
合规要求更长的场景,建议定期导出到外部归档系统.
# ...
### Q6:支持多租户隔离吗?
# ...
支持。通过不同网关实例实现租户隔离,各租户的节点、设备、审计日志物理隔离。租户间数据互不影响.
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
## 已知限制
# ...
- 本地运行，不支持多设备同步
# ...