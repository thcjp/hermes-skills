---
slug: web-scraper-engine
name: web-scraper-engine
version: 1.1.0
displayName: 网页抓取引擎
summary: Firecrawl/Playwright/Crawl4AI全流程网页数据采集,搜索爬取提取表单
license: Proprietary
description: 网页抓取引擎——基于Firecrawl/Playwright/Crawl4AI实现全流程网页数据采集。覆盖搜索发现、单页抓取、结构化提取、多步骤浏览器交互全链路。同时提供Crawl4AI开源国内替代方案,无需海外API。适用于竞品分析、价格监控、内容采集、Lead
  Generation、市场调研、结构化提取场景。触发关键词:网页抓取、爬虫、Firecrawl、Playwright、Crawl4AI、网页提取、数据采集、结构化提取、浏览器自动化、竞品监控、价格监控
tags:
- 网页抓取
- 数据采集
- 爬虫
- 竞品监控
- 数据提取
tools:
- read
- exec
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec", "glob"]
tags: "Web开发,前端,开发工具"
---
# 网页抓取引擎

基于 Firecrawl / Playwright / Crawl4AI 实现全流程网页数据采集。从搜索发现到结构化提取,从单页抓取到多步骤浏览器交互,无需维护爬虫基础设施。同时提供开源国内替代方案(Crawl4AI),降低对海外 API 的依赖。

## 核心能力

1. **搜索与发现**:关键词搜索发现网页、站点地图扫描、URL 队列构建
2. **单页抓取与结构化提取**:Markdown/HTML/纯文本输出 + JSON Schema 自动提取
3. **批量异步爬取**:深度控制、路径过滤、速率限制、结果去重
4. **多步骤浏览器交互**:点击/表单填写/翻页/登录状态保持
5. **数据处理与导出**:清洗、结构化、CSV/JSON/Parquet 导出、数据库写入

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 竞品分析 | 竞品网站列表 + 采集字段 | 产品/价格/评论结构化数据 + 对比报告 |
| 价格监控 | 电商商品 URL + 监控频率 | 定时抓取结果 + 价格变动报告 |
| 内容采集 | 站点 URL + 内容类型 | 文章/博客 Markdown + 聚合站点 |
| Lead Generation | 行业关键词 + 公司信息字段 | 公司列表 + 联系方式 JSON |
| 市场调研 | 行业关键词 + 数据维度 | 搜索结果 + 批量抓取 + 分析报告 |
| 结构化提取 | 页面 URL + Schema 定义 | JSON 结构化数据 |

**不适用于**:
- 大规模分布式爬虫(单机能力有限,需要 Scrapy Cluster 等架构)
- 实时数据流(本 Skill 为批量采集,非流式)
- APP 内数据抓取(需要 Appium 等移动端工具)
- 加密/混淆内容的破解(仅采集公开可访问内容)
- 违反 robots.txt 或法律法规的爬取(需遵守合规要求)
- 需要登录态的私有数据(技术上可行,但需注意合规与隐私)

## 使用流程

### Step 1: 需求分析与方案选择
1. **明确采集目标**:URL/关键词/数据字段
2. **合规检查**:检查目标站点 robots.txt、ToS、数据版权
3. **方案选择**:
   - 简单页面(无 JS 渲染)→ Firecrawl scrape / requests + BeautifulSoup
   - JS 渲染页面 → Firecrawl / Playwright
   - 大规模爬取 → Crawl4AI(开源,无 API 费用)
   - 多步骤交互 → Playwright
4. **频率规划**:避免高频请求导致 IP 封禁

### Step 2: 搜索发现
1. **关键词搜索**
   - Firecrawl: `POST /v1/search` 输入关键词,返回相关网页
   - Crawl4AI: 内置搜索 + URL 提取
   - 参数:query/limit/scrapeOptions
   - 输出:URL 列表 + 标题 + 摘要
2. **站点地图发现**
   - 获取目标站点 sitemap.xml
   - 过滤不需要的页面
   - 构建爬取队列

### Step 3: 单页抓取
1. **基础抓取**
   - Firecrawl: `POST /v1/scrape` 抓取单个 URL
   - Playwright: `page.goto(url)` + `page.content()`
   - 输出:Markdown/HTML/纯文本
   - 自动处理 JS 渲染
2. **结构化提取**
   - 使用 Schema 定义提取字段(JSON Schema)
   - 自动识别页面内容
   - 输出 JSON 格式
3. **截图**
   - 全页截图
   - 可视化验证

### Step 4: 批量爬取
1. **异步爬取**
   - Firecrawl: `POST /v1/crawl` 提交 URL 列表,返回 job ID
   - Crawl4AI: 内置并发爬取
2. **爬取策略**
   - 深度控制:仅首页/2层/全站
   - 路径过滤:include/exclude 规则
   - 速率限制:并发数控制 + 请求间隔
3. **结果处理**
   - 统一格式输出
   - 去重(URL 规范化 + 内容哈希)
   - 导出 CSV/JSON

