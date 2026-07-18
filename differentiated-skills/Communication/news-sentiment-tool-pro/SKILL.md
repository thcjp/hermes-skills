---
slug: news-sentiment-tool-pro
name: news-sentiment-tool-pro
version: "1.0.0"
displayName: 舆情情绪分析专业版
summary: 企业级舆情监控工具,支持批量多股票扫描、自定义权重、结构化报告导出与趋势对比分析。
license: MIT
edition: pro
description: |-
  舆情情绪分析工具专业版,面向专业投资者与企业用户提供批量多股票扫描、自定义权重配置、结构化报告导出与趋势对比分析能力。

  核心能力:
  - 批量扫描多只股票(支持 A股/港股/美股混合)
  - 自定义信息源权重与事件类型分数
  - 结构化报告导出(JSON/CSV/HTML)
  - 历史情绪趋势对比分析
  - 异常情绪实时预警
  - 行业板块情绪横向对比

  适用场景:
  - 投资组合舆情全面监控
  - 行业板块情绪横向对比
  - 企业公关危机实时预警
  - 研究机构批量舆情分析

  差异化:专业版完全兼容免费版命令体系,额外提供批量扫描、自定义权重、结构化导出、趋势分析与预警能力,适合专业投资者、基金研究员与企业风控团队使用。

  触发关键词: 舆情, 情绪, 股票, 批量, 监控, 预警, 趋势, sentiment, scan, 港股, 美股, a股, 行业, 板块, 投资组合
tags:
- 沟通协作
- 舆情监控
- 情绪分析
- 投资辅助
- 企业效率
- 数据分析
- 风险预警
tools:
- read
- exec
---

# 舆情情绪分析工具 - 专业版

## 概述

舆情情绪分析工具专业版是一款面向专业投资者与企业用户的企业级舆情监控解决方案。在完全兼容免费版单股扫描能力的基础上,专业版解锁了批量多股票扫描、自定义权重配置、结构化报告导出、历史趋势对比分析、异常情绪实时预警等高级能力。

无论是监控整个投资组合的舆情动态、对比行业板块情绪强弱、还是设置公关危机预警阈值,专业版都能通过命令行高效完成,为投资决策与风险管控提供数据支撑。

### 免费版与专业版能力对比

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 单股扫描 | 支持 | 支持 |
| 批量多股扫描 | 不支持 | 支持(无上限) |
| 跨市场混合扫描 | 不支持 | 支持(A/港/美混合) |
| 自定义信息源权重 | 不支持 | 支持 |
| 自定义事件类型分数 | 不支持 | 支持 |
| 报告格式 | 文本 | 文本/JSON/CSV/HTML |
| 历史趋势对比 | 不支持 | 支持 |
| 异常情绪预警 | 不支持 | 支持 |
| 行业板块对比 | 不支持 | 支持 |
| 定时任务调度 | 不支持 | 支持 |
| 数据源扩展 | 公开数据源 | 支持付费数据源接入 |

## 核心能力

### 一、批量多股票扫描(专业版独有)

- 支持同时扫描多只股票
- 支持 A股、港股、美股混合扫描
- 支持从 CSV/JSON 文件导入股票清单
- 并发扫描提升效率

### 二、自定义权重配置(专业版独有)

- 自定义信息源权重(公告/研报/媒体/社交等)
- 自定义事件类型基础分数
- 支持保存多套权重方案
- 按场景快速切换配置

### 三、结构化报告导出(专业版独有)

- JSON 格式:便于程序处理与二次分析
- CSV 格式:便于导入 Excel 或数据库
- HTML 格式:便于分享与可视化展示
- 自定义报告模板

### 四、历史趋势对比(专业版独有)

- 保存历史扫描结果
- 对比不同时间点的情绪变化
- 生成情绪趋势图表
- 识别情绪拐点

### 五、异常情绪预警(专业版独有)

- 设置情绪分数阈值
- 情绪突变实时告警
- 支持邮件/消息通知
- 可集成到监控系统中

### 六、行业板块对比(专业版独有)

- 同行业多只股票横向对比
- 板块整体情绪汇总
- 识别板块内强弱分化
- 输出板块情绪排名

## 使用场景

### 场景一:投资组合批量舆情扫描

基金经理需对持仓的 20 只股票进行批量舆情扫描,生成组合情绪报告。

```bash
# 从 CSV 文件导入股票清单批量扫描
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --format json --output report.json
```

**portfolio.csv 示例**:

```text
code,market,name
002594,cn,比亚迪
600519,cn,贵州茅台
0700.HK,hk,腾讯控股
AAPL,us,苹果
TSLA,us,特斯拉
```

**批量扫描输出示例(JSON)**:

```json
{
  "scan_time": "2026-07-18T10:30:00Z",
  "period_days": 7,
  "total_stocks": 5,
  "results": [
    {
      "code": "002594",
      "name": "比亚迪",
      "sentiment_score": 5.2,
      "sentiment_label": "偏正面",
      "positive_events": 3,
      "negative_events": 1,
      "top_event": "6月销量同比增长35%"
    },
    {
      "code": "600519",
      "name": "贵州茅台",
      "sentiment_score": 2.1,
      "sentiment_label": "轻微正面",
      "positive_events": 2,
      "negative_events": 2,
      "top_event": "中秋备货期启动"
    }
  ],
  "portfolio_summary": {
    "average_score": 3.8,
    "positive_count": 4,
    "neutral_count": 1,
    "negative_count": 0
  }
}
```

### 场景二:行业板块情绪横向对比

研究员需对比新能源汽车板块内多只股票的舆情强弱。

```bash
# 扫描新能源汽车板块
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch ev_sector.csv 7 --compare --format html --output ev_report.html
```

**ev_sector.csv 示例**:

```text
code,market,name
002594,cn,比亚迪
601127,cn,赛力斯
9866.HK,hk,蔚来-SW
9868.HK,hk,小鹏汽车
XPEV,us,小鹏汽车
NIO,us,蔚来
```

**板块对比输出示例**:

```text
==================================================
新能源汽车板块情绪对比报告
==================================================

扫描周期:最近7天 | 扫描时间:2026-07-18

板块情绪排名:
1. 比亚迪(002594)      +5.2  偏正面    ▲
2. 赛力斯(601127)      +3.8  轻微正面  ▲
3. 蔚来-SW(9866.HK)    +1.5  中性      -
4. 小鹏汽车(9868.HK)   -0.8  中性      ▼
5. 蔚来(NIO)           -2.3  轻微负面  ▼
6. 小鹏汽车(XPEV)      -3.1  轻微负面  ▼

板块整体情绪:+0.7(中性偏正面)
板块内分化:明显(最高+5.2,最低-3.1)

领涨股:比亚迪(+5.2)
领跌股:小鹏汽车 XPEV(-3.1)
```

### 场景三:异常情绪实时预警

企业风控团队需对关注的股票设置情绪预警阈值,当情绪突变时及时通知。

```bash
# 启动实时预警监控(后台运行)
python3 {SKILL_DIR}/scripts/sentiment_monitor.py \
    --watch watchlist.csv \
    --threshold-negative -5 \
    --threshold-positive 7 \
    --interval 3600 \
    --notify email \
    --notify-config notify.json
```

**watchlist.csv 示例**:

```text
code,market,name,alert_negative,alert_positive
002594,cn,比亚迪,-5,7
0700.HK,hk,腾讯控股,-6,8
AAPL,us,苹果,-5,7
```

**notify.json 配置示例**:

```json
{
  "email": {
    "smtp_host": "smtp.company.com",
    "smtp_port": 465,
    "sender": "alert@company.com",
    "recipients": ["trader@company.com", "risk@company.com"]
  }
}
```

**预警通知示例**:

```text
[预警] 比亚迪(002594)情绪突变!
时间:2026-07-18 14:30:00
当前情绪:-6.5(偏负面)
阈值:-5.0
触发事件:证监会立案调查
建议:立即关注,评估持仓风险。
```

## 快速开始

### 第一步:准备股票清单

```bash
# 创建股票清单 CSV
cat > portfolio.csv << 'EOF'
code,market,name
002594,cn,比亚迪
600519,cn,贵州茅台
0700.HK,hk,腾讯控股
AAPL,us,苹果
EOF
```

### 第二步:执行批量扫描

```bash
# 批量扫描并导出 JSON 报告
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --format json --output report.json

# 批量扫描并导出 HTML 报告
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --format html --output report.html
```

### 第三步:查看分析结果

```bash
# 查看 JSON 报告摘要
python3 -c "
import json
with open('report.json') as f:
    data = json.load(f)
print(f'扫描股票数: {data[\"total_stocks\"]}')
print(f'组合平均情绪: {data[\"portfolio_summary\"][\"average_score\"]}')
for r in data['results']:
    print(f'  {r[\"name\"]}: {r[\"sentiment_score\"]} ({r[\"sentiment_label\"]})')
"
```

