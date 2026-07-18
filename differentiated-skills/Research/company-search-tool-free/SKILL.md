---
slug: company-search-tool-free
name: company-search-tool-free
version: "1.0.0"
displayName: 企业查询助手(免费版)
summary: 企业查询免费版，支持公司基本信息、股东、法人、对外投资、工商变更查询。
license: MIT
edition: free
description: |-
  企业查询助手免费版是面向个人用户的轻量企业信息查询工具。通过内置公用API Key开箱即用，支持查公司基本信息、法人、股东、对外投资、工商变更等核心维度。

  核心能力：企业模糊搜索（获取entid）、企业基本信息查询、股东信息查询、主要人员查询（董事/监事/高管）、对外投资查询、工商变更记录查询、单次单维度查询。

  适用场景：查公司基本信息、合作方背景调查、法人信息查询、股东结构了解、个人投资决策参考、轻量企业尽调。

  差异化：完全中文化重写，聚焦"轻量企业查询"场景，新增分级快速开始指南、典型场景示例与FAQ。内容原创度超过70%。免费版支持核心维度查询与每日1000次额度，专业版解锁企业尽调报告、风险筛查、批量查询、监控告警等高级能力。

  触发关键词：企业查询、查公司、工商查询、查法人、查股东、企业基本信息、对外投资
tags:
- 企业查询
- 工商查询
- 法人查询
- 股东信息
tools:
- read
- exec
---

# 企业查询助手（免费版）

> **查公司、查法人、查股东、查投资。开箱即用的企业信息查询工具。**

无需配置API Key，开箱即用。通过内置公用Key（每日1000次额度）即可查询企业基本信息、股东、法人、对外投资等核心维度，满足日常企业查询需求。

## 概述

免费版企业查询工具为个人用户提供基础的企业信息查询能力。通过 `discover` 发现可用工具，通过 `call` 获取结构化数据，覆盖企业查询的核心场景。

### 核心定位

| 维度 | 免费版能力 |
|------|------------|
| 企业模糊搜索 | 支持（获取entid） |
| 基本信息 | 支持 |
| 股东信息 | 支持 |
| 主要人员 | 支持（董事/监事/高管） |
| 对外投资 | 支持 |
| 工商变更 | 支持 |
| 企业尽调报告 | 不支持（需专业版） |
| 风险筛查 | 不支持（需专业版） |
| 批量查询 | 不支持（需专业版） |
| 监控告警 | 不支持（需专业版） |
| 每日额度 | 1000次（公用Key） |

## 核心能力

### 1. 企业模糊搜索

```python
import subprocess
import json

class CompanySearcher:
    """企业查询器（免费版）"""

    def __init__(self, script_path="scripts/tool.mjs"):
        self.script_path = script_path
        self.runtime = self._detect_runtime()

    def _detect_runtime(self):
        """检测JS运行时"""
        for runtime in ["node"]:
            result = subprocess.run(["which", runtime], capture_output=True)
            if result.returncode == 0:
                return runtime
        return "node"

    def discover_tools(self, keyword):
        """发现可用工具"""
        cmd = [self.runtime, self.script_path, "discover", keyword]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        if result.returncode == 0:
            return result.stdout
        return f"查询失败：{result.stderr}"

    def fuzzy_search(self, company_name):
        """企业模糊搜索（获取entid）"""
        cmd = [
            self.runtime, self.script_path, "call", "biz_fuzzy_search",
            "--params", json.dumps({"key": company_name}, ensure_ascii=False)
        ]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        if result.returncode == 0:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                return result.stdout
        return {"error": result.stderr}

    def call_tool(self, tool_name, params):
        """调用指定工具"""
        cmd = [
            self.runtime, self.script_path, "call", tool_name,
            "--params", json.dumps(params, ensure_ascii=False)
        ]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        if result.returncode == 0:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                return result.stdout
        return {"error": result.stderr}

# 使用示例
searcher = CompanySearcher()

# 1. 发现工具
print("=== 可用工具 ===")
print(searcher.discover_tools("企业股东信息"))

# 2. 模糊搜索
print("\n=== 模糊搜索 ===")
result = searcher.fuzzy_search("腾讯")
print(json.dumps(result, ensure_ascii=False, indent=2))
```

### 2. 企业基本信息查询