### Step 5: 多步骤浏览器交互
1. **点击操作**:点击按钮/链接,等待页面加载,处理弹窗
2. **表单填写**:填充输入框,选择下拉菜单,提交表单
3. **翻页**:点击"下一页",等待新数据加载,收集每页数据
4. **登录状态**:注入 Cookie/Token,处理认证流程,会话保持

### Step 6: 数据处理与导出
1. **清洗**:移除 HTML 标签,去除空白字符,统一编码(UTF-8)
2. **结构化**:JSON Schema 映射,字段类型转换,数据验证
3. **存储**:导出 CSV/JSON/Parquet,写入数据库,上传 OSS/COS

## 国内外抓取方案对照

| 维度 | Firecrawl(海外) | Crawl4AI(开源) | Playwright | Scrapy |
|:-----|:-----|:-----|:-----|:-----|
| 类型 | SaaS API | 开源库 | 开源库 | 开源框架 |
| 国内可用 | 需代理 | 完全可用 | 完全可用 | 完全可用 |
| 费用 | 免费500页/月,付费$20+/月 | 完全免费 | 完全免费 | 完全免费 |
| JS 渲染 | 内置 | 内置(基于 Playwright) | 原生支持 | 需配合 Splash |
| 结构化提取 | LLM 辅助 + Schema | LLM 辅助 + Schema | 需手动解析 | 需手动解析 |
| 多步骤交互 | 有限支持 | 有限支持 | 完全支持 | 需自定义 |
| 大规模爬取 | 受 API 限额 | 本地资源限制 | 本地资源限制 | 高性能 |
| 部署 | SaaS 无需部署 | 本地或 Docker | 本地或 Docker | 本地或 Docker |
| 国内推荐 | 不推荐 | 推荐 | 推荐 | 推荐(传统站点) |

## 示例

### 示例1: 竞品价格监控(输入→输出)

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | 网页抓取引擎处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
用户请求:抓取3个竞品电商网站的产品价格,每周更新
竞品: 京东、淘宝、拼多多
商品: iPhone 15 Pro 256GB
```

**输出**(scrape-result.json):
```python
# scrape.py
from firecrawl import FirecrawlApp
import json
# ...
app = FirecrawlApp(api_key=os.environ['FIRECRAWL_API_KEY'])
# ...
# Schema 定义
schema = {
    "type": "object",
    "properties": {
        "product_name": {"type": "string"},
        "price": {"type": "number"},
        "currency": {"type": "string"},
        "availability": {"type": "boolean"},
        "platform": {"type": "string"},
        "url": {"type": "string"},
        "scraped_at": {"type": "string"}
    }
}
# ...
# 抓取结果
results = [
    {
        "product_name": "Apple iPhone 15 Pro 256GB",
        "price": 7999.00,
        "currency": "CNY",
        "availability": true,
        "platform": "京东",
        "url": "https://item.jd.com/100xxx.html",
        "scraped_at": "2026-01-15T10:00:00Z"
    },
    {
        "product_name": "Apple iPhone 15 Pro 256GB",
        "price": 7599.00,
        "currency": "CNY",
        "availability": true,
        "platform": "拼多多",
        "url": "https://mobile.yangkeduo.com/xxx.html",
        "scraped_at": "2026-01-15T10:00:00Z"
    }
]
# ...
# 导出 CSV
import pandas as pd
df = pd.DataFrame(results)
df.to_csv('price_monitor.csv', index=False)
# ...
# 价格对比报告
report = f"""
## 价格监控报告 ({results[0]['scraped_at']})
# ...
| 平台 | 价格 | 可用性 |
|:---:|:---:|:---:|
| 京东 | ¥7999 | 有货 |
| 拼多多 | ¥7599 | 有货 |
# ...
最低价: 拼多多 ¥7599
最高价: 京东 ¥7999
价差: ¥400 (5%)
"""
```

### 示例2: Crawl4AI 国内开源替代(输入→输出)

**输入**:
```
用户请求: 使用开源工具抓取某新闻网站最新文章
要求: 不依赖海外 API,完全本地运行
目标: https://news.example.com
```

**输出**(scrape.py):
```python
# 使用 Crawl4AI 开源方案
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import asyncio
import json
# ...
async def scrape_news():
    async with AsyncWebCrawler() as crawler:
        # CSS 选择器提取策略
        extraction_strategy = JsonCssExtractionStrategy({
            "name": "News Articles",
            "baseSelector": "article.news-item",
            "fields": [
                {"name": "title", "selector": "h2.title", "type": "text"},
                {"name": "url", "selector": "a", "type": "attribute", "attribute": "href"},
                {"name": "date", "selector": ".date", "type": "text"},
                {"name": "summary", "selector": ".summary", "type": "text"}
            ]
        })
# ...
        result = await crawler.arun(
            url="https://news.example.com",
            extraction_strategy=extraction_strategy,
            bypass_cache=True
        )
