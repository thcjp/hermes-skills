---
slug: "git-helper-paid"
name: "git-helper-paid"
version: 1.0.1
displayName: "Git助手专业版"
summary: "企业级Git辅助工具,支持智能冲突分析、自动修复、批量诊断与团队知识库,提升协作效率。。面向企业研发团队的高级Git辅助工具,提供智能冲突分析、自动修复建议、批量仓库诊断、团队知识库与故障自"
license: "MIT"
edition: "pro"
description: |-
  面向企业研发团队的高级Git辅助工具,提供智能冲突分析、自动修复建议、批量仓库诊断、团队知识库与故障自动恢复。核心能力:
  - 智能冲突分析与自动修复建议
  - 批量仓库健康诊断
  - 自动化故障恢复
  - 团队Git知识库与FAQ
  - 操作审计与回溯
  - 团队工作流向导

  适用场景:
  - 企业级Git问题排查
  - 复杂冲突智能分析
  - 多仓库批量诊断
  - 团队Git培训与知识沉淀

  差异化:
  - 专业版完全兼容免费版指引,支持平滑升级
  - 提供智能冲突分析和修复建议
  - 支持批量诊断和自动恢复
tags:
  - 开发工具
  - Git
  - 辅助工具
  - 企业级
  - 智能分析
  - 版本控制
  - analysis
  - print
  - git
  - strip
tools:
  - read
  - exec
  - write
homepage: ""
category: "Development"
---
# Git助手专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Git助手专业版支持智能冲突分析 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

