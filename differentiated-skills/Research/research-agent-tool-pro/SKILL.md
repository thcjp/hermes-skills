---
slug: research-agent-tool-pro
name: research-agent-tool-pro
version: "1.0.0"
displayName: 研究代理助手专业版
summary: 企业级研究代理平台，支持深度异步研究、多主题并行、定时任务与API集成
license: MIT
edition: pro
description: |-
  研究代理助手专业版，面向研究机构和企业提供深度异步研究、多主题并行处理、定时任务与API集成能力。

  核心能力:
  - 深度异步研究模式（后台自动执行）
  - 多主题并行研究（10+个同时进行）
  - 定时研究任务与自动结果检查
  - 多格式导出（PDF/Word/HTML）
  - 研究文档版本管理与回溯
  - 多租户团队协作与权限控制
  - REST API 集成与自动化工作流
  - 研究模板自定义

  适用场景:
  - 研究机构批量课题调研
  - 企业战略规划深度研究
  - 咨询公司项目制研究
  - 投资机构尽职调查

  差异化:
  - PRO 版本与免费版完全兼容，支持平滑升级
  - 新增深度异步研究、多主题并行、团队协作等企业级能力
  - 支持API集成与自动化工作流
  - 提供优先技术支持与定制化服务

  触发关键词: 深度研究代理, 异步研究, 多主题并行, 研究API, 批量调研, research agent pro
tags:
- 研究
- 企业级
- 深度研究
- 团队协作
- 自动化
tools:
- read
- exec
---

# 研究代理助手（专业版）

## 概述

研究代理助手专业版在免费版交互式研究的基础上，新增深度异步研究模式、多主题并行处理、定时研究任务、多格式导出、版本管理、多租户团队协作和 REST API 集成等企业级能力，满足研究机构和企业对深度、批量、自动化研究的全面需求。

PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有研究文档和工作区均可无缝迁移。

## 核心能力

### 能力矩阵

| 能力项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| 研究模式 | 交互式 | 交互式+深度异步 |
| 并发主题 | 1个 | 10+个并行 |
| 处理深度 | 实时对话 | 分钟至小时级深度 |
| 定时研究 | 不支持 | cron调度 |
| 自动检查 | 不支持 | 自动轮询结果 |
| 导出格式 | PDF | PDF/Word/HTML |
| 版本管理 | 不支持 | 完整版本控制 |
| 团队协作 | 不支持 | 多租户+权限 |
| API 集成 | 不支持 | REST API |
| 研究模板 | 固定 | 自定义模板 |
| 历史检索 | 不支持 | 全文检索 |
| 研究毕业 | 基础 | 自动转化为项目spec |

### PRO 专属能力详解

```text
[PRO] 深度异步研究模式（后台自动执行）
[PRO] 多主题并行研究（最多10个并发）
[PRO] 定时研究任务（cron调度）
[PRO] 自动结果检查与通知
[PRO] 多格式导出（PDF/Word/HTML/Markdown）
[PRO] 研究文档版本管理与回溯
[PRO] 多租户团队协作与权限控制
[PRO] REST API 集成与自动化工作流
[PRO] 自定义研究模板
[PRO] 历史研究全文检索
[PRO] 研究自动毕业为项目spec
[PRO] 研究质量评估报告
```

## 使用场景

### 场景一：深度异步研究

对复杂主题进行全面的异步深度研究，无需实时交互等待。

```text
用户：deep research: 2026年全球量子计算产业发展前景分析

Agent 执行流程：
1. 启动深度异步研究任务
2. 任务在后台运行（数分钟至数小时）
3. 自动定期检查进度
4. 完成后保存详细报告
5. 通知用户查看结果
```

启动命令：

```bash
# 启动深度研究（异步模式）
research-agent create "2026年全球量子计算产业发展前景分析" \
    --mode deep \
    --async

# 查看任务状态
research-agent status <run_id>

# 获取研究结果
research-agent result <run_id>

# 等待完成（阻塞模式，适合短任务）
research-agent create "简单主题研究" --mode deep --wait
```

### 场景二：批量多主题并行研究

研究机构需要同时开展多个相关课题的深度研究。