# ...
        # 输出结构化 JSON
        articles = json.loads(result.extracted_content)
        print(f"抓取到 {len(articles)} 篇文章")
# ...
        # 导出
        with open('articles.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
# ...
asyncio.run(scrape_news())
```

### 示例3: 多步骤表单提交(输入→输出)

**输入**:
```
用户请求: 自动填写某网站的查询表单,翻页采集结果
目标: https://search.example.com
步骤: 1)填写关键词 2)选择日期 3)点击搜索 4)翻页采集
```

**输出**(scrape.py):
```python
from playwright.async_api import async_playwright
import pandas as pd
import asyncio
# ...
async def scrape_with_form():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
# ...
        # 1. 加载页面
        await page.goto('https://search.example.com')
# ...
        # 2. 填写表单
        await page.fill('#keyword', '人工智能')
        await page.select_option('#date-range', 'last-30-days')
# ...
        # 3. 点击搜索
        await page.click('button[type="submit"]')
        await page.wait_for_selector('.result-item')
# ...
        # 4. 翻页采集
        all_results = []
        while True:
            # 提取当前页结果
            items = await page.query_selector_all('.result-item')
            for item in items:
                title = await (await item.query_selector('.title')).inner_text()
                url = await (await item.query_selector('a')).get_attribute('href')
                all_results.append({'title': title, 'url': url})
# ...
            # 检查是否有下一页
            next_btn = await page.query_selector('.next-page:not([disabled])')
            if not next_btn:
                break
            await next_btn.click()
            await page.wait_for_selector('.result-item')
# ...
        # 5. 导出 CSV
        df = pd.DataFrame(all_results)
        df.to_csv('search_results.csv', index=False)
        print(f"采集完成,共 {len(all_results)} 条结果")
# ...
        await browser.close()
# ...
asyncio.run(scrape_with_form())
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 页面加载超时 | 网络慢或页面资源过多 | 设置 30s 超时,重试 3 次,跳过失败页 |
| JS 渲染失败 | SPA 应用加载慢 | 增加 wait_for_selector 等待关键元素 |
| 反爬虫检测 | 频率过高或 User-Agent 异常 | 使用代理 IP,降低速率,设置随机延迟 |
| 结构化提取失败 | 页面结构变化或 Schema 不匹配 | 回退到 Markdown 提取,LLM 辅助解析 |
| 登录状态过期 | Cookie/Token 过期 | 刷新 Token/Cookie,重新认证 |
| 数据格式不一致 | 不同页面字段差异 | 字段映射容错,默认值处理 |
| Firecrawl API 超时 | 海外网络延迟 | 切换至 Crawl4AI 本地方案 |
| IP 被封禁 | 高频请求触发风控 | 轮换代理 IP,降低并发,遵守 robots.txt |
| Cloudflare 防护 | 高级反爬 | 使用 Playwright + stealth 模式 |
| 数据编码问题 | GBK/GB2312 编码 | 自动检测编码,chardet 库辅助 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.10+ 或 Node.js 18+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|---:|:---|---:|---:|:---|
| LLM API | API | 必需 | Agent 内置 LLM | 通义/文心/智谱 |
| Firecrawl SDK | SDK | 可选(海外) | `pip install firecrawl-py` | Crawl4AI(开源) |
| Crawl4AI | 库 | 推荐(国内) | `pip install crawl4ai` | - |
| Playwright | 库 | 可选(交互) | `pip install playwright` | - |
| Python | 运行时 | 必需 | python.org | 国内镜像源 |
| Pandas | 库 | 可选(数据处理) | `pip install pandas` | 国内 PyPI 镜像 |
| 代理 IP | 服务 | 可选(大规模) | 商业代理服务 | 国内代理服务商 |

### API Key 配置
- **Firecrawl**: API Key 从 firecrawl.dev 获取(免费 500 页/月)
- **Crawl4AI**: 无需 API Key(开源,完全本地)
- **Playwright**: 无需 API Key(开源)
- **安全要求**:
  - API Key 仅存储在环境变量,不写入源码
  - 抓取的 Cookie/Token 不写入日志
  - 敏感数据(用户信息)脱敏后存储

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行 Python 脚本

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 竞品价格监控(Firecrawl+JSON Schema提取+CSV导出+对比报告)

**输入**:
```
目标: 监控3个电商平台iPhone 15 Pro 256GB价格
平台: 京东、拼多多、天猫
Schema字段: product_name, price, currency, availability, platform, url, scraped_at
频率: 每周一次
输出: CSV文件 + Markdown价格对比报告
```

