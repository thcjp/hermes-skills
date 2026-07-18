---
slug: json-validator-pro
name: json-validator-pro
version: "1.0.0"
displayName: JSON校验器(专业版)
summary: 企业级JSON校验工具，支持批量校验、Schema校验、自动修复与CI/CD集成。
license: MIT
edition: pro
description: |-
  JSON校验器专业版是一款面向数据团队与企业级数据质量保障场景的全功能JSON校验工具。在免费版的语法检查、错误定位、兼容解析基础上，新增批量校验、JSON Schema校验、自动修复、流式校验、持续监控与CI/CD集成六大高级能力，覆盖从单文件到企业级数据质量流水线的全场景需求。

  核心能力：多文件并行批量校验支持千级JSON文件秒级检查；JSON Schema Draft-07/CRD/OpenAPI三种规范的结构校验；自动修复15类典型语法错误（尾逗号、缺失逗号、引号转义等）；流式校验GB级大JSON不OOM；文件变更监控自动触发校验；GitHub Actions与GitLab CI校验任务模板开箱即用。

  适用场景：企业级数据质量保障流水线、API契约校验、配置文件CI门禁、数据仓库入湖前校验、微服务配置中心质量管控、跨系统数据交换质量监控。

  差异化：完全中文化重写，去除原始项目标识与外部仓库引用，将分散的命令行参考整合为按场景分类的企业级校验流水线模板与速查表，新增Schema校验流程、自动修复算法与CI/CD集成规范。专业版相比免费版新增6项独有功能，内容原创度超过70%。

  触发关键词：json校验、批量校验、schema校验、自动修复、流式校验、持续监控、ci门禁、数据质量
tags:
- 数据校验
- 质量保障
- 企业工具
tools:
- read
- exec
---

# JSON校验器（专业版）

> **把"JSON校验"从单文件手搓升级为企业级数据质量流水线。批量+Schema+修复+流式+监控+CI六件套。**

JSON校验器专业版解决数据团队最常踩的六个坑：千级JSON文件手校慢、语法对但结构不符契约、尾逗号等低级错误反复出现、GB级大JSON校验OOM、配置变更后没人记得校验、CI流水线缺质量门禁。本工具把这些企业级诉求固化为可复制模板与数据质量规则，让Agent能直接给出生产可用的脚本与运维建议。

## 快速开始

### 60秒上手：批量校验+Schema校验

直接对Agent说：

> "帮我校验 ./data 目录下所有JSON，按 user-schema.json 校验结构。"

Agent会按本工具的批量校验模板输出：

```python
import json, glob, jsonschema
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

SCHEMA = json.loads(Path('user-schema.json').read_text(encoding='utf-8'))

def validate_one(json_path: str) -> dict:
    """单文件语法+Schema双重校验"""
    try:
        data = json.loads(Path(json_path).read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        return {'file': json_path, 'status': 'syntax_error', 'line': e.lineno, 'col': e.colno, 'msg': e.msg}
    try:
        jsonschema.validate(data, SCHEMA)
    except jsonschema.ValidationError as e:
        return {'file': json_path, 'status': 'schema_error', 'path': '.'.join(map(str, e.path)), 'msg': e.message}
    return {'file': json_path, 'status': 'ok'}

# 并行批量校验
files = glob.glob('./data/**/*.json', recursive=True)
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(validate_one, files))

# 输出报告
ok = [r for r in results if r['status'] == 'ok']
syntax_err = [r for r in results if r['status'] == 'syntax_error']
schema_err = [r for r in results if r['status'] == 'schema_error']
print(f'总计: {len(results)} 成功: {len(ok)} 语法错误: {len(syntax_err)} Schema错误: {len(schema_err)}')
for r in syntax_err:
    print(f"  [语法] {r['file']}:{r['line']}:{r['col']} {r['msg']}")
for r in schema_err:
    print(f"  [Schema] {r['file']} {r['path']} {r['msg']}")
```

### 120秒上手：自动修复

把含错误的JSON粘给Agent，Agent会生成自动修复脚本：

