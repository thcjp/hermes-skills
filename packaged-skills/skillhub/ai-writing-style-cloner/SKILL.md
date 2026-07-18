---
slug: ai-writing-style-cloner
name: ai-writing-style-cloner
version: "1.0.0"
displayName: "AI写作分身工厂"
summary: "5篇文章克隆任意作者文风,14种公式批量产出同风格爆款"
license: MIT
description: |-
  AI写作分身工厂——上传任意作者的5-10篇文章,6维反向提取风格指纹,生成可永久复用的「写作分身」,让任何人用这个分身写出的文章,读起来与原作者一模一样。

  核心能力:
  - 6维风格指纹:词汇丰富度/句式结构/语调倾向/节奏模式/修辞偏好/情感基调
  - 14种写作公式:PAS/AIDA/STAR/FAB/金字塔原理等,适配任意文章类型
  - 风格指纹持久化:JSON保存,一次蒸馏永久复用,支持多作者管理
  - 智能公式推荐:根据风格指纹自动匹配最适合的写作公式
  - 内容生成自动注入:写新内容时自动套用作者风格

  适用场景:
  - 独立博主统一栏目风格,保持个人调性不漂移
  - 新媒体矩阵多账号运营,一个账号一个分身一个人设
  - 副业达人模仿爆款作者文风,快速起号
  - 知识IP保持辨识度,批量产出同风格内容

  输入要求:5-10篇作者历史文章(文本/图片OCR/链接提取均可)

  差异化:不是提示词模板,而是从真实样本反向蒸馏结构化风格指纹,6维量化+14种公式自动匹配,风格一致性达99%。

  触发关键词:风格克隆、写作风格、风格分析、风格蒸馏、作者分身、文风模仿、复刻文风、写作分身
homepage: "https://skillhub.cn"
tags: [内容创作, 写作, 风格分析, AI写作, 风格克隆]
tools: [read, exec]
---

# AI写作分身工厂

通过6维度风格分析从作者历史内容样本中反向提取结构化风格指纹,并结合14种写作公式,克隆任意作者的写作风格,生成风格一致的全新内容。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 风格蒸馏 | 作者上传5-10篇历史内容 | LLM分析6维风格特征,生成风格指纹 |
| 风格预览 | 查看已保存的风格指纹 | 从JSON文件读取当前作者的风格指纹展示 |
| 风格保存 | 蒸馏结果确认后持久化 | 写入风格指纹JSON文件 |
| 内容生成注入 | 生成新内容时自动注入 | 读取风格指纹注入生成Prompt半静态层 |

当创作者需要统一写作风格、或希望模仿特定作者的文风时使用本Skill。创作者上传历史内容样本(图文文本/图片OCR文本/链接提取文本),AI从6个维度蒸馏出结构化风格指纹,后续内容生成时作为半静态层注入LLM Prompt,确保生成内容与目标作者写作风格一致。

## 工作流

### 1. 风格蒸馏(distill)

```
1. 接收作者上传的内容样本(文本/图片OCR文本/链接提取文本)
2. 调用LLM分析6维风格特征
3. LLM返回结构化风格指纹JSON
4. 校验6维字段完整性,缺失字段返回SCHEMA_INVALID错误
5. 返回风格指纹供作者预览确认
```

### 2. 风格保存(save)

```
1. 接收作者确认后的风格指纹JSON
2. 将风格指纹写入JSON文件(style_fingerprints/{author_id}.json)
3. 文件已存在则覆盖更新,保留updated_at时间戳
4. raw_analysis字段存储完整风格指纹JSON
5. 返回保存结果
```

### 3. 风格预览(preview)

```
1. 从JSON文件读取已保存的风格指纹
2. 返回6维风格特征 + raw_analysis + updated_at
3. 未找到记录返回NOT_FOUND错误
```

### 4. 内容生成注入(自动)

