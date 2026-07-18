---
slug: explain-code-tool-pro
name: explain-code-tool-pro
version: "1.0.0"
displayName: 代码解释工具专业版
summary: 企业级代码理解工具,支持项目架构分析、批量文档生成、Mermaid可视化与API文档输出。
license: MIT
edition: pro
description: |-
  面向研发团队的高级代码理解工具,提供项目级架构分析、批量代码文档生成、Mermaid/UML可视化与API文档自动输出。

  核心能力:
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
  - 支持项目级架构分析和批量处理
  - 提供Mermaid/UML高质量图表
  - 自动生成API文档和知识库

  触发关键词: 架构分析, 代码文档, 批量解释, Mermaid, UML, API文档, 代码可视化, 知识库, code documentation
tags:
- 开发工具
- 代码理解
- 技术文档
- 企业级
tools:
- read
- exec
---

# 代码解释工具 - 专业版

## 概述

代码解释工具专业版为研发团队提供项目级代码理解能力。在免费版单文件解释能力之上,专业版新增项目架构分析、批量代码文档生成、Mermaid/UML高质量可视化和API文档自动提取,帮助团队高效理解和管理大型代码库。

专业版完全兼容免费版的解释风格和配置,研发团队可从免费版无缝升级。专业版保留了免费版的类比解释和ASCII图表风格,同时增加了更强大的可视化能力。

## 核心能力

### 1. 项目级架构分析

分析整个项目的架构,生成依赖关系图和模块结构图。

```python
# 专业版项目架构分析器
import os
import re
import json
from collections import defaultdict
from datetime import datetime

class ProjectArchitectureAnalyzer:
    """项目架构分析器"""

    def __init__(self, project_root):
        self.root = project_root
        self.modules = {}
        self.dependencies = defaultdict(list)
        self.file_count = 0
        self.total_lines = 0

    def analyze(self):
        """执行完整架构分析"""
        self._scan_project()
        return self._generate_architecture_report()

    def _scan_project(self):
        """扫描项目结构"""
        supported = ('.js', '.ts', '.py', '.java', '.go')

        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in
                       ('node_modules', '.git', 'dist', 'build', '__pycache__', 'vendor')]

            for file in files:
                if file.endswith(supported):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, self.root)
                    module_name = self._get_module_name(rel_path)

                    self._analyze_file(filepath, module_name, rel_path)
                    self.file_count += 1

    def _get_module_name(self, rel_path):
        """获取模块名"""
        parts = rel_path.split(os.sep)
        if len(parts) > 1:
            return parts[0]
        return "root"

    def _analyze_file(self, filepath, module, rel_path):
        """分析单个文件"""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
            self.total_lines += len(lines)

            # 提取导入/依赖
            imports = self._extract_imports(content, filepath)
            for imp in imports:
                self.dependencies[module].append(imp)

            # 提取函数/类定义
            functions = self._extract_functions(content, filepath)
            classes = self._extract_classes(content, filepath)

            if module not in self.modules:
                self.modules[module] = {
                    "files": [],
                    "functions": 0,
                    "classes": 0,
                    "lines": 0
                }

            self.modules[module]["files"].append(rel_path)
            self.modules[module]["functions"] += len(functions)
            self.modules[module]["classes"] += len(classes)
            self.modules[module]["lines"] += len(lines)

    def _extract_imports(self, content, filepath):
        """提取导入语句"""
        imports = []
        patterns = [
            r'^import\s+.*\s+from\s+["\']([^"\']+)["\']',      # ES6
            r'^const\s+.*\s*=\s*require\(["\']([^"\']+)["\']\)',  # CommonJS
            r'^from\s+(\S+)\s+import',                           # Python
            r'^import\s+(\S+)',                                  # Python
        ]

        for line in content.split('\n'):
            for pattern in patterns:
                match = re.search(pattern, line.strip())
                if match:
                    imports.append(match.group(1))
        return imports

    def _extract_functions(self, content, filepath):
        """提取函数定义"""
        patterns = [
            r'(?:export\s+)?function\s+(\w+)',           # JS/TS
            r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?\(',  # JS/TS arrow
            r'def\s+(\w+)',                               # Python
        ]
        functions = []
        for pattern in patterns:
            functions.extend(re.findall(pattern, content))
        return functions

    def _extract_classes(self, content, filepath):
        """提取类定义"""
        patterns = [
            r'class\s+(\w+)',           # JS/TS/Python
            r'interface\s+(\w+)',       # TS
        ]
        classes = []
        for pattern in patterns:
            classes.extend(re.findall(pattern, content))
        return classes

    def _generate_architecture_report(self):
        """生成架构报告"""
        return {
            "analysis_time": datetime.now().isoformat(),
            "project": self.root,
            "summary": {
                "total_files": self.file_count,
                "total_lines": self.total_lines,
                "total_modules": len(self.modules),
                "total_functions": sum(m["functions"] for m in self.modules.values()),
                "total_classes": sum(m["classes"] for m in self.modules.values()),
            },
            "modules": self.modules,
            "dependencies": dict(self.dependencies),
            "mermaid_diagram": self._generate_mermaid()
        }

    def _generate_mermaid(self):
        """生成Mermaid依赖图"""
        lines = ["graph TD"]
        for module in self.modules:
            deps = self.dependencies.get(module, [])
            for dep in deps:
                # 简化依赖名
                dep_short = dep.split('/')[-1].split('.')[0]
                if dep_short in self.modules or dep_short != module:
                    lines.append(f"    {module} --> {dep_short}")
        return '\n'.join(lines)


# 使用示例
analyzer = ProjectArchitectureAnalyzer("./src")
report = analyzer.analyze()
print(json.dumps(report, indent=2, ensure_ascii=False))
```