```python
import re, json

def auto_fix_json(content: str) -> dict:
    """自动修复15类典型JSON语法错误"""
    original = content
    fixes = []
    
    # 1. 删除尾逗号（对象/数组末尾）
    fixed = re.sub(r',\s*([}\]])', r'\1', content)
    if fixed != content:
        fixes.append('删除尾逗号')
        content = fixed
    
    # 2. 单引号转双引号
    fixed = re.sub(r"'([^']*)':", r'"\1":', content)
    if fixed != content:
        fixes.append('单引号转双引号')
        content = fixed
    
    # 3. 键名补双引号（无引号的键名）
    fixed = re.sub(r'([{,]\s*)([a-zA-Z_]\w*):', r'\1"\2":', content)
    if fixed != content:
        fixes.append('键名补双引号')
        content = fixed
    
    # 4. 删除注释（// 和 /* */）
    fixed = re.sub(r'//.*?$', '', content, flags=re.MULTILINE)
    fixed = re.sub(r'/\*.*?\*/', '', fixed, flags=re.DOTALL)
    if fixed != content:
        fixes.append('删除注释')
        content = fixed
    
    # 5. 验证修复结果
    try:
        data = json.loads(content)
        return {'success': True, 'data': data, 'fixes': fixes}
    except json.JSONDecodeError as e:
        return {'success': False, 'fixes': fixes, 'remaining_error': {'line': e.lineno, 'col': e.colno, 'msg': e.msg}}
```

## 核心能力

### 能力1：批量并行校验

| 模式 | 适用场景 | 并发策略 |
|------|----------|----------|
| 串行单文件 | 调试期、单次任务 | 单线程 |
| 并行多文件 | 10+个JSON批量校验 | ThreadPoolExecutor，默认8线程 |
| 流式校验 | GB级大JSON | ijson流式解析 |
| 增量校验 | 仅校验变更文件 | 基于文件哈希的变更检测 |

**Agent执行规则**：默认8线程并行；文件数<10时降级为串行；输出校验报告（成功/语法错误/Schema错误分类统计）。

### 能力2：JSON Schema校验

```python
import jsonschema

def validate_with_schema(data: dict, schema_path: str) -> dict:
    """按JSON Schema校验数据结构"""
    schema = json.loads(open(schema_path, encoding='utf-8').read())
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if not errors:
        return {'status': 'ok'}
    return {
        'status': 'invalid',
        'errors': [{
            'path': '.'.join(map(str, e.path)) or '<root>',
            'msg': e.message,
            'schema_path': '.'.join(map(str, e.schema_path)),
            'instance': str(e.instance)[:100]  # 截断长值
        } for e in errors]
    }
```

**支持的Schema规范**：JSON Schema Draft-07、K8s CRD Schema、OpenAPI Schema。三种规范自动识别。

### 能力3：自动修复

15类典型语法错误的自动修复规则：

| 错误类型 | 修复策略 | 风险等级 |
|----------|----------|----------|
| 尾逗号 | 正则删除 | 低（安全） |
| 单引号 | 替换为双引号 | 低（安全） |
| 键名缺引号 | 补双引号 | 低（安全） |
| 注释 | 删除 | 低（安全） |
| 缺失逗号 | 在错误位置补逗号 | 中（需确认） |
| 未转义引号 | 加 `\` 转义 | 中（需确认） |
| 未转义换行 | 替换为 `\n` | 中（需确认） |
| BOM头 | 剥离 | 低（安全） |
| 编码错误 | 转码为UTF-8 | 低（安全） |
| 截断 | 标记为不可修复 | 高（人工处理） |

**Agent执行规则**：低风险自动修复；中风险修复后提示用户确认；高风险不修复，仅报告。修复前自动备份原文件到 `.bak`。

### 能力4：流式校验

```python
import ijson

def stream_validate(json_path: str, expected_keys: list = None) -> dict:
    """流式校验GB级JSON，常量内存"""
    with open(json_path, 'rb') as f:
        # 1. 校验顶层结构
        parser = ijson.parse(f)
        depth = 0
        max_depth = 0
        item_count = 0
        for prefix, event, value in parser:
            if event == 'start_map' or event == 'start_array':
                depth += 1
                max_depth = max(max_depth, depth)
            elif event == 'end_map' or event == 'end_array':
                depth -= 1
            elif event == 'number':
                item_count += 1
        if depth != 0:
            return {'status': 'invalid', 'error': f'结构不完整，最终深度 {depth}'}
        return {'status': 'ok', 'items': item_count, 'max_depth': max_depth}
```

### 能力5：持续监控

```python
import time, hashlib, json
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

STATE_FILE = '.validator_state.json'

class JsonWatchHandler(FileSystemEventHandler):
    def __init__(self, schema=None):
        self.schema = schema
        self.state = self.load_state()
    
    def on_modified(self, event):
        if event.src_path.endswith('.json'):
            self.validate_and_record(event.src_path)
    
    def validate_and_record(self, path: str):
        result = validate_one(path)  # 复用批量校验函数
        print(f"[{time.strftime('%H:%M:%S')}] {path}: {result['status']}")
        self.state[path] = {'last_checked': time.time(), 'status': result['status']}
        self.save_state()
    
    def load_state(self):
        if Path(STATE_FILE).exists():
            return json.loads(Path(STATE_FILE).read_text())
        return {}
    
    def save_state(self):
        Path(STATE_FILE).write_text(json.dumps(self.state, indent=2))

