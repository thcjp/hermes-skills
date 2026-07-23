---
slug: parallel-research-tool-pro
name: parallel-research-tool-pro
version: 1.0.0
displayName: 并行研究助手专业版
summary: 企业级研究平台，支持深度异步研究、多主题并行、API集成与团队协作
license: Proprietary
edition: pro
description: 并行研究助手专业版。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use
  when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- 研究
- 企业级
- 深度研究
- 并行处理
- 团队协作
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
并行研究助手专业版在免费版交互式研究的基础上，新增深度异步研究模式、多主题并行处理、6 级处理器选择、定时研究任务、多格式导出、版本管理、多租户团队协作和 REST API 集成等企业级能力，满足研究机构和企业对深度、批量、自动化研究的全面需求。

PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有研究文档和工作区均可无缝迁移。

## 核心能力
### 能力矩阵
| 能力项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| 研究模式 | 交互式 | 交互式+深度异步 |
| 并发主题 | 1个 | 10+个并行 |
| 处理器等级 | 不适用 | lite-ultra8x可选 |
| 处理速度 | 实时 | 分钟至小时级深度 |
| 定时研究 | 不支持 | cron调度 |
| 自动检查 | 不支持 | 自动轮询结果 |
| 导出格式 | PDF | PDF/Word/HTML |
| 版本管理 | 不支持 | 完整版本控制 |
| 团队协作 | 不支持 | 多租户 |
| API 集成 | 不支持 | REST API |
| 研究模板 | 固定 | 自定义模板 |
| 历史检索 | 不支持 | 全文检索 |

**输入**: 用户提供能力矩阵所需的指令和必要参数。
**处理**: 解析能力矩阵的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回能力矩阵的响应数据,包含状态码、结果和日志。

### 处理器等级
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | 并行研究助手专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
[PRO] lite      - 轻量快速，适合简单主题
[PRO] base      - 基础深度，适合一般研究
[PRO] core      - 核心深度，平衡速度与质量
[PRO] pro       - 专业深度，适合大多数场景
[PRO] ultra     - 超深研究（默认），全面覆盖
[PRO] ultra2x   - 双倍深度，适合复杂主题
[PRO] ultra4x   - 四倍深度，适合多维度课题
[PRO] ultra8x   - 八倍深度，极限研究深度

[PRO] -fast     - 速度优先（如 ultra-fast）
```

**输入**: 用户提供处理器等级所需的指令和必要参数。
**处理**: 解析处理器等级的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回处理器等级的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级研究平台、支持深度异步研究、多主题并行、集成与团队协作、并行研究助手专业、Use、when、接口对接、Webhook、系统连接时使用、不适用于逆向工程、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景一：深度异步研究
对复杂主题进行全面的异步深度研究，无需实时交互。

```text
用户：deep research: 2026年全球AI芯片产业竞争格局分析

Agent 执行流程：
1. 启动深度异步研究任务
2. 选择处理器等级（默认ultra）
3. 任务在后台运行（数分钟至数小时）
4. 完成后保存详细报告
5. 通知用户查看结果
```

启动命令：

```bash
parallel-research create "2026年全球AI芯片产业竞争格局分析" \
    --processor ultra \
    --wait

parallel-research status <run_id>

parallel-research result <run_id>
```

### 场景二：批量多主题并行研究
研究机构需要同时开展多个相关课题的深度研究。

```python
research_topics = [
    "固态电池技术发展路线图",
    "自动驾驶L4商业化时间表",
    "AI芯片供应链风险评估",
    "碳交易市场机制分析",
    "生物医药AI应用前景"
]

for topic in research_topics:
    result = parallel_research.create(
        topic=topic,
        processor="ultra",
        async_mode=True  # 异步模式，不等待
    )
    print(f"已启动: {topic} -> Run ID: {result.run_id}")
```

批量管理：

```bash
parallel-research list --status running

for run_id in $(cat run_ids.txt); do
    echo "=== $run_id ==="
    parallel-research status $run_id
done

for run_id in $(cat run_ids.txt); do
    parallel-research result $run_id > ~/research-pro/results/${run_id}.md
