---
slug: news-aggregator-tool-pro
name: news-aggregator-tool-pro
version: "1.0.0"
displayName: 新闻聚合工具专业版
summary: 企业级新闻聚合平台，支持国内外30+信息源、定时聚合、多格式导出与API集成
license: Proprietary
edition: pro
description: |-
  新闻聚合工具专业版。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- 新闻
- 聚合
- 企业级
- 国际新闻
- 舆情监控
tools:
  - - read
- exec
# 新闻聚合工具（专业版）
## 概述
---
新闻聚合工具专业版在免费版国内新闻聚合的基础上，新增 30+ 国内外信息源、定时自动聚合、突发新闻触发推送、多格式导出、自定义新闻源接入、多语言聚合和 REST API 集成等企业级能力，满足企业舆情监控、媒体采编和行业研究的深度需求。

PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有新闻源配置和过滤规则均可无缝迁移。

## 核心能力
### 能力矩阵
| 能力项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| 新闻类别 | 3类（科技/军事/社会） | 6类+自定义 |
| 信息源数 | 10个国内源 | 30+国内外源 |
| 国际新闻 | 不支持 | 完整支持 |
| 定时聚合 | 不支持 | 多时段自动聚合 |
| 突发推送 | 不支持 | 实时事件触发 |
| 导出格式 | Markdown | MD/PDF/Email/Webhook |
| 自定义源 | 不支持 | 支持接入+评级 |
| 多语言 | 中文 | 中/英/日/韩 |
| API 集成 | 不支持 | REST API |
| 趋势分析 | 不支持 | 热点追踪+趋势 |
| 历史检索 | 不支持 | 90天历史检索 |

### PRO 专属信息源
```text
[PRO] 国际科技：TechCrunch、The Verge、Wired、Ars Technica
[PRO] 国际军事：Defense News、Jane's Defence、Military Times
[PRO] 国际社会：BBC、Reuters、AP、Al Jazeera
[PRO] 财经新闻：Bloomberg、Financial Times、Wall Street Journal
[PRO] 行业新闻：自定义行业垂直媒体
[PRO] 多语言源：日语（Nikkei）、韩语（Yonhap）等
```

## 使用场景
### 场景一：企业舆情监控
企业公关部门需要全天候监控与企业相关的新闻动态。

```python
monitoring_config = {
    "keywords": ["企业名称", "CEO姓名", "产品名称", "竞品名称"],
    "sources": {
        "domestic": ["baidu_news", "sogou_news", "weibo", "weixin"],
        "international": ["google_news", "reuters", "bloomberg"],
        "social": ["weibo", "zhihu", "twitter"]
    },
    "alert_levels": {
        "critical": ["负面报道", "监管处罚", "安全事故"],
        "warning": ["竞品动态", "行业政策", "高管变动"],
        "info": ["正面报道", "行业趋势", "市场分析"]
    },
    "notification": {
        "critical": ["sms", "email", "webhook", "phone"],
        "warning": ["email", "webhook"],
        "info": ["email"]
    }
}
```

### 场景二：定时多类别聚合
媒体机构需要定时获取多个类别的新闻，用于采编参考。

```bash
cat > ~/news-agg-pro/schedules/editorial.yaml << 'EOF'
schedules:
  - name: "tech_morning"
    cron: "0 6 * * 1-5"
    categories: [tech]
    sources: [all_domestic, all_international]
    max_items: 20
    deduplicate: true
    output:
      format: markdown
      path: "~/news-agg-pro/reports/tech_morning_{date}.md"

  - name: "all_categories_noon"
    cron: "0 12 * * 1-5"
    categories: [tech, military, society, finance]
    sources: [all_domestic]
    max_items: 15
    deduplicate: true
    output:
      format: pdf
      path: "~/news-agg-pro/reports/noon_brief_{date}.pdf"
      email_to: ["editor@media.local"]

  - name: "intl_evening"
    cron: "0 18 * * 1-5"
    categories: [international]
    sources: [bbc, reuters, ap, aljazeera]
    max_items: 10
    language: en
    translate: true
    output:
      format: markdown
      path: "~/news-agg-pro/reports/intl_evening_{date}.md"
EOF
```

### 场景三：突发新闻触发推送
当检测到重大新闻事件时，自动触发推送通知。

```text
用户：配置突发新闻触发，当出现"重大政策"或"市场异常"相关新闻时立即推送

Agent：
1. 设置关键词监控
2. 配置触发条件（A级来源+关键词匹配）
3. 设置推送渠道（邮件+Webhook+短信）
4. 启动实时监控
```