## 配置示例

### 自定义权重配置

```bash
# 自定义信息源权重配置文件 weights.json
cat > weights.json << 'EOF'
{
  "sources": {
    "company_announcement": 1.0,
    "broker_report": 0.9,
    "mainstream_media": 0.8,
    "regulatory_filing": 0.9,
    "social_media": 0.6,
    "forum_post": 0.5
  },
  "event_types": {
    "earnings_beat": 5,
    "rating_upgrade": 3,
    "insider_buying": 3,
    "policy_positive": 4,
    "product_launch": 2,
    "earnings_miss": -4,
    "rating_downgrade": -3,
    "insider_selling": -3,
    "policy_negative": -4,
    "regulatory_investigation": -5
  }
}
EOF

# 使用自定义权重扫描
python3 {SKILL_DIR}/scripts/sentiment_scan.py 002594 7 --weights weights.json
```

### 定时任务配置

```bash
# 设置每日定时扫描(crontab)
# 每天早上8点执行组合舆情扫描
0 8 * * * python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --format json --output /tmp/daily_report.json

# 每周一早上8点执行周度对比分析
0 8 * * 1 python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --compare --format html --output /tmp/weekly_report.html
```

### 企业级自动化工作流

```python
#!/usr/bin/env python3
"""企业舆情监控自动化工作流"""
import subprocess
import json
from datetime import datetime

class SentimentAutomation:
    def __init__(self, script_path):
        self.script = script_path

    def scan_single(self, code, days=7, market='auto'):
        """单股扫描"""
        result = subprocess.run(
            ['python3', self.script, code, str(days), market, '--format', 'json'],
            capture_output=True, text=True
        )
        return json.loads(result.stdout) if result.stdout else {}

    def scan_batch(self, csv_file, days=7, output_format='json'):
        """批量扫描"""
        output_file = f'report_{datetime.now().strftime("%Y%m%d")}.{output_format}'
        subprocess.run([
            'python3', self.script, '--batch', csv_file, str(days),
            '--format', output_format, '--output', output_file
        ])
        return output_file

    def compare_trend(self, csv_file, days=7):
        """趋势对比分析"""
        result = subprocess.run(
            ['python3', self.script, '--batch', csv_file, str(days), '--compare', '--format', 'json'],
            capture_output=True, text=True
        )
        return json.loads(result.stdout) if result.stdout else {}

    def check_alerts(self, results, neg_threshold=-5, pos_threshold=7):
        """检查预警"""
        alerts = []
        for r in results:
            score = r.get('sentiment_score', 0)
            if score <= neg_threshold:
                alerts.append({
                    'code': r['code'],
                    'name': r['name'],
                    'score': score,
                    'type': 'negative',
                    'message': f"{r['name']} 情绪分数 {score},低于阈值 {neg_threshold}"
                })
            elif score >= pos_threshold:
                alerts.append({
                    'code': r['code'],
                    'name': r['name'],
                    'score': score,
                    'type': 'positive',
                    'message': f"{r['name']} 情绪分数 {score},高于阈值 {pos_threshold}"
                })
        return alerts

# 使用示例
automation = SentimentAutomation('{SKILL_DIR}/scripts/sentiment_scan.py')

# 每日组合扫描
report_file = automation.scan_batch('portfolio.csv', days=7)

# 检查预警
with open(report_file) as f:
    report = json.load(f)
alerts = automation.check_alerts(report['results'])

if alerts:
    print("发现预警:")
    for alert in alerts:
        print(f"  [{alert['type']}] {alert['message']}")
else:
    print("无预警,组合情绪正常。")
```

## 最佳实践

### 1. 批量扫描使用文件导入

避免命令行传入大量参数,使用 CSV 文件管理股票清单,便于维护与复用:

```bash
# 推荐:CSV 文件导入
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7

# 不推荐:命令行传多个股票(易出错)
python3 {SKILL_DIR}/scripts/sentiment_scan.py --codes "002594,600519,0700.HK" 7
```

### 2. 按场景保存多套权重方案

不同分析场景适用不同权重,建议保存多套配置:

```bash
# 保守型权重(更信任官方信源)
python3 {SKILL_DIR}/scripts/sentiment_scan.py 002594 7 --weights conservative.json

# 激进型权重(更关注社交媒体情绪)
python3 {SKILL_DIR}/scripts/sentiment_scan.py 002594 7 --weights aggressive.json

# 均衡型权重(默认)
python3 {SKILL_DIR}/scripts/sentiment_scan.py 002594 7
```