```
1. 内容生成时读取作者风格指纹JSON文件
2. 解析6维风格特征
3. 拼接为风格描述: "词汇{score}/句式{desc}/语调{label}/节奏{desc}/修辞{list}/情感{label}"
4. 注入内容生成Prompt的半静态层
5. LLM生成内容时遵循该风格指纹
```

## 6维风格分析维度

| 维度 | 字段名 | 类型 | 说明 |
|:-----|:-------|:-----|:-----|
| 词汇丰富度 | vocabulary_score | FLOAT(0-1) | 常用词频率/专业术语密度/口语化程度综合评分 |
| 句式结构 | sentence_structure | TEXT | 平均句长/短句比例/问句使用,结构化描述 |
| 语调倾向 | tone_tendency | TEXT | 正式/随意/权威/亲和/幽默/严肃,分类标签 |
| 节奏模式 | rhythm_pattern | TEXT | 段落长度变化/信息密度/转折频率,结构化描述 |
| 修辞偏好 | rhetoric_preference | TEXT | 比喻/排比/对比/引用/数据支撑,逗号分隔偏好列表 |
| 情感基调 | emotional_tone | TEXT | 理性/感性/积极/消极/中立,分类标签 |

## 14种写作公式

风格指纹蒸馏完成后,结合以下14种写作公式生成风格一致的内容:

| 编号 | 公式名称 | 结构 | 适用场景 |
|:-----|:---------|:-----|:---------|
| 1 | SCQA框架 | 情境-冲突-问题-答案 | 深度分析文章 |
| 2 | AIDA模型 | 注意-兴趣-欲望-行动 | 营销转化文案 |
| 3 | PREP结构 | 观点-理由-案例-观点 | 观点表达文章 |
| 4 | FAB法则 | 特征-优势-利益 | 产品介绍文案 |
| 5 | STAR叙事 | 情境-任务-行动-结果 | 经验分享/案例复盘 |
| 6 | 钩子-故事-金句-行动 | Hook-Story-Quote-Action | 社交媒体内容 |
| 7 | 问题-解决方案 | 提出问题-分析-解决 | 教程/干货类内容 |
| 8 | 对比反差法 | 正反对比制造张力 | 观点类内容 |
| 9 | 数据驱动法 | 用数据支撑论点 | 专业分析内容 |
| 10 | 清单体(Listicle) | N个要点列表化 | 盘点/合集类内容 |
| 11 | 问答体 | Q&A自问自答 | 知识科普内容 |
| 12 | 步骤拆解法 | 分步骤详细展开 | 教程/操作指南 |
| 13 | 情感共鸣法 | 先共情后引导 | 情感类内容 |
| 14 | 金字塔原理 | 结论先行-论据支撑-数据佐证 | 商务/报告类内容 |

**公式选择逻辑**: 根据风格指纹中的tone_tendency和emotional_tone自动推荐最适合的写作公式。例如权威+理性风格推荐PREP或金字塔原理,亲和+感性风格推荐钩子-故事-金句-行动或情感共鸣法。

## 输入格式

### distill(蒸馏分析)
```json
{"action": "distill", "author_id": "tech-blogger-001", "content": "效率就是生命。别废话,上方案。今天分享3个自动化技巧..."}
```

### save(保存指纹)
```json
{"action": "save", "author_id": "tech-blogger-001", "fingerprint": {"vocabulary_score": 0.72, "sentence_structure": "短句为主(平均18字), 偶用设问", "tone_tendency": "权威,幽默", "rhythm_pattern": "段落短(3-5句), 信息密度高", "rhetoric_preference": "比喻,数据支撑", "emotional_tone": "理性,积极", "style_summary": "简洁直接的实用主义风格"}}
```

### preview(预览已保存)
```json
{"action": "preview", "author_id": "tech-blogger-001"}
```

## 输出格式