## 快速开始
### 步骤一：初始化 PRO 环境
```bash
mkdir -p ~/news-agg-pro/{config,schedules,reports,exports,history,analytics}

cat > ~/news-agg-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

sources:
  tech:
    domestic: [36kr, jiqizhixin, ithome, baijia]
    international: [techcrunch, theverge, wired, arstechnica]
  military:
    domestic: [guancha, thepaper, qq_mil]
    international: [defensenews, janes, militarytimes]
  society:
    domestic: [cctv, xinhua, tencent]
    international: [bbc, reuters, ap, aljazeera]
  finance:
    domestic: [cls, stcn, yicai]
    international: [bloomberg, ft, wsj]
  international:
    - bbc, reuters, ap, aljazeera, dw, npr

custom_sources:
  enabled: true
  config_path: "~/news-agg-pro/config/custom_sources.yaml"

aggregation:
  deduplicate: true
  similarity_threshold: 0.85
  credibility_filter: true
  max_items_per_category: 20
  cross_language_dedup: true

scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  config_path: "~/news-agg-pro/schedules/"

export:
  formats: ["markdown", "pdf", "email", "webhook"]
  path: "~/news-agg-pro/exports/"

languages: ["zh-CN", "en-US", "ja-JP", "ko-KR"]
auto_translate: true

analytics:
  enabled: true
  trend_tracking: true
  hotspot_detection: true

history:
  enabled: true
  retention_days: 90
  searchable: true

api:
  enabled: true
  rate_limit: "200/hour"
EOF
```

### 步骤二：从免费版迁移
```bash
if [ -f ~/news-aggregator/config.yaml ]; then
    cp ~/news-aggregator/config.yaml ~/news-agg-pro/config/free_config.bak
    echo "免费版配置已备份"
fi
```

### 步骤三：执行首次全类别聚合
```text
用户：执行首次全类别新闻聚合

Agent：
1. 读取所有配置的新闻源
2. 按类别并行搜索
3. 跨语言去重合并
4. 可信度过滤排序
5. 生成综合报告并导出
```

## 示例
### 自定义新闻源
```yaml
custom_sources:
  - name: "企业内部新闻"
    type: "rss"
    url: "https://intranet.company.com/rss/news"
    category: "internal"
    tier: "A"
    auth:
      type: "bearer"
      token: "${INTERNAL_TOKEN}"

  - name: "行业垂直媒体"
    type: "api"
    url: "https://api.industry-media.local/v1/articles"
    category: "industry"
    tier: "B"
    query_params:
      industry: "semiconductor"
      language: "zh"

  - name: "合作伙伴动态"
    type: "webhook"
    url: "https://partner.local/news-webhook"
    category: "partner"
    tier: "B"
    direction: "incoming"
```

### 跨语言去重配置
```python
class CrossLanguageDedup:
    def __init__(self):
        self.translator = TranslationService()
        self.similarity = SemanticSimilarity()

    def deduplicate(self, articles):
        """跨语言新闻去重"""
        for article in articles:
            if article['language'] != 'zh':
                article['translated_summary'] = self.translator.translate(
                    article['summary'], target='zh'
                )
            else:
                article['translated_summary'] = article['summary']

        unique = []
        for article in articles:
            is_dup = False
            for existing in unique:
                ratio = self.similarity.compute(
                    article['translated_summary'],
                    existing['translated_summary']
                )
                if ratio > 0.85:
                    is_dup = True
                    existing['related_articles'].append({
                        'url': article['url'],
                        'language': article['language'],
                        'source': article['source']
                    })
                    break
            if not is_dup:
                article['related_articles'] = []
                unique.append(article)

        return unique
```

### REST API 集成
```python
import requests

class NewsAggregatorProClient:
    def __init__(self, api_key, base_url="https://api.news-agg-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def aggregate(self, categories, sources=None, language="zh"):
        """执行新闻聚合"""
        resp = requests.post(
            f"{self.base_url}/v1/aggregate",
            headers=self.headers,
            json={
                "categories": categories,
                "sources": sources or "all",
                "language": language
            }
        )
        return resp.json()

    def create_schedule(self, schedule_config):
        """创建定时聚合任务"""
        resp = requests.post(
            f"{self.base_url}/v1/schedules",
            headers=self.headers,
            json=schedule_config
        )
        return resp.json()

    def search_history(self, query, days=90):
        """搜索历史新闻"""
        resp = requests.get(
            f"{self.base_url}/v1/history",
            headers=self.headers,
            params={"q": query, "days": days}
        )
        return resp.json()

    def get_trends(self, category, period="7d"):
        """获取新闻趋势分析"""
        resp = requests.get(
            f"{self.base_url}/v1/trends",
            headers=self.headers,
            params={"category": category, "period": period}
        )
        return resp.json()
```