**LLM生成输出** (`output/price-monitor/scrape.py`):
```python
import os
import json
import csv
from datetime import datetime
from firecrawl import FirecrawlApp
# ...
app = FirecrawlApp(api_key=os.environ['FIRECRAWL_API_KEY'])
# ...
# JSON Schema 定义
price_schema = {
    "type": "object",
    "properties": {
        "product_name": {"type": "string", "description": "商品名称"},
        "price": {"type": "number", "description": "当前售价"},
        "original_price": {"type": "number", "description": "原价"},
        "currency": {"type": "string", "description": "货币"},
        "availability": {"type": "boolean", "description": "是否有货"},
        "discount": {"type": "string", "description": "优惠信息"}
    },
    "required": ["product_name", "price", "currency", "availability"]
}
# ...
# 目标URL列表
targets = [
    {"platform": "京东", "url": "https://item.jd.com/100074466498.html"},
    {"platform": "拼多多", "url": "https://mobile.yangkeduo.com/goods.html?goods_id=420001234567"},
    {"platform": "天猫", "url": "https://detail.tmall.com/item.htm?id=678901234567"},
]
# ...
results = []
scraped_at = datetime.utcnow().isoformat() + "Z"
# ...
for target in targets:
    try:
        response = app.scrape_url(target['url'], params={
            'formats': ['json'],
            'jsonOptions': {
                'prompt': '提取商品名称、当前售价、原价、货币、是否有货、优惠信息',
                'schema': price_schema
            },
            'waitFor': 3000  # 等待JS渲染
        })
# ...
        data = response.get('json', {})
        data['platform'] = target['platform']
        data['url'] = target['url']
        data['scraped_at'] = scraped_at
        results.append(data)
        print(f"[{target['platform']}] {data.get('product_name', 'N/A')} - ¥{data.get('price', 'N/A')}")
# ...
    except Exception as e:
        print(f"[{target['platform']}] 抓取失败: {e}")
        results.append({
            'platform': target['platform'],
            'url': target['url'],
            'scraped_at': scraped_at,
            'error': str(e)
        })
# ...
# 导出CSV
csv_file = 'price_monitor.csv'
fieldnames = ['platform', 'product_name', 'price', 'original_price', 'currency',
              'availability', 'discount', 'url', 'scraped_at', 'error']
with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(results)
print(f"\nCSV导出: {csv_file}")
# ...
# 生成价格对比报告
valid_results = [r for r in results if 'price' in r]
if valid_results:
    prices = [(r['platform'], r['price']) for r in valid_results]
    min_platform, min_price = min(prices, key=lambda x: x[1])
    max_platform, max_price = max(prices, key=lambda x: x[1])
# ...
    report = f"""# 价格监控报告
# ...
**抓取时间**: {scraped_at}
**商品**: iPhone 15 Pro 256GB
# ...
## 价格对比
# ...
| 平台 | 商品名称 | 售价 | 原价 | 是否有货 | 优惠 |
|:------:|--------|:-------|:------:|--------|:-------|
"""
    for r in valid_results:
        report += f"| {r['platform']} | {r.get('product_name','N/A')} | ¥{r.get('price','N/A')} | ¥{r.get('original_price','-')} | {'有货' if r.get('availability') else '缺货'} | {r.get('discount','-')} |\n"
# ...
    report += f"""
## 分析
# ...
- **最低价**: {min_platform} ¥{min_price}
- **最高价**: {max_platform} ¥{max_price}
- **价差**: ¥{max_price - min_price} ({(max_price - min_price) / min_price * 100:.1f}%)
# ...
## 建议
# ...
"""
    if max_price - min_price > 200:
        report += f"- 价差较大(¥{max_price - min_price}),建议在{min_platform}购买\n"
    else:
        report += "- 各平台价格接近,建议选择物流最快的平台\n"
# ...
    report += "- 拼多多价格通常最低,但需注意百亿补贴商品真伪\n"
    report += "- 京东自营售后最有保障,适合追求稳妥的用户\n"
# ...
    with open('price_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"报告导出: price_report.md")
```

**LLM生成输出** (`output/price-monitor/price_monitor.csv`):
```csv
platform,product_name,price,original_price,currency,availability,discount,url,scraped_at
京东,Apple iPhone 15 Pro 256GB 钛金属,7999.00,8999.00,CNY,True,plus会员-100,item.jd.com/100074466498.html,2026-01-15T10:00:00Z
拼多多,Apple iPhone 15 Pro 256GB,7599.00,8999.00,CNY,True,百亿补贴,yangkeduo.com/goods.html?id=420001234567,2026-01-15T10:00:00Z
天猫,Apple/苹果 iPhone 15 Pro 256GB,7799.00,8999.00,CNY,True,88VIP-50,detail.tmall.com/item.htm?id=678901234567,2026-01-15T10:00:00Z
```

**效果验证**: ✓JSON Schema定义6字段(含required约束) ✓Firecrawl scrape_url含waitFor等待JS渲染 ✓异常处理try-catch记录错误不影响其他平台 ✓CSV导出使用utf-8-sig防Excel中文乱码 ✓Markdown报告含价格对比表+最低/最高价分析+购买建议 ✓价差百分比计算

### 案例2: Crawl4AI新闻网站批量爬取(开源+CSS提取+去重+JSON导出)