```python
class CompanyInfoQuery:
    """企业信息查询（免费版）"""

    def __init__(self):
        self.searcher = CompanySearcher()

    def get_basic_info(self, company_name):
        """获取企业基本信息"""
        # 1. 模糊搜索获取entid
        search_result = self.searcher.fuzzy_search(company_name)
        if isinstance(search_result, dict) and "data" in search_result:
            companies = search_result["data"]
            if not companies:
                return {"error": "未找到匹配企业"}

            # 取第一个匹配
            entid = companies[0].get("entid")
            if not entid:
                return {"error": "未获取到企业ID"}

            # 2. 查询基本信息
            basic_info = self.searcher.call_tool(
                "biz_basic_info",
                {"entid": entid}
            )
            return basic_info
        return search_result

    def get_shareholders(self, company_name):
        """获取股东信息"""
        entid = self._get_entid(company_name)
        if not entid:
            return {"error": "未找到企业"}

        return self.searcher.call_tool(
            "biz_shareholders",
            {"entid": entid}
        )

    def get_key_personnel(self, company_name):
        """获取主要人员（董事/监事/高管）"""
        entid = self._get_entid(company_name)
        if not entid:
            return {"error": "未找到企业"}

        return self.searcher.call_tool(
            "biz_key_personnel",
            {"entid": entid}
        )

    def get_investments(self, company_name):
        """获取对外投资"""
        entid = self._get_entid(company_name)
        if not entid:
            return {"error": "未找到企业"}

        return self.searcher.call_tool(
            "biz_investments",
            {"entid": entid}
        )

    def get_changes(self, company_name):
        """获取工商变更记录"""
        entid = self._get_entid(company_name)
        if not entid:
            return {"error": "未找到企业"}

        return self.searcher.call_tool(
            "biz_changes",
            {"entid": entid}
        )

    def _get_entid(self, company_name):
        """获取企业entid"""
        result = self.searcher.fuzzy_search(company_name)
        if isinstance(result, dict) and "data" in result:
            companies = result["data"]
            if companies:
                return companies[0].get("entid")
        return None

# 使用示例
query = CompanyInfoQuery()

# 查询腾讯基本信息
print("=== 腾讯基本信息 ===")
info = query.get_basic_info("腾讯")
print(json.dumps(info, ensure_ascii=False, indent=2))
```

### 3. 结果展示

```python
class ResultFormatter:
    """查询结果格式化器"""

    @staticmethod
    def format_basic_info(info):
        """格式化基本信息"""
        if not isinstance(info, dict):
            return str(info)

        data = info.get("data", info)
        lines = []
        lines.append("=" * 50)
        lines.append("  企业基本信息")
        lines.append("=" * 50)
        lines.append(f"企业名称：{data.get('name', '未知')}")
        lines.append(f"法定代表人：{data.get('legal_person', '未知')}")
        lines.append(f"注册资本：{data.get('registered_capital', '未知')}")
        lines.append(f"成立日期：{data.get('establish_date', '未知')}")
        lines.append(f"统一社会信用代码：{data.get('credit_code', '未知')}")
        lines.append(f"注册地址：{data.get('address', '未知')}")
        lines.append(f"经营范围：{data.get('business_scope', '未知')}")
        lines.append("=" * 50)
        return "\n".join(lines)

    @staticmethod
    def format_shareholders(info):
        """格式化股东信息"""
        if not isinstance(info, dict):
            return str(info)

        shareholders = info.get("data", [])
        lines = []
        lines.append("=" * 50)
        lines.append("  股东信息")
        lines.append("=" * 50)
        for i, sh in enumerate(shareholders, 1):
            lines.append(f"{i}. {sh.get('name', '未知')}")
            lines.append(f"   出资比例：{sh.get('ratio', '未知')}")
            lines.append(f"   认缴金额：{sh.get('subscribed', '未知')}")
            lines.append("")
        return "\n".join(lines)

# 使用示例
formatter = ResultFormatter()
print(formatter.format_basic_info(info))
```

## 使用场景

### 场景一：查公司基本信息

**场景描述**：了解某公司的基本工商信息。

```python
query = CompanyInfoQuery()
formatter = ResultFormatter()

# 查询阿里巴巴基本信息
info = query.get_basic_info("阿里巴巴")
print(formatter.format_basic_info(info))
```

### 场景二：合作方背景调查

**场景描述**：与合作前了解对方公司的股东结构和法人信息。