### 1. 智能冲突分析
自动分析冲突内容,提供修复建议.
> 详细代码示例已移至 `references/detail.md`- 验证返回数据的完整性和格式正确性
- 参考`自动修复建议`的配置文档进行参数调优
### 2. 自动修复建议
```python
class ConflictResolver:
    """冲突自动修复工具"""
# ...
    @staticmethod
    def auto_resolve(filepath, cwd=None):
        """自动解决可自动处理的冲突"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
# ...
        resolved_count = 0
        pattern = re.compile(
            r'<<<<<<< (\S+)\n(.*?)=======\n(.*?)>>>>>>> (\S+)',
            re.DOTALL
        )
# ...
        def resolver(match):
            nonlocal resolved_count
            our_code = match.group(2)
            their_code = match.group(3)
# ...
            analysis = ConflictAnalyzer._analyze_conflict_content(
                our_code.strip(), their_code.strip()
            )
# ...
            if analysis["auto_resolvable"]:
                resolved_count += 1
# ...
                if analysis["type"] == "whitespace":
                    return our_code.strip() + '\n'
                elif analysis["type"] == "import":
                    all_imports = set()
                    for line in (our_code + their_code).split('\n'):
                        if line.strip():
                            all_imports.add(line.strip())
                    return '\n'.join(sorted(all_imports)) + '\n'
                elif analysis["type"] == "addition":
                    return our_code if our_code.strip() else their_code
            else:
                return match.group(0)
# ...
        new_content = pattern.sub(resolver, content)
# ...
        if resolved_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
# ...
        return {
            "file": filepath,
            "auto_resolved": resolved_count,
            "remaining": content.count('<<<<<<<') - resolved_count
        }
# ...
    @staticmethod
    def batch_auto_resolve(cwd=None):
        """批量自动解决冲突"""
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=U"],
            capture_output=True, text=True, cwd=cwd
        )
        files = result.stdout.strip().split('\n') if result.stdout.strip() else []
# ...
        results = []
        for f in files:
            if f:
                results.append(ConflictResolver.auto_resolve(f, cwd))
# ...
        return {
            "total_files": len(files),
            "results": results,
            "total_auto_resolved": sum(r["auto_resolved"] for r in results)
        }
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `自动修复建议` 选项
- 处理流程: 接收输入 -> 执行自动修复建议 -> 返回结果
- 输入: 用户提供自动修复建议所需的参数和指令
- 输出: 返回自动修复建议的处理结果,包含执行状态码、结果数据和执行日志

### 3. 批量仓库诊断
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量仓库诊断所需的指令和必要参数.
**处理**: 解析批量仓库诊断的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回批量仓库诊断的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供自动化故障恢复所需的指令和必要参数.
**处理**: 解析自动化故障恢复的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自动化故障恢复的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供团队知识库所需的指令和必要参数.
**处理**: 解析团队知识库的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回团队知识库的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:智能冲突解决
遇到复杂冲突时获取智能分析.
```bash
#!/bin/bash
echo "=== 智能冲突解决 ==="
# ...
echo "1. 分析冲突..."
python3 -c "
from conflict_analyzer import ConflictAnalyzer
import json
analysis = ConflictAnalyzer.analyze_conflicts()
print(json.dumps(analysis, indent=2, ensure_ascii=False))
print(f\"\\n冲突总数: {analysis['summary']['total_conflicts']}\")
print(f\"可自动解决: {analysis['summary']['auto_resolvable']}\")
print(f\"需手动处理: {analysis['summary']['manual_required']}\")
"
# ...
echo -e "\n2. 自动解决冲突..."
python3 -c "
from conflict_resolver import ConflictResolver
result = ConflictResolver.batch_auto_resolve()
print(f'自动解决: {result[\"total_auto_resolved\"]} 个')
"
# ...
echo -e "\n3. 剩余冲突需手动处理"
git diff --name-only --diff-filter=U
# ...
echo -e "\n4. 所有冲突解决后:"
echo "  git add ."
echo "  git commit"
```

### 场景二:批量仓库健康检查
检查团队所有仓库的健康状态.
```bash
#!/bin/bash
echo "=== 批量仓库健康检查 ==="
# ...
python3 -c "
from batch_diagnostics import BatchRepositoryDiagnostics
import json
# ...
repos = [
    '/home/user/project-a',
    '/home/user/project-b',
    '/home/user/project-c'
]
# ...
diagnostics = BatchRepositoryDiagnostics(repos)
report = diagnostics.diagnose_all()
# ...
print(f\"总仓库数: {report['total_repos']}\")
print(f\"健康: {report['healthy']}\")
print(f\"需关注: {report['needs_attention']}\")
print(f\"错误: {report['errors']}\")
# ...
for repo, diag in report['details'].items():
    status = diag['status']
    issues = len(diag.get('issues', []))
    print(f'  [{status}] {repo} ({issues}个问题)')
"
```

### 场景三:自动故障恢复
遇到Git问题时自动检测并恢复.
```bash
#!/bin/bash
echo "=== Git故障检测 ==="
# ...
python3 -c "
from recovery_assistant import GitRecoveryAssistant
import json
# ...
issues = GitRecoveryAssistant.detect_issue()
if issues:
    print('检测到问题:')
    for issue in issues:
        print(f'  - {issue[\"message\"]}')
# ...
        plan = GitRecoveryAssistant.get_recovery_plan(issue['scenario'])
        if plan:
            print(f'    描述: {plan[\"description\"]}')
            print(f'    步骤:')
            for step in plan['steps']:
                print(f'      {step}')
# ...
            print(f'    尝试自动恢复...')
            result = GitRecoveryAssistant.auto_recover(issue['scenario'])
            print(f'    结果: {\"成功\" if result[\"success\"] else \"失败\"}')
else:
    print('未检测到问题,仓库状态正常')
"
```

## 使用流程

### 步骤一:运行诊断
```
请对当前Git仓库进行健康诊断,发现问题并提供修复建议.
```

### 步骤二:智能解决
```
请分析当前的合并冲突,自动解决可处理的冲突.
```

### 步骤三:查看知识库
```
如何撤销已推送的提交?
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | git-helper处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.20+ / Python 3.8+ / Bash

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Git 2.20+ | 运行时 | 必需 | git-scm.com 下载 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证配置:

```bash
ssh-keygen -t ed25519 -C "your@email.com"
# ...
git config --global credential.helper store
```

### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持智能分析、批量诊断和自动恢复)
- **说明**:企业级Git辅助工具,支持智能冲突分析和团队知识库
- **适用规模**:个人到大型团队多仓库项目
- **兼容性**:完全兼容免费版指引和配置,支持平滑升级

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有指引和检查清单。免费版的配置可直接使用,专业版会自动启用智能分析和诊断功能.
### Q2:自动冲突解决安全吗?
自动解决仅处理可安全自动处理的冲突类型(空白差异、导入合并、单方新增),复杂冲突仍需手动处理.
### Q3:支持多少个仓库批量诊断?
| 仓库数量 | 耗时 | 并行 |
|:------|------:|:------|
| 1-10 | <30s | 串行 |
| 10-50 | 1-3min | 并行 |
| 50-100 | 3-10min | 并行 |
| 100+ | 10min+ | 分批 |

### Q4:如何扩展知识库?
```yaml
custom_faq:
  - question: "如何配置Git代理"
    answer: "使用 git config 设置HTTP代理"
    command: "git config --global http.proxy http://proxy:8080"
    category: "配置"
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

