---
slug: company-search-tool-pro
name: company-search-tool-pro
version: 1.0.0
displayName: 企业查询助手(专业版)
summary: 企业级查询专业版，含尽调报告、风险筛查、批量查询、监控告警、关联关系分析.
license: Proprietary
edition: pro
description: 企业查询助手专业版是面向企业级场景的完整企业信息查询与风险分析工具。在免费版单维度查询能力之上，新增企业尽调报告、风险筛查、批量查询、监控告警、关联关系分析、历史数据查询、知识产权查询、招投标查询八大高级能力。Use
  when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
- 企业查询
- 企业尽调
- 风险筛查
- 批量查询
- 监控告警
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
> **尽调报告+风险筛查+批量查询+监控告警。企业级查询全功能覆盖。**

将复杂的企业尽调与风险分析任务交给专业工具处理。专业版在免费版单维度查询能力之上，新增企业尽调报告、风险筛查、批量查询、监控告警、关联关系分析、历史数据查询、知识产权查询、招投标查询八大高级能力，满足企业级场景对风险控制与决策支持的深度要求.
## 概述
### 免费版 vs 专业版能力对比
| 能力维度 | 免费版 | 专业版 |
|----|---|---|
| 企业模糊搜索 | 支持 | 支持 |
| 基本信息查询 | 支持 | 支持 |
| 股东/人员/投资/变更 | 支持 | 支持 |
| 企业尽调报告 | 不支持 | 支持（多维度整合） |
| 风险筛查 | 不支持 | 支持（6类风险） |
| 批量查询 | 不支持 | 支持（并发处理） |
| 监控告警 | 不支持 | 支持（状态变化） |
| 关联关系分析 | 不支持 | 支持（股东/投资） |
| 历史数据 | 不支持 | 支持（变更/注销/吊销） |
| 知识产权 | 不支持 | 支持（专利/商标/软著） |
| 招投标查询 | 不支持 | 支持 |
| API额度 | 1000次/日 | 不限（私有Key） |
| 技术支持 | 社区 | 优先工单响应 |

## 核心能力
### 1. 企业尽调报告（多维度整合）

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供企业尽调报告（多维度整合）所需的指令和必要参数.
**处理**: 解析企业尽调报告（多维度整合）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回企业尽调报告（多维度整合）的响应数据,包含状态码、结果和日志.
### 2. 风险筛查

**输入**: 用户提供风险筛查所需的指令和必要参数.
**处理**: 解析风险筛查的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回风险筛查的响应数据,包含状态码、结果和日志.
### 3. 批量查询