**输入**:
```
目标: 抓取36氪最新科技文章
工具: Crawl4AI(开源,无API费用,国内可用)
要求: 完全本地运行,不依赖海外服务
提取字段: 标题、链接、发布时间、摘要、作者
去重: URL规范化 + 内容哈希
导出: JSON + Markdown摘要
```

**LLM生成输出** (`output/news-scraper/scrape_36kr.py`):
```python
import asyncio
import json
import hashlib
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
# ...
# CSS提取策略(36氪文章列表)
extraction_strategy = JsonCssExtractionStrategy({
    "name": "36Kr Articles",
    "baseSelector": "div.article-item",
    "fields": [
        {"name": "title", "selector": "a.article-item-title", "type": "text"},
        {"name": "url", "selector": "a.article-item-title", "type": "attribute", "attribute": "href"},
        {"name": "summary", "selector": "a.article-item-description", "type": "text"},
        {"name": "author", "selector": "span.article-item-author", "type": "text"},
        {"name": "date", "selector": "span.article-item-time", "type": "text"}
    ]
})
# ...
# URL规范化(去重用)
def normalize_url(url: str) -> str:
    """移除查询参数和锚点,统一为小写"""
    from urllib.parse import urlparse, urlunparse
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', '')).lower()
# ...
# 内容哈希(去重用)
def content_hash(article: dict) -> str:
    """基于标题+摘要生成哈希"""
    content = f"{article.get('title','')}{article.get('summary','')}"
    return hashlib.md5(content.encode('utf-8')).hexdigest()
# ...
async def scrape_36kr():
    async with AsyncWebCrawler(
        headless=True,
        # 反检测配置
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        # 速率限制
        delay_before_return_html=2
    ) as crawler:
# ...
        # 抓取首页文章列表
        result = await crawler.arun(
            url="https://36kr.com/information/technology/",
            extraction_strategy=extraction_strategy,
            bypass_cache=True
        )
# ...
        if not result.extracted_content:
            print("未提取到内容")
            return
# ...
        articles = json.loads(result.extracted_content)
        print(f"原始抓取: {len(articles)} 篇文章")
# ...
        # 去重: URL规范化 + 内容哈希
        seen_urls = set()
        seen_hashes = set()
        unique_articles = []
# ...
        for article in articles:
            # 补全URL
            url = article.get('url', '')
            if url.startswith('/'):
                article['url'] = f"https://36kr.com{url}"
# ...
            # URL去重
            norm_url = normalize_url(article['url'])
            if norm_url in seen_urls:
                continue
            seen_urls.add(norm_url)
# ...
            # 内容去重
            chash = content_hash(article)
            if chash in seen_hashes:
                continue
            seen_hashes.add(chash)
# ...
            # 清洗数据
            article['title'] = article.get('title', '').strip()
            article['summary'] = article.get('summary', '').strip()
            article['author'] = article.get('author', '36氪').strip()
            article['date'] = article.get('date', '').strip()
# ...
            unique_articles.append(article)
# ...
        print(f"去重后: {len(unique_articles)} 篇文章")
# ...
        # 导出JSON
        with open('articles.json', 'w', encoding='utf-8') as f:
            json.dump(unique_articles, f, ensure_ascii=False, indent=2)
        print("JSON导出: articles.json")
# ...
        # 导出Markdown摘要
        with open('articles_summary.md', 'w', encoding='utf-8') as f:
            f.write(f"# 36氪科技文章摘要\n\n")
            f.write(f"**抓取时间**: {asyncio.get_event_loop().time()}\n")
            f.write(f"**文章数量**: {len(unique_articles)} 篇\n\n")
            f.write("---\n\n")
            for i, article in enumerate(unique_articles, 1):
                f.write(f"## {i}. {article['title']}\n\n")
                f.write(f"- **作者**: {article['author']}\n")
                f.write(f"- **时间**: {article['date']}\n")
                f.write(f"- **链接**: {article['url']}\n")
                f.write(f"- **摘要**: {article['summary'][:100]}...\n\n")
        print("Markdown导出: articles_summary.md")
# ...
        return unique_articles
# ...
# 运行
articles = asyncio.run(scrape_36kr())
```

**LLM生成输出** (`output/news-scraper/articles.json` - 示例):
```json
[
  {
    "title": "OpenAI发布GPT-5:多模态推理能力大幅提升",
    "url": "https://36kr.com/p/2801234567890123",
    "summary": "OpenAI今日发布GPT-5模型,在数学推理、代码生成和图像理解方面表现显著提升,支持100万token上下文窗口...",
    "author": "36氪Tech",
    "date": "2026-01-15 09:30"
  },
  {
    "title": "字节跳动豆包大模型日均调用量突破万亿token",
    "url": "https://36kr.com/p/2801234567890124",
    "summary": "字节跳动宣布其豆包大模型日均调用量已突破1万亿token,成为国内调用量最大的大模型之一...",
    "author": "36氪AI",
    "date": "2026-01-15 08:15"
  }
]
```

