---
slug: pptx-presentation-pro
name: pptx-presentation-pro
version: 1.0.1
displayName: 演示文稿大师
summary: "从大纲到专业PPT一键生成,布局模板图表母版全流程演示文稿处理。演示文稿大师全面处理PowerPoint演示文稿,核心功能包括从大纲生成PPT、读取编辑现有PPT、模板与母版应用、数据图表可"
license: Proprietary
description: 演示文稿大师全面处理PowerPoint演示文稿,核心功能包括从大纲生成PPT、读取编辑现有PPT、模板与母版应用、数据图表可视化、批量参数化生成。适用于商业汇报、产品发布、教学课件、培训演示、会议演讲场景。触发关键词:PPT、PowerPoint、演示文稿、幻灯片、pptx、演讲、汇报、课件、母版、幻灯片模板。
tags: 演示文稿,幻灯片,商业汇报,工具,pptx,ppt
tools:
  - read
  - exec
  - write
category: "Automation"
---
# 演示文稿大师

全面处理 PowerPoint 演示文稿。从读取现有 PPT 到从零生成专业演示,覆盖布局、模板、图表、母版全流程。

## 核心能力

1. **内容规划与大纲生成**:接收演讲主题/受众/时长/目的(说服/汇报/教学),生成大纲(封面→议程→核心内容3-7要点→总结→Q&A),每页一个核心观点避免信息过载,输出结构化大纲供用户确认。
2. **设计规范制定**:尺寸选择(16:9 1920x1080或4:3 1024x768),主题配色(主色+辅色+强调色,限制3-5色),字体规范(标题36pt/正文24pt/注释18pt),母版设计(封面/内容/章节/结束四种母版)。
3. **幻灯片生成**:封面页(标题+副标题+作者+日期)、议程页(章节导航)、内容页(标题+要点列表/图文混排/数据图表/对比表格)、章节过渡页、总结页(核心要点回顾+行动号召)、结束页(感谢+联系方式)。
4. **视觉优化**:布局原则(留白充足/对齐一致/视觉层级清晰),图表规范(数据来源标注/坐标轴清晰/颜色一致/关键数据高亮),动画过渡(适度使用不分散注意力)。
5. **输出与交付**:生成可编辑.pptx文件,导出PDF(固定格式分享),演讲者备注(每页备注栏填写演讲要点),版本管理(保留可编辑源文件)。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 从零生成 | 演讲主题+受众+时长 | 大纲→自动生成PPT,输出到`output/{name}/presentation.pptx` |
| 现有PPT编辑 | 已有.pptx文件+修改需求 | 读取/调整/输出修改后的PPT |
| 模板应用 | 品牌风格规范+PPT内容 | 应用母版/主题/配色的统一风格PPT |
| 数据图表 | Excel数据+展示需求 | 数据可视化PPT(柱状/折线/饼图),输出到`output/{name}/` |
| 批量生成 | 参数化模板+多组数据 | 批量生成的系列演示文稿 |

**不适用于**:
- 复杂动画演示(如Keynote级动画效果,本工具动画有限)
- 交互式演示(如包含超链接跳转的复杂交互课件)
- 视频编辑合成(请用remotion-video-studio)
- 3D模型展示(PPT对3D支持有限)

## 使用流程

### Step 1: 内容规划
1. 接收主题与目标:演讲主题、受众、时长、目的(说服/汇报/教学)
2. 生成大纲:封面→议程→核心内容(3-7个要点)→总结→Q&A,每页一个核心观点
3. 确认大纲:输出结构化大纲供用户确认

### Step 2: 设计规范制定
1. 尺寸选择:16:9(1920x1080)或4:3(1024x768)
2. 主题配色:主色+辅色+强调色,限制3-5色
3. 字体规范:标题字体+正文字体,字号层级(标题36pt/正文24pt/注释18pt)
4. 母版设计:封面母版/内容母版/章节母版/结束母版

### Step 3: 幻灯片生成
1. 封面页:标题+副标题+作者+日期,视觉冲击力
2. 议程页:列出主要章节,清晰的导航
3. 内容页:标题+要点列表(3-5个)、图文混排、数据图表(柱状/折线/饼图)、对比表格
4. 章节过渡页:章节标题,视觉分隔
5. 总结页:核心要点回顾+行动号召
6. 结束页:感谢+联系方式

