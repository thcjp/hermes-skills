---
slug: "explain-code-paid"
name: "explain-code-paid"
version: "1.0.0"
displayName: "代码解释工具专业版"
summary: "企业级代码理解工具,支持项目架构分析、批量文档生成、Mermaid可视化与API文档输出。"
license: "Proprietary"
edition: "pro"
description: |-
  面向研发团队的高级代码理解工具,提供项目级架构分析、批量代码文档生成、Mermaid/UML可视化与API文档自动输出。核心能力:
  - 项目级架构分析与依赖图
  - 批量代码文档自动生成
  - Mermaid/UML 高质量可视化
  - API 文档自动提取与生成
  - 代码复杂度与质量分析
  - 团队知识库构建

  适用场景:
  - 大型项目代码理解与onboarding
  - 技术文档自动化生成
  - 架构评审与可视化
  - 遗留系统逆向理解

  差异化:
  - 专业版完全兼容免费版解释风格,支持平滑升级
  - 支...
tags:
  - 开发工具
  - 代码理解
  - 技术文档
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec", "glob", "grep"]
tags: "开发工具,代码生成,编程辅助"
---
# 代码解释工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码解释工具专业版支持项目架构分析 | 不支持 | 支持 |
| 代码解释工具专业版批量文档生成 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |

## 核心能力

### 1. 项目级架构分析
分析整个项目的架构,生成依赖关系图和模块结构图。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供项目级架构分析所需的指令和必要参数。
### 2. 批量代码文档生成
自动为整个项目生成代码文档。

**输入**: 用户提供批量代码文档生成所需的指令和必要参数。
**处理**: 解析批量代码文档生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。

### 3. Mermaid 高质量可视化
```python
class MermaidDiagramGenerator:
    """Mermaid图表生成器"""
# ...
    @staticmethod
    def generate_flowchart(code_structure):
        """生成流程图"""
        return f"""```mermaid
graph TD
    A[用户请求] --> B{路由器}
    B --> C{参数验证}
    C -->|通过| D[控制器]
    C -->|失败| E[返回错误]
    D --> E[服务层]
    E --> F[数据库]
    F --> G[返回结果]
```"""

    @staticmethod
    def generate_sequence_diagram(interaction_flow):
        """生成时序图"""
        return """```mermaid
sequenceDiagram
    participant U as 用户
    participant C as 客户端
    participant S as 服务器
    participant D as 数据库

    U->>C: 发起请求
    C->>S: HTTP请求
    S->>D: 查询数据
    D-->>S: 返回数据
    S-->>C: 响应数据
    C-->>U: 显示结果
```"""
# ...
    @staticmethod
    def generate_class_diagram(class_structure):
        """生成类图"""
        return """```mermaid
classDiagram
    class User {
        +String name
        +String email
        +login()
        +logout()
    }
# ...
    class Order {
        +String id
        +Date createdAt
        +addItem()
        +checkout()
    }
# ...
    class Product {
        +String name
        +Number price
        +getInfo()
    }
# ...
    User --> Order : 创建
    Order --> Product : 包含
```"""

    @staticmethod
    def generate_dependency_graph(modules):
        """生成依赖关系图"""
        lines = ["```mermaid", "graph LR"]
        for module, deps in modules.items():
            for dep in deps:
                lines.append(f"    {module} --> {dep}")
        lines.append("```")
        return '\n'.join(lines)
```
# ...
**处理**: 解析Mermaid 高质量可视化的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
### 4. 代码复杂度分析
> 详细代码示例已移至 `references/detail.md`
# ...
**输入**: 用户提供代码复杂度分析所需的指令和必要参数。
**处理**: 解析代码复杂度分析的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回代码复杂度分析的处理结果,包含执行状态码、结果数据和执行日志。
# ...
#
## 适用场景
# ...
### 场景一:大型项目onboarding
新成员加入团队时快速理解项目架构。
# ...
```bash
#!/bin/bash
echo "=== 生成项目理解文档 ==="

echo "1. 项目架构分析..."
python3 architecture_analyzer.py ./src > architecture.json

echo "2. 生成架构图..."
python3 mermaid_generator.py --input architecture.json --output architecture.mmd