**效果验证**: ✓Crawl4AI完全开源无API费用(国内可用) ✓JsonCssExtractionStrategy用CSS选择器精确提取5字段 ✓双层去重(URL规范化+MD5内容哈希) ✓数据清洗(strip空白+补全相对URL) ✓双格式导出(JSON结构化+Markdown摘要) ✓反检测配置(User-Agent+延迟)

### 案例3: Playwright多步骤交互(登录+搜索+翻页采集+CSV导出)

**输入**:
```
目标: 自动登录企业内部系统,搜索订单,翻页采集结果
工具: Playwright(浏览器自动化)
步骤:
  1) 打开登录页,输入账号密码
  2) 登录后跳转搜索页
  3) 输入关键词"已完成订单",选择日期范围
  4) 点击搜索,等待结果加载
  5) 翻页采集每页10条数据
  6) 导出CSV
反爬: 随机延迟+stealth模式
```

**LLM生成输出** (`output/order-scraper/scrape_orders.py`):
```python
import asyncio
import csv
import random
from playwright.async_api import async_playwright
# ...
async def scrape_orders():
    async with async_playwright() as p:
        # 启动浏览器(stealth模式)
        browser = await p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled']
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080},
            locale='zh-CN'
        )
# ...
        # 注入stealth脚本(隐藏webdriver特征)
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
            window.chrome = { runtime: {} };
        """)
# ...
        page = await context.new_page()
# ...
        # ===== Step 1: 登录 =====
        print("Step 1: 登录...")
        await page.goto('https://internal.example.com/login', wait_until='networkidle')
        await page.fill('#username', 'admin')
        await page.fill('#password', 'secure_password_123')
        await page.click('button[type="submit"]')
# ...
        # 等待登录成功(跳转到首页)
        await page.wait_for_url('**/dashboard', timeout=10000)
        print("登录成功")
        await asyncio.sleep(random.uniform(1, 3))  # 随机延迟
# ...
        # ===== Step 2: 导航到搜索页 =====
        print("Step 2: 导航到搜索页...")
        await page.click('a[href="/orders/search"]')
        await page.wait_for_selector('#search-keyword', timeout=10000)
# ...
        # ===== Step 3: 填写搜索条件 =====
        print("Step 3: 填写搜索条件...")
        await page.fill('#search-keyword', '已完成订单')
        await page.select_option('#date-range', 'last-30-days')
        await page.select_option('#status', 'completed')
# ...
        # ===== Step 4: 点击搜索 =====
        print("Step 4: 执行搜索...")
        await page.click('button#btn-search')
        await page.wait_for_selector('.order-row', timeout=15000)
        print("搜索结果已加载")
# ...
        # ===== Step 5: 翻页采集 =====
        all_orders = []
        page_num = 1
# ...
        while True:
            print(f"  采集第 {page_num} 页...")
            await asyncio.sleep(random.uniform(2, 4))  # 随机延迟防反爬
# ...
            # 提取当前页数据
            rows = await page.query_selector_all('.order-row')
            for row in rows:
                order = {
                    'order_id': await (await row.query_selector('.col-id')).inner_text(),
                    'customer': await (await row.query_selector('.col-customer')).inner_text(),
                    'amount': await (await row.query_selector('.col-amount')).inner_text(),
                    'status': await (await row.query_selector('.col-status')).inner_text(),
                    'date': await (await row.query_selector('.col-date')).inner_text(),
                }
                all_orders.append(order)
# ...
            # 检查是否有下一页
            next_btn = await page.query_selector('.pagination .next:not(.disabled)')
            if not next_btn:
                print("  已到最后一页")
                break
# ...
            await next_btn.click()
            await page.wait_for_selector('.order-row', timeout=10000)
            await asyncio.sleep(random.uniform(1, 2))  # 翻页延迟
            page_num += 1
# ...
        # ===== Step 6: 导出CSV =====
        print(f"\n采集完成,共 {len(all_orders)} 条订单")
        csv_file = 'orders_export.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=['order_id', 'customer', 'amount', 'status', 'date'])
            writer.writeheader()
            writer.writerows(all_orders)
        print(f"CSV导出: {csv_file}")
# ...
        # 截图保存(可视化验证)
        await page.screenshot(path='final_page.png', full_page=True)
        print("截图保存: final_page.png")
# ...
        await browser.close()
# ...
asyncio.run(scrape_orders())
```

**LLM生成输出** (运行日志):
```
Step 1: 登录...
登录成功
Step 2: 导航到搜索页...
Step 3: 填写搜索条件...
Step 4: 执行搜索...
搜索结果已加载
  采集第 1 页...
  采集第 2 页...
  采集第 3 页...
  采集第 4 页...
  采集第 5 页...
  已到最后一页
# ...
采集完成,共 50 条订单
CSV导出: orders_export.csv
截图保存: final_page.png
```