### Step 4: 视觉优化
1. 布局原则:留白充足不拥挤、对齐一致、视觉层级清晰
2. 图表规范:数据来源标注、坐标轴清晰、颜色与主题一致、关键数据高亮
3. 动画过渡:适度使用,不分散注意力

### Step 5: 输出与交付
1. 生成.pptx文件:可编辑的PowerPoint文件
2. 导出PDF:分享用,固定格式
3. 演讲者备注:每页备注栏填写演讲要点
4. 版本管理:保留可编辑源文件

## 示例

### 示例1: 从大纲生成产品发布PPT

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 演示文稿大师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
主题: 新产品"智能助手X"发布
受众: 投资人和媒体
时长: 15分钟
目的: 说服投资价值
大纲: 封面→市场痛点→产品介绍→核心功能→技术优势→商业模式→团队→融资计划→Q&A
```

**输出** (`output/product-launch/presentation.pptx`):
生成脚本 (`output/product-launch/generate.js`):
```javascript
const PptxGenJS = require("pptxgenjs");
const pptx = new PptxGenJS();
// ...
pptx.defineLayout({ name: "CUSTOM", width: 13.33, height: 7.5 });
pptx.layout = "CUSTOM";
// ...
// 定义主题
const theme = {
  primary: "1A2B3C",
  accent: "FF6B35",
  bg: "FFFFFF",
  text: "333333",
};
// ...
// 封面页
const slide1 = pptx.addSlide();
slide1.background = { color: theme.primary };
slide1.addText("智能助手X", { x: 1, y: 2.5, w: 11, h: 1.5, fontSize: 44, color: "FFFFFF", bold: true });
slide1.addText("重新定义AI助手", { x: 1, y: 4, w: 11, h: 0.8, fontSize: 24, color: theme.accent });
slide1.addText("2024年产品发布会", { x: 1, y: 5.5, w: 11, h: 0.5, fontSize: 18, color: "CCCCCC" });
// ...
// 市场痛点页
const slide2 = pptx.addSlide();
slide2.addText("市场痛点", { x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true });
slide2.addText([
  { text: "效率低下: 80%用户每天浪费2小时在重复任务\n", options: { fontSize: 24, color: theme.text } },
  { text: "成本高昂: 现有方案月费超500元\n", options: { fontSize: 24, color: theme.text } },
  { text: "体验差: 学习曲线陡峭,上手困难", options: { fontSize: 24, color: theme.text } },
], { x: 0.5, y: 1.5, w: 12, h: 4, valign: "top" });
// ...
// 数据图表页
const slide3 = pptx.addSlide();
slide3.addText("市场增长趋势", { x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true });
slide3.addChart(pptx.ChartType.line, [{
  name: "市场规模(亿元)",
  labels: ["2021", "2022", "2023", "2024E", "2025E"],
  values: [120, 180, 280, 420, 600],
}], { x: 1, y: 1.5, w: 11, h: 5, showValue: true });
// ...
pptx.writeFile({ fileName: "output/product-launch/presentation.pptx" });
```

### 示例2: 数据报表PPT生成

**输入**:
```
将季度销售数据生成PPT,包含柱状图(各产品线销售额)和饼图(区域分布)。
数据: 产品A 1.2亿, 产品B 0.8亿, 产品C 0.5亿; 华东40%, 华北25%, 华南20%, 其他15%
```

**输出** (`output/sales-report/presentation.pptx`):
```python
# 使用python-pptx生成
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
# ...
prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)
# ...
# 柱状图页
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "各产品线销售额"
chart_data = CategoryChartData()
chart_data.categories = ["产品A", "产品B", "产品C"]
chart_data.add_series("销售额(亿元)", (1.2, 0.8, 0.5))
slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(1), Inches(2), Inches(6), Inches(4), chart_data)
# ...
# 饼图页
slide2 = prs.slides.add_slide(prs.slide_layouts[5])
slide2.shapes.title.text = "区域销售分布"
pie_data = CategoryChartData()
pie_data.categories = ["华东", "华北", "华南", "其他"]
pie_data.add_series("占比", (40, 25, 20, 15))
slide2.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(1), Inches(2), Inches(6), Inches(4), pie_data)
# ...
prs.save("output/sales-report/presentation.pptx")
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| PptxGenJS安装失败 | 网络问题或Node.js版本低 | 用cnpm安装,Node.js 18+ |
| 中文字体显示异常 | 系统缺少中文字体 | 指定中文字体(微软雅黑/思源黑体),或嵌入字体 |
| 图表数据格式错误 | 数据类型不匹配或缺失 | 校验数据格式,数值型数据不能传字符串 |
| PPT文件过大 | 高清图片或过多动画 | 压缩图片(建议<500KB/张),减少动画效果 |
| 读取PPT失败 | 文件损坏或格式不支持 | 确认文件为.pptx(非.ppt旧格式),用Office修复后重试 |
| 母版应用错乱 | 母版布局与内容不匹配 | 先确认母版占位符,再填充内容 |
| PDF导出失真 | 字体或布局在PDF中变化 | 导出前用PowerPoint检查,嵌入字体,固定布局 |
| 批量生成内存溢出 | 一次生成过多PPT | 分批生成,每次不超过50个,生成后释放资源 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:---:|:---:|:---:|:---:|:---:|
| Node.js 18+ | 运行时 | 可选 | PptxGenJS运行环境 | Node.js官网,国内用cnpm/nvm镜像 |
| PptxGenJS | 库 | 可选 | `npm install pptxgenjs` | `cnpm install pptxgenjs` |
| Python 3.8+ | 运行时 | 可选 | python-pptx运行环境 | Python官网下载 |
| python-pptx | 库 | 可选 | `pip install python-pptx` | 清华源:`-i https://pypi.tuna.tsinghua.edu.cn/simple` |
| LibreOffice | 工具 | 可选 | PDF导出(PPT→PDF转换) | Linux用apt,macOS用brew |
| 中文字体 | 资源 | 推荐 | 思源黑体/微软雅黑 | 开源思源字体(google fonts) |
| LLM API | API | 可选 | 由Agent内置LLM提供内容生成 | 国内Agent(通义/文心/智谱)均可 |

