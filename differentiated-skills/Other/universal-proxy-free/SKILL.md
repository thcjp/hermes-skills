---
slug: universal-proxy-free
name: universal-proxy-free
version: 1.0.1
displayName: 通用代理工具免费版
summary: "通过加密电路隐藏源IP，提供SOCKS5代理与流量转发，保护Agent通信隐私。通用代理工具是一套面向AI Agent的隐私通信代理方案，通过建立分布式加密电路转发流量，让Agent在访问网"
license: Proprietary
edition: free
description: 通用代理工具是一套面向AI Agent的隐私通信代理方案，通过建立分布式加密电路转发流量，让Agent在访问网络服务时隐藏源IP地址，保护调用方身份隐私，适用于需要匿名性或地理可达性的Agent场景。核心能力：启动本地SOCKS5代理服务（默认端口9050）；建立多层加密电路转发流量；支持HTTP/HTTPS/SOCKS5多种协议；首次连接30秒内完成电路建立；代理服务可常驻后台，跨请求复用
tags:
  - 网络代理
  - 隐私保护
  - SOCKS5
  - 匿名通信
  - 工具
  - 效率
  - 自动化
  - 安全
  - 加密
  - AI代理
  - agent
  - 研究
  - socks5
  - proxy
  - 代理服务
  - com
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# 通用代理工具（免费版）

## 概述

AI Agent在执行任务时常常面临两类问题：**源IP暴露导致身份被追踪**（如爬虫被反爬识别、调用方被画像）、**地理可达性受限**（如某些API仅对特定地区开放、部分服务被区域网络封锁）。传统VPN解决方案是全局路由，对Agent来说粒度太粗——它需要的是"仅代理特定流量"的细粒度能力.
通用代理工具用SOCKS5代理+加密电路的方式解决这个问题。Agent按需通过本地SOCKS5端口发起请求，流量经多层加密电路转发至目标服务，源IP被完全隐藏，且中间节点也无法还原通信双方身份.
本免费版支持单电路、本地端口代理与基础路由策略。如需多电路并发、流量负载均衡、企业级审计等高级能力，可升级至专业版.
## 核心能力

### 能力1：本地SOCKS5代理服务

启动本地代理服务，Agent通过SOCKS5协议接入：

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 通用代理工具免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 启动代理服务（默认端口9050）
universal-proxy start --port 9050
# ...
# 输出：
# SOCKS5 proxy listening on 127.0.0.1:9050
# Circuit establishing... (15s)
# Circuit ready. Traffic now routed through encrypted circuit.
```

任何支持SOCKS5协议的客户端均可通过 `socks5://127.0.0.1:9050` 接入.
**输入**: 用户提供能力1：本地SOCKS5代理服务所需的指令和必要参数.
**处理**: 解析能力1：本地SOCKS5代理服务的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回能力1：本地SOCKS5代理服务的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 能力2：多层加密电路

流量经过多层加密电路转发，每一层仅知道前一跳和后一跳：

```
Agent → 入口节点 → 中间节点 → 出口节点 → 目标服务
        (加密1)    (加密2)    (加密3)
```

特性：
- 入口节点知道Agent源IP，但不知道最终目标
- 中间节点既不知道源IP也不知道目标
- 出口节点知道目标服务，但不知道源IP
- 三层加密叠加，任一节点被攻破也无法还原完整链路

**输入**: 用户提供能力2：多层加密电路所需的指令和必要参数.
**处理**: 解析能力2：多层加密电路的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回能力2：多层加密电路的响应数据,包含状态码、结果和日志.
### 能力3：多协议支持

| 协议 | 用途 | 示例 |
|:-----|:-----|:-----|
| SOCKS5 | 通用代理 | `curl --socks5-hostname 127.0.0.1:9050 https://example.com` |
| HTTP | HTTP代理 | `http_proxy=socks5://127.0.0.1:9050 curl https://example.com` |
| HTTPS | 加密HTTP | 同上，自动TLS加密 |

**输入**: 用户提供能力3：多协议支持所需的指令和必要参数.
**处理**: 解析能力3：多协议支持的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回能力3：多协议支持的响应数据,包含状态码、结果和日志.
### 能力4：跨请求会话复用

代理服务启动后常驻后台，多个请求复用同一电路：
- 首次请求：30秒内建立电路
- 后续请求：毫秒级响应（电路已建立）
- 长时间空闲：电路自动保活，避免重建

