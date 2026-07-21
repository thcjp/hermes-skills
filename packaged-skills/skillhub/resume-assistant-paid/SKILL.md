---
slug: resume-assistant-paid
name: resume-assistant-paid
version: "1.0.0"
displayName: 简历助手工具(专业版)
summary: 求职全流程套件,含岗位定制、JD分析、5格式导出、4模板与详细评分。
license: Proprietary
edition: pro
description: |-
  简历助手工具(专业版)面向求职者与招聘方,提供完整的简历润色、岗位定制、多格式导出与专业评分能力。核心能力:
  - 4大命令:润色 / 岗位定制 / 多格式导出 / 详细评分
  - 5种导出格式:Word / Markdown / HTML / LaTeX / PDF
  - 4种专业模板:professional / modern / minimal / academic
  - JD分析与关键词优化,匹配度从62%提升至89%
  - 100分制详细评分与岗位匹配度评估

  适用场景:
  - 针对具体岗位定制简历
  - 多格式投递(在...
tags:
- Development
- 求职
- 简历
- 企业级
- 文档
- 多格式
tools:
  - - read
- exec
---
# 简历助手工具(专业版)

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
| --- | --- | --- |
| 简历润色 | 40+项清单审查,8大类别 | 与免费版一致 |
| 基础评分 | 100分制,5维度 | 与免费版一致 |
| 岗位定制 | JD分析+差距分析+关键词优化 | 免费版无 |
| 详细评分 | 评分+岗位匹配度+竞争力百分位 | 免费版仅基础评分 |
| 多格式导出 | Word/Markdown/HTML/LaTeX/PDF | 免费版仅Markdown |
| 多模板 | 4种专业模板 | 免费版无 |
| JD分析 | 必需技能/偏好技能/职责/关键词 | 免费版无 |
| 面试要点 | 附赠面试要点与求职信要点 | 免费版无 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。
### 简历润色

执行简历润色操作,处理用户输入并返回结果。

**输入**: 用户提供简历润色所需的参数和指令。

**输出**: 返回简历润色的处理结果。
### 基础评分

执行基础评分操作,处理用户输入并返回结果。

**输入**: 用户提供基础评分所需的参数和指令。

**输出**: 返回基础评分的处理结果。


## 适用场景

### 场景一:针对具体岗位定制简历

用户针对某岗位JD定制简历,工具进行差距分析与关键词优化。

```text
用户: 针对以下岗位定制我的简历:
高级后端工程师 | 某支付公司
要求:Go、分布式系统、支付API...

工具: 🎯 岗位分析完成
📊 当前匹配度: 62% → 优化后: 89%

JD拆解:
- 必需技能: Go, 分布式系统, 支付API, 微服务
- 偏好技能: Kubernetes, gRPC, 消息队列
- 关键职责: 支付系统设计、性能优化、稳定性保障
- 关键词: 高并发、最终一致、对账、风控

差距分析矩阵:
| 要求 | 你的简历 | 状态 |
| --- | --- | --- |
| Go | 有(2年) | ✅ |
| 分布式系统 | 有(微服务) | ✅ |
| 支付API | 无显式提及 | ⚠️ 建议补充 |
| 高并发 | 有(QPS提升) | ✅ |

[输出定制后简历,关键词自然融入]

关键词覆盖报告:
优化前: 60% → 优化后: 89%

附赠:
- 求职信要点
- 面试准备要点
```

### 场景二:多格式导出与多模板

用户根据投递场景选择格式与模板。

```text
用户: 把简历导出为PDF,使用modern模板

工具: [生成PDF,采用modern模板]
- HTML自包含文件,嵌入CSS,4种配色主题
- @media print 优化,适合打印
- A4页面尺寸
```

格式与模板选择:

| 格式 | 特点 | 适用场景 |
| --- | --- | --- |
| Word | Pandoc优化,带YAML front matter | 在线投递(可编辑) |
| Markdown | 结构化,版本控制友好 | 工作格式 |
| HTML | 自包含,4种配色主题 | 在线作品集 |
| LaTeX | XeLaTeX+CJK支持 | 学术申请 |
| PDF | A4优化,多转换方法 | 正式投递 |

| 模板 | 风格 | 适用 |
| --- | --- | --- |
| professional | 海军蓝、衬线标题、经典边框 | 金融/咨询/法律/医疗 |
| modern | 青色强调、创意布局、emoji图标 | 科技/初创/产品/市场 |
| minimal | 单色、极简、内容密集 | 资深人士/工程 |
| academic | 正式衬线、多页、出版物 | 教职/研究/博士申请 |

### 场景三:详细评分与岗位匹配度

用户希望了解简历针对目标岗位的匹配度与竞争力。

```text
用户: 评估我的简历,目标岗位:高级前端工程师

工具: 📊 简历评分: 82/100 (等级: B)

评分明细:
| 维度 | 分数 | 说明 |
| --- | --- | --- |
| 内容质量 | 26/30 | 量化成果充分 |
| 结构格式 | 22/25 | 章节顺序合理 |
| 语言语法 | 18/20 | 时态统一 |
| ATS优化 | 13/15 | 关键词覆盖87% |
| 印象冲击 | 3/10 | 缺少记忆点 |

优势:
1. ✅ 工作经历量化充分(性能提升35%)
2. ✅ 技术栈完整,匹配度高
3. ✅ 倒序排列,格式专业

优先改进(附Before→After改写):
1. 🔴 个人简介缺少差异化
   Before: 5年前端经验
   After: 5年前端经验,主导3个百万级DAU产品首屏优化
2. 🟡 补充技术领导力证据

岗位匹配度:
- 匹配度: 87/100
- 竞争力百分位: 75%(优于75%的同类简历)
- 优势: React生态深度、性能优化
- 差距: 团队管理经验

5步行动计划(含工作量估算):
1. 补充个人简介差异化(15分钟)
2. 添加团队领导经历(30分钟)
3. 补充开源贡献(1小时)
4. 优化技能分组(20分钟)
5. 导出PDF投递(5分钟)
```

## 使用流程

### 1. 推荐工作流

```text
┌──────────────────────────────────────────────────┐
│           推荐工作流(PRO版完整版)              │
├──────────────────────────────────────────────────┤
│  1. /resume score     ← 了解现状                │
│     "评估我的简历"                              │
│          │                                      │
│          ▼                                      │
│  2. /resume polish    ← 修复基础问题            │
│     "润色我的简历"                              │
│          │                                      │
│          ▼                                      │
│  3. /resume customize ← 针对岗位定制            │
│     "针对这个JD定制: [粘贴JD]"                 │
│          │                                      │
│          ▼                                      │
│  4. /resume export    ← 导出最终文件            │
│     "导出为PDF,使用modern模板"                │
│          │                                      │
│          ▼                                      │
│  5. /resume score     ← 验证改进                │
│     "重新评估"                                  │
└──────────────────────────────────────────────────┘
```

### 2. 命令参考

| 命令 | 参数 | 输出 |
| --- | --- | --- |
| `/resume polish` | resume_content, language | 40+项清单+润色版本 |
| `/resume customize` | resume_content, job_description, language | JD分析+定制版本 |
| `/resume export` | resume_content, format, template | 对应格式文件 |
| `/resume score` | resume_content, target_role, language | 100分评分+匹配度 |

### 3. 集成方式

#### 自然语言(推荐)

```text
"针对这个岗位定制简历: [JD]"
"导出为PDF,使用professional模板"
"评估并告诉我与高级前端岗位的匹配度"
```

#### REST API

```bash
curl -X POST https://your-agent-api.com/skills/resume-assistant/customize \
  -H "Content-Type: application/json" \
  -d '{
    "resume_content": "简历内容...",
    "job_description": "JD内容...",
    "language": "zh"
  }'

curl -X POST https://your-agent-api.com/skills/resume-assistant/export \
  -H "Content-Type: application/json" \
  -d '{
    "resume_content": "简历内容...",
    "format": "pdf",
    "template": "modern"
  }'
```

#### LangChain集成

```python
from langchain.tools import Tool

resume_tools = [
    Tool(
        name="resume_customize",
        description="针对具体岗位定制简历,含JD分析与关键词优化",
        func=lambda input: agent.run_skill(
            "resume-assistant", "customize",
            {"resume_content": input.split("---JD---")[0],
             "job_description": input.split("---JD---")[1]}
        )
    ),
    Tool(
        name="resume_export",
        description="导出简历为Word/Markdown/HTML/LaTeX/PDF",
        func=lambda input: agent.run_skill(
            "resume-assistant", "export",
            {"resume_content": input, "format": "pdf", "template": "modern"}
        )
    ),
]
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **LaTeX环境**: XeLaTeX(LaTeX导出需要)
- **浏览器**: 现代浏览器(HTML导出与PDF打印)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Pandoc | 命令行工具 | 可选 | pandoc.org 下载(Word/LaTeX转换) |
| XeLaTeX | 排版系统 | 可选 | TeX Live / MacTeX / MiKTeX(LaTeX导出) |
| wkhtmltopdf | 命令行工具 | 可选 | wkhtmltopdf.org 下载(PDF转换) |
| Python | 运行时 | 可选 | python.org 下载(批量处理脚本) |

### API Key 配置

- 。
- 简历内容本地处理,不上传外部服务。
- 若通过REST API集成,需按所在Agent平台配置访问令牌。

### 可用性分类

- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。PRO版面向求职全流程,提供岗位定制、多格式导出、多模板与详细评分能力,完全兼容免费版润色与基础评分。


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 完整配置

| 键 | 值 | 说明 |
| --- | --- | --- |
| `max_resume_length` | 10000字符 | 最大输入长度 |
| `supported_languages` | en, zh | 支持语言 |
| `supported_export_formats` | word, markdown, html, latex, pdf | 导出格式 |
| `supported_templates` | professional, modern, minimal, academic | 模板 |

### 模板项目结构

```text
templates/
├── professional.md      # 经典企业模板
├── modern.md            # 现代科技模板
├── minimal.md           # 极简资深模板
├── academic.md          # 学术CV模板
└── export/
    ├── resume.html      # HTML模板(4种CSS主题)
    └── resume.tex       # LaTeX模板(XeLaTeX+CJK)
```

### LaTeX导出示例

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[UTF8]{ctex}
\usepackage{geometry}
\geometry{margin=2cm}

\title{张三 \\ 高级前端工程师}
\date{}

\begin{document}
\maketitle

\section*{个人简介}
5年前端开发经验,主导多个百万级DAU产品...

\section*{工作经历}
\subsection*{高级前端工程师 | ABC科技 | 2022-至今}
\begin{itemize}
  \item 主导React 18升级,首屏性能提升35\%
\end{itemize}
\end{document}
```

## 常见问题

### Q1:PRO版与免费版如何共存?

两者润色与基础评分完全兼容,PRO版包含免费版全部能力。求职者升级时直接替换Skill文件,已有简历内容无需重新整理。

### Q2:LaTeX导出需要什么环境?

需要安装 XeLaTeX(支持CJK)。常用发行版:TeX Live(跨平台)、MacTeX(macOS)、MiKTeX(Windows)。HTML导出无需额外环境。

### Q3:PDF导出如何实现?

提供多种转换方法:HTML → 浏览器打印为PDF、Pandoc + LaTeX、wkhtmltopdf 等。建议优先用HTML + 浏览器打印,最可控。

### Q4:岗位定制会改变我的经历吗?

不会。岗位定制只调整表达方式与关键词融入,不会虚构经历。差距分析会明确指出哪些要求你尚未满足,建议如实补充或学习。

### Q5:支持中英双语简历吗?

支持。可生成纯中文、纯英文或中英对照简历。CJK导出在LaTeX中通过 `ctex` 包支持,在HTML中通过UTF-8编码支持。

### Q6:能批量优化多份简历吗?

可以。通过REST API或LangChain集成,可批量为多个目标岗位生成定制简历。建议为每个岗位维护独立Markdown源文件,避免混淆。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