### API Key 配置
- **本Skill无需额外API Key配置**: 纯本地PPT生成
- **安全要求**: API Key零暴露,不写入文档、不输出到日志、不硬编码到代码中

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于运行PptxGenJS/python-pptx

## 设计原则

1. **一页一观点**:不要在单页塞过多信息
2. **视觉优先**:图胜于表,表胜于文
3. **一致性**:全篇风格统一(字体/配色/布局)
4. **可读性**:后排观众也能看清(字号>=24pt)
5. **少即是多**:克制装饰,突出内容

## 输出规范

- PPT文件:`output/{presentation-name}/presentation.pptx`
- PDF导出:`output/{presentation-name}/export.pdf`
- 大纲:`output/{presentation-name}/outline.md`
- 演讲备注:`output/{presentation-name}/speaker-notes.md`

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 季度业务汇报PPT(含数据图表+演讲备注)

**输入**:
```
主题: 2024年Q3业务汇报
受众: 公司管理层
时长: 20分钟
目的: 汇报业绩+申请Q4预算
数据:
- 营收: Q1 800万, Q2 1200万, Q3 1850万
- 用户增长: Q1 5万, Q2 12万, Q3 28万
- 产品线: 企业版60%, 标准版30%, 基础版10%
```

**LLM生成输出** (`output/q3-report/outline.md`):
```markdown
# 2024年Q3业务汇报 - 大纲
# ...
## 幻灯片结构(12页)
1. 封面页: Q3业务汇报 + 汇报人 + 日期
2. 议程页: 业绩概览 → 增长分析 → 产品表现 → 挑战与对策 → Q4规划
3. 业绩概览: Q3营收1850万,环比增长54%
4. 营收趋势图: Q1-Q3季度营收柱状图
5. 用户增长曲线: Q1-Q3用户增长折线图
6. 产品线分布: 企业版/标准版/基础版占比饼图
7. 关键成就: 3个核心里程碑
8. 挑战分析: 获客成本上升+竞品压力
9. 对策方案: 渠道优化+产品差异化
10. Q4规划: 目标+策略+预算需求
11. 总结: 核心要点回顾+行动号召
12. Q&A: 感谢+联系方式
# ...
## 配色方案
- 主色: #1A2B3C(深蓝)
- 强调色: #FF6B35(橙色)
- 背景: #FFFFFF(白色)
- 文字: #333333(深灰)
# ...
## 字体规范
- 标题: 36pt 微软雅黑 加粗
- 正文: 24pt 微软雅黑
- 注释: 18pt 微软雅黑
```

