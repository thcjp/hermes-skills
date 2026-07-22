---
slug: intel-sentinel
name: intel-sentinel
version: "1.0.1"
displayName: "情报哨兵"
summary: "开源情报自动收集与威胁分析,多源监控+AI分析+实时告警"
license: Proprietary
description: |-
  情报哨兵是一款开源情报(OSINT)自动收集与威胁分析工具。
  支持多源情报监控、AI威胁分析、实时告警推送、情报去重与关联分析。
  
  核心能力:
  - 多源情报监控(5大类情报源)
  - AI威胁分析与等级评估
  - 实时告警多渠道推送
  - 情报去重与威胁画像IOC提取
homepage: "https://skillhub.cn"
tags: [安全, 情报分析, OSINT, 威胁监控]
tools:
  - read
  - exec
suggested_price: "15.00"
pricing_tier: "business"
pricing_rationale: "数据分析类, medium市场, enterprise复杂度, weekly频次, business层 → 中频专业工具,中等市场"
---
# 情报哨兵 Intel Sentinel

开源情报(OSINT)自动收集与威胁分析工具,支持多源监控、AI威胁分析、实时告警推送、情报去重与关联分析。

## 核心能力

1. **多源情报监控**:5大类情报源监控——社交媒体(微博/推特/Telegram)、暗网论坛(Tor隐藏服务)、漏洞数据库(CVE/NVD/CNNVD)、新闻资讯(安全媒体/通用新闻)、技术博客(安全研究员博客),按配置定期采集
2. **AI威胁分析**:LLM分析情报内容,输出威胁等级评估(critical/high/medium/low/info)、攻击意图识别(APT组织/勒索软件/挖矿木马/钓鱼攻击)、影响范围预测(受影响系统/行业/地域),结构化威胁报告
3. **实时告警推送**:多渠道告警——邮件(SMTP)/Webhook(自定义HTTP回调)/IM(企业微信/钉钉/飞书),按威胁等级分级推送(critical即时推送/info汇总推送)
4. **情报去重与关联分析**:SimHash相似度检测去重(相似度>85%判定重复),关联分析识别同一攻击活动的多个情报,构建情报关联图谱
5. **威胁画像与IOC提取**:从情报中自动提取IOC(IP/域名/URL/文件哈希/邮箱),构建威胁画像(攻击者/攻击手法/目标/工具/TTPs),支持STIX 2.1格式输出共享
#
## 适用场景

| 场景 | 输入 | 输出 | 是否适用 |
|:-----|:-----|:-----|:---------|
| 企业安全态势感知 | 监控关键词+情报源配置 | 威胁情报报告+实时告警 | 适用 |
| 竞品情报监控 | 竞品名称+监控渠道 | 竞品动态情报报告 | 适用 |
| 品牌声誉监测 | 品牌关键词+社交媒体 | 品牌提及情报+负面预警 | 适用 |
| 漏洞预警追踪 | CVE ID/产品名称 | 漏洞情报+影响评估+修复建议 | 适用 |
| 暗网数据泄露监控 | 企业域名/邮箱后缀 | 泄露数据情报+告警 | 适用 |
| 内网渗透测试攻击 | 主动攻击内网系统 | 不适用(本Skill为被动情报收集非主动攻击) | 不适用 |
| 封闭私域情报获取 | 私有群组/加密通信 | 不适用(本Skill仅监控公开开源情报) | 不适用 |
| 实时网络流量分析 | 网络流量包分析 | 不适用(本Skill为情报分析非流量分析) | 不适用 |

## 使用流程

### Step 1: 配置监控任务
- 配置监控关键词(企业名称/产品名称/CVE ID/攻击组织名等)
- 配置情报源(社交媒体/暗网/漏洞库/新闻/博客,可多选)
- 配置告警渠道(邮件/Webhook/IM)和告警阈值(威胁等级)
- 配置采集频率(每小时/每天/每周)