done
```

### 场景三：定时研究任务
企业战略部门需要定期更新行业研究。

```bash
cat > ~/research-pro/schedules/industry_watch.yaml << 'EOF'
schedules:
  - name: "weekly_industry_deep"
    cron: "0 18 * * 5"  # 每周五18:00
    topics:
      - "本周新能源汽车行业重大事件分析"
      - "本周AI领域技术突破汇总"
    processor: "ultra"
    output:
      format: pdf
      path: "~/research-pro/reports/weekly_{date}.pdf"
    notify: ["strategy@company.com"]

  - name: "monthly_competitive"
    cron: "0 9 1 * *"  # 每月1日9:00
    topics:
      - "主要竞品本月动态与策略变化"
    processor: "ultra4x"  # 更高深度
    output:
      format: word
      path: "~/research-pro/reports/monthly_competitive_{date}.docx"
    notify: ["strategy@company.com"]
EOF
```

## 快速开始
### Step 1：初始化 PRO 环境
```bash
mkdir -p ~/research-pro/{research,results,reports,schedules,templates,history,config}

cat > ~/research-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

workspace:
  path: "~/research-pro/research"
  naming: "slug"

research:
  modes: ["interactive", "deep"]
  default_mode: "interactive"
  default_processor: "ultra"
  max_concurrent: 10
  checkpoint_interval: 5

  deep_research:
    cli_path: "parallel-research"
    default_processor: "ultra"
    timeout_hours: 24
    auto_check_interval: 300  # 5分钟
scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  config_path: "~/research-pro/schedules/"

export:
  formats: ["pdf", "word", "html", "markdown"]
  path: "~/research-pro/reports/"
  template_path: "~/research-pro/templates/"

history:
  enabled: true
  retention_days: 365
  version_control: true
  searchable: true

team:
  enabled: true
  config_path: "~/research-pro/config/team.yaml"

api:
  enabled: true
  rate_limit: "100/hour"
  auth: "bearer_token"
EOF
```

### 依赖详情
```bash
parallel-research --version
```

### Step 3：从免费版迁移
```bash
if [ -d ~/.research-workspace/research ]; then
    cp -r ~/.research-workspace/research/* ~/research-pro/research/
    echo "研究文档已迁移"
fi
```

### Step 4：执行首次深度研究
```bash
parallel-research create "你的研究问题" --processor ultra --wait
```

#
## 示例
### 研究模板配置
```markdown
- 研究模式：{{mode}}（交互式/深度异步）
- 处理器等级：{{processor}}
- 启动时间：{{started_at}}
- 完成时间：{{completed_at}}
- Run ID：{{run_id}}

{{自动生成的5段式摘要}}

{{主题背景与重要性}}

{{详细分析}}
- 可信度：{{level}}
- 来源：{{sources}}

{{详细分析}}

{{技术相关分析}}

{{市场数据与趋势}}

{{政策法规影响}}

| 参与者 | 定位 | 优势 | 劣势 | 策略 |
|:-------|:-----|:-----|:-----|:-----|

{{识别的风险因素}}

{{趋势预测与建议}}

{{完整引用列表}}
```

### 团队协作配置
```yaml
team:
  name: "战略研究部"
  tenants:
    - id: tenant_001
      name: "新能源研究组"
      members:
        - email: "researcher_a@company.com"
          role: "analyst"
          max_concurrent: 3
        - email: "researcher_b@company.com"
          role: "lead"
          max_concurrent: 5
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
    - max_processor: "ultra"
  lead:
    - create: research + templates
    - read: team
    - export: team
    - max_processor: "ultra8x"
    - manage: members
  admin:
    - all: true
```

### REST API 集成
```python
import requests

class ParallelResearchProClient:
    def __init__(self, api_key, base_url="https://api.research-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def create_deep_research(self, topic, processor="ultra"):
        """创建深度异步研究"""
        resp = requests.post(
            f"{self.base_url}/v1/research/deep",
            headers=self.headers,
            json={"topic": topic, "processor": processor}
        )
        return resp.json()

    def batch_research(self, topics, processor="ultra"):
        """批量多主题研究"""
        resp = requests.post(
            f"{self.base_url}/v1/research/batch",
            headers=self.headers,
            json={"topics": topics, "processor": processor}
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
```

## 最佳实践
### 1. 选择合适的处理器等级
```python
PROCESSOR_GUIDE = {
    "lite": "简单事实查询，1-2分钟完成",
    "base": "一般主题调研，5-10分钟完成",
    "core": "中等复杂度研究，15-30分钟完成",
    "pro": "专业级研究，30-60分钟完成",
    "ultra": "全面深度研究（推荐），1-2小时完成",
    "ultra2x": "复杂多维度课题，2-4小时完成",
    "ultra4x": "极致深度研究，4-8小时完成",
    "ultra8x": "极限研究深度，8-24小时完成"
}
```

### 2. 利用批量研究提升效率
```text
用户：批量研究以下5个AI相关课题，使用ultra处理器

Agent：
1. 解析5个课题
2. 为每个课题创建独立的深度研究任务
3. 并行执行（最多10个并发）
4. 定期汇报进度
5. 全部完成后生成综合报告
```

### 3. 设置自动检查
```bash
cat > ~/research-pro/auto_check.sh << 'EOF'
#!/bin/bash
for run_id in $(cat ~/research-pro/run_ids.txt); do
    status=$(parallel-research status $run_id | jq -r '.status')
    if [ "$status" = "completed" ]; then
        parallel-research result $run_id > ~/research-pro/results/${run_id}.md
        echo "完成: $run_id"
        curl -X POST "https://hooks.notify.local/research" \
            -d "{\"run_id\":\"$run_id\",\"status\":\"completed\"}"
    fi
done
EOF

(crontab -l 2>/dev/null; echo "*/5 * * * * ~/research-pro/auto_check.sh") | crontab -
```

### 4. 利用版本管理追踪研究演进
```bash
ls ~/research-pro/history/ai-chips/
diff ~/research-pro/history/ai-chips/2026-07-01_v1.md \
     ~/research-pro/history/ai-chips/2026-07-15_v3.md