**LLM生成输出** (`output/q3-report/generate.js`):
```javascript
const PptxGenJS = require("pptxgenjs");
const pptx = new PptxGenJS();
// ...
pptx.defineLayout({ name: "WIDE", width: 13.33, height: 7.5 });
pptx.layout = "WIDE";
// ...
const theme = {
  primary: "1A2B3C",
  accent: "FF6B35",
  bg: "FFFFFF",
  text: "333333",
  light: "CCCCCC",
};
// ...
// Slide 1: 封面
const s1 = pptx.addSlide();
s1.background = { color: theme.primary };
s1.addText("2024年Q3业务汇报", {
  x: 1, y: 2.5, w: 11, h: 1.2, fontSize: 44, color: "FFFFFF", bold: true, fontFace: "微软雅黑",
});
s1.addText("持续高速增长 突破历史新高", {
  x: 1, y: 3.8, w: 11, h: 0.8, fontSize: 24, color: theme.accent, fontFace: "微软雅黑",
});
s1.addText("汇报人: 张明  |  2024年10月15日", {
  x: 1, y: 5.5, w: 11, h: 0.5, fontSize: 18, color: theme.light, fontFace: "微软雅黑",
});
// ...
// Slide 2: 议程
const s2 = pptx.addSlide();
s2.addText("议程", {
  x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
});
s2.addText([
  { text: "1. 业绩概览\n", options: { fontSize: 24, color: theme.text, fontFace: "微软雅黑" } },
  { text: "2. 增长分析\n", options: { fontSize: 24, color: theme.text, fontFace: "微软雅黑" } },
  { text: "3. 产品表现\n", options: { fontSize: 24, color: theme.text, fontFace: "微软雅黑" } },
  { text: "4. 挑战与对策\n", options: { fontSize: 24, color: theme.text, fontFace: "微软雅黑" } },
  { text: "5. Q4规划与预算", options: { fontSize: 24, color: theme.text, fontFace: "微软雅黑" } },
], { x: 1, y: 1.5, w: 11, h: 5, valign: "top", lineSpacing: 40 });
// ...
// Slide 4: 营收趋势柱状图
const s4 = pptx.addSlide();
s4.addText("季度营收趋势(万元)", {
  x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
});
s4.addChart(pptx.ChartType.bar, [{
  name: "营收(万元)",
  labels: ["Q1", "Q2", "Q3"],
  values: [800, 1200, 1850],
}], {
  x: 1, y: 1.5, w: 11, h: 5,
  showValue: true,
  showLegend: false,
  chartColors: [theme.accent],
  catAxisLabelColor: theme.text,
  valAxisLabelColor: theme.text,
  dataLabelColor: "FFFFFF",
  dataLabelFontSize: 14,
});
s4.addText("数据来源: 财务部 2024年Q3报表", {
  x: 0.5, y: 6.8, w: 12, h: 0.4, fontSize: 12, color: theme.light, fontFace: "微软雅黑",
});
// ...
// Slide 5: 用户增长折线图
const s5 = pptx.addSlide();
s5.addText("用户增长趋势(万人)", {
  x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
});
s5.addChart(pptx.ChartType.line, [{
  name: "用户数(万)",
  labels: ["Q1", "Q2", "Q3"],
  values: [5, 12, 28],
}], {
  x: 1, y: 1.5, w: 11, h: 5,
  showValue: true,
  showLegend: false,
  chartColors: [theme.primary],
  lineSize: 3,
  lineDataSymbolSize: 10,
  catAxisLabelColor: theme.text,
  valAxisLabelColor: theme.text,
});
// ...
// Slide 6: 产品线分布饼图
const s6 = pptx.addSlide();
s6.addText("产品线营收占比", {
  x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
});
s6.addChart(pptx.ChartType.pie, [{
  name: "产品线占比",
  labels: ["企业版", "标准版", "基础版"],
  values: [60, 30, 10],
}], {
  x: 2, y: 1.5, w: 9, h: 5,
  showLegend: true,
  legendPos: "r",
  showValue: true,
  dataLabelColor: "FFFFFF",
  dataLabelFontSize: 14,
});
// ...
// 演讲备注
s4.addNotes("Q3营收1850万,环比增长54%。重点强调Q3增速远超Q2的50%。企业版贡献主要营收增长,占比从50%提升至60%。");
s5.addNotes("用户数Q3达28万,环比增长133%。增长主要来自企业版直销渠道和合作伙伴渠道。获客成本从Q2的320元降至280元。");
s6.addNotes("企业版60%占比是健康的产品结构,说明产品在企业市场获得认可。Q4计划进一步提升企业版占比至65%。");
// ...
pptx.writeFile({ fileName: "output/q3-report/presentation.pptx" });
```