### Step 2: 多源情报采集
- 按配置的情报源和频率定期采集
- 社交媒体:监控关键词提及(微博/推特/Telegram公开频道)
- 暗网论坛:监控Tor隐藏服务公开论坛的关键词(需Tor代理)
- 漏洞数据库:监控CVE/NVD/CNNVD新增漏洞
- 新闻资讯:监控安全媒体和通用新闻
- 技术博客:监控安全研究员博客
- 采集失败时记录日志,不阻塞其他源采集

### Step 3: 情报去重
- 计算每条情报的SimHash指纹
- 与历史情报库比对,相似度>85%判定为重复
- 重复情报标记并跳过,不重复告警
- 新情报进入分析流程

### Step 4: AI威胁分析
- LLM分析情报内容,输出:
  - 威胁等级(critical/high/medium/low/info)
  - 攻击意图(APT/勒索软件/挖矿木马/钓鱼/数据泄露/其他)
  - 影响范围(受影响系统/行业/地域)
  - IOC提取(IP/域名/URL/文件哈希/邮箱)
- 生成结构化威胁报告

### Step 5: 关联分析
- 识别同一攻击活动的多个情报(基于IOC重叠/时间关联/攻击手法相似)
- 构建情报关联图谱(节点=情报,边=关联关系)
- 输出关联分析结果

### Step 6: 告警推送
- 按威胁等级分级推送:
  - critical:即时推送(所有渠道)
  - high:即时推送(IM+邮件)
  - medium:汇总推送(每日)
  - low/info:汇总推送(每周)
- 推送失败时重试3次,仍失败记录日志

### Step 7: 威胁画像与IOC共享
- 构建威胁画像(攻击者/攻击手法/目标/工具/TTPs)
- IOC提取并存储到IOC库
- 支持STIX 2.1格式输出,便于与其他安全系统共享

## 输入格式

### 创建监控任务
```json
{
  "action": "create_monitor",
  "task_name": "企业安全监控",
  "keywords": ["企业名称", "产品名称", "CVE-2024"],
  "sources": ["social_media", "dark_web", "vulnerability_db", "news", "tech_blog"],
  "alert_channels": [{"type": "email", "target": "security@company.com"}, {"type": "webhook", "target": "https://hooks.company.com/security"}],
  "alert_threshold": "high",
  "frequency": "daily"
}
```

### 查询情报
```json
{
  "action": "query_intel",
  "keyword": "CVE-2024-1234",
  "time_range": "7d"
}
```

## 输出格式

### 威胁情报报告
```json
{
  "success": true,
  "data": {
    "intel_id": "intel_20260717_001",
    "source": "vulnerability_db",
    "title": "CVE-2024-1234: Apache Log4j 远程代码执行漏洞",
    "content": "漏洞详情...",
    "threat_level": "critical",
    "attack_intent": "远程代码执行",
    "impact_scope": {"systems": ["Apache Log4j 2.0-2.14.1"], "industries": ["全行业"], "regions": ["全球"]},
    "iocs": {"ips": [], "domains": [], "urls": [], "file_hashes": ["sha256:abc123..."], "emails": []},
    "related_intels": ["intel_20260717_002"],
    "alert_sent": true,
    "alert_channels": ["email", "webhook"],
    "timestamp": "2026-07-17T10:30:00Z"
  },
  "error": null,
  "code": null
}
```

### STIX 2.1格式输出
```json
{
  "type": "bundle",
  "id": "bundle--示例",
  "objects": [
    {"type": "indicator", "id": "indicator--示例", "pattern": "[file:hashes.'SHA-256' = 'abc123...']", "pattern_type": "stix", "valid_from": "2026-07-17T10:30:00Z"},
    {"type": "report", "id": "report--示例", "name": "CVE-2024-1234威胁报告", "published": "2026-07-17T10:30:00Z"}
  ]
}
```

## 异常处理