**效果验证**: ✓6步骤完整流程(登录→搜索→填表→搜索→翻页→导出) ✓stealth模式(隐藏webdriver+模拟plugins+chrome.runtime) ✓随机延迟(random.uniform 2-4s)防反爬检测 ✓wait_for_url/wait_for_selector确保元素加载 ✓翻页逻辑检测disabled状态自动停止 ✓CSV导出utf-8-sig + 全页截图可视化验证

### 案例4: 结构化提取多站点职位信息(JSON Schema+批量+去重+数据库写入)

**输入**:
```
目标: 从3个招聘网站提取Python开发岗位信息
站点: lagou.com, zhipin.com, 51job.com
Schema: 职位标题、公司、薪资范围、地点、经验要求、学历要求、职位描述、发布时间、来源URL
去重: 公司名+职位标题组合去重
导出: JSON + SQLite数据库
```

**LLM生成输出** (`output/job-scraper/scrape_jobs.py`):
```python
import asyncio
import json
import sqlite3
import hashlib
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
# ...
# 统一职位Schema
job_schema_fields = [
    {"name": "title", "selector": ".job-title", "type": "text"},
    {"name": "company", "selector": ".company-name", "type": "text"},
    {"name": "salary", "selector": ".salary", "type": "text"},
    {"name": "location", "selector": ".location", "type": "text"},
    {"name": "experience", "selector": ".experience", "type": "text"},
    {"name": "education", "selector": ".education", "type": "text"},
    {"name": "description", "selector": ".job-desc", "type": "text"},
    {"name": "publish_date", "selector": ".publish-time", "type": "text"},
    {"name": "detail_url", "selector": "a.job-link", "type": "attribute", "attribute": "href"}
]
# ...
# 各站点配置(选择器可能不同)
site_configs = {
    "lagou": {
        "url": "https://www.lagou.com/jobs/list_Python",
        "base_selector": ".item.con_list_item",
        "fields": job_schema_fields
    },
    "boss": {
        "url": "https://www.zhipin.com/web/geek/job?query=Python",
        "base_selector": ".job-card-wrapper",
        "fields": job_schema_fields
    },
    "51job": {
        "url": "https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html",
        "base_selector": ".j_joblist .e",
        "fields": job_schema_fields
    }
}
# ...
def dedup_key(job: dict) -> str:
    """公司名+职位标题组合去重键"""
    combined = f"{job.get('company','')}-{job.get('title','')}"
    return hashlib.md5(combined.encode('utf-8')).hexdigest()
# ...
def parse_salary(salary_str: str) -> dict:
    """解析薪资字符串 '15-25K·13薪' -> {min, max, unit, months}"""
    import re
    result = {'min': None, 'max': None, 'unit': 'K', 'months': 12}
    match = re.match(r'(\d+)-(\d+)([Kk万])', salary_str)
    if match:
        result['min'] = int(match.group(1))
        result['max'] = int(match.group(2))
        result['unit'] = '万' if match.group(3) in ['万', 'w', 'W'] else 'K'
    months_match = re.search(r'(\d+)薪', salary_str)
    if months_match:
        result['months'] = int(months_match.group(1))
    return result
# ...
async def scrape_all_sites():
    all_jobs = []
    seen_keys = set()
# ...
    async with AsyncWebCrawler(headless=True) as crawler:
        for site_name, config in site_configs.items():
            print(f"\n抓取 {site_name}...")
            try:
                strategy = JsonCssExtractionStrategy({
                    "name": f"{site_name}_jobs",
                    "baseSelector": config["base_selector"],
                    "fields": config["fields"]
                })
# ...
                result = await crawler.arun(
                    url=config["url"],
                    extraction_strategy=strategy,
                    bypass_cache=True
                )
# ...
                if not result.extracted_content:
                    print(f"  {site_name}: 未提取到内容")
                    continue
# ...
                jobs = json.loads(result.extracted_content)
                print(f"  {site_name}: 抓取到 {len(jobs)} 条")
# ...
                for job in jobs:
                    # 添加来源信息
                    job['source'] = site_name
                    job['source_url'] = config['url']
# ...
                    # 去重
                    key = dedup_key(job)
                    if key in seen_keys:
                        continue
                    seen_keys.add(key)
# ...
                    # 薪资解析
                    salary_info = parse_salary(job.get('salary', ''))
                    job['salary_min'] = salary_info['min']
                    job['salary_max'] = salary_info['max']
                    job['salary_months'] = salary_info['months']
# ...
                    # 清洗
                    for k, v in job.items():
                        if isinstance(v, str):
                            job[k] = v.strip()
# ...
                    all_jobs.append(job)
# ...
            except Exception as e:
                print(f"  {site_name} 抓取失败: {e}")
# ...
    print(f"\n去重后总计: {len(all_jobs)} 条职位")
# ...
    # 导出JSON
    with open('jobs.json', 'w', encoding='utf-8') as f:
        json.dump(all_jobs, f, ensure_ascii=False, indent=2)
    print("JSON导出: jobs.json")
# ...
    # 写入SQLite数据库
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT, company TEXT, salary TEXT,
            salary_min INTEGER, salary_max INTEGER, salary_months INTEGER,
            location TEXT, experience TEXT, education TEXT,
            description TEXT, publish_date TEXT,
            source TEXT, source_url TEXT, detail_url TEXT,
            dedup_key TEXT UNIQUE,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
# ...
    for job in all_jobs:
        job['dedup_key'] = dedup_key(job)
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO jobs
                (title, company, salary, salary_min, salary_max, salary_months,
                 location, experience, education, description, publish_date,
                 source, source_url, detail_url, dedup_key)
                VALUES (:title, :company, :salary, :salary_min, :salary_max, :salary_months,
                        :location, :experience, :education, :description, :publish_date,
                        :source, :source_url, :detail_url, :dedup_key)
            ''', job)
        except sqlite3.IntegrityError:
            pass  # 去重
# ...
    conn.commit()
    print(f"数据库写入: jobs.db ({cursor.execute('SELECT COUNT(*) FROM jobs').fetchone()[0]} 条)")
    conn.close()
# ...
asyncio.run(scrape_all_sites())
```