**效果验证**: ✓大纲结构完整(封面+议程+内容+总结+Q&A) ✓三种图表类型(柱状图/折线图/饼图) ✓配色字体一致(主题色+微软雅黑) ✓数据来源标注 ✓演讲备注填写

### 案例2: 教学课件PPT(结构化内容+对比表格)

**输入**:
```
主题: Python装饰器入门
受众: 编程初学者
时长: 30分钟
目的: 教学
内容: 装饰器概念、基本语法、常用场景、实战示例
```

**LLM生成输出** (`output/python-decorator/generate.js`):
```javascript
const PptxGenJS = require("pptxgenjs");
const pptx = new PptxGenJS();
pptx.defineLayout({ name: "WIDE", width: 13.33, height: 7.5 });
pptx.layout = "WIDE";
// ...
const theme = {
  primary: "2D5BFF",
  accent: "00C896",
  bg: "F8F9FA",
  text: "2C3E50",
  code: "1E1E1E",
};
// ...
// Slide 1: 封面
const s1 = pptx.addSlide();
s1.background = { color: theme.primary };
s1.addText("Python装饰器入门", {
  x: 1, y: 2.5, w: 11, h: 1.2, fontSize: 44, color: "FFFFFF", bold: true, fontFace: "微软雅黑",
});
s1.addText("从概念到实战,30分钟掌握装饰器", {
  x: 1, y: 4, w: 11, h: 0.8, fontSize: 24, color: theme.accent, fontFace: "微软雅黑",
});
s1.addText("讲师: 李老师  |  Python进阶课程", {
  x: 1, y: 5.5, w: 11, h: 0.5, fontSize: 18, color: "CCCCCC", fontFace: "微软雅黑",
});
// ...
// Slide 2: 什么是装饰器
const s2 = pptx.addSlide();
s2.background = { color: theme.bg };
s2.addText("什么是装饰器?", {
  x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
});
s2.addText([
  { text: "装饰器本质", options: { fontSize: 28, color: theme.accent, bold: true, fontFace: "微软雅黑", breakLine: true } },
  { text: "装饰器是一个函数,接收一个函数作为参数,返回一个新函数\n", options: { fontSize: 22, color: theme.text, fontFace: "微软雅黑", breakLine: true } },
  { text: "\n核心作用", options: { fontSize: 28, color: theme.accent, bold: true, fontFace: "微软雅黑", breakLine: true } },
  { text: "在不修改原函数代码的前提下,增加额外功能", options: { fontSize: 22, color: theme.text, fontFace: "微软雅黑" } },
], { x: 0.5, y: 1.5, w: 12, h: 5, valign: "top", lineSpacing: 36 });
// ...
// Slide 3: 代码示例(深色背景模拟代码块)
const s3 = pptx.addSlide();
s3.background = { color: theme.code };
s3.addText("基本语法", {
  x: 0.5, y: 0.3, w: 12, h: 0.6, fontSize: 28, color: "00FF88", bold: true, fontFace: "Consolas",
});
s3.addText(
  `# 定义装饰器\ndef my_decorator(func):\n    def wrapper(*args, **kwargs):\n        print("函数执行前")\n        result = func(*args, **kwargs)\n        print("函数执行后")\n        return result\n    return wrapper\n\n# 使用装饰器\n@my_decorator\ndef say_hello(name):\n    print(f"Hello, {name}!")\n\nsay_hello("Python")`,
  {
    x: 0.5, y: 1.2, w: 12, h: 5.5, fontSize: 16, color: "D4D4D4", fontFace: "Consolas",
    align: "left", valign: "top", lineSpacing: 22,
  }
);
// ...
// Slide 4: 常用场景对比表
const s4 = pptx.addSlide();
s4.background = { color: theme.bg };
s4.addText("装饰器常用场景", {
  x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
});
s4.addTable([
  [{ text: "场景", options: { bold: true, color: "FFFFFF", fill: { color: theme.primary } } },
   { text: "装饰器", options: { bold: true, color: "FFFFFF", fill: { color: theme.primary } } },
   { text: "作用", options: { bold: true, color: "FFFFFF", fill: { color: theme.primary } } }],
  ["日志记录", "@log", "自动记录函数调用参数和返回值"],
  ["性能计时", "@timer", "测量函数执行时间"],
  ["权限校验", "@require_auth", "验证用户权限后再执行"],
  ["缓存", "@cache", "缓存函数结果,避免重复计算"],
  ["重试", "@retry", "失败时自动重试指定次数"],
], {
  x: 0.5, y: 1.5, w: 12, h: 4,
  fontSize: 18, fontFace: "微软雅黑", color: theme.text,
  border: { type: "solid", color: theme.light, pt: 1 },
  colW: [3, 3, 6],
});
// ...
pptx.writeFile({ fileName: "output/python-decorator/presentation.pptx" });
```

**效果验证**: ✓教学结构清晰(概念→语法→场景→实战) ✓代码块深色背景模拟IDE ✓对比表格含5个常用场景 ✓配色适合教学(蓝+绿+代码黑) ✓字体规范(标题36pt/正文22pt/代码16pt)

### 案例3: 读取现有PPT并修改内容

**输入**:
```
已有PPT: output/template/company-template.pptx
修改需求:
1. 将第3页标题"2023年总结"改为"2024年Q3总结"
2. 第5页添加一行文字"同比增长54%"
3. 全局将旧Logo图片替换为新Logo
技术: 使用python-pptx
```

**LLM生成输出** (`output/template/modify.py`):
```python
from pptx import Presentation
from pptx.util import Inches, Pt
import os
# ...
# 读取现有PPT
pptx_path = "output/template/company-template.pptx"
prs = Presentation(pptx_path)
# ...
print(f"读取PPT: {pptx_path}")
print(f"幻灯片数量: {len(prs.slides)}")
# ...
# 需求1: 修改第3页标题
slide3 = prs.slides[2]  # 0-indexed
for shape in slide3.shapes:
    if shape.has_text_frame:
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                if "2023年总结" in run.text:
                    run.text = run.text.replace("2023年总结", "2024年Q3总结")
                    print(f"已修改第3页标题: 2023年总结 → 2024年Q3总结")
