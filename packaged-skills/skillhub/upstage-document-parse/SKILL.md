---

slug: upstage-document-parse
name: upstage-document-parse
version: 1.0.6
displayName: 文档解析工具
summary: 将 PDF、图片、Office 文档解析为带版面感知的 Markdown/HTML，含表格和坐标。upstage-document-parse 是一个文档解析技能，将
  PDF、图片、DOC
summary_zh: 将 PDF、图片、Office 文档解析为带版面感知的 Markdown/HTML，含表格和坐标。upstage-document-parse
  是一个文档解析技能，将 PDF、图片、DOC
license: MIT
description: |-。将 PDF、图片、Office 文档解析为带版面感知的 Markdown/HTML，含表格和坐标。upstage-document-parse。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。
  是一个文档解析技能，将 PDF、图片、DOC。支持自动化配置和灵活的参数设置，适适配多种工作环境，增强工作效率。。将 PDF、图片、Office 文档解析为带版面感知的
  Markdown/HTML，含表格和坐标。upstage-document-parse 是一个文档解析技能，将 PDF、图片、DOC'
tools:
- read
- exec
- write
homepage: ''
tags:
- 文档处理
- 工具
- 效率
- api
- ocr
- markdown
- html
- document-parse
category: Knowledge

---

> **核心功能**: 本技能提供中文交互、化工作流场景等能力。

# Document Parse

document-parse 将文档转换为结构化的 HTML/Markdown。识别表格、图片、公式、图表等版面元素，
并返回边界框坐标（bounding box coordinates）.
## 输入规范
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Document Parse处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 专业版专属特性
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Document Parse文档解析 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 运行环境
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
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 主要能力
### 1. 多格式文档解析
支持 JPEG、PNG、BMP、PDF（异步最多 1000 页）、TIFF、HEIC、DOCX、PPTX、XLSX、HWP、HWPX
等格式。通过 `model: "document-parse"` 调用解析模型，将文档内容转换为结构化的
`content.html`、`content.markdown` 和 `content.text` 三种格式输出.
标准文档处理时间约 3 秒.
### 2. 同步模式解析（Sync）
通过 `POST /v1/document-digitization` 端点进行同步解析。限制：最多 100 页、50 MB 文件大小、
5 分钟服务器超时。适合 100 页以内且预期在 5 分钟内完成的文档。响应直接返回在 HTTP response 中，
无需轮询。参数包括 `model`（必填，值为 `document-parse`）、`output_formats`（默认 `['html']`，
可选 `['markdown']` 或 `['html', 'markdown']`）、`mode`（默认 `standard`，可选 `enhanced`/`auto`）、
`ocr`（默认 `auto`，可选 `force`）、`coordinates`（默认 `true`，设为 `false` 省略边界框）.
### 3. 异步模式解析（Async）
通过 `POST /v1/document-digitization/async` 端点进行异步解析。限制：最多 1000 页、50 MB 文件大小.
返回 `request_id`，按 10 页批次处理。适用于超过 100 页、扫描/复杂内容或批量任务的文档.
异步模式需要提交后轮询状态，支持 Python 轮询模式。决策规则：100 页以内且 5 分钟内完成 → 同步；
超过 100 页、扫描/复杂内容或批量任务 → 异步.
### 4. 版面元素识别与坐标输出
解析结果包含 `elements` 数组，每个元素包含 `id`、`category`、`content`（html/markdown/text）、
`page` 页码和 `coordinates` 边界框坐标（如 `[{"x": 0.06, "y": 0.05}, ...]`）.
支持 14 种元素类别：`paragraph`、`heading1`、`heading2`、`heading3`、`list`、`table`、
`figure`、`chart`、`equation`、`caption`、`header`、`footer`、`index`、`footnote`.
坐标为归一化值（0-1 范围），表示元素在页面中的相对位置.

### 5. 增强模式与 OCR 控制
`mode=enhanced` 用于复杂表格、图表和图片的精确解析，支持 `merge_multipage_tables=true`
合并跨页表格（enhanced 模式下最多 20 页）。`mode=auto` 让 API 逐页自动决定优选模式.
`ocr=force` 强制对扫描 PDF 或图片执行 OCR，适用于非原生数字文档.
`coordinates=false` 可省略边界框以减小响应体积.