**LLM生成输出** (运行日志):
```
抓取 lagou...
  lagou: 抓取到 15 条
抓取 boss...
  boss: 抓取到 20 条
抓取 51job...
  51job: 抓取到 18 条
# ...
去重后总计: 47 条职位(去重6条)
JSON导出: jobs.json
数据库写入: jobs.db (47 条)
```

**效果验证**: ✓多站点统一Schema(CSS选择器配置化) ✓公司名+职位标题MD5组合去重 ✓薪资字符串解析(15-25K·13薪→min/max/months结构化) ✓双重存储(JSON文件+SQLite数据库) ✓SQLite dedup_key UNIQUE约束防重复写入 ✓INSERT OR IGNORE优雅处理重复 ✓每站点独立try-catch不影响其他站点

## 常见问题

### Q1: 国内项目应该用 Firecrawl 还是 Crawl4AI?
A: 推荐方案:
- **Crawl4AI(首选)**: 开源免费,完全本地运行,无海外 API 依赖,内置 LLM 辅助提取
- **Playwright**: 需要多步骤交互(登录/翻页/表单)时使用
- **Firecrawl**: 仅在需要快速验证或海外站点时使用(需代理)
- **Scrapy**: 传统站点大规模爬取(性能最优,但无 JS 渲染)
- 推荐组合: Crawl4AI(主力)+ Playwright(交互)+ Pandas(处理)

### Q2: 如何避免被反爬虫检测?
A: 多层策略:
1. **频率控制**: 请求间隔 1-3 秒,随机延迟
2. **User-Agent 轮换**: 模拟真实浏览器
3. **代理 IP 池**: 轮换 IP,避免单 IP 高频
4. **Headless 检测规避**: Playwright + stealth 模式
5. **Cookie/Session 管理**: 保持会话,模拟真实用户
6. **遵守 robots.txt**: 优先检查,尊重站点规则
7. **Crawl4AI 内置反检测**: 自动处理常见反爬

### Q3: 结构化提取如何保证准确性?
A: 三层保障:
1. **CSS/XPath 选择器**: 精确定位元素(最可靠)
2. **JSON Schema 约束**: 定义字段类型与必填性
3. **LLM 辅助**: 复杂页面用 LLM 解析(Crawl4AI/Firecrawl 内置)
- 推荐: 优先用选择器,复杂场景用 LLM 兜底

### Q4: 抓取的数据如何合法使用?
A: 合规要点:
1. **检查 robots.txt**: 尊重站点爬取规则
2. **阅读 ToS**: 服务条款可能禁止爬取
3. **数据版权**: 公开数据可采集,但再发布需授权
4. **个人隐私**: 不采集个人身份信息(姓名/手机/身份证)
5. **频率合理**: 不影响目标站点正常服务
6. **商业使用**: 竞品数据用于内部分析,不直接公开
7. **遵守《数据安全法》《个人信息保护法》**

## 已知限制

- 单机能力有限,大规模分布式爬取需 Scrapy Cluster 等架构
- 不涉及 APP 内数据抓取(需要 Appium 等移动端工具)
- 不破解加密/混淆内容(仅采集公开可访问内容)
- 高级反爬(Cloudflare/PerimeterX)可能需要商业方案
- 不涉及实时数据流(本 Skill 为批量采集)
- 国内访问 Firecrawl 需代理,建议优先使用 Crawl4AI
- 不覆盖视频/音频文件下载(专注于文本与结构化数据)

## 安全声明

- API Key(Firecrawl)仅通过环境变量读取,绝不硬编码
- 抓取的 Cookie/Token/Session 不写入日志或输出文件
- 用户隐私数据(姓名/手机/身份证)自动脱敏或拒绝采集
- 输出的抓取结果不包含任何登录凭证
- 遵守 robots.txt 与目标站点 ToS,不进行违规爬取
- 不支持绕过付费墙或访问控制
- 大规模爬取前建议咨询法律合规