# ...
# 需求2: 第5页添加文字
slide5 = prs.slides[4]
left = Inches(1)
top = Inches(5.5)
width = Inches(8)
height = Inches(0.8)
text_box = slide5.shapes.add_textbox(left, top, width, height)
text_frame = text_box.text_frame
p = text_frame.paragraphs[0]
run = p.add_run()
run.text = "同比增长54%"
run.font.size = Pt(28)
run.font.bold = True
run.font.color.rgb = None  # 使用默认颜色
run.font.name = "微软雅黑"
print("已在第5页添加: 同比增长54%")
# ...
# 需求3: 全局替换Logo图片
old_logo = "old-logo.png"
new_logo = "new-logo.png"
logo_count = 0
# ...
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.shape_type == 13:  # PICTURE
            # 检查是否为旧Logo(通过图片名或尺寸判断)
            if shape.name and "logo" in shape.name.lower():
                # 记录原位置和尺寸
                left = shape.left
                top = shape.top
                width = shape.width
                height = shape.height
# ...
                # 删除旧图片
                sp = shape._element
                sp.getparent().remove(sp)
# ...
                # 添加新图片到相同位置
                slide.shapes.add_picture(
                    new_logo, left, top, width, height
                )
                logo_count += 1
# ...
print(f"已替换Logo图片: {logo_count}处")
# ...
# 保存修改后的PPT
output_path = "output/template/company-template-modified.pptx"
prs.save(output_path)
print(f"已保存修改后的PPT: {output_path}")
```

**效果验证**: ✓成功读取现有PPT(slide数量输出) ✓第3页标题精确替换(遍历runs) ✓第5页文字添加(指定位置+字体) ✓全局Logo替换(保留位置尺寸) ✓修改日志输出可追踪

### 案例4: 批量参数化生成PPT

**输入**:
```
需求: 为10个销售区域生成季度业绩PPT
模板: 统一布局,变量为{区域名}、{销售额}、{增长率}、{排名}
数据源:
- 华东, 1850万, 54%, 1
- 华北, 1200万, 38%, 2
- 华南, 980万, 42%, 3
... (共10个区域)
```

**LLM生成输出** (`output/batch-sales/generate.js`):
```javascript
const PptxGenJS = require("pptxgenjs");
const fs = require("fs");
// ...
// 读取数据源
const regions = [
  { name: "华东", sales: 1850, growth: 54, rank: 1 },
  { name: "华北", sales: 1200, growth: 38, rank: 2 },
  { name: "华南", sales: 980, growth: 42, rank: 3 },
  { name: "西南", sales: 750, growth: 35, rank: 4 },
  { name: "华中", sales: 680, growth: 28, rank: 5 },
  { name: "东北", sales: 520, growth: 22, rank: 6 },
  { name: "西北", sales: 380, growth: 45, rank: 7 },
  { name: "海外", sales: 320, growth: 68, rank: 8 },
  { name: "港澳台", sales: 180, growth: 15, rank: 9 },
  { name: "其他", sales: 90, growth: 10, rank: 10 },
];
// ...
const theme = {
  primary: "1A2B3C",
  accent: "FF6B35",
  gold: "FFD700",
  text: "333333",
};
// ...
// 批量生成函数
function generateRegionPPT(region) {
  const pptx = new PptxGenJS();
  pptx.defineLayout({ name: "WIDE", width: 13.33, height: 7.5 });
  pptx.layout = "WIDE";
// ...
  // 根据排名选择颜色
  const rankColor = region.rank <= 3 ? theme.gold : theme.accent;
// ...
  // 封面页
  const s1 = pptx.addSlide();
  s1.background = { color: theme.primary };
  s1.addText(`${region.name}区域`, {
    x: 1, y: 2, w: 11, h: 1.2, fontSize: 44, color: "FFFFFF", bold: true, fontFace: "微软雅黑",
  });
  s1.addText("2024年Q3业绩报告", {
    x: 1, y: 3.3, w: 11, h: 0.8, fontSize: 28, color: rankColor, fontFace: "微软雅黑",
  });
  s1.addText(`全国排名第 ${region.rank} 位`, {
    x: 1, y: 4.5, w: 11, h: 0.6, fontSize: 22, color: "CCCCCC", fontFace: "微软雅黑",
  });
// ...
  // 业绩数据页
  const s2 = pptx.addSlide();
  s2.addText("核心业绩指标", {
    x: 0.5, y: 0.3, w: 12, h: 0.8, fontSize: 36, color: theme.primary, bold: true, fontFace: "微软雅黑",
  });
// ...
  // 三个数据卡片
  const cardY = 1.5;
  const cardH = 2.5;
  // 销售额卡片
  s2.addText("Q3销售额", {
    x: 0.5, y: cardY, w: 3.8, h: 0.5, fontSize: 18, color: theme.text, fontFace: "微软雅黑",
    align: "center", fill: { color: "F0F0F0" },
  });
  s2.addText(`${region.sales}万元`, {
    x: 0.5, y: cardY + 0.6, w: 3.8, h: 1.5, fontSize: 40, color: theme.primary, bold: true,
    fontFace: "微软雅黑", align: "center", fill: { color: "F0F0F0" },
  });
// ...
  // 增长率卡片
  s2.addText("同比增长", {
    x: 4.7, y: cardY, w: 3.8, h: 0.5, fontSize: 18, color: theme.text, fontFace: "微软雅黑",
    align: "center", fill: { color: "F0F0F0" },
  });
  s2.addText(`${region.growth}%`, {
    x: 4.7, y: cardY + 0.6, w: 3.8, h: 1.5, fontSize: 40, color: theme.accent, bold: true,
    fontFace: "微软雅黑", align: "center", fill: { color: "F0F0F0" },
  });
// ...
  // 排名卡片
  s2.addText("全国排名", {
    x: 8.9, y: cardY, w: 3.8, h: 0.5, fontSize: 18, color: theme.text, fontFace: "微软雅黑",
    align: "center", fill: { color: "F0F0F0" },
  });
  s2.addText(`第${region.rank}名`, {
    x: 8.9, y: cardY + 0.6, w: 3.8, h: 1.5, fontSize: 40, color: rankColor, bold: true,
    fontFace: "微软雅黑", align: "center", fill: { color: "F0F0F0" },
  });
// ...
  const fileName = `output/batch-sales/${region.name}-Q3-report.pptx`;
  pptx.writeFile({ fileName });
  console.log(`已生成: ${fileName}`);
  return fileName;
}
// ...
// 批量执行
const outputDir = "output/batch-sales";
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}
// ...
console.log(`开始批量生成 ${regions.length} 份PPT...`);
const files = regions.map(generateRegionPPT);
console.log(`\n批量生成完成! 共 ${files.length} 份PPT`);
console.log("文件列表:");
files.forEach((f, i) => console.log(`  ${i + 1}. ${f}`));
```

**效果验证**: ✓10份PPT参数化生成(区域名/销售额/增长率/排名) ✓排名前三用金色高亮 ✓三卡片布局(销售额/增长/排名) ✓自动创建输出目录 ✓生成日志可追踪

## 常见问题

### Q1: PptxGenJS和python-pptx怎么选?
A: PptxGenJS(Node.js)适合Web应用集成、模板化批量生成、图表丰富(内置多种图表类型);python-pptx适合数据分析场景(与pandas/matplotlib集成)、读取编辑现有PPT、服务器端批量处理。两者功能有重叠,PptxGenJS图表更美观,python-pptx对现有PPT编辑更强。国内安装:PptxGenJS用cnpm,python-pptx用清华源pip。

### Q2: 生成PPT时中文乱码或字体不一致?
A: (1)明确指定中文字体:PptxGenJS用`fontFace: "微软雅黑"`,python-pptx用`font.name = "微软雅黑"`;(2)服务器Linux环境可能缺中文字体,需安装:`apt install fonts-wqy-zenhei`或下载思源黑体;(3)导出PDF时字体可能变化,建议在PowerPoint中打开检查,或用LibreOffice headless模式转换:`libreoffice --headless --convert-to pdf presentation.pptx`。

### Q3: 如何批量生成多份定制PPT?
A: 参数化模板方法:(1)设计模板PPT,用占位符标记可变内容(如{{title}}、{{data}});(2)读取数据源(Excel/JSON/数据库);(3)循环生成:每行数据替换占位符生成一份PPT。建议用PptxGenJS的pres接口或python-pptx的模板替换。注意批量生成时内存管理,每份生成后释放。

### Q4: 如何将现有PPT转为PDF?
A: 三种方式:(1)PowerPoint/WPS直接另存为PDF(最准确);(2)LibreOffice headless:`libreoffice --headless --convert-to pdf input.pptx --outdir output/`(Linux服务器常用);(3)python-pptx读取+reportlab重建PDF(不推荐,格式可能失真)。推荐方案2用于服务器端自动化。

### Q5: PPT中的数据图表如何动态更新?
A: PptxGenJS和python-pptx生成的图表是静态嵌入的。如需动态更新:(1)重新生成PPT(推荐,数据变化时重跑脚本);(2)链接外部Excel数据源(python-pptx支持,图表引用Excel单元格,更新Excel后PPT图表更新);(3)用PowerPoint COM接口自动化(仅Windows,需安装Office)。

## 已知限制

- PptxGenJS/python-pptx的动画支持有限,复杂动画(如路径动画、触发器动画)无法通过代码生成,需在PowerPoint中手动添加
- 图表样式受库限制,不如PowerPoint原生图表美观,复杂图表(组合图、瀑布图)可能不支持
- 中文字体在跨平台(Windows/macOS/Linux)显示可能不一致,服务器端生成需确保字体安装
- PDF导出可能丢失动画和过渡效果,PDF为静态版本
- 超大PPT(100页+)生成时内存占用高,建议分批生成或优化图片资源

## 安全

- **API Key零暴露**: 如使用云端PPT服务,API Key通过环境变量传入,不硬编码到代码
- **文件权限**: 生成的PPT文件可能含敏感商业数据,输出目录按需设置访问权限
- **数据脱敏**: 批量生成PPT时,确保数据源中的敏感信息(如客户姓名)按需脱敏
- **临时文件清理**: 生成过程中的临时文件(中间PPT、图片缓存)处理完成后及时删除
- **字体版权**: 商用PPT注意字体版权,推荐使用开源字体(思源黑体/阿里巴巴普惠体)
