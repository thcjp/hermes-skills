---
slug: "resume-assistant"
name: "resume-assistant"
version: "1.0.0"
displayName: "简历助手"
summary: "AI简历助手，支持polish润色、customize定制、score评分与export多格式导出。"
license: "Proprietary"
description: |-
  AI驱动的简历/CV助手，帮助求职者创建、优化与导出简历.
  支持polish润色（40+检查项）、customize针对岗位定制、score 100分制评分.
  支持export导出为Word、Markdown、HTML、LaTeX、PDF多格式.
  提供ATS优化、差距分析与改进建议，适用于各行业求职场景.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 简历助手

AI简历助手，支持polish润色、customize定制、score评分与export多格式导出.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 简历助手处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 简历助手xport多格式导出 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### Polish - 简历润色

运行40+检查项的全面审查，返回完全改进的简历：

**检查覆盖8大类别：**
- 联系信息（contact）
- 个人简介（summary）
- 工作经历（experience）
- 教育背景（education）
- 技能（skills）
- 语法（grammar）
- 格式（formatting）
- ATS兼容性（ATS）

**输出内容：**
- 每个检查项的 ✅/❌/⚠️ 结果
- 完全润色后的简历（强动词+量化成果）
- 按优先级分类的变更摘要：🔴 Critical → 🟡 Major → 🟢 Minor → 💡 Suggestion
- 动作动词参考表与量化指南

**参数：**
| 参数 | 类型 | 必需 | 默认 | 说明 |
|:---:|:---:|:---:|:---:|:---:|
| `resume_content` | string | 是 | - | 简历文本（纯文本或Markdown） |
| `language` | string | 否 | `en` | `en`英文 / `zh`中文 |

### Customize - 岗位定制

针对特定职位发布（job posting）进行定制，含差距分析与关键词优化：

**输出内容：**
- 职位描述分解（必需技能、偏好技能、职责、关键词）
- 差距分析矩阵：将每个要求映射到你的简历
- 定制化简历：关键词自然融入
- 关键词覆盖报告：优化前后对比
- 附加：求职信要点 + 面试准备笔记

**参数：**
| 参数(续)| 类型 | 必需 | 默认 | 说明 |
|:-------|-------:|:-------|:-------|-------:|
| `resume_content` | string | 是 | - | 简历文本 |
| `job_description` | string | 是 | - | 目标职位描述或职位名 |
| `language` | string | 否 | `en` | `en`英文 / `zh`中文 |

### Score - 简历评分
100分制专业评估，含具体改进建议：

**评分维度（100分）：**
| 维度 | 分值 | 评估内容 |
|---:|:---|---:|
| Content Quality | 30 | 成就、动作动词、相关性、完整性 |
| Structure & Formatting | 25 | 布局、一致性、长度、章节顺序 |
| Language & Grammar | 20 | 语法、拼写、语气、清晰度 |
| ATS Optimization | 15 | 关键词、标准标题、格式兼容性 |
| Impact & Impression | 10 | 6秒测试、职业故事、专业性 |

**等级：** A+ (95-100) → A (90-94) → B+ (85-89) → B (80-84) → C+ (75-79) → C (70-74) → D (60-69) → F (<60)

**参数：**
| 参数(续)(续)| 类型 | 必需 | 默认 | 说明 |
|:----------:|------------|:-----------|:----------:|------------|
| `resume_content` | string | 是 | - | 简历文本 |
| `target_role` | string | 否 | - | 目标职位（用于匹配度评估） |
| `language` | string | 否 | `en` | `en`英文 / `zh`中文 |

**输出**: 返回Score - 简历评分的处理结果,包含执行状态码、结果数据和执行日志.
### Export - 多格式导出

将简历转换为Word、Markdown、HTML、LaTeX或PDF格式：

**支持格式：** `word` / `markdown` / `html` / `latex` / `pdf`

**模板选择：**
| 模板 | 风格 | 适用场景 |
|----|:--:|---:|
| `professional` | 海军蓝、衬线标题、经典边框 | 金融、咨询、法律、医疗 |
| `modern` | 青色点缀、创意布局、emoji图标 | 科技、创业、产品、营销 |
| `minimal` | 单色、极简、内容密集 | 资深专业人士、工程 |
| `academic` | 正式衬线、多页、出版物 | 学术、研究、博士申请 |

**导出细节：**
- HTML：自包含文件，内嵌CSS，4种配色主题，`@media print`优化
- LaTeX：完整可编译`.tex`，支持XeLaTeX + CJK
- Word：Pandoc优化的Markdown + YAML front matter + 转换命令
- PDF：打印优化HTML，A4页面尺寸，多种转换方法
- Markdown：干净、结构化、版本控制友好

