---
slug: "vpn-rotator"
name: "vpn-rotator"
version: 1.0.1
displayName: "VPN轮换工具专业版"
summary: "全功能VPN轮换平台，支持自动重连、多VPN并发、负载均衡与熔断机制。面向数据工程团队与自动化测试团队的全功能VPN轮换平台，支持多VPN并发管理、智能负载均衡、自动重连与失败熔断。核心能力"
license: "Proprietary"
edition: "pro"
description: |-
  面向数据工程团队与自动化测试团队的全功能VPN轮换平台，支持多VPN并发管理、智能负载均衡、自动重连与失败熔断。核心能力：在免费版基础上新增自动重连机制、多VPN会话池、智能负载均衡、失败熔断器、VPN+SOCKS5代理链、按地区智能路由与性能监控仪表盘。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - 网络工具
  - IP轮换
  - 企业级网络
  - 分布式采集
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# VPN轮换工具专业版

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

| 能力模块 | 说明 | 专业版增强 |
|:-----|:-----|:-----|
| VPN连接管理 | 连接/断开/状态查询 | 支持多VPN并发会话池 |
| IP轮换 | 按请求/时间切换 | 支持智能轮换策略 |
| 自动重连 | 断线恢复 | 指数退避自动重连 |
| 负载均衡 | 服务器选择 | 延迟+成功率综合评分 |
| 失败熔断 | 故障隔离 | 连续失败自动熔断+恢复 |
| VPN+代理链 | 混合代理 | VPN+SOCKS5双重匿名 |
| 按地区路由 | 地理路由 | 按目标域名自动选区 |
| 性能监控 | 运行指标 | 实时仪表盘+告警 |
| 服务器优选 | 质量评分 | 自动剔除低质量节点 |
| 配置热更新 | 动态配置 | 不中断服务更新配置 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### VPN连接管理

针对VPN连接,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供VPN连接管理相关的配置参数、输入数据和处理选项.
**输出**: 返回VPN连接管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`VPN连接管理`的配置文档进行参数调优
### IP轮换

针对IP轮换,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供IP轮换相关的配置参数、输入数据和处理选项.
**输出**: 返回IP轮换的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`IP轮换`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：大规模分布式采集（数据工程师视角）

某数据采集平台需要同时运行50个采集任务，每个任务需要独立的出口IP。专业版的多VPN会话池支持：

```python
from vpn_rotator import VPNPool, LoadBalancer, CircuitBreaker
# ...
# 初始化VPN会话池
pool = VPNPool(
    max_connections=20,            # 最大并发VPN连接数
    auto_reconnect=True,           # 自动重连
    reconnect_backoff="exponential", # 指数退避
    health_check_interval=30,      # 健康检查间隔
)
# ...
# 负载均衡器：智能选择最优VPN
balancer = LoadBalancer(
    strategy="weighted",           # 加权轮询
    metrics=["latency", "success_rate", "stability"],
    fallback_on_failure=True,
)
# ...
# 熔断器：连续失败自动隔离
breaker = CircuitBreaker(
    failure_threshold=5,           # 连续失败5次熔断
    reset_timeout=300,             # 5分钟后尝试恢复
    half_open_max_calls=3,
)
# ...
async def scrape_with_pool(url):
    """从池中获取VPN并执行采集"""
    vpn = await pool.acquire(balancer=balancer, breaker=breaker)
    try:
        async with vpn.session():
            response = await fetch(url)
            breaker.record_success(vpn.id)
            return response
    except Exception as e:
        breaker.record_failure(vpn.id)
        raise
    finally:
        await pool.release(vpn)
```

### 场景二：多地区价格监控（运维视角）

某比价系统需要监控20个国家、100个电商网站的价格。专业版支持按目标地区自动选择VPN节点：

```python
class GeoRouter:
    """按目标域名/地区自动路由VPN"""
    REGION_MAP = {
        "amazon.com": "US",
        "amazon.co.uk": "UK",
        "amazon.de": "DE",
        "amazon.co.jp": "JP",
        "amazon.fr": "FR",
    }
# ...
    async def route(self, target_url):
        region = self._detect_region(target_url)
        vpn = await self.pool.acquire(
            country=region,
            balancer=self.balancer
        )
        return vpn
# ...
    def _detect_region(self, url):
        for domain, region in self.REGION_MAP.items():
            if domain in url:
                return region
        return None  # 默认任意地区
```

### 场景三：VPN+SOCKS5代理链（安全测试视角）

