---
slug: google-fonts
name: google-fonts
version: "1.0.0"
displayName: Google Fonts指南
summary: Google Fonts字体选择与配对指南，覆盖加载优化、可变字体、子集化与自托管
license: MIT
description: |-
  Google Fonts 字体选择与配对指南，涵盖加载优化、可变字体、子集化、经典字体配对、
  按用途选字体、自托管方案。提供 12 组经验证的字体配对方案，覆盖正文、标题、代码场景。
tags:
  - Other
tools:
  - read
  - exec
---

# Google Fonts 字体选择与配对指南

Google Fonts 字体加载优化、配对选择、子集化与自托管的完整参考。

## 核心能力

### Loading Mistakes（加载常见错误）
常见字体加载问题及修复方案：

- **缺少 preconnect**：未在 `<link>` 前添加 `<link rel="preconnect" href="https://fonts.googleapis.com">` 和 `crossorigin`，导致 TLS 握手延迟
- **font-display: swap 缺失**：未设置 `display=swap` 参数，字体加载期间显示空白而非降级到系统字体
- **加载全字重**：请求 `wght@100..900` 全部字重导致文件过大，应只加载实际使用的 `wght@400;600;700`
- **未启用 variable**：可变字体未加 `&display=swap`，无法享受单文件多字重优势

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Lora:wght@500;700&display=swap" rel="stylesheet">
```

**处理**: 按照skill规范执行Loading Mistakes（加载常见错误）操作,遵循单一意图原则。
**输出**: 返回Loading Mistakes（加载常见错误）的执行结果,包含操作状态和输出数据。### Variable Fonts（可变字体）
可变字体在单文件中包含整个字重和宽度范围，通过 `font-variation-settings` 控制轴值：

```css
.text {
  font-family: 'Inter', system-ui, sans-serif;
  font-variation-settings: 'wght' 450, 'opsz' 14;
}
```

推荐可变字体：Inter、Roboto Flex、Montserrat、Work Sans、DM Sans、Source Sans 3、IBM Plex Sans。启用方式：CSS2 API URL 中使用 `wght@300..700` 范围语法。

**处理**: 按照skill规范执行Variable Fonts（可变字体）操作,遵循单一意图原则。
**输出**: 返回Variable Fonts（可变字体）的执行结果,包含操作状态和输出数据。### Subsetting（字体子集化）
Google Fonts CSS2 API 默认只返回 `latin` 子集。如需中文（Noto Sans SC）或日文（Noto Sans JP），需显式指定 `&subset=latin,latin-ext` 或按需引入。

自托管场景使用 `google-webfonts-helper` 或 `pyftsubset` 工具生成子集字体，只保留页面实际使用的字符（可从 1MB+ 降至 20KB）。

```bash
pyftsubset NotoSansSC-Regular.otf --text-file=chars.txt --output-file=NotoSansSC-subset.woff2 --flavor=woff2
```

**输入**: 用户提供Subsetting（字体子集化）所需的指令和必要参数。
**处理**: 按照skill规范执行Subsetting（字体子集化）操作,遵循单一意图原则。### Proven Pairings（经典字体配对）
12 组经验证的 Google Fonts 配对方案，覆盖设计风格与用途：

| 配对方案 | 用途 |
|---------|------|
| Playfair Display（heading）+ Source Sans Pro（body） | 杂志/编辑风格，serif 标题 + sans 正文 |
| Lora（heading）+ Roboto（body） | 博客/阅读，warm serif + 中性 sans |
| Libre Baskerville（heading）+ Montserrat（body） | 学术/文档，传统 serif + 现代 sans |
| Merriweather（heading）+ Open Sans（body） | 长文阅读，高可读性组合 |
| Inter（both）— vary weight for hierarchy | 极简/UI，单字体多字重建立层次 |
| Montserrat（heading）+ Hind（body） | 电商/品牌，几何 sans + 可读 sans |
| Poppins（heading）+ Nunito（body） | 友好/教育，圆润几何配对 |
| Work Sans（heading）+ Open Sans（body） | 企业/报告，干净专业 |
| Space Grotesk（heading）+ Space Mono（code） | 科技/开发者，等宽配对 |
| DM Sans（heading）+ DM Mono（code） | 现代/产品文档 |
| IBM Plex Sans + IBM Plex Mono | 企业级统一字体方案 |
| Abril Fatface, Bebas Neue, Oswald — never use these for body text | 装饰性字体仅限标题 |

**处理**: 按照skill规范执行Proven Pairings（经典字体配对）操作,遵循单一意图原则。
**输出**: 返回Proven Pairings（经典字体配对）的执行结果,包含操作状态和输出数据。### Font Selection by Purpose（按用途选字体）
- **长文正文**：Inter、Source Sans Pro、Open Sans、Work Sans — 高 x-height，小字号清晰
- **标题/Display**：Playfair Display、Abril Fatface、Bebas Neue、Oswald — 有表现力但勿用于正文
- **代码/等宽**：JetBrains Mono、Fira Code、Source Code Pro、Space Mono、DM Mono — 连字支持好
- **品牌/Logo**：Poppins、Montserrat、Space Grotesk — 几何感强，辨识度高
- **学术/法律**：Crimson Text、Libre Baskerville、Source Serif Pro — 传统 serif

**处理**: 按照skill规范执行Font Selection by Purpose（按用途选字体）操作,遵循单一意图原则。
**输出**: 返回Font Selection by Purpose（按用途选字体）的执行结果,包含操作状态和输出数据。### Self-Hosting（自托管字体方案）
Google Fonts CDN 在部分地区（如欧盟 GDPR 场景）可能有隐私问题。自托管方案：

1. 下载 woff2 字体文件
2. 用 `@font-face` 声明字体路径和 `font-display: swap`
3. 配置 CORS 头和缓存策略（`Cache-Control: max-age=31536000, immutable`）

```css
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400 700;
  font-display: swap;
  src: url('/fonts/inter- Variable.woff2') format('woff2-variations');
}
```

**输入**: 用户提供Self-Hosting（自托管字体方案）所需的指令和必要参数。
**处理**: 按照skill规范执行Self-Hosting（自托管字体方案）操作,遵循单一意图原则。
**输出**: 返回Self-Hosting（自托管字体方案）的执行结果,包含操作状态和输出数据。
### 配对方案

执行配对方案操作,处理用户输入并返回结果。

**输入**: 用户提供配对方案所需的参数和指令。

**输出**: 返回配对方案的处理结果。

- 执行`配对方案`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`配对方案`相关配置参数进行设置
### Playfair Display（heading）+ Source Sans Pro（body）

执行Playfair Display（heading）+ Source Sans Pro（body）操作,处理用户输入并返回结果。

**输入**: 用户提供Playfair Display（heading）+ Source Sans Pro（body）所需的参数和指令。

**输出**: 返回Playfair Display（heading）+ Source Sans Pro（body）的处理结果。

- 执行`Playfair Display（heading）+ Source Sans Pro（body）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`Playfair Display（heading）+ Source Sans Pro（body）`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 字体选择与配对指、覆盖加载优化、子集化与自托管、涵盖加载优化、组经验证的字体配、覆盖正文、代码场景。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`google-fonts`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

