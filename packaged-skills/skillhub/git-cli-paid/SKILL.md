---
slug: "git-cli-paid"
name: "git-cli-paid"
version: 1.0.1
displayName: "Git命令行助手专业版"
summary: "企业级Git CLI工具,支持自动化脚本、深度诊断、工作流模板与故障排除,提升团队效率。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业研发团队的高级Git命令行工具,提供自动化脚本、深度仓库诊断、工作流模板、故障排除与批量操作能力。核心能力:
  - Git自动化脚本库
  - 深度仓库诊断与分析
  - 标准化工作流模板
  - 故障排除与恢复
  - 批量Git操作
  - 多仓库管理

  适用场景:
  - 企业级Git工作流自动化
  - 仓库健康诊断
  - 团队标准化操作
  - 复杂故障排除

  差异化:
  - 专业版完全兼容免费版命令,支持平滑升级
  - 提供自动化脚本和批量操作
  - 内置深度诊断和工作流模板
  - 支持多仓库统一管理

  ...
tags:
  - 开发工具
  - Git
  - 命令行
  - 企业级
  - 自动化
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Git命令行助手专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

### 1. Git自动化脚本库
提供常用Git操作的自动化脚本.
> 详细代码示例已移至 `references/detail.md`

**处理**: 解析Git自动化脚本库的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Git自动化脚本库的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供深度仓库诊断所需的指令和必要参数.
**处理**: 解析深度仓库诊断的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回深度仓库诊断的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供工作流模板所需的指令和必要参数.
**处理**: 解析工作流模板的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回工作流模板的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供多仓库管理所需的指令和必要参数.
**处理**: 解析多仓库管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多仓库管理的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景一:日常开发自动化
自动化日常Git操作.
```bash
#!/bin/bash
echo "=== Git日常自动化 ==="
# ...
echo "1. 仓库状态:"
python3 -c "
from git_automation import GitAutomation
import json
status = GitAutomation.get_repo_status()
print(json.dumps(status, indent=2, ensure_ascii=False))
"
# ...
echo -e "\n2. 智能提交:"
python3 -c "
from git_automation import GitAutomation
result = GitAutomation.smart_commit('feat: 日常开发提交')
print(result)
"
# ...
echo -e "\n3. 智能同步:"
python3 -c "
from git_automation import GitAutomation
result = GitAutomation.sync_branch()
print(result)
"
```

### 场景二:仓库健康诊断
定期对仓库进行健康诊断.
```bash
#!/bin/bash
echo "=== Git仓库健康诊断 ==="
# ...
python3 -c "
from git_diagnostics import GitDiagnostics
import json
# ...
diagnosis = GitDiagnostics.full_diagnosis()
print(json.dumps(diagnosis, indent=2, ensure_ascii=False))
# ...
print('\n=== 建议 ===')
for rec in diagnosis.get('recommendations', []):
    print(f'  - {rec}')
"
```

### 场景三:多仓库批量管理
统一管理多个Git仓库.
```bash
#!/bin/bash
echo "=== 多仓库批量管理 ==="
# ...
cat > repos.txt << 'EOF'
/home/user/project-a
/home/user/project-b
/home/user/project-c
EOF
# ...
echo "1. 批量状态检查:"
python3 -c "
from multi_repo import MultiRepoManager
import json
manager = MultiRepoManager('repos.txt')
status = manager.batch_status()
for repo, info in status.items():
    if 'error' in info:
        print(f'[ERROR] {repo}: {info[\"error\"]}')
    else:
        branch = info.get('branch', '?')
        clean = '干净' if info.get('is_clean') else '有变更'
        print(f'[OK] {repo}: {branch} ({clean})')
"
# ...
echo -e "\n2. 批量同步:"
python3 -c "
from multi_repo import MultiRepoManager
manager = MultiRepoManager('repos.txt')
results = manager.batch_sync()
for repo, result in results.items():
    print(f'{repo}: {result}')
"
# ...
echo -e "\n3. 批量清理:"
python3 -c "
from multi_repo import MultiRepoManager
manager = MultiRepoManager('repos.txt')
results = manager.batch_cleanup()
for repo, result in results.items():
    print(f'{repo}: {result}')
"
```

## 使用流程

### 步骤一:配置自动化
```yaml
version: "2.0"
edition: pro
# ...
automation:
  smart_commit: true
  auto_sync: true
  auto_cleanup: true
# ...
diagnostics:
  health_check: true
  performance_check: true
  security_check: true
  large_file_threshold: 10MB
# ...
workflows:
  feature:
    branch_prefix: "feature/"
    auto_push: true
    auto_cleanup_on_merge: true
  hotfix:
    branch_prefix: "hotfix/"
    auto_tag: true
  release:
    branch_prefix: "release/"
    auto_tag: true
# ...
multi_repo:
  repos_file: repos.txt
  batch_operations: [status, sync, cleanup]
```

### 步骤二:运行诊断
```
请对当前Git仓库进行深度健康诊断,输出问题和建议.
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | git-cli处理的内容输入 |,  |
| content | string | 否 | git-cli处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

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
- **分类**:MD+EXEC+PRO(专业版支持自动化脚本、深度诊断和批量操作)
- **说明**:企业级Git CLI工具,支持自动化工作流和多仓库管理
- **适用规模**:个人到大型团队多仓库项目
- **兼容性**:完全兼容免费版命令和配置,支持平滑升级

## 案例展示

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

## 常见问题

### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有Git命令和配置。免费版的别名和配置可直接使用,专业版会自动启用自动化和诊断功能.
### Q2:自动化脚本安全吗?
所有自动化脚本遵循安全优先原则:
- 危险操作需要确认
- 不会自动执行force push
- 不会自动删除未合并分支
- 保留操作日志

### Q3:支持多少个仓库批量管理?
| 仓库数量 | 并行处理 | 耗时 |
|:------|------:|:------|
| 1-10 | 串行 | <10s |
| 10-50 | 并行 | 10-30s |
| 50-100 | 并行 | 30-60s |
| 100+ | 分批并行 | 1-5min |

### Q4:如何自定义工作流?
```bash
workflows:
  custom:
    prefix: "custom/"
    steps:
      - fetch
      - create_branch
      - push
      - notify
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