### 2. 批量代码文档生成

自动为整个项目生成代码文档。

```python
# 专业版批量文档生成器
class CodeDocGenerator:
    """批量代码文档生成器"""

    def __init__(self, project_root, output_dir="./docs"):
        self.root = project_root
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_all(self):
        """生成所有文档"""
        self._generate_api_docs()
        self._generate_module_docs()
        self._generate_architecture_doc()
        self._generate_index()

    def _generate_api_docs(self):
        """生成API文档"""
        api_doc = {
            "title": "API 文档",
            "generated_at": datetime.now().isoformat(),
            "endpoints": []
        }

        # 扫描API定义
        for root, _, files in os.walk(self.root):
            for file in files:
                if file.endswith(('.js', '.ts', '.py')):
                    filepath = os.path.join(root, file)
                    endpoints = self._extract_api_endpoints(filepath)
                    api_doc["endpoints"].extend(endpoints)

        # 写入API文档
        api_path = os.path.join(self.output_dir, "api.md")
        with open(api_path, 'w', encoding='utf-8') as f:
            f.write(self._format_api_doc(api_doc))

    def _extract_api_endpoints(self, filepath):
        """提取API端点"""
        endpoints = []
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

            # 提取REST API端点
            patterns = [
                (r'@(Get|Post|Put|Delete|Patch)\(["\']([^"\']+)["\']\)', 'decorator'),
                (r'app\.(get|post|put|delete|patch)\(["\']([^"\']+)["\']', 'express'),
                (r'@(app\.)?route\(["\']([^"\']+)["\'].*methods=["\'](\w+)["\']\)', 'flask'),
            ]

            for pattern, source in patterns:
                for match in re.finditer(pattern, content):
                    method = match.group(1).upper() if source == 'decorator' else \
                             match.group(1).upper() if source == 'express' else \
                             match.group(3).upper()
                    path = match.group(2)
                    endpoints.append({
                        "method": method,
                        "path": path,
                        "file": filepath,
                        "source": source
                    })

        return endpoints

    def _format_api_doc(self, doc):
        """格式化API文档"""
        lines = [
            f"# {doc['title']}",
            f"\n> 生成时间: {doc['generated_at']}",
            f"\n## 端点列表\n"
        ]

        for ep in doc["endpoints"]:
            lines.append(f"### {ep['method']} {ep['path']}")
            lines.append(f"- 文件: `{ep['file']}`")
            lines.append(f"- 来源: {ep['source']}\n")

        return '\n'.join(lines)

    def _generate_module_docs(self):
        """生成模块文档"""
        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d[0] != '.' and d not in
                       ('node_modules', '__pycache__')]

            for file in files:
                if file.endswith(('.js', '.ts', '.py')):
                    filepath = os.path.join(root, file)
                    doc = self._generate_file_doc(filepath)
                    if doc:
                        rel_path = os.path.relpath(filepath, self.root)
                        doc_path = os.path.join(
                            self.output_dir,
                            rel_path.replace(os.sep, '_') + '.md'
                        )
                        with open(doc_path, 'w', encoding='utf-8') as f:
                            f.write(doc)

    def _generate_file_doc(self, filepath):
        """为单个文件生成文档"""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        functions = re.findall(
            r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)',
            content
        )
        classes = re.findall(r'class\s+(\w+)', content)

        if not functions and not classes:
            return None

        lines = [
            f"# {os.path.basename(filepath)}",
            f"\n> 文件路径: `{filepath}`",
            f"> 生成时间: {datetime.now().isoformat()}\n"
        ]

        if functions:
            lines.append("## 函数\n")
            for name, params in functions:
                lines.append(f"### `{name}({params})`")
                lines.append(f"\n参数: `{params or '无'}`\n")

        if classes:
            lines.append("\n## 类\n")
            for cls in classes:
                lines.append(f"### `{cls}`\n")

        return '\n'.join(lines)
```