```python
# batch_research.py - 批量研究脚本
research_topics = [
    "固态电池技术发展路线图与商业化时间表",
    "自动驾驶L4级别量产技术瓶颈分析",
    "AI芯片供应链安全风险评估",
    "碳交易市场机制与投资机会分析",
    "生物医药AI应用前景与监管挑战"
]

# 批量启动深度研究
results = []
for topic in research_topics:
    result = research_agent.create(
        topic=topic,
        mode="deep",
        async_mode=True
    )
    results.append(result)
    print(f"已启动: {topic}")
    print(f"  Run ID: {result.run_id}")
    print(f"  预计完成: {result.estimated_completion}")
```

批量管理：

```bash
# 查看所有运行中的研究
research-agent list --status running

# 批量检查状态
for run_id in $(cat ~/research-agent-pro/run_ids.txt); do
    echo "=== $run_id ==="
    research-agent status $run_id
done

# 批量获取结果并生成综合报告
python3 scripts/generate_comprehensive_report.py \
    --run-ids $(cat ~/research-agent-pro/run_ids.txt) \
    --output ~/research-agent-pro/reports/comprehensive.md
```

### 场景三：定时研究任务

企业战略部门需要定期更新行业研究。

```bash
# 配置定时研究任务
cat > ~/research-agent-pro/schedules/strategy.yaml << 'EOF'
schedules:
  # 每周行业动态深度研究
  - name: "weekly_industry_deep"
    cron: "0 18 * * 5"  # 每周五18:00
    config:
      topics:
        - "本周新能源汽车行业重大事件深度分析"
        - "本周AI领域技术突破汇总与影响评估"
      mode: "deep"
      async: true
    output:
      format: pdf
      path: "~/research-agent-pro/reports/weekly_{date}.pdf"
    notify:
      - "strategy@company.com"

  # 每月竞争格局更新
  - name: "monthly_competitive"
    cron: "0 9 1 * *"  # 每月1日9:00
    config:
      topics:
        - "主要竞品本月动态与策略变化深度分析"
      mode: "deep"
    output:
      format: word
      path: "~/research-agent-pro/reports/monthly_competitive_{date}.docx"
    notify:
      - "strategy@company.com"
      - "ceo@company.com"
EOF
```

## 快速开始

### 步骤一：初始化 PRO 环境

```bash
# 创建 PRO 版本工作目录
mkdir -p ~/research-agent-pro/{research,results,reports,schedules,templates,history,config}

# 初始化配置文件
cat > ~/research-agent-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

workspace:
  path: "~/research-agent-pro/research"
  naming: "slug"

research:
  modes: ["interactive", "deep"]
  default_mode: "interactive"
  max_concurrent: 10
  checkpoint_interval: 5

  deep_research:
    enabled: true
    default_timeout_hours: 24
    auto_check_interval: 300  # 5分钟自动检查
    notify_on_complete: true

  principles:
    atomic_findings: true
    link_everything: true
    capture_context: true
    note_confidence: true
    date_findings: true

scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  config_path: "~/research-agent-pro/schedules/"

export:
  formats: ["pdf", "word", "html", "markdown"]
  path: "~/research-agent-pro/reports/"
  template_path: "~/research-agent-pro/templates/"

history:
  enabled: true
  retention_days: 365
  version_control: true
  searchable: true
  path: "~/research-agent-pro/history/"

team:
  enabled: true
  config_path: "~/research-agent-pro/config/team.yaml"

api:
  enabled: true
  rate_limit: "100/hour"
  auth: "bearer_token"
EOF
```

### 步骤二：从免费版迁移

```bash
# 迁移免费版研究文档
if [ -d ~/.research-agent/workspace/research ]; then
    cp -r ~/.research-agent/workspace/research/* ~/research-agent-pro/research/
    echo "研究文档已迁移"
fi
```

### 步骤三：执行首次深度研究

```bash
# 启动深度异步研究
research-agent create "你的研究问题" --mode deep --async

# 查看状态
research-agent list --status running
```

## 配置示例

### 研究模板配置