### 命令参数说明

- `-Regular`: 命令参数,用于指定操作选项
- `-family`: 命令参数,用于指定操作选项
- `-variations`: 命令参数,用于指定操作选项
- `--text-file`: 命令参数,用于指定操作选项
- `-style`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Regular`: 命令参数,用于指定操作选项
- `--flavor`: 命令参数,用于指定操作选项
- `--output-file`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Regular`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Regular`: 命令参数,用于指定操作选项

## 示例

### 基本用法

向Agent发送指令:

```
使用 Google Fonts指南 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令执行操作，返回处理结果。结果格式取决于具体能力点的输出定义。

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Chrome / Firefox / Safari / Edge（现代浏览器支持 woff2 和可变字体）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Google Fonts CDN | 网络服务 | CDN 方案必需 | 无需安装，直接引用 fonts.googleapis.com |
| pyftsubset | 命令行工具 | 子集化场景可选 | `pip install fonttools` |
| google-webfonts-helper | Web 工具 | 自托管场景可选 | 访问 gwfh.mranftl.com |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### 可用性分类
- **分类**: MD+KNOW（Markdown 知识 + 无外部依赖）
- **说明**: 字体配对与加载优化知识库，Agent 读取后直接输出 CSS/HTML 建议

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 字体未加载显示空白 | 缺少 font-display: swap | 在 CSS2 API URL 中添加 display=swap 参数 |
| FOUT 闪烁明显 | CDN 延迟或未预连接 | 添加 preconnect 到 fonts.googleapis.com 和 fonts.gstatic.com |
| 字体文件过大 | 加载全字重或全语言子集 | 只请求使用的 wght 值，指定 subset=latin |
| 可变字体不生效 | 浏览器不支持或 CSS 语法错误 | 确认浏览器支持 font-variation-settings，检查轴值语法 |
| 中文字体加载极慢 | CJK 字体体积大（数 MB） | 使用子集化工具只保留页面字符，或按需动态加载 |
| 自托管字体 CORS 错误 | 服务器未配置 CORS 头 | 在字体响应中添加 Access-Control-Allow-Origin |
| CDN 被墙不可用 | 区域网络限制 | 切换自托管方案或使用国内镜像 |
| 配对可读性差 | 标题字体用于正文或字重冲突 | 遵循装饰字体仅限标题原则，正文用高可读性字体 |

## 常见问题

### Q1: 如何选择标题和正文的字体配对？
A: 标题用有表现力的 serif（Playfair Display）或几何 sans（Montserrat），正文用高可读性 sans（Source Sans Pro、Open Sans）。同族配对（如 Inter both）通过字重差异建立层次。

### Q2: 可变字体和静态字体如何选择？
A: 可变字体单文件支持多字重，体积更小、灵活性更高，推荐用于新项目。静态字体兼容性更好，适合维护老项目。

### Q3: GDPR 合规如何处理 Google Fonts？
A: 德国法院裁定 Google Fonts CDN 涉及 IP 传输。合规方案：自托管 woff2 文件，用 @font-face 声明，配置 CORS 和缓存头。

## 已知限制

- Google Fonts 目录不包含商业付费字体（如 Helvetica、Proxima Nova）
- 中日韩字体体积大，CDN 加载可能影响性能
- 可变字体需要现代浏览器支持（Chrome 62+ / Firefox 62+ / Safari 11+）
- 自托管方案需自行处理子集化和缓存策略