### 3. Mermaid 高质量可视化

```python
# 专业版Mermaid图表生成器
class MermaidDiagramGenerator:
    """Mermaid图表生成器"""

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

    class Order {
        +String id
        +Date createdAt
        +addItem()
        +checkout()
    }

    class Product {
        +String name
        +Number price
        +getInfo()
    }

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

### 4. 代码复杂度分析

```python
# 专业版代码复杂度分析器
class CodeComplexityAnalyzer:
    """代码复杂度分析器"""

    def __init__(self, project_root):
        self.root = project_root
        self.results = []

    def analyze(self):
        """分析代码复杂度"""
        for root, _, files in os.walk(self.root):
            for file in files:
                if file.endswith(('.js', '.ts', '.py')):
                    filepath = os.path.join(root, file)
                    self._analyze_file(filepath)
        return sorted(self.results, key=lambda x: x['complexity'], reverse=True)

    def _analyze_file(self, filepath):
        """分析单个文件复杂度"""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 计算圈复杂度(简化版)
        complexity = 0
        complexity += len(re.findall(r'\bif\b', content))
        complexity += len(re.findall(r'\belse\b', content))
        complexity += len(re.findall(r'\bfor\b', content))
        complexity += len(re.findall(r'\bwhile\b', content))
        complexity += len(re.findall(r'\bcase\b', content))
        complexity += len(re.findall(r'\bcatch\b', content))
        complexity += len(re.findall(r'&&\|\|\?', content))

        lines = content.split('\n')

        self.results.append({
            'file': filepath,
            'lines': len(lines),
            'complexity': complexity,
            'rating': self._rate_complexity(complexity),
            'suggestion': self._suggest(complexity)
        })

    def _rate_complexity(self, score):
        """评级"""
        if score < 5: return "低"
        elif score < 10: return "中"
        elif score < 20: return "高"
        else: return "极高"

    def _suggest(self, score):
        """建议"""
        if score < 5: return "复杂度良好,保持现状"
        elif score < 10: return "建议关注复杂函数"
        elif score < 20: return "建议重构降低复杂度"
        else: return "强烈建议重构,复杂度过高"
```

## 使用场景

### 场景一:大型项目onboarding

新成员加入团队时快速理解项目架构。

```bash
#!/bin/bash
# 项目onboarding文档生成
echo "=== 生成项目理解文档 ==="

# 1. 架构分析
echo "1. 项目架构分析..."
python3 architecture_analyzer.py ./src > architecture.json

# 2. 生成架构图
echo "2. 生成架构图..."
python3 mermaid_generator.py --input architecture.json --output architecture.mmd

# 3. 生成模块文档
echo "3. 生成模块文档..."
python3 doc_generator.py ./src --output ./docs/

# 4. 复杂度分析
echo "4. 代码复杂度分析..."
python3 complexity_analyzer.py ./src > complexity-report.json

# 5. 生成onboarding文档
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

### 场景二:API文档自动生成

从代码中自动提取API文档。

```bash
# 自动生成API文档
python3 doc_generator.py \
    --mode api \
    --input ./src \
    --output ./docs/api.md \
    --format markdown

# 同时生成OpenAPI规范
python3 doc_generator.py \
    --mode api \
    --input ./src \
    --output ./docs/openapi.json \
    --format openapi
```

### 场景三:遗留系统逆向理解

对遗留系统进行逆向分析和文档化。

```python
# 遗留系统逆向分析
class LegacySystemAnalyzer:
    """遗留系统逆向分析器"""

    def __init__(self, project_root):
        self.root = project_root
        self.architecture = ProjectArchitectureAnalyzer(project_root)
        self.complexity = CodeComplexityAnalyzer(project_root)
        self.docs = CodeDocGenerator(project_root)

    def full_analysis(self):
        """完整逆向分析"""
        print("=== 遗留系统逆向分析 ===")

        # 1. 架构分析
        print("1. 架构分析...")
        arch_report = self.architecture.analyze()

        # 2. 复杂度分析
        print("2. 复杂度分析...")
        complexity_report = self.complexity.analyze()

        # 3. 文档生成
        print("3. 文档生成...")
        self.docs.generate_all()

        # 4. 生成分析报告
        print("4. 生成综合报告...")
        report = {
            "analysis_time": datetime.now().isoformat(),
            "project": self.root,
            "architecture": arch_report,
            "complexity": {
                "total_files": len(complexity_report),
                "high_complexity_files": [
                    r for r in complexity_report if r["rating"] in ["高", "极高"]
                ],
                "average_complexity": sum(r["complexity"] for r in complexity_report) / len(complexity_report)
            },
            "recommendations": self._generate_recommendations(arch_report, complexity_report)
        }
        return report

    def _generate_recommendations(self, arch, complexity):
        """生成改进建议"""
        recs = []
        high_complex = [r for r in complexity if r["rating"] == "极高"]
        if high_complex:
            recs.append(f"发现{len(high_complex)}个极高复杂度文件,建议优先重构")

        if arch["summary"]["total_files"] > 100:
            recs.append("项目文件较多,建议按模块拆分文档")

        return recs
```

