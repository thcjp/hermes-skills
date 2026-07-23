---
slug: "ziptax-paid"
name: "ziptax-paid"
version: "1.0.0"
displayName: "销售税查询(专业版)"
summary: "面向团队的企业级销售税工程平台,含批量查询、本地缓存、合规报告与CI集成,支持高并发。"
license: "Proprietary"
edition: "pro"
description: |-
  销售税查询工具专业版为团队与企业提供端到端销售税工程能力,涵盖批量查询、本地缓存、税务合规报告、CI集成与高并发API封装。核心能力:
  - 批量地址/邮编查询(并行处理)
  - 本地缓存与增量刷新(降低API消耗)
  - 税务合规报告(历史税率/审计追溯)
  - 企业级API封装(SDK/重试/限流)
  - CI/CD税率同步流水线
  - 多税区聚合与对比分析
  - 优先技术支持

  适用场景:
  - 中大型电商企业税率计算与结算
  - 企业税务合规与审计追溯
  - 跨州销售税率对比分析
  - 高并发订单税率实时计算
tags:
  - 销售税
  - 税务工程
  - 企业开发
  - 电商
  - CI/CD
  - 合规审计
  - 团队协作
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 销售税查询(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 是否兼容免费版 | 支持 | 支持 |
| 基础查询 | 不支持 | 支持 |
| 完全兼容 | 不支持 | 支持 |
| 批量查询 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
| --- | --- | --- |
| 基础查询 | 免费版全部地址/邮编/经纬度查询 | 完全兼容 |
| 批量查询 | 多地址并行查询与汇总 | Pro 新增 |
| 本地缓存 | 缓存查询结果,增量刷新降低消耗 | Pro 新增 |
| 合规报告 | 历史税率快照与审计追溯 | Pro 新增 |
| 企业 API 封装 | SDK、重试、限流、错误处理 | Pro 新增 |
| CI/CD 集成 | 税率定期同步与异常告警 | Pro 新增 |
| 多税区对比 | 跨州/县/市税率对比分析 | Pro 新增 |
| 优先支持 | 专属技术支持通道 | Pro 新增 |
### 基础查询

针对基础,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供基础查询相关的配置参数、输入数据和处理选项。

**输出**: 返回基础查询的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础查询`的配置文档进行参数调优
### 批量查询

针对批量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供批量查询相关的配置参数、输入数据和处理选项。

**输出**: 返回批量查询的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量查询`的配置文档进行参数调优
### 本地缓存

针对本地缓存,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供本地缓存相关的配置参数、输入数据和处理选项。

**输出**: 返回本地缓存的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`本地缓存`的配置文档进行参数调优
#
## 适用场景

### 场景 1:批量地址查询(并行处理)
为电商订单批量计算销售税,支持高并发。

```python
#!/usr/bin/env python3
# （请参考skill目录中的脚本文件） — 批量地址销售税查询
import asyncio
import aiohttp
import json
import csv
from pathlib import Path
from typing import List, Dict

API_URL = "https://api.zip-tax.com/request/v60"
API_KEY = ""  # 从环境变量读取
CONCURRENCY = 10  # 并发数
async def lookup_one(session: aiohttp.ClientSession, address: str) -> Dict:
    """查询单个地址的税率"""
    try:
        async with session.get(API_URL, params={"address": address}, headers={"X-API-KEY": API_KEY}) as resp:
            data = await resp.json()
            if data.get("metadata", {}).get("response", {}).get("code") == 100:
                rate = data["taxSummaries"][0]["rate"]
                return {
                    "address": address,
                    "rate": rate,
                    "rate_percent": f"{rate * 100:.4f}%",
                    "status": "success"
                }
            return {"address": address, "rate": None, "status": f"error: {data}"}
    except Exception as e:
        return {"address": address, "rate": None, "status": f"exception: {e}"}

async def batch_lookup(addresses: List[str], output_file: str):
    """批量查询地址税率"""
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async with aiohttp.ClientSession() as session:
        async def limited_lookup(addr):
            async with semaphore:
                return await lookup_one(session, addr)

        results = await asyncio.gather(*[limited_lookup(a) for a in addresses])

    # 写入 CSV 报告
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["address", "rate", "rate_percent", "status"])
        writer.writeheader()
        writer.writerows(results)

    # 汇总
    success = sum(1 for r in results if r["status"] == "success")
    print(f"批量查询完成: {success}/{len(results)} 成功")
    print(f"报告: {output_file}")

if __name__ == "__main__":
    import os
    API_KEY = os.environ.get("ZIPTAX_API_KEY", "")
    if not API_KEY:
        print("错误:未设置 ZIPTAX_API_KEY")
        exit(1)

    # 从文件读取地址列表
    addresses = Path("input/addresses.txt").read_text(encoding="utf-8").splitlines()
    asyncio.run(batch_lookup(addresses, "reports/tax-rates.csv"))
```

### 场景 2:本地缓存与增量刷新
通过本地缓存减少 API 调用,降低成本并提升性能。

```python
#!/usr/bin/env python3
# （请参考skill目录中的脚本文件） — 带本地缓存的税率查询
import json
import time
import hashlib
import os
from pathlib import Path
import requests

CACHE_DIR = Path("cache/taxrates")
CACHE_TTL = 7 * 24 * 3600  # 7 天缓存
API_URL = "https://api.zip-tax.com/request/v60"
API_KEY = os.environ.get("ZIPTAX_API_KEY", "")

def cache_key(query: str) -> str:
    """生成缓存键"""
    return hashlib.sha256(query.encode()).hexdigest()[:16]

def get_cached(key: str):
    """读取缓存"""
    cache_file = CACHE_DIR / f"{key}.json"
    if cache_file.exists():
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        if time.time() - data["cached_at"] < CACHE_TTL:
            return data["result"]
    return None

def set_cached(key: str, result):
    """写入缓存"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"{key}.json"
    cache_file.write_text(json.dumps({
        "cached_at": time.time(),
        "result": result
    }, ensure_ascii=False, indent=2), encoding="utf-8")

def lookup_with_cache(query: str, query_type: str = "postalcode") -> dict:
    """带缓存的查询"""
    key = cache_key(f"{query_type}:{query}")

    # 1. 尝试缓存
    cached = get_cached(key)
    if cached:
        return {**cached, "source": "cache"}

    # 2. 调用 API
    params = {query_type: query}
    resp = requests.get(API_URL, params=params, headers={"X-API-KEY": API_KEY})
    data = resp.json()

    if data.get("metadata", {}).get("response", {}).get("code") == 100:
        result = {
            "rate": data["taxSummaries"][0]["rate"],
            "base_rates": data.get("baseRates", []),
            "service_taxable": data.get("service", {}).get("taxable"),
            "shipping_taxable": data.get("shipping", {}).get("taxable"),
            "queried_at": time.time()
        }
        set_cached(key, result)
        return {**result, "source": "api"}

    return {"error": data, "source": "api"}

if __name__ == "__main__":
    result = lookup_with_cache("92618", "postalcode")
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

### 场景 3:税务合规报告生成
为审计生成本地税率快照与合规报告。

```python
#!/usr/bin/env python3
# （请参考skill目录中的脚本文件） — 税务合规报告生成
import json
import csv
from datetime import datetime, date
from pathlib import Path
from cached_lookup import lookup_with_cache

REPORT_DIR = Path("reports/compliance")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# 示例
KEY_JURISDICTIONS = [
    {"state": "CA", "postalcode": "92618", "name": "Irvine, CA"},
    {"state": "NY", "postalcode": "10001", "name": "New York, NY"},
    {"state": "TX", "postalcode": "75001", "name": "Dallas, TX"},
]

def generate_report():
    """生成合规报告"""
    today = date.today().isoformat()
    report_file = REPORT_DIR / f"compliance-{today}.csv"
    snapshot_file = REPORT_DIR / f"snapshot-{today}.json"
    report_data = []
    snapshot = {"report_date": today, "generated_at": datetime.now().isoformat(), "jurisdictions": []}

    for j in KEY_JURISDICTIONS:
        result = lookup_with_cache(j["postalcode"], "postalcode")
        if "rate" in result:
            row = {
                "date": today,
                "state": j["state"],
                "location": j["name"],
                "postalcode": j["postalcode"],
                "total_rate": f"{result['rate'] * 100:.4f}%",
                "service_taxable": result.get("service_taxable", ""),
                "shipping_taxable": result.get("shipping_taxable", ""),
                "source": result.get("source", "")
            }
            report_data.append(row)
            snapshot["jurisdictions"].append({
                **j,
                "rate": result["rate"],
                "base_rates": result.get("base_rates", [])
            })

    # CSV 报告(供审计)
    with open(report_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=report_data[0].keys())
        writer.writeheader()
        writer.writerows(report_data)

    # JSON 快照(供历史对比)
    snapshot_file.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"合规报告: {report_file}")
    print(f"税率快照: {snapshot_file}")
    print(f"覆盖税区: {len(report_data)}")