**参数：**
| 参数(续)(续)| 类型 | 必需 | 默认 | 说明 |
|--------|--------|--------|--------|--------|
| `resume_content` | string | 是 | - | 简历文本（Markdown优先） |
| `format` | string | 是 | - | `word`/`markdown`/`html`/`latex`/`pdf` |
| `template` | string | 否 | `professional` | `professional`/`modern`/`minimal`/`academic` |

### Start with Score - 评分优先工作流

推荐从评分（score）开始的完整优化流程：

1. **Score** - 了解基线分数与主要问题
2. **Polish** - 修复所有基础问题
3. **Customize** - 针对每个申请单独定制
4. **Export** - 内容完善后再格式化
5. **Score again** - 评分验证改进效果

当用户说"Here's my resume, help?"时，自动先评分再建议下一步.
#
## 使用流程

1. 准备简历文本（纯文本或Markdown格式）
2. 选择操作：polish润色 / customize定制 / score评分 / export导出
3. 可使用自然语言描述需求，也可使用斜杠命令（如 `/resume polish`）
4. Agent自动路由到正确的工作流
5. 查看结果并按建议进行修改
6. 推荐流程：score → polish → customize → export → score again

## 示例

### 示例1：评分并润色简历

```
用户: Here's my resume, what do you think?
[粘贴简历]
# ...
Agent: Resume Score: 68/100 (Grade: C)
Top 3 Issues:
1. No quantified achievements
2. Weak action verbs
3. Missing keywords for target role
# ...
Would you like me to polish it now?
# ...
用户: Yes, polish it
# ...
Agent: [运行40+检查项润色]
- 联系信息: ✅
- 个人简介: ⚠️ 需添加价值主张
- 工作经历: ❌ 缺少量化成果
[返回完全润色后的简历]
```

### 示例2：针对岗位定制

```
用户: Tailor my resume for this job:
Senior Backend Engineer at Stripe
Requirements: Go, distributed systems, payment APIs...
# ...
Agent: Job Analysis Complete
Current Match: 62% → After Optimization: 89%
- Gap Analysis: 缺少Go关键词，分布式系统经验未突出
- Customized Resume: [关键词自然融入的定制版本]
- Keyword Coverage: before 45% → after 89%
- Cover letter talking points: [附赠]
```

### 示例3：导出为PDF

```
用户: Convert my resume to PDF with modern template
# ...
Agent: 导出完成：
- 格式: PDF
- 模板: modern（青色点缀、创意布局）
- 页面: A4打印优化
- 文件: resume-modern.pdf
[提供下载路径]
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| 简历内容为空 | 未提供resume_content | 提示用户提供简历文本（纯文本或Markdown） |
| 简历超长 | 超过10,000字符 | 精简内容；分章节处理；移除冗余经历 |
| 职位描述缺失（customize） | 未提供job_description | 提示用户提供目标职位描述或职位名 |
| 导出格式不支持 | format参数错误 | 使用支持的格式：word/markdown/html/latex/pdf |
| Pandoc未安装（Word导出） | 依赖缺失 | 安装Pandoc；或先导出HTML再转换 |
| LaTeX编译失败 | LaTeX环境问题 | 检查LaTeX发行版安装；使用XeLaTeX编译；或改用HTML导出 |
| 语言参数无效 | language值错误 | 使用 `en`（英文）或 `zh`（中文） |

## 常见问题

### Q1: 应该从哪个命令开始？
A: 推荐从score开始，了解简历的基线分数与主要问题。然后polish修复基础问题，再customize针对岗位定制，最后export导出。完成后再score一次验证改进.
### Q2: 支持哪些语言？
A: 支持英文（en）和中文（zh）。英文支持US/UK规范，中文支持中英文混排规范与CJK导出。通过language参数指定.
### Q3: ATS优化是什么？
A: ATS（Applicant Tracking System）是招聘管理系统。ATS优化确保简历能被系统正确解析，包括标准标题、关键词优化、格式兼容性等。score命令会评估ATS兼容性.
### Q4: 导出PDF需要什么工具？
A: PDF导出通过打印优化的HTML实现，使用浏览器即可转换。也可使用Pandoc或wkhtmltopdf等工具。LaTeX导出需要安装LaTeX发行版（如TeX Live、MiKTeX）.
### Q5: 如何使用斜杠命令？
A: 在clawbot对话中使用 `/resume polish`、`/resume customize`、`/resume score`、`/resume export` 命令。也可使用自然语言描述需求，Agent会自动路由.
### Q6: customize和polish有什么区别？
A: polish是通用润色，运行40+检查项修复基础问题。customize是针对特定职位的定制，包含差距分析与关键词优化，每次申请不同职位都应重新customize.
## 已知限制

- 简历最大长度10,000字符，超长需精简
- 仅支持英文与中文两种语言
- LaTeX导出需要本地LaTeX环境，无环境时无法编译
- 评分基于AI评估，不同模型可能给出略有差异的分数
- PDF导出质量取决于浏览器或转换工具的渲染能力
- 无法直接编辑PDF/Word文件，需通过Markdown中间格式转换