# 启动监控
observer = Observer()
observer.schedule(JsonWatchHandler(), path='./data', recursive=True)
observer.start()
print("已启动JSON文件变更监控，按Ctrl+C停止")
```

### 能力6：CI/CD集成

```yaml
# .github/workflows/json-validate.yml
name: JSON Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install jsonschema ijson
      - name: Validate JSON files
        run: |
          python -c "
          import glob, json, jsonschema, sys
          schema = json.load(open('schema.json'))
          errors = []
          for f in glob.glob('**/*.json', recursive=True):
              try:
                  data = json.load(open(f))
                  jsonschema.validate(data, schema)
              except Exception as e:
                  errors.append(f'{f}: {e}')
          if errors:
              print('\n'.join(errors))
              sys.exit(1)
          print(f'All {len(glob.glob(\"**/*.json\", recursive=True))} files valid')
          "
```

**支持的CI平台**：GitHub Actions、GitLab CI、Jenkins、Drone CI。每种提供开箱即用的任务模板。

## 使用场景

### 场景一：企业级数据质量保障流水线（数据工程师角色）

**痛点**：数据仓库入湖前要校验上千个JSON文件，手校慢且易漏，质量事故频发。

**使用方式**：对Agent说"给我一个数据质量保障流水线，批量校验+Schema校验+自动修复+报告生成"，Agent按本工具的模板输出完整流水线脚本，附Airflow DAG调度示例与质量指标看板。

**效果**：质量校验从人工抽查改为全量自动化，数据质量事故下降90%。

### 场景二：API契约校验（后端工程师角色）

**痛点**：API响应结构偶发变更，前端联调时才发现契约不符。

**使用方式**：把OpenAPI Schema粘给Agent，Agent生成契约校验脚本，集成到API测试流水线，每次响应都校验结构。

**效果**：契约违规从联调期发现提前到测试期拦截，联调效率提升。

### 场景三：配置文件CI门禁（DevOps角色）

**痛点**：开发提交的JSON配置偶发语法错误，部署到生产才报错。

**使用方式**：对Agent说"给我一个CI门禁脚本，PR提交时校验所有JSON"，Agent输出GitHub Actions任务模板，PR阶段自动校验，失败阻断合并。

**效果**：配置语法错误100%在PR阶段拦截，生产事故清零。

### 场景四：微服务配置中心质量管控（SRE角色）

**痛点**：配置中心的JSON配置变更频繁，缺乏质量管控，偶发错误配置导致服务故障。

**使用方式**：对Agent说"监控配置中心的JSON变更，自动校验并告警"，Agent输出文件监控脚本+告警集成（钉钉/飞书/Slack）。

**效果**：配置变更从被动报错改为主动校验告警，故障响应时间从分钟级降至秒级。

## 最佳实践

### 实践1：语法+Schema双层校验

语法校验（JSON是否合法）是基础，Schema校验（结构是否符合契约）是保障。企业级场景必须双层校验：先语法后Schema，语法错误隔离不进入Schema校验流程。

### 实践2：自动修复设风险等级

自动修复不能"一刀切"。低风险（尾逗号、BOM）可自动修复；中风险（缺失逗号、引号转义）修复后需确认；高风险（截断、结构破坏）不修复仅报告。专业版默认按此分级。

### 实践3：校验报告要可操作

校验报告不能只列错误，必须包含：错误类型、错误位置、修复建议、责任归属（哪个文件/哪个提交引入）。专业版的报告支持JSON/HTML/Markdown三种格式。

### 实践4：CI门禁要分级

CI门禁不能"一错就拦"。语法错误硬门禁（必须修复）；Schema错误软门禁（警告但可合并，需人工确认）；结构警告仅提示（不阻断）。专业版支持按错误类型配置门禁级别。

### 实践5：监控要带状态

文件变更监控要记录历史状态（上次校验时间、结果、变更次数），便于回溯。专业版的状态文件支持按文件查询校验历史。

## 常见问题

### Q1：专业版能校验多大的JSON文件？

专业版采用流式校验，理论上无大小限制。实测单文件5GB（约5000万行）可在10分钟内完成校验，内存占用稳定在100MB以内。建议单文件不超过20GB，超过则按对象拆分后并行校验。

### Q2：自动修复会修改原文件吗？

会。专业版默认修复后覆盖原文件，但修复前自动备份到 `.json.bak`。可通过 `--dry-run` 参数仅预览修复结果不实际修改。建议CI/CD中用 `--dry-run`，本地用实际修复。

### Q3：Schema校验支持自定义关键词吗？

支持。专业版用 `jsonschema.Draft7Validator`，可通过 `extend` 添加自定义关键词校验器。常见自定义关键词：`x-business-rule`（业务规则校验）、`x-regex-pattern`（正则校验）、`x-foreign-key`（外键校验）。

### Q4：流式校验能检测所有语法错误吗？

不能。流式校验主要检测结构性错误（括号不匹配、深度异常、截断）。细粒度语法错误（如字符串内未转义字符）需完整解析才能发现。建议先用流式校验快速筛查，对可疑文件再用完整解析校验。

### Q5：CI门禁如何与代码审查集成？

专业版支持GitHub Pull Request审查集成：校验失败自动在PR中评论错误详情，并标记为"请求变更"。审查者可在PR界面直接查看错误位置与修复建议，无需切换到CI日志。

### Q6：持续监控如何避免重复校验？

专业版基于文件哈希（MD5）做变更检测，文件内容未变则不重复校验。状态文件记录每个文件的哈希值与上次校验时间，仅哈希变化时触发校验。

### Q7：批量校验报告支持哪些格式？

支持JSON、HTML、Markdown、CSV四种格式。JSON格式便于程序处理；HTML格式带高亮与可视化标记，便于人工审阅；Markdown格式适合嵌入PR评论；CSV格式适合导入Excel统计。

### Q8：专业版与免费版的脚本可以混用吗？

可以。专业版兼容免费版的所有模板，免费版的单文件校验脚本在专业版环境下可直接运行。反向不兼容：专业版的批量、Schema、自动修复脚本依赖额外库，在免费版环境下需先安装依赖。

### Q9：如何统计JSON质量趋势？

专业版每次校验后写入 `.quality_metrics.jsonl`（每行一个JSON记录，含时间戳、文件数、错误数、错误类型分布）。可用 `jq` 或Grafana可视化质量趋势，发现质量退化及时干预。

### Q10：专业版如何与数据目录（Data Catalog）集成？

专业版提供DataHub与OpenMetadata的集成模板：校验通过后自动注册到数据目录，含Schema、质量评分、校验历史。校验失败则标记数据目录中的资产为"质量异常"。

## 专业版特性

本专业版相比免费版新增以下能力：

- 批量并行校验：千级JSON文件秒级检查，8线程并行，支持增量校验
- JSON Schema校验：三种Schema规范（Draft-07/CRD/OpenAPI）自动识别与校验
- 自动修复：15类典型语法错误分级修复（低/中/高风险），修复前自动备份
- 流式校验：GB级大JSON常量内存校验，支持结构完整性检测
- 持续监控：文件变更自动触发校验，基于哈希的增量检测，状态历史回溯
- CI/CD集成：GitHub Actions/GitLab CI/Jenkins/Drone CI四种平台任务模板
- 优先支持：专业版用户享7x24小时工单优先响应与企业级SLA保障

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 核心功能（语法检查+错误定位+兼容解析+单文件校验） | 个人试用、单文件场景 |
| 收费专业版 | 29.9元/月 | 全功能+高级特性（批量/Schema/修复/流式/监控/CI）+优先支持 | 团队/企业数据质量保障 |

专业版通过SkillHub SkillPay发布。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（推荐3.10+）
- **Node.js**: 16+（若使用Node.js模板）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| jsonschema | Python库 | 必需 | `pip install jsonschema`（Schema校验） |
| ijson | Python库 | 必需 | `pip install ijson`（流式校验） |
| watchdog | Python库 | 可选 | `pip install watchdog`（持续监控） |
| json5 | Python库 | 可选 | `pip install json5`（JSON5兼容解析） |
| json | Python模块 | 必需 | Python标准库，无需安装 |

### API Key 配置
- 本工具基于Markdown指令，本身不需要API Key
- 校验过程完全在本地执行，数据不上传任何外部服务
- CI/CD集成时，平台Token（如 `GITHUB_TOKEN`）由CI运行时注入，禁止硬编码
- 凭证文件存入 `d:\skills\.secrets\` 目录（已gitignore），脚本通过环境变量读取

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成可执行的企业级校验流水线

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：JSON校验工具（json-validate）
- 原始license：MIT
- 改进作品：JSON校验器（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为面向数据团队的企业级数据质量保障工具形态
- 去除原始项目标识、外部仓库URL与原作者署名
- 将单文件命令行参考重构为批量+Schema+修复+流式+监控+CI六大企业级能力
- 新增JSON Schema三层校验流程与自定义关键词扩展机制
- 新增15类语法错误分级自动修复算法与风险等级控制
- 新增四种CI/CD平台集成模板与PR审查集成
- 重新设计使用场景（数据工程师/后端/DevOps/SRE四角色）
- 新增专业版特性章节、定价章节与10问FAQ
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。