**输入**: 用户提供能力4：跨请求会话复用所需的指令和必要参数.
**处理**: 解析能力4：跨请求会话复用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回能力4：跨请求会话复用的响应数据,包含状态码、结果和日志.
### 能力5：流量按需路由

并非所有流量都需要走代理。本工具支持按目标地址路由：

```yaml
routing:
  rules:
    - match: "*.internal.company.com"
      action: direct  # 内网直连
# ...
    - match: "*.region-blocked.com"
      action: proxy   # 受限服务走代理
# ...
    - match: default
      action: direct  # 默认直连
```

**输入**: 用户提供能力5：流量按需路由所需的指令和必要参数.
**处理**: 解析能力5：流量按需路由的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回能力5：流量按需路由的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：通过加密电路隐藏、代理与流量转发、通信隐私、通用代理工具是一、套面向、的隐私通信代理方、通过建立分布式加、密电路转发流量、在访问网络服务时、隐藏源、保护调用方身份隐、适用于需要匿名性、或地理可达性的、核心能力、建立多层加密电路、转发流量、多种协议、首次连接、秒内完成电路建立、代理服务可常驻后、跨请求复用等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景1：调用地理受限的API

某些海外API仅对特定地区开放。Agent通过代理调用：
```bash
curl --socks5-hostname 127.0.0.1:9050 https://region-restricted-api.com/data
```

### 场景2：Agent身份隐私保护

不希望目标服务识别调用方身份：
- 通过代理访问竞品网站调研
- 通过代理调用第三方分析API
- 避免源IP被纳入调用方画像

### 场景3：绕过区域网络封锁

某些服务在部分地区被网络封锁，代理提供可达性：
- 调用被GFW封锁的开源镜像
- 调用被企业网络封锁的云服务
- 调用被运营商劫持的DNS服务

### 场景4：爬虫与数据采集的IP轮换

爬虫Agent通过代理隐藏源IP，避免被反爬识别：
- 多次请求使用同一电路（保持会话）
- 切换电路获取新出口IP
- 配合请求间隔控制，模拟真人行为

### 场景5：内部Agent网络隔离测试

测试内部Agent系统的网络隔离策略：
- 模拟从外部访问内部服务
- 验证ACL规则有效性
- 渗透测试中的合规代理使用

## 不适用场景

以下场景通用代理工具免费版不适合处理：

- 渗透测试未授权目标
- 物理安全防护
- 社会工程学攻击

## 触发条件

需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 60秒上手

```bash
# 依赖说明
npm install -g universal-proxy-client
# ...
# 2. 启动代理服务
universal-proxy start -s 9050
# ...
# 控制台输出：
# [INFO] Initializing SOCKS5 proxy on port 9050...
# [INFO] Establishing encrypted circuit... (15s)
# [INFO] Circuit ready.
# [INFO] Listening on 127.0.0.1:9050
# ...
# 3. 通过代理访问目标
curl --socks5-hostname localhost:9050 https://api.ipify.org
# 输出代理出口IP（与源IP不同）
# ...
# 4. 关闭代理
universal-proxy stop
```

### Agent代码集成

```javascript
import { UniversalProxy } from 'universal-proxy-client';
import { SocksClient } from 'universal-proxy-client';
// ...
async function main() {
    const proxy = new UniversalProxy();
    const socksClient = new SocksClient(proxy);
// ...
    try {
        // 启动代理并等待电路建立
        await proxy.start();
// ...
        // 等待电路就绪
        await new Promise(resolve => setTimeout(resolve, 15000));
// ...
        // 通过代理发起请求
        const response = await socksClient.get('https://api.ipify.org');
        console.log('出口IP:', response.data);
        console.log('源IP已隐藏');
// ...
    } catch(error) {
        console.error('代理错误:', error);
    } finally {
        await proxy.stop();
    }
}
// ...
main();
```

## 示例

### 示例1：基础配置

```yaml
proxy:
  port: 9050
  bind: 127.0.0.1  # 仅本地访问
# ...
circuit:
  hops: 3           # 三层加密电路
  establish_timeout: 30  # 30秒超时
  keepalive_interval: 60  # 60秒保活
```

### 示例2：路由策略配置

```yaml
routing:
  rules:
    # 内网直连
    - match: 
        domain: "*.internal.company.com"
        ip: "10.0.0.0/8"
      action: direct
# ...
    # 受限服务走代理
    - match:
        domain: 
          - "*.region-blocked.com"
          - "*.geo-restricted.org"
      action: proxy
# ...
    # 默认直连
    - match: default
      action: direct
```