| 异常场景 | 原因 | 处理方式 | 错误码 |
|:---------|:-----|:---------|:-------|
| 监控任务配置错误 | keywords为空或sources无效 | 返回错误+提示正确配置 | MONITOR_CONFIG_ERROR |
| 情报源采集失败 | 源API不可用或网络超时 | 记录日志,跳过失败源,不阻塞其他源 | SOURCE_FETCH_FAILED |
| Tor代理不可用 | 暗网监控需Tor代理但未配置 | 跳过暗网源,记录warning | TOR_UNAVAILABLE |
| LLM分析失败 | LLM服务不可用 | 延迟分析,加入执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令队列,3次失败标记ANALYSIS_FAILED | LLM_FAILED |
| 告警推送失败 | 邮件/Webhook/IM渠道不可用 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令3次,仍失败记录日志,不丢失情报 | ALERT_FAILED |
| 情报去重异常 | SimHash计算失败 | 跳过去重,直接进入分析(可能重复告警) | DEDUP_SKIPPED |
| IOC提取失败 | 情报内容格式异常 | 跳过IOC提取,保留威胁报告 | IOC_EXTRACTION_FAILED |
| STIX格式转换失败 | STIX 2.1 schema校验失败 | 返回原始JSON,标记warning | STIX_CONVERT_FAILED |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | DeepSeek/通义千问/文心一言/Kimi等国内模型 |
| 情报源API | API | 可选 | 社交媒体/漏洞库/新闻等公开API(可手动提供情报) | 微博API/CNNVD(国家漏洞库)等国内情报源 |
| Tor代理 | 工具 | 可选 | 暗网论坛监控(无Tor跳过暗网源) | Tor浏览器自带,无国内替代(暗网访问需合规) |
| 邮件SMTP | 服务 | 可选 | 告警邮件推送(可仅用Webhook/IM) | 腾讯企业邮箱/阿里企业邮箱等国内SMTP服务 |
| IM推送 | API | 可选 | 企业微信/钉钉/飞书告警推送 | 企业微信/钉钉/飞书等国内IM |
| JSON文件存储 | 文件系统 | 必需 | exec工具保存情报库和配置 | 本地文件系统,无海外依赖 |

### API Key 配置与安全要求
- **LLM_API_KEY**: 必需(通常由Agent内置) - AI威胁分析
- **INTEL_API_KEY**: 可选 - 情报源API(可手动提供情报替代)
- **SMTP_PASSWORD**: 可选 - 邮件告警推送(可仅用Webhook/IM替代)
- **IM_WEBHOOK_URL**: 可选 - IM告警推送
- 配置方式: 在Agent的环境变量中设置
- **零暴露原则**: API Key必须通过环境变量注入(如`$env:INTEL_API_KEY`),严禁硬编码在SKILL.md或脚本源码中;所有示例代码中Key位置使用环境变量占位符;禁止在日志、错误信息、输出JSON中打印Key明文;情报数据中可能包含敏感IOC,存储时需加密

### 使用流程
情报源API可选,可手动提供情报数据。Tor代理可选,无Tor跳过暗网源。邮件告警可选,可仅用Webhook/IM。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 漏洞预警监控

**输入**:
```json
{
  "action": "create_monitor",
  "task_name": "Apache漏洞监控",
  "keywords": ["CVE-2024", "Apache Log4j"],
  "sources": ["vulnerability_db", "news", "tech_blog"],
  "alert_channels": [{"type": "email", "target": "security@company.com"}, {"type": "webhook", "target": "https://hooks.company.com/security"}],
  "alert_threshold": "high",
  "frequency": "daily"
}
```

**执行流程**: 创建监控任务→每日采集漏洞库/新闻/博客→SimHash去重→LLM威胁分析(等级critical)→IOC提取→告警推送(邮件+Webhook)→威胁画像构建

**输出**:
```json
{
  "success": true,
  "data": {
    "task_id": "monitor_20260717_001",
    "task_name": "Apache漏洞监控",
    "status": "active",
    "intels_collected": 3,
    "latest_intel": {
      "intel_id": "intel_20260717_001",
      "source": "vulnerability_db",
      "title": "CVE-2024-1234: Apache Log4j 远程代码执行漏洞",
      "threat_level": "critical",
      "attack_intent": "远程代码执行",
      "impact_scope": {"systems": ["Apache Log4j 2.0-2.14.1"], "industries": ["全行业"]},
      "iocs": {"file_hashes": ["sha256:abc123..."]},
      "alert_sent": true
    }
  },
  "error": null,
  "code": null
}
```