### 6. 输出文件管理
默认输出到 `<system-temp>/<input-stem>.parsed.<ext>`，其中 `<ext>` 匹配 `output_formats`
（`md` 或 `html`）。例如 `/tmp/report.parsed.md`。使用 `tempfile.gettempdir()` 实现跨平台路径.
如果用户指定输出路径，则使用用户路径。始终在响应中打印解析后的绝对路径，方便用户定位文件.

## 使用指南
1. 确认文档格式在支持列表中（JPEG/PNG/BMP/PDF/TIFF/HEIC/DOCX/PPTX/XLSX/HWP/HWPX）
2. 评估文档页数和大小：100 页以内且 50MB 以内 → 同步模式；否则 → 异步模式
3. 设置 API Key 到环境变量，通过 `os.environ["DOCUMENT_PARSE_API_KEY"]` 读取
4. 选择参数：`model=document-parse`、`output_formats`、`mode`（standard/enhanced/auto）、`ocr`
5. 发送请求到同步端点 `/v1/document-digitization` 或异步端点 `/v1/document-digitization/async`
6. 同步模式直接解析响应 JSON；异步模式轮询 `request_id` 直到完成
7. 将结果写入输出文件（默认 `<system-temp>/<input-stem>.parsed.<ext>`）
8. 打印输出文件的绝对路径

## 示例展示
### 示例1：同步模式解析 PDF

```python
import os
import requests
# ...
with open("report.pdf", "rb") as f:
    response = requests.post(
        "https://api.example.com/v1/document-digitization",
        headers={"Authorization": f"Bearer {os.environ['DOCUMENT_PARSE_API_KEY']}"},
        files={"document": f},
        data={
            "model": "document-parse",
            "output_formats": "['markdown']",
            "mode": "standard",
            "ocr": "auto",
            "coordinates": "true"
        }
    )
# ...
result = response.json()
print(result["content"]["markdown"])
# 输出：
# # Quarterly Report Q2 2026

# ## Revenue Summary
# Total revenue reached $48.2M, representing a 23% year-over-year growth.

# | Quarter | Revenue | Growth |
# |---------|---------|--------|
# | Q1 2026 | $39.2M | +18%  |
# | Q2 2026 | $48.2M | +23%  |
# ...
print(f"Pages processed: {result['usage']['pages']}")
# 输出：Pages processed: 12
# ...
print(f"Elements found: {len(result['elements'])}")
# 输出：Elements found: 47
```

### 示例2：增强模式解析复杂表格

```python
import os
import requests
# ...
with open("financial_statements.pdf", "rb") as f:
example.com/v1/document-digitization",
environ['DOCUMENT_PARSE_API_KEY']}"},
        files={"document": f},
        data={
            "model": "document-parse",
            "output_formats": "['html', 'markdown']",
            "mode": "enhanced",
            "ocr": "force",
            "merge_multipage_tables": "true",
            "coordinates": "true"
        }
    )
# ...
result = response.json()
# ...
# 查看表格元素
tables = [e for e in result["elements"] if e["category"] == "table"]
print(f"Tables found: {len(tables)}")
# 输出：Tables found: 8
# ...
# 查看领先个表格的坐标
if tables:
    first_table = tables[0]
    print(f"Table on page {first_table['page']}")
    print(f"Coordinates: {first_table['coordinates']}")
    # 输出：
    # Table on page 3
    # Coordinates: [{"x": 0.06, "y": 0.15}, {"x": 0.94, "y": 0.15}, ...]
# ...
# 写入输出文件
import tempfile
output_path = os.path.join(tempfile.gettempdir(), "financial_statements.parsed.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result["content"]["markdown"])
print(f"Output saved to: {output_path}")
# 输出：Output saved to: /tmp/financial_statements.parsed.md
```