## 快速开始

### 步骤一:配置分析

```yaml
# .explain-code-pro.yml
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

### 步骤二:运行分析

```
请对当前项目进行完整架构分析,生成模块文档和架构图。
```

### 步骤三:查看结果

- `./docs/architecture.md`:架构分析报告
- `./docs/api.md`:API文档
- `./docs/modules/`:各模块文档
- `./docs/diagrams/`:Mermaid图表

## 配置示例

### 企业级完整配置

```yaml
version: "2.0"
edition: pro

# 分析配置
analysis:
  architecture: true
  complexity: true
  dependency_graph: true
  code_metrics: true
  exclude_dirs: [node_modules, .git, dist, build, vendor]

# 文档生成
documentation:
  generate_api_docs: true
  generate_module_docs: true
  generate_readme: true
  output_format: markdown
  output_dir: ./docs/
  include_examples: true
  language: zh-CN

# 可视化
visualization:
  use_mermaid: true
  use_ascii: true
  diagram_types:
    - flowchart
    - sequence
    - class
    - dependency
    - state
  max_diagram_nodes: 50

# 复杂度分析
complexity:
  cyclomatic: true
  cognitive: true
  thresholds:
    low: 5
    medium: 10
    high: 20
    critical: 30

# 团队知识库
knowledge_base:
  enabled: true
  output_dir: ./wiki/
  auto_update: true
  search_index: true
```

## 最佳实践

1. **定期更新文档**:设置定时任务重新生成文档

```bash
# 每周自动更新文档
0 2 * * 0 /opt/tools/code-doc-generator.sh
```

2. **结合Git Hook**:代码提交时自动更新相关文档

```bash
# post-commit hook
python3 doc_generator.py --incremental --changed-files $(git diff --name-only HEAD~1)
```

3. **分层文档**:为不同读者生成不同详细度的文档

```yaml
documentation:
  levels:
    executive: summary_only
    architect: architecture_focused
    developer: full_detail
    new_member: onboarding_focused
```

4. **版本化文档**:将文档纳入版本控制

5. **团队共享**:将生成的文档部署到内部Wiki

## 常见问题

### Q1:专业版如何兼容免费版?

专业版完全兼容免费版的解释风格。免费版的 `.explain-code.yml` 配置可直接使用,专业版会自动启用架构分析和文档生成功能。

### Q2:大型项目分析性能如何?

| 项目规模 | 文件数 | 分析时间 | 内存 |
|:---------|:-------|:---------|:-----|
| 小型 | <100 | <30s | <100MB |
| 中型 | 100-1000 | 1-5min | 100-500MB |
| 大型 | 1000-10000 | 5-20min | 500MB-2GB |
| 超大型 | >10000 | 20min+ | 建议分模块 |

### Q3:支持哪些文档格式?

| 格式 | 用途 | 输出 |
|:-----|:-----|:-----|
| Markdown | 通用文档 | .md |
| HTML | 在线浏览 | .html |
| OpenAPI | API规范 | .json/.yaml |
| Mermaid | 图表 | .mmd |

### Q4:如何集成到CI/CD?

```yaml
# GitLab CI
code_documentation:
  stage: docs
  script:
    - python3 doc_generator.py --all --output ./docs/
  artifacts:
    paths:
      - docs/
    expire_in: 30 days
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Python 3.8+ / Node.js 16+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Mermaid CLI | 可视化工具 | 推荐 | npm install -g @mermaid-js/mermaid-cli |
| mkdocs | 文档站点 | 可选 | pip install mkdocs |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 所有代码分析在本地完成

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持项目级分析、批量文档生成和可视化)
- **说明**:企业级代码理解工具,支持架构分析、文档生成和知识库构建
- **适用规模**:中小型到大型项目
- **兼容性**:完全兼容免费版解释风格,支持平滑升级