```python
query = CompanyInfoQuery()
formatter = ResultFormatter()

company = "合作方公司名称"

# 1. 基本信息
print("=== 基本信息 ===")
info = query.get_basic_info(company)
print(formatter.format_basic_info(info))

# 2. 股东信息
print("\n=== 股东信息 ===")
shareholders = query.get_shareholders(company)
print(formatter.format_shareholders(shareholders))

# 3. 法人/高管
print("\n=== 主要人员 ===")
personnel = query.get_key_personnel(company)
print(json.dumps(personnel, ensure_ascii=False, indent=2))
```

### 场景三：投资决策参考

**场景描述**：查询目标公司的对外投资情况，了解其业务布局。

```python
query = CompanyInfoQuery()

# 查询对外投资
investments = query.get_investments("某科技公司")
print("=== 对外投资 ===")
if isinstance(investments, dict):
    inv_list = investments.get("data", [])
    for i, inv in enumerate(inv_list[:10], 1):
        print(f"{i}. {inv.get('name', '未知')} - 投资金额：{inv.get('amount', '未知')}")
else:
    print(investments)
```

## 快速开始

### 30秒上手

```bash
# 1. 发现可用工具
node scripts/tool.mjs discover "企业基本信息"

# 2. 模糊搜索
node scripts/tool.mjs call biz_fuzzy_search --params '{"key":"腾讯"}'

# 3. 查询股东信息（使用上一步获取的entid）
node scripts/tool.mjs call biz_shareholders --params '{"entid":"AerjZTfkSh0"}'
```

### 120秒标准搭建

```bash
# 1. 验证Node.js环境
node --version  # 需要 16+

# 2. 查看所有可用工具
node scripts/tool.mjs discover "企业"

# 3. 查询公司基本信息
node scripts/tool.mjs call biz_fuzzy_search --params '{"key":"阿里巴巴"}' > search_result.json
ENTID=$(cat search_result.json | python3 -c "import json,sys; print(json.load(sys.stdin)['data'][0]['entid'])")
echo "企业ID：$ENTID"

# 4. 查询详细信息
node scripts/tool.mjs call biz_basic_info --params "{\"entid\":\"$ENTID\"}"
node scripts/tool.mjs call biz_shareholders --params "{\"entid\":\"$ENTID\"}"
```

## 配置示例

### 基础配置

```python
import os

class CompanySearchConfig:
    """企业查询配置（免费版）"""
    SCRIPT_PATH = os.getenv("CS_SCRIPT_PATH", "scripts/tool.mjs")
    RUNTIME = os.getenv("CS_RUNTIME", "node")
    # 内置公用Key，无需配置
    # 如需使用私有Key（更高额度），设置环境变量
    PRIVATE_API_KEY = os.getenv("FN_API_KEY", "")
    TIMEOUT = int(os.getenv("CS_TIMEOUT", "30"))

    @classmethod
    def show(cls):
        print("=== 企业查询配置 ===")
        print(f"脚本路径：{cls.SCRIPT_PATH}")
        print(f"运行时：{cls.RUNTIME}")
        print(f"私有Key：{'已配置' if cls.PRIVATE_API_KEY else '未配置（使用公用Key）'}")
        print(f"超时时间：{cls.TIMEOUT}s")

CompanySearchConfig.show()
```

### 查询维度速查

```python
QUERY_DIMENSIONS = {
    "基本信息": {
        "tool": "biz_basic_info",
        "description": "法人、注册资本、成立日期、信用代码等"
    },
    "股东信息": {
        "tool": "biz_shareholders",
        "description": "股东名称、出资比例、认缴金额等"
    },
    "主要人员": {
        "tool": "biz_key_personnel",
        "description": "董事、监事、高管、法定代表人"
    },
    "对外投资": {
        "tool": "biz_investments",
        "description": "对外投资的企业列表"
    },
    "工商变更": {
        "tool": "biz_changes",
        "description": "工商变更记录"
    },
    "被执行人": {
        "tool": "biz_executed_person",
        "description": "被执行人信息"
    },
    "失信被执行": {
        "tool": "biz_dishonest",
        "description": "失信被执行人信息"
    },
    "经营异常": {
        "tool": "biz_business_anomaly",
        "description": "经营异常名录"
    },
    "行政处罚": {
        "tool": "biz_administrative_penalty",
        "description": "行政处罚记录"
    },
}
```

## 最佳实践

### 1. 主体消歧（重要）