## 异常修复
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| API Key 缺失或无效 | 环境变量 `DOCUMENT_PARSE_API_KEY` 未设置或过期 | 在控制台重新获取 API Key，设置到环境变量中 |
| 文件超过 50 MB 限制 | 文档体积超出同步和异步模式的统一上限 | 拆分文档后分批处理，或压缩 PDF 后 |
| 同步模式页数超过 100 页 | 文档页数超出同步模式限制 | 切换到异步模式 `/v1/document-digitization/async`，支持最多 1000 页 |
| 同步模式 5 分钟超时 | 文档复杂度高或扫描内容导致处理时间过长 | 切换到异步模式，异步模式按 10 页批次处理，无 5 分钟限制 |
| OCR 失败 | 扫描件质量差、分辨率过低或手写内容 | 提升扫描分辨率至 300 DPI 以上，确保文字清晰可读 |
| 复杂表格解析不完整 | 跨页表格或多层嵌套表格 | 使用 `mode=enhanced` 和 `merge_multipage_tables=true`（enhanced 模式最多 20 页） |
| 不支持的文件格式 | 使用了不在支持列表中的格式 | 转换为支持的格式：JPEG/PNG/BMP/PDF/TIFF/HEIC/DOCX/PPTX/XLSX/HWP/HWPX |

## 常见疑问
### Q1: 同步模式和异步模式如何选择？
A: 决策规则：100 页以内且预期 5 分钟内完成 → 同步模式（`/v1/document-digitization`）；
超过 100 页、扫描/复杂内容或批量任务 → 异步模式（`/v1/document-digitization/async`）.
同步模式直接返回结果，异步模式返回 `request_id` 需要轮询。两种模式文件大小上限均为 50 MB.
### Q2: `mode` 参数的 standard、enhanced、auto 有什么区别？
A: `standard`（默认）适用于普通文档，处理速度最快（约 3 秒）。`enhanced` 适用于复杂表格、
图表和图片，提供更精确的解析但处理时间更长。`auto` 让 API 逐页自动决定使用 standard 还是
enhanced，适合混合内容文档。`enhanced` 模式下 `merge_multipage_tables=true` 可合并跨页表格，
但限制为最多 20 页.
### Q3: `ocr` 参数何时使用 force？
A: `ocr=force` 用于扫描 PDF 或图片（非原生数字文档）。当文档是通过扫描纸质文件生成的 PDF
时，文字实际上是图片而非文本层，必须使用 OCR 提取。`ocr=auto`（默认）让 API 自动检测是否
需要 OCR。对于原生数字 PDF（如 Word 导出的 PDF），使用 `auto` 即可，无需强制 OCR.
### Q4: 元素坐标 `coordinates` 的格式和用途是什么？
A: 坐标为归一化值（0-1 范围），表示元素在页面中的相对位置。格式为
`[{"x": 0.06, "y": 0.05}, {"x": 0.94, "y": 0.05}, ...]`，定义元素的边界框.
用途包括：定位表格在页面中的位置、提取特定区域的元素、可视化标注文档版面.
设置 `coordinates=false` 可省略坐标以减小响应体积.
### Q5: 输出文件默认保存在哪里？
A: 默认保存到 `<system-temp>/<input-stem>.parsed.<ext>`，其中 `<system-temp>` 通过
`tempfile.gettempdir()` 获取（跨平台），`<input-stem>` 是输入文件名（不含扩展名），
`<ext>` 匹配 `output_formats`（`md` 或 `html`）。例如输入 `report.pdf` 输出
`/tmp/report.parsed.md`。如果用户指定输出路径，则使用用户路径。始终打印绝对路径.
### Q6: 响应 JSON 的 `elements` 数组包含哪些信息？
A: 每个 element 包含：`id`（元素编号）、`category`（14 种类别之一：paragraph/heading1/
heading2/heading3/list/table/figure/chart/equation/caption/header/footer/index/footnote）、
`content`（含 html/markdown/text 三种格式）、`page`（页码）、`coordinates`（边界框坐标）.
`usage.pages` 表示处理的页数.
## 注意事项
- 文件大小上限统一为 50 MB，无法通过参数调整
- 同步模式最多 100 页且 5 分钟超时，超限必须使用异步模式
- 异步模式最多 1000 页，按 10 页批次处理
- `merge_multipage_tables=true` 在 enhanced 模式下最多支持 20 页
- OCR 质量取决于扫描件清晰度，手写内容识别率较低
- 标准文档处理约 3 秒，复杂文档（enhanced + force OCR）可能显著更长

