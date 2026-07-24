# 深度差异化改造方法论

## 核心原则
**不重写、不抄袭、不伪装** — 基于原始skill的能力定位，结合用户痛点和真实使用场景，打造功能更强、成本更低、体验更好的新一代skill。

## 五大差异化维度

### 1. 质量提升 (Quality)
- 补充原始skill缺失的边界情况处理
- 增加完整的错误代码与恢复策略
- 提供更详细的使用示例（至少3个真实场景）
- 补充参数说明、返回值结构、限制条件

### 2. 实用性增强 (Practicality)
- 基于用户评论/痛点新增高频功能
- 简化复杂工作流为"一键式"模板
- 增加场景化使用指南（按用户角色分类）
- 提供常见问题FAQ与故障排查

### 3. 易用性优化 (Simplicity)
- 精简冗长指令，降低token消耗
- 使用结构化模板（表格、清单）替代段落描述
- 提供"快速开始"章节（<50行）
- 分层文档：快速入门 → 标准用法 → 高级配置

### 4. LLM成本降低 (Cost)
- 压缩重复说明，合并相似指令
- 使用变量引用而非重复定义
- 按需加载机制（references分层）
- 提供token用量预估与优化建议

### 5. 性能提升 (Performance)
- 增加缓存策略（结果复用、批量请求）
- 优化API调用顺序（并行化、减少往返）
- 提供增量更新机制
- 增加重试与熔断策略

## 改造流程（每个skill）

### 步骤1：原始内容分析
- 阅读完整SKILL.md
- 识别核心能力（3-5个）
- 标记薄弱环节

### 步骤2：痛点研究
- WebSearch该领域的用户痛点
- 查找竞品/同类工具的评论
- 总结3-5个高频痛点

### 步骤3：差异化设计
- 针对每个痛点设计解决方案
- 确定新增功能模块
- 规划新的工作流

### 步骤4：内容重写
- 完全重写SKILL.md（保留核心API引用）
- 新slug命名：`[功能化新概念]`，不使用 -pro/-free 后缀（详见 `NAMING_CONVENTION.md`）
- 更新frontmatter（新slug、新displayName、新summary）
- 增加差异化说明章节

### 步骤5：验证
- 确认内容完全不同于原始（非简单修改）
- 确认frontmatter合规
- 确认无原始仓库引用

## 新slug命名规则
- 使用功能化命名，不使用`-pro`后缀的简单变体
- 体现差异化特色（如`admapix` → `ad-insight-hub`）
- 全局唯一kebab-case
- 长度控制在20字符内
- 付费版与免费版的命名规则参见 `NAMING_CONVENTION.md` 第2.1节

## frontmatter规范
```yaml
---
slug: [new-slug]
name: [新名称]
version: "1.0.0"
displayName: [<=20字符]
summary: [<=100字符, 痛点导向]
license: MIT
description: |-
  [5段结构：价值主张 + 核心能力 + 适用场景 + 差异化 + 触发词]
tags:
- [分类]
tools:
- read
- exec
---
```

## 依赖说明章节（必须）
每个SKILL.md末尾必须包含：
```markdown
## 依赖说明

### 运行环境
- Agent平台、操作系统要求

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |

### API Key 配置
- 明确说明所需Key

### 可用性分类
- MD / MD+EXEC / MD+CODE
```

## 进度跟踪
- 改造记录保存到 `d:\skills\clawhub-skills\differentiation-log.csv`
- 字段：timestamp, category, original_slug, new_slug, enhancements, status
