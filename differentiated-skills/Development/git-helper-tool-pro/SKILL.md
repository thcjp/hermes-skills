---
slug: git-helper-tool-pro
name: git-helper-tool-pro
version: "1.0.0"
displayName: Git助手专业版
summary: 企业级Git辅助工具,支持智能冲突分析、自动修复、批量诊断与团队知识库,提升协作效率。
license: Proprietary
edition: pro
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
tools:
  - read
  - exec
---
# Git助手 - 专业版
## 概述
Git助手专业版为企业研发团队提供智能Git辅助能力。在免费版操作指引之上,专业版新增智能冲突分析、自动修复建议、批量仓库诊断、自动化故障恢复和团队知识库,帮助团队高效解决Git问题。

专业版完全兼容免费版的所有指引和检查清单,研发团队可从免费版无缝升级,已有配置和工作流无需修改。

## 核心能力
### 1. 智能冲突分析
自动分析冲突内容,提供修复建议。

> 详细代码示例已移至 `references/detail.md`

### 2. 自动修复建议
```python
class ConflictResolver:
    """冲突自动修复工具"""

    @staticmethod
    def auto_resolve(filepath, cwd=None):
        """自动解决可自动处理的冲突"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        resolved_count = 0
        pattern = re.compile(
            r'<<<<<<< (\S+)\n(.*?)=======\n(.*?)>>>>>>> (\S+)',
            re.DOTALL
        )

        def resolver(match):
            nonlocal resolved_count
            our_code = match.group(2)
            their_code = match.group(3)

            analysis = ConflictAnalyzer._analyze_conflict_content(
                our_code.strip(), their_code.strip()
            )

            if analysis["auto_resolvable"]:
                resolved_count += 1

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

        new_content = pattern.sub(resolver, content)

        if resolved_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return {
            "file": filepath,
            "auto_resolved": resolved_count,
            "remaining": content.count('<<<<<<<') - resolved_count
        }

    @staticmethod
    def batch_auto_resolve(cwd=None):
        """批量自动解决冲突"""
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=U"],
            capture_output=True, text=True, cwd=cwd
        )
        files = result.stdout.strip().split('\n') if result.stdout.strip() else []

        results = []
        for f in files:
            if f:
                results.append(ConflictResolver.auto_resolve(f, cwd))

        return {
            "total_files": len(files),
            "results": results,
            "total_auto_resolved": sum(r["auto_resolved"] for r in results)
        }
```

### 3. 批量仓库诊断

> 详细代码示例已移至 `references/detail.md`

### 4. 自动化故障恢复

> 详细代码示例已移至 `references/detail.md`

### 5. 团队知识库

> 详细代码示例已移至 `references/detail.md`

## 使用场景
### 场景一:智能冲突解决
遇到复杂冲突时获取智能分析。

```bash
#!/bin/bash
echo "=== 智能冲突解决 ==="

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

echo -e "\n2. 自动解决冲突..."
python3 -c "
from conflict_resolver import ConflictResolver
result = ConflictResolver.batch_auto_resolve()
print(f'自动解决: {result[\"total_auto_resolved\"]} 个')
"

echo -e "\n3. 剩余冲突需手动处理"
git diff --name-only --diff-filter=U

echo -e "\n4. 所有冲突解决后:"
echo "  git add ."
echo "  git commit"
```

### 场景二:批量仓库健康检查
检查团队所有仓库的健康状态。

```bash
#!/bin/bash
echo "=== 批量仓库健康检查 ==="

python3 -c "
from batch_diagnostics import BatchRepositoryDiagnostics
import json

repos = [
    '/home/user/project-a',
    '/home/user/project-b',
    '/home/user/project-c'
]

diagnostics = BatchRepositoryDiagnostics(repos)
report = diagnostics.diagnose_all()

print(f\"总仓库数: {report['total_repos']}\")
print(f\"健康: {report['healthy']}\")
print(f\"需关注: {report['needs_attention']}\")
print(f\"错误: {report['errors']}\")

for repo, diag in report['details'].items():
    status = diag['status']
    issues = len(diag.get('issues', []))
    print(f'  [{status}] {repo} ({issues}个问题)')
"
```

### 场景三:自动故障恢复
遇到Git问题时自动检测并恢复。

```bash
#!/bin/bash
echo "=== Git故障检测 ==="

python3 -c "
from recovery_assistant import GitRecoveryAssistant
import json

issues = GitRecoveryAssistant.detect_issue()
if issues:
    print('检测到问题:')
    for issue in issues:
        print(f'  - {issue[\"message\"]}')

        plan = GitRecoveryAssistant.get_recovery_plan(issue['scenario'])
        if plan:
            print(f'    描述: {plan[\"description\"]}')
            print(f'    步骤:')
            for step in plan['steps']:
                print(f'      {step}')

            print(f'    尝试自动恢复...')
            result = GitRecoveryAssistant.auto_recover(issue['scenario'])
            print(f'    结果: {\"成功\" if result[\"success\"] else \"失败\"}')
else:
    print('未检测到问题,仓库状态正常')
"
```

## 不适用场景

以下场景Git助手专业版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调


## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。


## 快速开始
### 步骤一:运行诊断
```
请对当前Git仓库进行健康诊断,发现问题并提供修复建议。
```

### 步骤二:智能解决
```
请分析当前的合并冲突,自动解决可处理的冲突。
```

### 步骤三:查看知识库
```
如何撤销已推送的提交?
```

## 配置示例
### 企业级配置
```yaml
version: "2.0"
edition: pro

conflict_analysis:
  enabled: true
  auto_resolve: true
  safe_mode: true
  complexity_threshold: 50

batch_diagnostics:
  enabled: true
  repos:
    - /home/user/project-a
    - /home/user/project-b
  schedule: weekly
  report_format: json

auto_recovery:
  enabled: true
  safe_only: true
  create_backup: true

knowledge_base:
  enabled: true
  auto_search: true
  custom_faq: ./git-faq.yml

audit:
  enabled: true
  log_file: ./git-audit.log
  log_level: info
  include_commands: true
  retention_days: 90
```

## 最佳实践
1. **定期诊断**:设置定期仓库健康检查

```bash
0 2 * * 0 python3 batch_diagnostics.py
```

2. **智能解决**:优先使用自动分析处理冲突

3. **安全恢复**:恢复前创建备份

4. **知识沉淀**:将常见问题添加到知识库

5. **审计追踪**:记录所有Git操作用于追溯

## 常见问题
### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有指引和检查清单。免费版的配置可直接使用,专业版会自动启用智能分析和诊断功能。

### Q2:自动冲突解决安全吗?
自动解决仅处理可安全自动处理的冲突类型(空白差异、导入合并、单方新增),复杂冲突仍需手动处理。

### Q3:支持多少个仓库批量诊断?
| 仓库数量 | 耗时 | 并行 |
|:---------|:-----|:-----|
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

## 依赖说明
### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.20+ / Python 3.8+ / Bash

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git 2.20+ | 运行时 | 必需 | git-scm.com 下载 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证配置:

```bash
ssh-keygen -t ed25519 -C "your@email.com"

git config --global credential.helper store
```

### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持智能分析、批量诊断和自动恢复)
- **说明**:企业级Git辅助工具,支持智能冲突分析和团队知识库
- **适用规模**:个人到大型团队多仓库项目
- **兼容性**:完全兼容免费版指引和配置,支持平滑升级

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