## 最佳实践
### 1. 按场景配置聚合策略
```python
AGGREGATION_PRESETS = {
    "daily_brief": {
        "categories": ["tech", "society"],
        "sources": "tier_a_only",
        "max_items": 10,
        "deduplicate": True,
        "format": "markdown"
    },
    "industry_monitor": {
        "categories": ["tech", "finance"],
        "sources": "all",
        "max_items": 30,
        "deduplicate": True,
        "cross_language": True,
        "format": "pdf"
    },
    "crisis_alert": {
        "categories": "all",
        "sources": "all",
        "trigger": "keyword_match",
        "keywords": ["危机", "事故", "处罚", "召回"],
        "format": "email",
        "immediate": True
    }
}
```

### 2. 利用趋势分析
```text
用户：分析过去7天科技新闻的热点趋势

Agent：
1. 调取7天内所有科技新闻
2. 按关键词聚类分析
3. 识别热度上升趋势
4. 生成趋势分析报告
```

### 3. 设置多级告警
```bash
cat > ~/news-agg-pro/alerts.yaml << 'EOF'
alerts:
  - level: critical
    conditions:
      - keywords: ["重大事故", "监管处罚", "数据泄露"]
        credibility: "A"
    action: immediate_push
    channels: [sms, email, webhook, phone]

  - level: warning
    conditions:
      - keywords: ["高管变动", "业绩预警", "诉讼"]
        credibility: "B"
    action: batch_push
    channels: [email, webhook]
    interval: "1h"

  - level: info
    conditions:
      - keywords: ["行业报告", "市场分析"]
        credibility: "B"
    action: daily_digest
    channels: [email]
EOF
```

### 4. 利用历史检索
```text
用户：搜索过去30天关于"AI监管"的新闻

Agent：
1. 检索90天历史新闻库
2. 关键词匹配"AI监管"
3. 按时间排序输出
4. 提供趋势分析
```

## 常见问题
### Q1：PRO 版本支持多少新闻源？
PRO 版本内置 30+ 国内外新闻源，并支持通过 RSS/API/Webhook 接入自定义新闻源，无上限限制。

### Q2：定时聚合最小间隔是多少？
定时聚合最小间隔为 30 分钟，突发新闻触发推送为实时（延迟 < 1 分钟）。

### Q3：跨语言去重如何工作？
PRO 版本先将所有新闻摘要翻译为统一语言（默认中文），再使用语义相似度模型进行去重，准确率高于标题匹配。

### Q4：历史新闻保留多久？
默认保留 90 天，可通过配置调整。历史新闻支持全文检索。

### 已知限制
默认每小时 200 次调用，突发新闻触发推送不受频率限制。

### Q6：免费版如何升级至 PRO 版本？
PRO 版本初始化时会自动检测免费版配置，新闻源和过滤规则可一键迁移。

## 依赖说明
### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.10 及以上（推荐 3.12）
- **网络连接**: 稳定的互联网连接，访问国际源需配置代理
- **存储空间**: 至少 1GB 用于历史新闻与报告存储

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| 网络搜索 | 服务 | 必需 | Agent 内置搜索能力 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| requests | Python 包 | 可选 | `pip install requests` |
| PyYAML | Python 包 | 可选 | `pip install pyyaml` |
| 翻译服务 | API | 可选 | 用于跨语言翻译 |
| pandoc | 工具 | 可选 | 系统包管理器安装（PDF导出） |
| 网络代理 | 服务 | 可选 | 用于访问国际新闻源 |

### API Key 配置
PRO 版本支持 API 集成，需配置相关密钥：

```bash
export NEWS_AGG_PRO_API_KEY="your_api_key"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

export TRANSLATION_API_KEY="your_translation_key"

cat > ~/news-agg-pro/.env << 'EOF'
NEWS_AGG_PRO_API_KEY=your_api_key
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
TRANSLATION_API_KEY=your_translation_key
EOF
```

### 可用性分类
- **分类**: MD+EXEC+API（Markdown 指令 + 命令行执行 + API 集成）
- **说明**: PRO 版本支持多源聚合、定时调度、跨语言去重、趋势分析与 REST API 集成
- **适用规模**: 企业公关部门、媒体机构、行业研究机构
- **兼容性**: 与 news-aggregator-tool-free 完全兼容，支持配置迁移与平滑升级
- **支持级别**: 优先技术支持，提供自定义新闻源接入与告警规则定制服务

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