某安全测试场景需要双重匿名：VPN提供优秀层IP隐藏，SOCKS5代理提供第二层出口IP。专业版支持代理链配置：

```python
class ProxyChain:
    """VPN + SOCKS5 代理链"""
    def __init__(self, vpn_pool, socks_pool):
        self.vpn_pool = vpn_pool
        self.socks_pool = socks_pool
# ...
    async def request(self, url):
        # 优秀层：VPN连接
        vpn = await self.vpn_pool.acquire()
        async with vpn.session():
            # 第二层：通过VPN连接SOCKS5代理
            socks = await self.socks_pool.acquire()
            try:
                proxy_url = f"socks5h://{socks.username}:{socks.password}@{socks.host}:{socks.port}"
                response = await fetch_through_proxy(url, proxy_url)
                return response
            finally:
                await self.socks_pool.release(socks)
```

## 使用流程

### 企业级部署（约180秒）

1. **安装依赖**：`pip install vpn-rotator aiohttp psutil`
2. **配置VPN凭证**：准备多服务商的.ovpn配置文件
3. **初始化会话池**：运行Agent生成的池管理代码
4. **启动监控**：开启性能仪表盘

```python
from vpn_rotator import VPNPool, LoadBalancer, MetricsCollector
# ...
# 企业级配置
pool = VPNPool(
    max_connections=20,
    config_dirs=[
        "~/.vpn/protonvpn/servers",
        "~/.vpn/nordvpn/servers",
        "~/.vpn/mullvad/servers"
    ],
    auto_reconnect=True,
    reconnect_attempts=3,
    reconnect_backoff_base=2.0,
    health_check_interval=30,
)
# ...
balancer = LoadBalancer(strategy="weighted")
metrics = MetricsCollector()
```

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | vpn-rotator处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

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

## 异常处理

| 问题现象 | 可能原因 | 排查步骤 | 优先级 |
|:---:|:---:|:---:|:---:|
| 所有VPN连接失败 | 网络中断或凭证过期 | ，验证凭证 | P0 |
| 大量请求超时 | VPN延迟过高 | 查看延迟指标，切换低延迟节点 | P0 |
| 频繁重连 | VPN服务器不稳定 | 查看重连日志，拉黑不稳定节点 | P1 |
| 熔断器频繁触发 | 目标网站封锁VPN IP | 更换VPN服务商，使用代理链 | P1 |
| 地区路由错误 | 域名映射表过时 | 更新地区映射表，检查匹配逻辑 | P1 |
| 内存占用过高 | 连接数过多 | 降低max_connections，检查连接泄漏 | P2 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Linux（推荐）/ macOS / Windows（WSL2）
- **Python**: 3.8+
- **OpenVPN**: 2.5+
- **sudo权限**: 配置openvpn免密执行
- **Redis**: 6.0+（会话池状态存储，可选）

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| OpenVPN | 系统软件 | 必需 | `apt install openvpn` / 官网下载 |
| aiohttp | Python库 | 必需 | `pip install aiohttp` |
| psutil | Python库 | 必需 | `pip install psutil` |
| redis | Python库 | 推荐 | `pip install redis` |
| prometheus-client | 监控库 | 推荐 | `pip install prometheus-client` |
| requests | Python库 | 推荐 | `pip install requests` |
| VPN服务商账号 | 订阅 | 必需 | NordVPN/Mullvad/ProtonVPN等 |

### API Key 配置
- **VPN凭证**: 存储于 `~/.vpn/creds.txt`，权限设为600
- **VPN配置文件**: 存储于 `~/.vpn/servers/` 目录，按服务商分子目录
- **Redis连接**: 存储于环境变量 `REDIS_URL`
- **禁止**: 在代码仓库中提交任何凭证文件
- **推荐**: 使用密钥管理服务管理VPN凭证，`.gitignore` 排除 `~/.vpn/`

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent管理企业级VPN轮换

## 案例展示

### 多VPN会话池配置

```python
POOL_CONFIG = {
    "max_connections": 20,           # 最大并发VPN连接
    "min_idle": 5,                   # 最小空闲连接
    "acquire_timeout": 30,           # 获取连接超时
    "idle_timeout": 300,             # 空闲连接超时
    "auto_reconnect": True,          # 自动重连
    "reconnect_attempts": 3,         # 重连次数
    "reconnect_backoff": "exponential",
    "reconnect_backoff_base": 2.0,   # 初始退避秒数
    "reconnect_backoff_max": 60,     # 最大退避秒数
    "health_check_interval": 30,     # 健康检查间隔
    "health_check_url": "https://api.ipify.org",
}
```