echo "3. 生成模块文档..."
python3 doc_generator.py ./src --output ./docs/

echo "4. 代码复杂度分析..."
python3 complexity_analyzer.py ./src > complexity-report.json

echo "5. 生成onboarding指南..."
python3 generate_onboarding.py \
    --architecture architecture.json \
    --docs ./docs/ \
    --complexity complexity-report.json \
    --output ONBOARDING.md

echo -e "\n项目文档已生成:"
echo "  - 架构图: architecture.mmd"
echo "  - 模块文档: ./docs/"
echo "  - 复杂度报告: complexity-report.json"
echo "  - 入门指南: ONBOARDING.md"
```
# ...
### 场景二:API文档自动生成
从代码中自动提取API文档。
# ...
```bash
python3 doc_generator.py \
    --mode api \
    --input ./src \
    --output ./docs/api.md \
    --format markdown

python3 doc_generator.py \
    --mode api \
    --input ./src \
    --output ./docs/openapi.json \
    --format openapi
```
# ...
### 场景三:遗留系统逆向理解
对遗留系统进行逆向分析和文档化。
# ...
> 详细代码示例已移至 `references/detail.md`
# ...
## 使用流程
# ...
### 步骤一:配置分析
```yaml
version: "2.0"
edition: pro

analysis:
  architecture: true
  complexity: true
  dependencies: true

documentation:
  generate_api_docs: true
  generate_module_docs: true
  output_format: markdown
  output_dir: ./docs/

visualization:
  use_mermaid: true
  diagram_types: [flowchart, sequence, class, dependency]
```
# ...
### 步骤二:运行分析
```
请对当前项目进行完整架构分析,生成模块文档和架构图。
```
# ...
### 步骤三:查看结果
1. `./docs/architecture.md`:架构分析报告
2. `./docs/api.md`:API文档
3. `./docs/modules/`:各模块文档
4. `./docs/diagrams/`:Mermaid图表
# ...
#
## 输入格式
# ...
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | explain-code处理的内容输入 |,  |
| content | string | 否 | explain-code处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    result: "code 相关配置参数",
    result: "code 相关配置参数",
    result: "code 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```
# ...
输出模板参考: `assets/output.json`
# ...
## 异常处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 
# ...
## 依赖说明
# ...
### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Python 3.8+ / Node.js 16+
# ...
### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Mermaid CLI | 可视化工具 | 推荐 | npm install -g @mermaid-js/mermaid-cli |
| mkdocs | 文档站点 | 可选 | pip install mkdocs |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
# ...
### API Key 配置
- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 所有代码分析在本地完成
# ...
### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持项目级分析、批量文档生成和可视化)
- **说明**:企业级代码理解工具,支持架构分析、文档生成和知识库构建
- **适用规模**:中小型到大型项目
- **兼容性**:完全兼容免费版解释风格,支持平滑升级
# ...
## 案例展示
# ...
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
# ...
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
# ...
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
# ...
## 常见问题
# ...
### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的解释风格。免费版的 `.explain-code.yml` 配置可直接使用,专业版会自动启用架构分析和文档生成功能。
# ...
### Q2:大型项目分析性能如何?
| 项目规模 | 文件数 | 分析时间 | 内存 |
|:------|------:|:------|:------|
| 小型 | <100 | <30s | <100MB |
| 中型 | 100-1000 | 1-5min | 100-500MB |
| 大型 | 1000-10000 | 5-20min | 500MB-2GB |
| 超大型 | >10000 | 20min+ | 建议分模块 |
# ...
### Q3:支持哪些文档格式?
| 格式 | 用途 | 输出 |
|---:|:---|---:|
| Markdown | 通用文档 | .md |
| HTML | 在线浏览 | .html |
| OpenAPI | API规范 | .json/.yaml |
| Mermaid | 图表 | .mmd |
# ...
### Q4:如何集成到CI/CD?
```yaml
code_documentation:
  stage: docs
  script:
    - python3 doc_generator.py --all --output ./docs/
  artifacts:
    paths:
      - docs/
    expire_in: 30 days
```
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
## 已知限制
# ...
- 需要API Key，无Key环境无法使用
# ...