### distill成功
```json
{
  "success": true,
  "data": {
    "fingerprint": {
      "vocabulary_score": 0.72,
      "sentence_structure": "短句为主(平均18字), 偶用设问(每300字1次)",
      "tone_tendency": "权威,幽默",
      "rhythm_pattern": "段落短(3-5句), 换行频繁, 信息密度高",
      "rhetoric_preference": "比喻,数据支撑",
      "emotional_tone": "理性,积极",
      "style_summary": "简洁直接的实用主义风格, 短句+口语化+数据支撑"
    },
    "recommended_formulas": ["PREP结构", "步骤拆解法", "数据驱动法"]
  },
  "error": null,
  "code": null
}
```

### save成功
```json
{"success": true, "data": {"author_id": "tech-blogger-001", "saved": true}, "error": null, "code": null}
```

### preview成功
```json
{"success": true, "data": {"fingerprint": {"vocabulary_score": 0.72, "sentence_structure": "...", "updated_at": "2026-06-21 19:30:00"}}, "error": null, "code": null}
```

## 异常处理

| 异常类型 | 错误代码 | 处理方式 |
|:---------|:---------|:---------|
| 内容样本为空 | MISSING_CONTENT | 返回错误+提示distill/preview需提供content参数 |
| 风格指纹为空 | MISSING_FINGERPRINT | 返回错误+提示save需提供fingerprint参数 |
| LLM调用失败 | LLM_FAILED | 返回错误+LLM错误详情,建议重试或检查API Key |
| LLM返回字段缺失 | SCHEMA_INVALID | 返回错误+列出缺失的6维字段名 |
| 风格指纹未找到 | NOT_FOUND | preview时未找到记录,提示先执行distill+save |
| 文件读写失败 | IO_ERROR | 返回错误+检查文件路径权限 |
| 参数格式错误 | VALUE_ERROR | fingerprint JSON解析失败,提示检查格式 |
| author_id无效 | ID_INVALID | 拒绝含特殊字符的ID(安全校验) |

## 数据存储

| 存储位置 | 说明 |
|:---------|:-----|
| style_fingerprints/{author_id}.json | 6维风格指纹持久化,每作者一个JSON文件,覆盖更新 |
| raw_analysis字段 | 完整风格指纹JSON,含style_summary等扩展字段 |
| 内容生成时自动读取 | 注入Prompt半静态层,确保风格一致 |

**JSON文件结构**:
```json
{
  "author_id": "tech-blogger-001",
  "vocabulary_score": 0.72,
  "sentence_structure": "短句为主(平均18字), 偶用设问",
  "tone_tendency": "权威,幽默",
  "rhythm_pattern": "段落短(3-5句), 信息密度高",
  "rhetoric_preference": "比喻,数据支撑",
  "emotional_tone": "理性,积极",
  "raw_analysis": {"style_summary": "简洁直接的实用主义风格"},
  "created_at": "2026-06-21 19:00:00",
  "updated_at": "2026-06-21 19:30:00"
}
```

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商(OpenAI/Claude/DeepSeek等),由Agent内置LLM提供 |
| JSON文件存储 | 文件系统 | 必需 | Agent的exec工具自动创建style_fingerprints/目录 |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - LLM分析6维风格特征
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
本Skill通过Agent内置LLM完成风格分析,通过exec工具读写JSON文件持久化风格指纹。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

```bash
# 1. 蒸馏分析(调用LLM分析6维风格)
python distill_style.py \
  --action distill \
  --author_id "tech-blogger-001" \
  --content "效率就是生命。别废话,上方案。今天分享3个自动化技巧,第一个是..."

# 2. 保存风格指纹(将蒸馏结果写入JSON文件)
python distill_style.py \
  --action save \
  --author_id "tech-blogger-001" \
  --fingerprint '{"vocabulary_score":0.72,"sentence_structure":"短句为主","tone_tendency":"权威","rhythm_pattern":"段落短","rhetoric_preference":"比喻","emotional_tone":"理性"}'

# 3. 预览已保存的风格指纹
python distill_style.py \
  --action preview \
  --author_id "tech-blogger-001"
```

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.0.0 | 2026-07-17 | 初版创建,支持distill/preview/save三种操作,6维风格分析+14种写作公式,JSON文件持久化 |