### 负载均衡策略

```python
BALANCER_CONFIG = {
    "strategy": "weighted",          # 加权轮询
    "metrics": {
        "latency_weight": 0.4,       # 延迟权重
        "success_rate_weight": 0.4,  # 成功率权重
        "stability_weight": 0.2,     # 稳定性权重
    },
    "scoring_window": 3600,          # 评分窗口（秒）
    "min_samples": 10,               # 最小样本数
    "blacklist_threshold": 0.3,      # 评分低于0.3拉黑
    "blacklist_duration": 1800,      # 拉黑时长（秒）
    "fallback_strategy": "round_robin",  # 无评分数据时回退策略
}
```

### 熔断器配置

```python
CIRCUIT_CONFIG = {
    "failure_threshold": 5,          # 连续失败5次熔断
    "reset_timeout": 300,            # 5分钟后尝试恢复
    "half_open_max_calls": 3,        # 半开状态最多测试3次
    "success_threshold": 2,          # 连续成功2次完全恢复
    "monitored_errors": [
        "ConnectionTimeout",
        "AuthFailure",
        "DNSResolutionError",
        "TLSError",
    ],
    "auto_isolate": True,            # 自动隔离熔断的VPN
    "isolation_duration": 1800,      # 隔离时长
}
```

### 性能监控指标

```python
METRICS_SCHEMA = {
    "vpn_id": "string",
    "provider": "string",
    "country": "string",
    "server": "string",
    "connection_uptime": "int",      # 连接时长
    "total_requests": "int",         # 总请求数
    "success_rate": "float",         # 成功率
    "avg_latency_ms": "float",       # 平均延迟
    "p99_latency_ms": "float",       # P99延迟
    "bandwidth_used_mb": "float",    # 带宽使用
    "reconnect_count": "int",        # 重连次数
    "last_rotation": "timestamp",    # 最后轮换时间
    "circuit_state": "string",       # 熔断状态
}
```

## 常见问题

### Q1：多VPN并发的上限是多少？

A：受系统资源限制（每个VPN连接约消耗50MB内存）。建议单机不超过30个并发连接。如需更多并发，建议使用多台机器分布式部署，通过中心控制器统一管理.
### Q2：自动重连的退避策略是怎样的？

A：采用指数退避：第1次立即重连，第2次等待2秒，第3次等待4秒，第4次等待8秒，最大等待60秒。连续3次重连失败后标记VPN为不可用并隔离.
### Q3：负载均衡如何评分？

A：综合三个维度评分（0-1分）：延迟（40%权重，延迟越低分越高）、成功率（40%权重，成功率越高分越高）、稳定性（20%权重，连接时长越长分越高）。评分低于0.3的VPN自动拉黑30分钟.
### Q4：VPN+SOCKS5代理链有什么优势？

A：双重匿名：(1) VPN隐藏真实IP；(2) SOCKS5代理提供二次出口IP，即使VPN被识别，目标网站看到的也是SOCKS5出口IP。适合对匿名性要求极高的安全测试场景.
### Q5：按地区路由如何工作？

A：维护域名到地区的映射表，发起请求前根据目标域名自动选择对应地区的VPN节点。例如访问amazon.de自动选择德国VPN。未匹配的域名使用默认VPN.
### Q6：配置热更新会影响在线服务吗？

A：不会。热更新采用原子替换：新配置加载到副本，验证通过后原子切换。正在进行的请求使用旧配置完成，新请求使用新配置.
### Q7：如何监控VPN池健康度？

A：专业版提供实时仪表盘，展示：(1) 活跃VPN数与地区分布；(2) 各VPN延迟与成功率；(3) 熔断状态与隔离列表；(4) 带宽使用与重连次数。支持推送到Prometheus/Grafana.
### Q8：服务器优选如何剔除低质量节点？

A：基于历史性能数据评分，评分低于0.3的节点自动拉黑30分钟。拉黑期间不分配新请求，30分钟后进入半开状态进行探测，连续成功2次后恢复.
### Q9：专业版是否支持WireGuard协议？

A：当前版本以OpenVPN为主。WireGuard支持在路线图中，预计下个大版本发布。WireGuard相比OpenVPN有更低的连接延迟和更高的吞吐量.
### Q10：如何评估是否需要专业版？

A：如果你有以下需求之一，建议升级：(1) 需要同时管理多个VPN连接；(2) 采集频率超过每分钟50次；(3) 需要多地区路由；(4) 需要自动重连与熔断；(5) 需要双重匿名代理链.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

