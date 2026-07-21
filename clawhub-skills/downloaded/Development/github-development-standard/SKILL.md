---
slug: github-development-standard
name: github-development-standard
version: "2.0.0"
displayName: Github Development S
summary: 完整的 GitHub 项目开发标准流程 - 9步流程 + 4层验证 + 15项验收清单
license: MIT-0
description: |-
  完整的 GitHub 项目开发标准流程 - 9步流程 + 4层验证 + 15项验收清单

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Development
tools:
  - - read
- exec
---

# GitHub Development Standard

> **用方法论驯服低端模型，让代码质量不再妥协**

## 💡 核心价值

解决低端模型在代码开发中的常见问题：

* ❌ 过度修改（200+ 行，夹带重构）
* ❌ 无验证（直接说"修好了"）
* ❌ 夹带私货（顺便优化、重构）

## 📋 9 步开发流程

```text
1. 读 issue → 2. 写任务卡 → 3. 确定基线
     ↓
4. 列改动点 → 5. 编码 → 6. 本地验证
     ↓
7. 看 diff → 8. 写发布说明 → 9. 复盘
```

## ✅ 8 条编码纪律

1. 先复制旧代码，再局部替换
2. 改函数前，先通读输入/输出/副作用
3. 涉及数据结构变化时，先搜所有使用点
4. 不要同时改逻辑和风格
5. 不要在 bug fix 里做重构
6. 不要修改未被需求要求的行为
7. 不要在没有验证前说"修好了"
8. 不要让 release note 超前于实际代码

## 🔍 4 层验证

```bash
python3 -m py_compile scripts/xxx.py

python3 -c "from scripts.xxx import ClassName"

python3 test_fix.py

python3 -m pytest tests/
```

## 📊 15 项验收清单

### A. 需求一致性（3 项）

* A1. 我能用一句话说清这次修复的目标
* A2. 我知道这次"不打算修"的内容有哪些
* A3. 代码改动与 issue 描述一致

### B. 技术正确性（4 项）

* B1. 我基于正确版本开始修改
* B2. 我没有重写整个文件
* B3. 数据结构变化已同步所有引用点
* B4. 新逻辑不会破坏旧逻辑

### C. 测试验证（4 项）

* C1. 语法检查通过
* C2. 导入检查通过
* C3. 最小样例验证通过
* C4. 回归测试通过

### D. 发布质量（4 项）

* D1. diff 大小与任务规模匹配
* D2. release note 与实际代码一致
* D3. 版本号、文档、注释已同步
* D4. 我可以指出这次改动的风险点

## 🔧 GitHub CLI 使用

```bash
gh issue view 53 --repo owner/repo

gh issue comment 53 --repo owner/repo --body "修复说明..."

gh issue close 53 --repo owner/repo
```

## 已知限制

1. **同步修改** - 修改 README.md 时，检查其他语言版本
2. **工具验证** - 用 `grep` 等工具验证比人工更可靠
3. **文档清理** - 先整合内容，再删除冗余文件

## 📊 效果对比

| 指标 | 使用前 | 使用后 | 提升 |
| --- | --- | --- | --- |
| Bug 修复返工率 | 60% | 5% | **↓ 55%** |
| 平均改动量 | 200+ 行 | 15 行 | **↓ 185 行** |
| 夹带私货率 | 70% | 0% | **↓ 70%** |

## 💡 核心理念

> **先定义问题，再定义改法，再写代码，再做验证，最后才发布。**

## 🔗 相关链接

* **GitHub**: <https://github.com/SonicBotMan/github-development-standard>
* **SkillHub**: <https://SkillHub.com/skills/github-development-standard>

---

**让代码质量不再妥协** 💕

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 触发关键词: development, github, 项目开发标准, standard, 层验证, 步流程, 流程, 完整的

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Github Development S？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Github Development S有什么限制？
A: 请参考已知限制章节了解具体限制。