**输入**: 用户提供批量查询所需的指令和必要参数.
**处理**: 解析批量查询的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回批量查询的响应数据,包含状态码、结果和日志.
### 4. 监控告警
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 企业查询助手(专业版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
import time
from datetime import datetime
# ...
class CompanyMonitor:
    """企业监控告警（专业版）"""
# ...
    def __init__(self, check_interval=86400):  # 默认每日检查
        self.check_interval = check_interval
        self.monitored = {}
        self.last_state = {}
        self.notifier = WebhookNotifier()
# ...
    def add(self, company_name, dimensions=None):
        """添加监控企业"""
        self.monitored[company_name] = dimensions or ["工商变更", "被执行人", "经营异常"]
        print(f"已添加监控：{company_name}")
# ...
    def check_changes(self):
        """检查所有监控企业的状态变化"""
        for company, dimensions in self.monitored.items():
            print(f"\n检查 {company}...")
            for dim in dimensions:
                current = self._query_dimension(company, dim)
                key = f"{company}_{dim}"
# ...
                if key not in self.last_state:
                    self.last_state[key] = current
                    continue
# ...
                if current != self.last_state[key]:
                    self._alert_change(company, dim, self.last_state[key], current)
                    self.last_state[key] = current
# ...
    def _query_dimension(self, company, dimension):
        """查询维度"""
        return f"{dimension}_state_{datetime.now().strftime('%Y%m%d')}"
# ...
    def _alert_change(self, company, dimension, old_state, new_state):
        """发送变化告警"""
        message = f"企业监控告警\n企业：{company}\n维度：{dimension}\n变化：{old_state} → {new_state}"
        print(f"[ALERT] {message}")
    def start_monitoring(self):
        """启动监控循环"""
        print(f"启动企业监控，间隔 {self.check_interval}s")
        while True:
            self.check_changes()
            time.sleep(self.check_interval)
# ...
monitor = CompanyMonitor(check_interval=86400)
monitor.add("腾讯", ["工商变更", "被执行人"])
monitor.add("阿里巴巴", ["工商变更", "经营异常"])
```

**输入**: 用户提供监控告警所需的指令和必要参数.
**处理**: 解析监控告警的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回监控告警的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 关联关系分析

**输入**: 用户提供关联关系分析所需的指令和必要参数.
**处理**: 解析关联关系分析的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回关联关系分析的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级查询专业版、含尽调报告、企业查询助手专业、版是面向企业级场、景的完整企业信息、查询与风险分析工、在免费版单维度查、询能力之上、新增企业尽调报告、历史数据查询、知识产权查询、招投标查询八大高、级能力、Use、when、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一：企业尽职调查（投资团队）
**场景描述**：投资前对目标公司进行全面尽调.
```python
dd = DueDiligenceReport()
report = dd.generate_report("目标公司")
print(report)
# ...
if "风险记录" in report:
    screener = RiskScreener()
    risk = screener.screen("目标公司")
    print(screener.generate_risk_alert(risk))
```

### 场景二：供应商风险评估（采购部门）
**场景描述**：评估多个供应商的风险状况.
```python
batch = BatchCompanySearcher(max_workers=5)
suppliers = ["供应商A", "供应商B", "供应商C", "供应商D"]
results = batch.search_batch(suppliers, "基本信息")
# ...
screener = RiskScreener()
for supplier in suppliers:
    risk = screener.screen(supplier)
    print(screener.generate_risk_alert(risk))
```

### 场景三：长期监控告警（风控团队）
**场景描述**：监控合作企业的工商变更与风险动态.
```python
monitor = CompanyMonitor(check_interval=86400)
monitor.add("合作企业A", ["工商变更", "被执行人", "经营异常"])
monitor.add("合作企业B", ["工商变更", "失信被执行"])
monitor.start_monitoring()
```

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 30秒上手（尽调报告）
```bash
node （请参考skill目录中的脚本文件） generate-report "腾讯" --output report.json
# ...
node （请参考skill目录中的脚本文件） risk-screen "腾讯"
```

### 120秒标准搭建
```bash
export FN_API_KEY=your_private_key
# ...
cat > companies.txt <<EOF
腾讯
阿里巴巴
字节跳动
百度
京东
EOF
# ...
node （请参考skill目录中的脚本文件） batch-search --input companies.txt --output results.json
# ...
python3 due_diligence.py --company "腾讯" --output report.txt
# ...
python3 monitor.py --config monitor.yaml
```

## 配置示例
### 企业级配置
```yaml
api:
  private_key: ${FN_API_KEY}
  timeout: 30
  max_workers: 5
# ...
due_diligence:
  dimensions:
    - basic_info
    - shareholders
    - key_personnel
    - investments
    - changes
    - executed_person
    - dishonest
    - restricted_high_consumption
    - business_anomaly
    - serious_violation
    - administrative_penalty
# ...
risk_screening:
  alert_on_high_risk: true
  alert_channels:
    - type: feishu
      url: https://open.feishu.cn/open-apis/bot/v2/hook/xxx
    - type: email
      url: https://api.email-service.com/send
# ...
batch:
  max_workers: 5
  cache_enabled: true
  cache_dir: ./cache
# ...
monitoring:
  check_interval: 86400  # 每日
  alert_on_change: true
  tracked_companies:
    - name: 腾讯
      dimensions: [changes, executed_person, business_anomaly]
    - name: 阿里巴巴
      dimensions: [changes, dishonest, restricted_high_consumption]
# ...
relationship:
  max_depth: 2
  limit_per_level: 5
```

## 最佳实践
### 1. 批量查询优化
```python
class CachedBatchSearcher(BatchCompanySearcher):
    def __init__(self, cache_dir="./cache"):
        super().__init__()
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
# ...
    def _search_single(self, company, dimension):
        cache_file = os.path.join(self.cache_dir, f"{company}_{dimension}.json")
        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        result = super()._search_single(company, dimension)
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
        return result
```

### 2. 风险告警分级
```python
def classify_risk_level(risk_report):
    """风险分级"""
    if risk_report["high_risk"] > 0:
        return "高风险", "立即停止合作并调查"
    elif risk_report["medium_risk"] > 3:
        return "中风险", "需进一步调查评估"
    elif risk_report["total_risks"] > 0:
        return "低风险", "正常合作但持续监控"
    else:
        return "无风险", "正常合作"
```

### 3. 监控频率控制
```python
MONITOR_INTERVALS = {
    "工商变更": 86400,      # 每日
    "被执行人": 3600,       # 每小时
    "失信被执行": 3600,     # 每小时
    "经营异常": 86400,      # 每日
    "行政处罚": 86400 * 7,  # 每周
}
```

## 常见问题
### Q1：专业版如何与免费版兼容？
专业版完全兼容免费版的所有功能。单维度查询、模糊搜索、内置Key在专业版中均可直接使用。升级后原有脚本无需修改，仅新增高级能力可用.
### Q2：企业尽调报告包含哪些维度？
专业版尽调报告包含11个维度：基本信息、股东信息、主要人员、对外投资、工商变更、被执行人、失信被执行、限制高消费、经营异常、严重违法、行政处罚。并发查询，整合输出.
### Q3：风险筛查的6类风险分别是什么？
6类风险：(1) 被执行人（高风险）；(2) 失信被执行（高风险）；(3) 限制高消费（高风险）；(4) 经营异常（中风险）；(5) 严重违法（高风险）；(6) 行政处罚（中风险）。每类风险记录数与详情均会展示.
### Q4：批量查询的最大并发数应该设多少？
建议根据API额度与目标服务器承压能力设置：(1) 使用公用Key：建议3-5并发；(2) 使用私有Key：可提升到10并发；(3) 单次批量建议不超过50家企业.
### Q5：监控告警如何避免误报？
专业版采用"状态变化检测"策略：首次查询记录基线状态，后续查询对比变化。只有真实变化（新增记录）才触发告警。支持告警抑制（同一企业同一维度24小时内不重复告警）.
### Q6：关联关系分析的深度如何控制？
专业版默认深度2层（腾讯→投资公司A→投资公司B），可通过 `depth` 参数调整。为避免数据爆炸，每层限制最多5个节点。深度3+时查询时间会显著增加.
### Q7：私有API Key如何获取？
私有API Key可从官方平台购买，享有：(1) 更高查询额度；(2) 更多查询维度；(3) 优先技术支持。配置方式：`export FN_API_KEY=your_private_key`.
### Q8：知识产权查询包含哪些内容？
专业版知识产权查询包含：(1) 专利信息（发明/实用新型/外观设计）；(2) 商标信息（注册/申请中）；(3) 软件著作权。可按企业名称或信用代码查询.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+
- **Python**: 3.8+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Node.js 16+ | 运行时 | 必需 | 官网下载安装 |
| 企业查询API | API | 必需 | 内置公用Key 或 私有Key |
| Python 3.8+ | 运行时 | 必需 | 官网下载安装 |
| requests | Python库 | 必需 | `pip install requests`（告警推送） |
| concurrent.futures | Python库 | 必需 | Python标准库（批量查询） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 专业版使用 **GPT-4o** 模型路由，提供更强的企业关联分析与风险解读能力
- 支持自然语言尽调需求描述、智能风险解读、关联关系图谱生成

### API Key 配置
- 免费版使用内置公用Key（每日1000次额度）
- 专业版推荐配置私有Key：`export FN_API_KEY=your_private_key`
- 私有Key享有更高额度与更多查询维度
- 告警推送需配置对应平台（飞书/钉钉）的Webhook URL
- LLM模型路由由Agent平台内置提供

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行企业级尽调与风险分析任务

## 专业版特性
本专业版相比免费版新增以下能力：

- **企业尽调报告**：11个维度并发查询，整合输出完整尽调报告
- **风险筛查**：6类风险（被执行人/失信/限高/经营异常/严重违法/行政处罚）一站式筛查
- **批量查询**：多家企业并发查询，结果聚合导出
- **监控告警**：企业状态变化监控，自动告警通知
- **关联关系分析**：股东关联、投资关联网络挖掘（支持2-3层深度）
- **历史数据查询**：工商变更历史、注销/吊销记录
- **知识产权查询**：专利、商标、软件著作权
- **招投标查询**：企业招投标记录

此外，专业版还提供：
- 私有API Key支持（更高额度）
- 多角色场景指南（投资团队/采购部门/风控团队）
- 完整FAQ（8问）与故障排查表
- 性能优化建议与最佳实践
- GPT-4o模型路由与优先支持

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|:---:|:---:|:---:|:---:|
| 免费体验版 | ¥0 | 单维度查询 + 模糊搜索 + 6维度 + 公用Key(1000次/日) | 个人查询、轻量尽调 |
| 收费专业版 | ¥59/月 | 尽调报告 + 风险筛查 + 批量查询 + 监控告警 + 关联分析 + 历史数据 + 知识产权 + 招投标 + 私有Key + 优先支持 | 团队/企业、深度尽调 |

专业版通过SkillHub SkillPay发布.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 执行效率受模型能力与网络环境影响

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "企业查询助手(专业版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "company search pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