if __name__ == "__main__":
    generate_report()
```

## 使用流程

### 优秀步:声明企业上下文
在对话中说明团队规模、业务场景与合规需求,例如:

```
我们是 50 人的电商团队,在美国 15 个州有销售业务,
需要每日同步关键税区税率、生成月度合规报告,
并集成到订单系统的税率计算模块。
```

### 第二步:获取工程方案
工具会输出批量查询脚本、缓存方案、合规报告模板与 CI 集成 YAML。

### 第三步:落地与持续运行
```bash
# 依赖说明
pip install aiohttp requests

# 配置 API Key
export ZIPTAX_API_KEY="your-key"

# 批量查询
python3 （请参考skill目录中的脚本文件）

# 生成合规报告
python3 （请参考skill目录中的脚本文件）

# 查看 CI 集成
cat .github/workflows/taxrate-sync.yml
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | ziptax处理的内容输入 |,  |
| content | string | 否 | ziptax处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "ziptax 相关配置参数",
    result: "ziptax 相关配置参数",
    result: "ziptax 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Python**:建议 3.10+(用于批量与缓存脚本)
- **Node.js**:建议 20 LTS+(用于 SDK 封装)
- **curl**:用于直接 API 调用(系统预装)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 系统工具 | 必需 | 系统预装 |
| Python | 运行时 | 推荐 | 官方安装包 |
| requests / aiohttp | Python 包 | 推荐 | `pip install requests aiohttp` |
| Node.js | 运行时 | 可选 | 官方安装包 |
| zip-tax.com API | 外部 API | 必需 | 官网注册并获取 API Key |
| jq(JSON 解析) | 系统工具 | 可选 | 系统包管理器 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- **必需**:zip-tax.com API Key,通过环境变量 `ZIPTAX_API_KEY` 配置
- **获取方式**:访问 zip-tax.com 平台,注册账号,进入 DEVELOP > API Keys 页面创建
- **额度**:免费 100 次/月;企业套餐按需购买,支持高并发
- **安全要求**:永不外泄、永不提交代码仓库;生产环境用密钥管理服务
- **CI 集成**:在 CI 平台(如 GitHub Actions)的 Secrets 中配置 `ZIPTAX_API_KEY`

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 调用 zip-tax.com API;批量脚本、缓存与 CI 集成需在仓库中落地并由本地或 CI 执行;需要预先注册并配置 API Key

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1: 批量查询如何避免触发 API 限流?
并发数控制在 10-20 之间,配合本地缓存(命中率高的地址不再调用 API)。如遇 429 限流,指数退避重试。

### Q2: 税率快照如何用于审计?
每次查询的税率与时间戳写入快照文件,审计时可通过订单时间反查当时适用的税率,证明税率计算的合规性。

### Q3: 缓存 TTL 设多久合适?
7-30 天。税率调整通常有提前公告,不会单日剧变。关键场景(结账)可缩短为 1 天或实时查询,报表场景可延长到 30 天。

### Q4: 如何检测税率异常波动?
维护历史快照,对比当日与昨日税率。若单税区变化 > 1% 或多个税区同时变化,触发告警人工审查,避免 API 数据错误影响业务。

### Q5: Pro 版与免费版如何协同?
Pro 版完全兼容免费版的所有查询接口与 CLI 封装。个人开发者可继续使用免费版,企业场景启用 Pro 版获得批量、缓存、合规报告与 CI 集成能力。两个版本可在同一仓库并存。

### Q6: 如何度量税务工程的可靠性?
跟踪四个指标:API 调用成功率、缓存命中率(目标 ≥ 90%)、税率快照归档完整率、异常波动告警响应时间。四者共同反映税务工程可靠性。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