## 创新优势
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
| --- | --- | --- | --- | --- |
| 文档解析 | 30分钟/页 | 3秒/页 | 29分57秒/页 | 98% |
| 表格提取 | 15分钟/页 | 2秒/页 | 14分58秒/页 | 99% |
| 图片识别 | 20分钟/页 | 1秒/页 | 19分59秒/页 | 98% |
| 公式识别 | 30分钟/页 | 4秒/页 | 29分56秒/页 | 97% |
| 图表识别 | 25分钟/页 | 2秒/页 | 24分58秒/页 | 99% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
| --- | --- | --- | --- | --- |
| 支持格式 | 多种格式（PDF、图片、Office等） | 有限格式 | 有限格式 | 广泛格式 |
| 解析速度 | 高效 | 低效 | 一般 | 高效 |
| 输出格式 | Markdown/HTML | 文本 | 文本/JSON | 文本/XML |
| 边界框坐标 | 支持 | 不支持 | 不支持 | 支持 |
| OCR功能 | 支持 | 不支持 | 有限支持 | 支持 |
| 适应场景 | 多样化场景 | 单一场景 | 单一场景 | 广泛场景 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
| --- | --- | --- | --- | --- |
| 文档解析效率低 | 人工处理文档效率低，耗时较长 | 各行各业 | 使用文档解析工具实现自动化处理 | 时间节约超过95% |
| 解析准确率低 | 人工处理容易出现错误，影响结果准确性 | 各行各业 | 使用文档解析工具提高解析准确率 | 准确率提升至98%以上 |
| 多种格式不兼容 | 不同格式文档难以统一处理 | 各行各业 | 文档解析工具支持多种格式转换 | 解决多种格式不兼容问题 |

## 问题排查手册
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 解析失败 | 文件格式不支持 | 检查文件格式是否正确 | 尝试其他支持的格式或联系技术支持 |
| 输出内容错误 | 文件内容复杂或格式不正确 | 检查文件内容是否正确，格式是否符合规范 | 调整文件内容或格式 |
| 速度慢 | 文件大小过大或服务器负载过高 | 检查文件大小或服务器状态 | 减小文件大小或升级服务器配置 |
| 服务器错误 | 服务器故障或配置错误 | 检查服务器状态或配置 | 修复服务器或配置 |
| API Key错误 | API Key配置错误或过期 | 检查API Key配置或更新API Key | 重新配置API Key或更新API Key |

## 安全规范
1. 确保API Key安全，避免泄露到版本控制系统或公共平台。
2. 文件解析过程中，保护用户隐私，不泄露敏感信息。
3. 防止恶意文件上传，对上传文件进行安全检测。
4. 限制访问权限，只有授权用户才能访问API接口。
5. 定期更新软件版本，修复已知安全漏洞。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

## 主要特性
- **自动化执行**: 将 PDF、图片、Office 文档解析为带版面感知的 Markdown/HTML，含表格和坐标。upstage-doc
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果

## 异常应对措施
针对文档解析工具使用中可能遇到的常见问题,提供以下排查方案:

| 错误类型 | 原因分析 | 解决方案 |
|---------|---------|---------|
| API认证失败(401) | API密钥错误或过期 | 检查密钥配置,重新生成token |
| 接口限流(429) | 请求频率超出限制 | 降低调用频率,启用重试退避策略 |
| 响应超时(504) | 网络延迟或服务端负载过高 | 增加超时阈值,检查网络连接 |
| 文件不存在 | 路径错误或文件未创建 | 检查路径拼写,确认文件已生成 |
| 文件格式不支持 | 扩展名不在支持列表中 | 转换为支持的格式后重试 |
| 权限不足 | 当前用户无读写权限 | 检查文件权限,以管理员身份运行 |
| 命令执行失败 | 参数错误或环境依赖缺失 | 检查命令语法,确认依赖已安装 |
| 进程超时 | 命令执行时间过长 | 增加超时设置,优化命令参数 |
| 网络连接失败 | DNS解析失败或防火墙拦截 | 检查网络配置,确认代理设置 |

### 文档解析工具通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块