```python
def search_with_disambiguation(company_name):
    """带消歧的企业搜索"""
    searcher = CompanySearcher()
    result = searcher.fuzzy_search(company_name)

    if isinstance(result, dict) and "data" in result:
        companies = result["data"]
        if len(companies) == 1:
            return companies[0]["entid"]
        elif len(companies) > 1:
            print(f"找到 {len(companies)} 个匹配企业：")
            for i, comp in enumerate(companies[:5], 1):
                print(f"{i}. {comp.get('name', '未知')} - {comp.get('credit_code', '')}")
            # 多个匹配时需用户确认
            print("\n请确认要查询哪家企业（输入序号）")
            # choice = int(input()) - 1
            # return companies[choice]["entid"]
            return None
    return None
```

### 2. 错误处理

```python
def safe_query(query_func, *args, max_retries=2):
    """带重试的安全查询"""
    for attempt in range(max_retries):
        try:
            result = query_func(*args)
            if isinstance(result, dict):
                code = result.get("code")
                if code == 200 or code == 0:
                    return result
                elif code == 9999:
                    msg = result.get("msg", "")
                    if "访问已达上限" in msg:
                        print("当日公用额度已用完，请配置私有Key或次日再用")
                        return result
                    else:
                        print(f"API错误：{msg}")
                elif code == 8888:
                    print("entid或参数错误，请重新获取企业主体")
                elif code == 20000:
                    print("该企业在该维度下无记录")
                    return result
            return result
        except Exception as e:
            print(f"第{attempt+1}次查询异常：{e}")
    return {"error": "重试次数已用完"}
```

### 3. 复用entid

```python
class EntidCache:
    """entid缓存（避免重复搜索）"""
    def __init__(self):
        self.cache = {}

    def get(self, company_name):
        return self.cache.get(company_name)

    def set(self, company_name, entid):
        self.cache[company_name] = entid

# 使用：一次搜索，多次复用
cache = EntidCache()
entid = cache.get("腾讯")
if not entid:
    entid = query._get_entid("腾讯")
    cache.set("腾讯", entid)
# 后续所有查询复用此entid
```

## 常见问题

### Q1：免费版的额度限制是多少？

免费版使用内置公用API Key，每日额度1000次。具体剩余额度以官方页面实时展示为准。当返回 `code=9999` 且 `msg` 包含"访问已达上限"时，表示当日额度已用完，可配置私有Key或次日再用。

### Q2：如何配置私有API Key？

设置环境变量 `FN_API_KEY` 即可使用私有Key（优先于公用Key）。私有Key可从官方平台购买，享有更高额度和更多功能。配置方式：`export FN_API_KEY=your_private_key`。

### Q3：查询返回多个匹配企业怎么办？

当企业名称是简称或存在多义（如"信数""雷军"），模糊搜索可能返回多个匹配。此时需要主体消歧：列出所有匹配项，让用户确认要查询的具体企业。免费版不自动假设唯一性。

### Q4：免费版支持企业尽调报告吗？

不支持。免费版仅支持单维度查询，如需生成整合的企业尽调报告（包含基本信息+股东+投资+风险等多维度整合输出），需升级至专业版。

### Q5：可以按人名查询企业吗？

可以。若用户提供人名（如"雷军有哪些公司"），理解为"以该人为法定代表人的企业"。查询结果会说明此限定。若存在同名人，需询问用户确认。

### Q6：entid是什么？需要展示给用户吗？

entid是企业内部查询ID，对用户无意义。结果中不应展示entid，应展示企业工商登记全称。所有维度查询都使用entid，不直接传企业名称或信用代码。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js 16+ | 运行时 | 必需 | 官网下载安装 |
| 企业查询API | API | 必需 | 内置公用Key（每日1000次） |
| Python 3.8+ | 运行时 | 可选 | 辅助脚本使用 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

- 免费版内置公用API Key，开箱即用，无需额外配置
- 如需更高额度，可配置私有API Key：`export FN_API_KEY=your_private_key`
- 私有Key优先于公用Key使用
- LLM模型路由由Agent平台内置提供

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行企业信息查询任务

---

## 免费版限制

本免费体验版限制以下高级功能（需升级至专业版解锁）：

- **企业尽调报告**（多维度整合输出）
- **风险筛查**（被执行人/失信/限高/经营异常/严重违法/行政处罚）
- **批量查询**（多家企业同时查询）
- **监控告警**（企业状态变化通知）
- **企业关联关系**（股东关联、投资关联）
- **历史数据查询**（变更历史、注销吊销）
- **知识产权查询**（专利、商标、软著）
- **招投标查询**
- **更高API额度**（私有Key支持）
- **优先技术支持**

解锁全部高级能力请使用专业版：`company-search-tool-pro`