### 示例2: 品牌声誉监测

**输入**:
```json
{
  "action": "create_monitor",
  "task_name": "品牌声誉监测",
  "keywords": ["企业名称", "品牌名", "产品名"],
  "sources": ["social_media", "news"],
  "alert_channels": [{"type": "im", "target": "企业微信群机器人webhook"}],
  "alert_threshold": "medium",
  "frequency": "hourly"
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "task_id": "monitor_20260717_002",
    "task_name": "品牌声誉监测",
    "status": "active",
    "intels_collected": 15,
    "latest_intel": {
      "intel_id": "intel_20260717_010",
      "source": "social_media",
      "title": "用户在微博投诉产品问题",
      "threat_level": "medium",
      "attack_intent": "品牌声誉风险",
      "impact_scope": {"industries": ["本企业"], "regions": ["国内"]},
      "alert_sent": true,
      "alert_channels": ["im"]
    }
  },
  "error": null,
  "code": null
}
```

### 示例3: 情报源采集失败降级

**输入**: 暗网源采集失败(Tor代理未配置)
```json
{"action": "create_monitor", "task_name": "暗网监控", "keywords": ["企业域名"], "sources": ["dark_web", "social_media"]}
```

**输出**: 跳过暗网源,仅采集社交媒体
```json
{
  "success": true,
  "data": {
    "task_id": "monitor_20260717_003",
    "task_name": "暗网监控",
    "status": "active",
    "intels_collected": 2,
    "source_status": {"dark_web": "skipped", "social_media": "active"},
    "warnings": ["Tor代理未配置,暗网源已跳过(TOR_UNAVAILABLE)"]
  },
  "error": "暗网源采集失败已跳过,仅采集社交媒体源",
  "code": "TOR_UNAVAILABLE"
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 企业安全监控任务创建(多源监控+告警配置)

**输入**:
```json
{
  "action": "create_monitor",
  "task_name": "ACME Corp安全监控",
  "keywords": ["ACME Corp", "ACME数据泄露", "CVE-2026"],
  "sources": ["social_media", "dark_web", "vulnerability_db", "news", "tech_blog"],
  "alert_channels": [
    {"type": "email", "target": "security@acme.com"},
    {"type": "webhook", "target": "https://hooks.acme.com/security-alert"},
    {"type": "im", "target": "企业微信群ID"}
  ],
  "alert_threshold": "high",
  "frequency": "daily"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "task_id": "monitor_20260720_001",
    "task_name": "ACME Corp安全监控",
    "keywords": ["ACME Corp", "ACME数据泄露", "CVE-2026"],
    "sources_configured": ["social_media", "dark_web", "vulnerability_db", "news", "tech_blog"],
    "alert_channels": ["email", "webhook", "im"],
    "alert_threshold": "high",
    "frequency": "daily",
    "status": "active",
    "created_at": "2026-07-20T10:00:00Z",
    "next_scan_at": "2026-07-21T10:00:00Z"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓监控任务创建成功 ✓5类情报源全部配置 ✓3种告警渠道配置 ✓告警阈值high正确设置 ✓下次扫描时间计算正确

### 案例2: 漏洞情报查询与AI威胁分析(CVE, critical级别)

**输入**:
```json
{
  "action": "query_intel",
  "keyword": "CVE-2026-1234",
  "time_range": "7d"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "intel_id": "intel_20260720_001",
    "source": "vulnerability_db",
    "title": "CVE-2026-1234: Apache Tomcat 远程代码执行漏洞",
    "content": "Apache Tomcat 10.1.0-10.1.34版本存在远程代码执行漏洞,攻击者可通过恶意HTTP请求在服务器上执行任意代码。CVSS评分9.8(Critical)。利用条件低,无需认证。",
    "threat_level": "critical",
    "attack_intent": "远程代码执行",
    "impact_scope": {
      "systems": ["Apache Tomcat 10.1.0-10.1.34"],
      "industries": ["全行业"],
      "regions": ["全球"]
    },
    "iocs": {
      "ips": [],
      "domains": [],
      "urls": ["/manager/html?exp=cmd"],
      "file_hashes": ["sha256:a1b2c3d4e5f6789abcdef0123456789abcdef0123456789abcdef0123456789"],
      "emails": []
    },
    "related_intels": ["intel_20260720_002"],
    "alert_sent": true,
    "alert_channels": ["email", "webhook", "im"],
    "recommendations": [
      "立即升级至Apache Tomcat 10.1.35或更高版本",
      "临时缓解:限制/manager路径访问权限",
      "检查服务器日志是否存在异常HTTP请求",
      "部署WAF规则拦截恶意请求模式"
    ],
    "timestamp": "2026-07-20T10:30:00Z"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓CVE漏洞情报正确查询 ✓威胁等级critical(CVSS 9.8) ✓攻击意图远程代码执行识别 ✓IOC提取完整(URL+文件哈希) ✓告警即时推送(critical级别全渠道)

### 案例3: 暗网监控降级(Tor不可用,跳过暗网源)

**输入**:
```json
{
  "action": "create_monitor",
  "task_name": "数据泄露监控",
  "keywords": ["company.com", "@company.com"],
  "sources": ["social_media", "dark_web", "vulnerability_db", "news"],
  "alert_channels": [{"type": "im", "target": "钉钉群ID"}],
  "alert_threshold": "medium",
  "frequency": "hourly"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "task_id": "monitor_20260720_002",
    "task_name": "数据泄露监控",
    "keywords": ["company.com", "@company.com"],
    "sources_configured": ["social_media", "vulnerability_db", "news"],
    "sources_skipped": ["dark_web"],
    "alert_channels": ["im"],
    "alert_threshold": "medium",
    "frequency": "hourly",
    "status": "active",
    "created_at": "2026-07-20T11:00:00Z"
  },
  "error": "Tor代理不可用,已跳过暗网源(dark_web),其余情报源正常监控。建议安装Tor浏览器以启用暗网监控。",
  "code": "TOR_UNAVAILABLE"
}
```

**效果验证**: ✓Tor不可用正确降级(跳过暗网源) ✓其余3个情报源正常配置 ✓降级原因在error字段标注 ✓错误码TOR_UNAVAILABLE正确返回 ✓服务可用性保证(降级而非失败)

### 案例4: LLM分析失败降级(延迟分析+重试队列)

**输入**:
```json
{
  "action": "query_intel",
  "keyword": "新型勒索软件LockBit4.0",
  "time_range": "3d"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "intel_id": "intel_20260720_003",
    "source": "social_media",
    "title": "LockBit 4.0勒索软件新型变种出现",
    "content": "安全研究员在推特发布告警,LockBit勒索组织疑似发布4.0版本变种,采用新型加密算法,已知影响3家企业。",
    "threat_level": "pending",
    "attack_intent": "待分析",
    "impact_scope": {"systems": ["待分析"], "industries": ["待分析"], "regions": ["待分析"]},
    "iocs": {"ips": [], "domains": [], "urls": [], "file_hashes": [], "emails": []},
    "related_intels": [],
    "alert_sent": false,
    "alert_channels": [],
    "timestamp": "2026-07-20T12:00:00Z",
    "analysis_status": "queued_for_retry",
    "retry_count": 1
  },
  "error": "LLM分析失败,情报已加入重试队列(第1次重试),威胁分析暂时不可用。情报已存储,稍后将自动重新分析。",
  "code": "LLM_FAILED"
}
```

**效果验证**: ✓LLM失败正确降级(情报存储+重试队列) ✓threat_level标记pending ✓analysis_status标记queued_for_retry ✓重试计数1次 ✓不丢失情报(存储后重试)

### 案例5: STIX 2.1格式输出(IOC共享)

**输入**:
```json
{
  "action": "export_stix",
  "intel_id": "intel_20260720_001"
}
```

**LLM生成输出**:
```json
{
  "type": "bundle",
  "id": "bundle--acme-intel-20260720-001",
  "objects": [

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |


## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 
- 和网络环境