```markdown
# {{topic}} 深度研究报告

## 报告元信息
- 研究模式：{{mode}}
- 启动时间：{{started_at}}
- 完成时间：{{completed_at}}
- Run ID：{{run_id}}
- 研究人员：{{researcher}}

## 执行摘要
{{自动生成的5段式摘要}}

## 研究背景
{{主题背景与重要性}}

## 核心发现
### 发现一：{{title}}
{{详细分析}}
- 可信度：{{level}}
- 来源：{{sources}}
- 发现日期：{{date}}

## 多维度分析
### 技术维度
### 市场维度
### 政策维度
### 竞争维度

## 风险评估
{{识别的风险因素与不确定性}}

## 未来展望
{{趋势预测与建议}}

## 引用来源
{{完整引用列表}}

## 附录
{{补充数据与图表}}
```

### 团队协作配置

```yaml
# team.yaml - 团队配置
team:
  name: "战略研究部"
  tenants:
    - id: tenant_001
      name: "新能源研究组"
      members:
        - email: "researcher_a@company.com"
          role: "analyst"
          max_concurrent: 3
          allowed_modes: ["interactive", "deep"]
        - email: "researcher_b@company.com"
          role: "lead"
          max_concurrent: 5
          allowed_modes: ["interactive", "deep"]
      shared_research: true
      shared_templates: true

    - id: tenant_002
      name: "AI研究组"
      members:
        - email: "ai_researcher@company.com"
          role: "analyst"
          max_concurrent: 3
      shared_research: true

permissions:
  analyst:
    - create: research
    - read: own + shared
    - export: self_only
    - modes: ["interactive", "deep"]
  lead:
    - create: research + templates
    - read: team
    - export: team
    - manage: members
    - modes: ["interactive", "deep"]
  admin:
    - all: true
    - manage: tenants
```

### REST API 集成

```python
# api_client.py - PRO 版本 API 客户端
import requests

class ResearchAgentProClient:
    def __init__(self, api_key, base_url="https://api.research-agent-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def create_research(self, topic, mode="interactive"):
        """创建研究任务"""
        resp = requests.post(
            f"{self.base_url}/v1/research",
            headers=self.headers,
            json={"topic": topic, "mode": mode}
        )
        return resp.json()

    def batch_research(self, topics, mode="deep"):
        """批量多主题研究"""
        resp = requests.post(
            f"{self.base_url}/v1/research/batch",
            headers=self.headers,
            json={"topics": topics, "mode": mode}
        )
        return resp.json()

    def get_status(self, run_id):
        """获取研究状态"""
        resp = requests.get(
            f"{self.base_url}/v1/research/{run_id}/status",
            headers=self.headers
        )
        return resp.json()

    def get_result(self, run_id, format="markdown"):
        """获取研究结果"""
        resp = requests.get(
            f"{self.base_url}/v1/research/{run_id}/result",
            headers=self.headers,
            params={"format": format}
        )
        return resp.json()

    def create_schedule(self, config):
        """创建定时研究任务"""
        resp = requests.post(
            f"{self.base_url}/v1/schedules",
            headers=self.headers,
            json=config
        )
        return resp.json()

    def search_history(self, query):
        """搜索历史研究"""
        resp = requests.get(
            f"{self.base_url}/v1/history",
            headers=self.headers,
            params={"q": query}
        )
        return resp.json()

    def graduate_research(self, run_id, project_name):
        """将研究毕业为项目spec"""
        resp = requests.post(
            f"{self.base_url}/v1/research/{run_id}/graduate",
            headers=self.headers,
            json={"project_name": project_name}
        )
        return resp.json()
```

## 最佳实践

### 1. 选择合适的研究模式

```python
# 研究模式选择指南
MODE_GUIDE = {
    "interactive": {
        "description": "实时对话推进研究",
        "best_for": "探索性研究、快速调研",
        "time": "实时",
        "depth": "中等"
    },
    "deep": {
        "description": "后台自动深度研究",
        "best_for": "复杂课题、全面调研",
        "time": "分钟至小时",
        "depth": "深入"
    }
}
```

### 2. 利用批量研究提升效率

```text
用户：批量研究以下5个AI相关课题，使用深度异步模式

Agent：
1. 解析5个课题
2. 为每个课题创建独立的深度研究任务
3. 并行执行（最多10个并发）
4. 定期汇报进度
5. 全部完成后生成综合报告
```

### 3. 设置自动检查与通知