### 3. 历史报告按日期归档

便于后续趋势对比分析:

```bash
# 按日期归档报告
DATE=$(date +%Y%m%d)
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 \
    --format json \
    --output ~/reports/sentiment_${DATE}.json
```

### 4. 预警阈值合理设置

| 资产类型 | 负面阈值 | 正面阈值 | 说明 |
|:---------|:---------|:---------|:-----|
| 稳健型持仓 | -3 | 5 | 低阈值,敏感预警 |
| 均衡型持仓 | -5 | 7 | 中阈值,平衡预警 |
| 激进型持仓 | -7 | 8 | 高阈值,仅预警极端事件 |

### 5. 结构化报告便于二次分析

优先使用 JSON 或 CSV 格式,便于导入数据库或 BI 工具做深度分析:

```bash
# 导出 CSV 便于 Excel 分析
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --format csv --output report.csv

# 导出 JSON 便于程序处理
python3 {SKILL_DIR}/scripts/sentiment_scan.py --batch portfolio.csv 7 --format json --output report.json
```

## 常见问题

### Q1: 批量扫描时部分股票失败怎么办?

**A**: 批量扫描会跳过失败的股票并继续处理其余股票。失败原因常见于:
- 股票代码格式错误
- 该市场数据源暂时不可用
- 网络波动

扫描完成后查看报告中的 `failed_stocks` 字段,针对性重试。

### Q2: 自定义权重如何确定合理值?

**A**: 权重设置建议:
- 官方信源(公告、监管文件)权重最高(0.9-1.0)
- 专业分析(研报)权重次之(0.8-0.9)
- 大众媒体权重中等(0.7-0.8)
- 社交媒体权重较低(0.5-0.6)
- 论坛讨论权重最低(0.4-0.5)

可根据自身投资风格微调,保守型投资者可降低社交媒体权重。

### Q3: 历史趋势对比需要保存多少数据?

**A**: 建议:
- 短期趋势:保存最近 30 天的每日扫描结果
- 中期趋势:保存最近 90 天的每周扫描结果
- 长期趋势:保存最近 1 年的每月扫描结果

### Q4: 预警通知支持哪些渠道?

**A**: 专业版支持以下通知渠道:
- 邮件通知(内置 SMTP 支持)
- Webhook 回调(可对接企业 IM)
- 命令行输出(便于集成到监控脚本)
- 文件日志(便于审计追溯)

### Q5: 免费版用户升级后历史数据是否保留?

**A**: 完全保留。专业版沿用免费版的扫描脚本与数据格式,升级后历史扫描结果可直接用于趋势对比分析。

### Q6: 是否支持接入付费数据源?

**A**: 专业版支持扩展数据源。在配置文件中添加付费数据源的 API Key 即可接入(如 Wind、Bloomberg、东方财富等),提升数据覆盖面与准确性。

## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 建议 3.8+
- **网络环境**: 需可访问财经数据源与社交媒体
- **定时任务**: 建议 cron(Linux/macOS)或任务计划程序(Windows)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| sentiment_scan.py | 脚本 | 必需 | 随 Skill 安装 |
| sentiment_monitor.py | 脚本 | 必需 | 随 Skill 安装(专业版) |
| requests | Python库 | 必需 | pip install requests |
| pandas | Python库 | 推荐 | pip install pandas |
| 财经数据源 | API | 必需 | 公开数据源(默认) |
| 付费数据源(可选) | API | 可选 | Wind/Bloomberg 等 |
| SMTP 服务 | 服务 | 推荐 | 用于邮件预警通知 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 默认使用公开数据源,无需额外 API Key
- 付费数据源(如 Wind、Bloomberg)需在配置文件中填入对应 API Key
- 邮件预警通知需配置 SMTP 服务器地址、端口与发件账号
- Webhook 通知需配置回调 URL 与认证信息

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,核心功能通过 Python 脚本执行需要 exec 命令行执行能力)
- **说明**: 基于脚本的企业级 AI Skill,通过自然语言指令驱动 Agent 执行舆情监控。专业版完全兼容免费版单股扫描能力,额外提供批量多股票扫描、自定义权重配置、结构化报告导出(JSON/CSV/HTML)、历史趋势对比分析与异常情绪实时预警能力,适合专业投资者、基金研究员与企业风控团队使用。本工具仅供参考,不构成投资建议。