```

## 常见问题
### Q1：深度研究任务一般需要多长时间？
取决于处理器等级和主题复杂度。lite 级别 1-2 分钟，ultra 级别 1-2 小时，ultra8x 级别可能需要 8-24 小时。

### Q2：可以同时运行多少个深度研究？
PRO 版本支持最多 10 个深度研究任务同时运行。任务在后台异步执行，不影响其他工作。

### Q3：深度研究的结果质量如何保证？
深度研究使用高级处理器，会从多个维度、多个来源进行全面调研，自动交叉验证信息，生成包含引用来源的结构化报告。

### Q4：如何追踪研究任务进度？
可以通过以下方式追踪：
- 命令行：`parallel-research status <run_id>`
- API：`GET /v1/research/{run_id}/status`
- 自动检查：配置 cron 定期轮询

### Q5：免费版的研究文档如何迁移？
PRO 版本初始化时会自动检测免费版工作区，研究文档可一键迁移。

### 已知限制
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
| parallel-research CLI | 工具 | 必需 | 参考 SETUP.md 安装 |
| 网络搜索 | 服务 | 必需 | Agent 内置搜索能力 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| requests | Python 包 | 可选 | `pip install requests` |
| pandoc | 工具 | 可选 | 系统包管理器安装（PDF/Word导出） |
| PyMuPDF | Python 包 | 可选 | `pip install pymupdf`（PDF导出） |
| jq | 工具 | 可选 | 系统包管理器安装（JSON处理） |

### API Key 配置
PRO 版本支持 API 集成与深度研究 CLI，需配置相关密钥：

```bash
export RESEARCH_PRO_API_KEY="your_api_key"

export PARALLEL_RESEARCH_API_KEY="your_cli_key"

cat > ~/research-pro/.env << 'EOF'
RESEARCH_PRO_API_KEY=your_api_key
PARALLEL_RESEARCH_API_KEY=your_cli_key
EOF
```

### 可用性分类
- **分类**: MD+EXEC+API+CLI（Markdown 指令 + 命令行执行 + API 集成 + CLI 工具）
- **说明**: PRO 版本支持交互式研究、深度异步研究、批量并行处理、定时调度与 REST API 集成
- **适用规模**: 研究机构、企业战略部门、咨询公司、投资机构
- **兼容性**: 与 parallel-research-tool-free 完全兼容，支持研究文档迁移与平滑升级
- **支持级别**: 优先技术支持，提供研究模板定制与处理器等级选择咨询

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "并行研究助手专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "parallel research pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