```bash
# 配置自动检查
cat > ~/research-agent-pro/auto_check.sh << 'EOF'
#!/bin/bash
for run_id in $(cat ~/research-agent-pro/run_ids.txt); do
    status=$(research-agent status $run_id | jq -r '.status')
    if [ "$status" = "completed" ]; then
        research-agent result $run_id > ~/research-agent-pro/results/${run_id}.md
        echo "完成: $run_id"
        # 发送通知
        curl -X POST "https://hooks.notify.local/research" \
            -d "{\"run_id\":\"$run_id\",\"status\":\"completed\"}"
    fi
done
EOF

# 每5分钟检查一次
(crontab -l 2>/dev/null; echo "*/5 * * * * ~/research-agent-pro/auto_check.sh") | crontab -
```

### 4. 利用版本管理追踪研究演进

```bash
# 查看研究版本历史
ls ~/research-agent-pro/history/ai-chips/
# 2026-07-01_v1.md
# 2026-07-08_v2.md
# 2026-07-15_v3.md

# 对比版本差异
diff ~/research-agent-pro/history/ai-chips/2026-07-01_v1.md \
     ~/research-agent-pro/history/ai-chips/2026-07-15_v3.md
```

### 5. 研究毕业为项目

```text
用户：将"AI编程助手市场研究"毕业为项目spec

Agent：
1. 提取研究核心发现
2. 转化为项目规格文档
3. 保存至 ~/specs/ai-coding-assistant.md
4. 更新研究状态为 "Graduated"
5. 保留原始研究文档作为参考
```

## 常见问题

### Q1：深度研究任务一般需要多长时间？

取决于主题复杂度。简单主题 5-15 分钟，中等复杂度 30-60 分钟，复杂多维度课题可能需要 1-4 小时。

### Q2：可以同时运行多少个深度研究？

PRO 版本支持最多 10 个深度研究任务同时运行。任务在后台异步执行，不影响其他工作。

### Q3：深度研究的结果质量如何保证？

深度研究从多个维度、多个来源进行全面调研，自动交叉验证信息，生成包含引用来源和可信度标注的结构化报告。

### Q4：如何追踪研究任务进度？

可以通过以下方式追踪：
- 命令行：`research-agent status <run_id>`
- API：`GET /v1/research/{run_id}/status`
- 自动检查：配置 cron 定期轮询
- 通知：完成后自动推送通知

### Q5：免费版的研究文档如何迁移？

PRO 版本初始化时会自动检测免费版工作区，研究文档可一键迁移。

### Q6：API 调用频率限制？

默认每小时 100 次调用。深度研究任务创建后通过 status 接口轮询，不计入频率限制。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.10 及以上（推荐 3.12）
- **网络连接**: 稳定的互联网连接
- **存储空间**: 至少 2GB 用于研究文档与历史版本存储

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| research-agent CLI | 工具 | 必需 | 参考 SETUP.md 安装 |
| 网络搜索 | 服务 | 必需 | Agent 内置搜索能力 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| requests | Python 包 | 可选 | `pip install requests` |
| PyYAML | Python 包 | 可选 | `pip install pyyaml` |
| pandoc | 工具 | 可选 | 系统包管理器安装（PDF/Word导出） |
| jq | 工具 | 可选 | 系统包管理器安装（JSON处理） |

### API Key 配置

PRO 版本支持 API 集成与深度研究 CLI，需配置相关密钥：

```bash
# 配置 API 认证
export RESEARCH_AGENT_PRO_API_KEY="your_api_key"

# 配置 CLI工具
export RESEARCH_AGENT_CLI_KEY="your_cli_key"

# 或写入配置文件
cat > ~/research-agent-pro/.env << 'EOF'
RESEARCH_AGENT_PRO_API_KEY=your_api_key
RESEARCH_AGENT_CLI_KEY=your_cli_key
EOF
```

### 可用性分类

- **分类**: MD+EXEC+API+CLI（Markdown 指令 + 命令行执行 + API 集成 + CLI 工具）
- **说明**: PRO 版本支持交互式研究、深度异步研究、批量并行处理、定时调度、团队协作与 REST API 集成
- **适用规模**: 研究机构、企业战略部门、咨询公司、投资机构
- **兼容性**: 与 research-agent-tool-free 完全兼容，支持研究文档迁移与平滑升级
- **支持级别**: 优先技术支持，提供研究模板定制与深度研究策略咨询服务