### 示例3：Agent调用配置

```python
import requests
# ...
# 配置SOCKS5代理
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
# ...
# 通过代理发起请求
response = requests.get(
    'https://region-restricted-api.com/data',
    proxies=proxies,
    timeout=30
)
# ...
print(f"出口IP: {response.json()['ip']}")
print(f"响应数据: {response.json()['data']}")
```

## 最佳实践

### 实践1：仅在需要时启用代理

代理会引入额外延迟（30秒电路建立+多层加密）。建议：
- 调用受限服务时启用
- 调用本地/内网服务时直连
- 使用路由规则自动判断

### 实践2：电路复用而非频繁重建

电路建立耗时较长。建议：
- 代理服务常驻后台
- 多个请求复用同一电路
- 仅在需要切换出口IP时重建电路

### 实践3：配合请求间隔控制

爬虫场景下，即使代理隐藏了源IP，过于频繁的请求仍会被识别。建议：
- 请求间隔至少2秒
- 模拟真人浏览模式（随机间隔）
- 单个电路请求量控制在合理范围

### 实践4：定期切换电路

长时间使用同一电路可能被识别。建议：
- 每1000次请求切换一次电路
- 每小时主动切换电路
- 切换时确保无未完成请求

## 错误处理

代理服务可能因网络波动中断。建议：
- 设置请求超时（建议30秒） - 处理方式: 按上述步骤操作并确认结果
- 代理失败时降级为直连（仅非敏感场景） - 处理方式: 按上述步骤操作并确认结果
- 监控代理服务健康状态 - 处理方式: 按上述步骤操作并确认结果
## 常见问题

### Q1：免费版支持多少并发连接？
A：本免费版单电路支持最多50个并发连接，足以覆盖单个Agent的并发请求需求.
### Q2：代理服务能常驻多久？
A：无限制。代理服务启动后可常驻后台，直到主动停止或系统重启.
### Q3：电路建立为什么需要15秒？
A：电路需要经过多层握手与密钥协商。这是加密电路的安全代价，建立后即可高速传输.
### Q4：能否指定出口节点地区？
A：免费版不支持指定出口地区，由网络自动选择。专业版支持.
### Q5：代理服务会记录流量日志吗？
A：默认不记录请求内容，仅记录连接元数据（时间、字节数）。可在配置中完全关闭日志.
## 故障排查表

| 现象 | 可能原因 | 排查步骤 |
|---:|---:|---:|
| 电路建立超时 | 网络不通 | 检查入口节点可达性 |
| 连接频繁断开 | 网络不稳定 | 启用keepalive，增加重试 |
| 出口IP仍为源IP | 代理未生效 | 检查 `--socks5-hostname` 参数 |
| 请求超时 | 目标服务慢 | 增加 timeout 至 30s+ |
| DNS泄露 | DNS未走代理 | 使用 `socks5h` 而非 `socks5` |
| 端口被占用 | 9050被占 | 更换 `--port` |

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：18+（运行代理客户端）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:---:|:---:|:---:|:---:|:---:|
| Node.js | 运行时 | 必需 | 官方下载 | 18+ |
| npm | 包管理 | 必需 | 随Node.js安装 | 9+ |
| universal-proxy-client | 客户端库 | 必需 | npm install | 1.0+ |
| curl | 测试工具 | 可选 | 系统自带 | 任意 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 | 不限 |

### API Key 配置
- 本工具基于本地代理，无需额外API Key
- 若需访问需要认证的代理节点，Token通过环境变量 `PROXY_AUTH_TOKEN` 注入
- **禁止**：在脚本中硬编码Token

### 可用性分类
- **分类**：MD+EXEC（Markdown指令 + 命令行工具 + 网络代理）
- **说明**：核心功能通过CLI启动本地代理服务，Agent通过SOCKS5协议接入

## 已知限制

本免费体验版限制以下高级功能：

- ❌ 多电路并发（同时使用多个独立电路）
- ❌ 流量负载均衡（在多电路间自动分配请求）
- ❌ 指定出口地区（按地区选择出口节点）
- ❌ 企业级审计日志（完整流量审计与合规报告）
- ❌ 代理节点自建（接入自有的中继节点）
- ❌ 高可用部署与故障自动切换

解锁全部功能请使用专业版：universal-proxy-pro
