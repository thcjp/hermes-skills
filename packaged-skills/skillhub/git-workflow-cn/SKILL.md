---
slug: "git-workflow-cn"
name: "git-workflow-cn"
version: 1.1.1
displayName: "Git Workflow Cn"
summary: "Git 工作流助手 - 分支管理、冲突解决、提交规范。适合：开发者、团队协作。"
license: "Proprietary"
description: |-
  Git 工作流助手 - 分支管理、冲突解决、提交规范。适合：开发者、团队协作。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Development
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "版本控制,Git,开发工具"
category: "Development"
---
# Git Workflow Cn

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Git Workflow Cn分支管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

| 功能 | 描述 |
|:-----|:-----|
| 分支管理 | 创建、切换、合并分支 |
| 冲突解决 | 识别和解决冲突 |
| 提交规范 | Conventional Commits |
| 常见问题 | 撤销、回滚、恢复 |
### 分支管理

针对分支,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供分支管理相关的配置参数、输入数据和处理选项.
**输出**: 返回分支管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`分支管理`的配置文档进行参数调优
### 冲突解决

针对冲突解决,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供冲突解决相关的配置参数、输入数据和处理选项.
**输出**: 返回冲突解决的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`冲突解决`的配置文档进行参数调优
### 提交规范

针对提交规范,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供提交规范相关的配置参数、输入数据和处理选项.
**输出**: 返回提交规范的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`提交规范`的配置文档进行参数调优
#
## 适用场景

| 场景 | 输入 | 输出 |
|---:|---:|---:|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 分支操作

```text
创建并切换到新分支 feature/login
```

### 冲突解决(补充)

```text
帮我解决 Git 合并冲突
```

### 提交建议

```text
为这些改动生成符合规范的提交信息
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | git-workflow-cn处理的内容输入 |, 默认: 全部维度 |
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
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
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

### 撤销操作

```bash
git checkout -- file.txt
git restore file.txt              # 新语法
# ...
git reset HEAD file.txt
git restore --staged file.txt     # 新语法
# ...
git reset --soft HEAD~1
# ...
git reset --hard HEAD~1
# ...
git commit --amend -m "新信息"
```

### 回滚代码

```bash
git revert COMMIT_ID
# ...
git revert COMMIT_ID1..COMMIT_ID2
# ...
git revert --no-commit COMMIT_ID
```

### 恢复删除

```bash
git checkout COMMIT_ID -- file.txt
# ...
git reflog                        # 查找提交
git reset --hard COMMIT_ID        # 恢复
# ...
git reflog                        # 找到分支最后的提交
git checkout -b branch_name COMMIT_ID
```

### 清理仓库

```bash
git clean -n                      # 预览
git clean -f                      # 删除文件
git clean -fd                     # 删除文件和目录
# ...
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/file' \
  --prune-empty --tag-name-filter cat -- --all
# ...
bfg --delete-folders folder_name
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

* 提交前先拉取最新代码
* 功能分支及时合并
* 避免直接提交到 main
* 重要操作先备份

---

创建：2026-03-12
版本：1.0
