---
slug: "md-export"
name: "md-export"
version: "1.0.0"
displayName: "文档导出工具专业版"
summary: "Markdown全格式专业导出工具，含批量并行、自定义样式、PDF加密水印、模板云同步与API服务模式。"
license: "Proprietary"
edition: "pro"
description: |-
  面向内容团队与企业的Markdown全格式专业导出工具。在免费版基础上新增批量并行转换、自定义样式表、PDF水印加密、模板云端同步、REST API服务模式、版本对比与差异导出等高级能力，配套面向技术写作、运维、产品经理的多角色场景指南。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
  - 集成工具
  - 文档转换
  - Markdown
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 文档导出工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力分类 | 支持 | 支持 |
| 专业版 | 不支持 | 支持 |
| 文件大小上限 | 不支持 | 支持 |
| 无上限 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|---------|--------|--------|
| 文件大小上限 | 10MB | 无上限 |
| 批量转换 | 串行 | 并行（多核加速） |
| 自定义样式 | 无 | CSS+模板完全自定义 |
| PDF安全 | 无 | 水印+密码加密+权限控制 |
| API服务 | 无 | REST API微服务模式 |
| 模板管理 | 本地 | 云端同步+团队共享 |
| 版本对比 | 无 | 差异导出+增量更新 |
| 监控统计 | 无 | 转换日志+成功率+耗时分析 |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项。

**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### 文件大小上限

针对文件大小上限,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供文件大小上限相关的配置参数、输入数据和处理选项。

**输出**: 返回文件大小上限的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`文件大小上限`的配置文档进行参数调优
### 批量转换

针对批量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供批量转换相关的配置参数、输入数据和处理选项。

**输出**: 返回批量转换的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量转换`的配置文档进行参数调优
#
## 适用场景

### 场景一：企业技术文档批量发布（技术写作视角）

技术文档团队每周发布数十份API文档，需同时输出HTML（网页）、PDF（打印）、DOCX（协作）三种格式。

```bash
# 批量并行转换，输出到指定目录
markdown-exporter-pro batch /docs/**/*.md \
  --output-dir /publish \
  --formats html,pdf,docx \
  --parallel 8 \
  --template /templates/corporate.docx
```

### 场景二：内容平台在线转换API（运维视角）

为内容平台提供在线文档转换微服务，用户上传Markdown即时返回目标格式。

```bash
# 启动API服务
markdown-exporter-pro serve --port 8080 --workers 4

# 调用API
curl -X POST http://localhost:8080/api/convert \
  -F "file=@input.md" \
  -F "format=pdf" \
  -F "watermark=CONFIDENTIAL" \
  -o output.pdf
```

### 场景三：品牌视觉规范统一（产品视角）

通过自定义样式表与模板，确保全公司文档输出视觉统一。

### 场景四：版本对比与增量更新（开发者视角）

文档版本更新时，仅导出变更部分，避免全量重发。

```bash
markdown-exporter-pro diff v1.2.md v1.3.md --output changelog.pdf
```

## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**: Windows / macOS / Linux
3. **Python**: 3.8+
4. **Docker**: 可选（API服务容器化部署）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 必需 | python.org 官方下载 |
| md-exporter-pro | Python包 | 必需 | `pip install md-exporter-pro` |
| pandoc | 系统工具 | 可选 | pandoc.org 官方下载（PPTX转换需要） |
| Redis | 缓存 | 可选 | redis.io 官方下载（API服务集群部署） |
| Nginx | 反向代理 | 可选 | nginx.org 官方下载（API服务负载均衡） |
| 中文字体 | 字体包 | 可选 | 系统包管理器安装 |

### API Key 配置
5. **API_TOKEN**: REST API服务的鉴权Token，通过环境变量注入，禁止硬编码
6. **PDF_PASSWORD**: PDF加密密码，通过环境变量注入
7. **ALERT_WEBHOOK_URL**: 监控告警Webhook地址，通过环境变量配置
8. **Redis密码**: 通过REDIS_PASSWORD环境变量配置

### 可用性分类
9. **分类**: MD+EXEC（）
10. **说明**: 基于Markdown的AI Skill，

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | md-export处理的内容输入 |,  |
| content | string | 否 | md-export处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "export 相关配置参数",
    result: "export 相关配置参数",
    result: "export 相关配置参数",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 自定义CSS样式表

```css
/* corporate.css */
body {
    font-family: "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
    line-height: 1.8;
    color: #333;
}

h1, h2, h3 {
    color: #1a5276;
    border-bottom: 2px solid #2980b9;
}

code {
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 3px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
```

### PDF水印与加密

```bash
markdown-exporter-pro md_to_pdf input.md output.pdf \
  --watermark "公司机密" \
  --watermark-opacity 0.1 \
  --encrypt-password "secret123" \
  --permissions "print,view" \
  --no-modify \
  --no-copy
```

### 批量并行转换

```bash
markdown-exporter-pro batch /docs/**/*.md \
  --output-dir /publish \
  --formats html,pdf,docx,xlsx \
  --parallel 8 \
  --template /templates/corporate.docx \
  --style /styles/corporate.css \
  --watermark "公司机密" \
  --fail-on-error false \
  --report /logs/batch-report.json
```

### REST API调用示例

```bash
# 转换单个文件
curl -X POST http://localhost:8080/api/convert \
  -H "Authorization: Bearer $API_TOKEN" \
  -F "file=@input.md" \
  -F "format=pdf" \
  -F "watermark=CONFIDENTIAL" \
  -o output.pdf

# 批量转换
curl -X POST http://localhost:8080/api/batch \
  -H "Authorization: Bearer $API_TOKEN" \
  -F "files[]=@doc1.md" \
  -F "files[]=@doc2.md" \
  -F "format=docx" \
  -o batch.zip
```

### 模板云端同步

```bash
# 推送模板到云端
markdown-exporter-pro template push /templates/corporate.docx --name corporate-v2

# 团队成员拉取最新模板
markdown-exporter-pro template pull corporate-v2 --to /templates/

# 查看团队模板列表
markdown-exporter-pro template list
```

### 版本差异导出

```bash
# 对比两个版本，仅导出变更部分
markdown-exporter-pro diff v1.2.md v1.3.md \
  --output changelog.pdf \
  --format pdf \
  --highlight-changes
```

## 常见问题

### Q1：批量转换部分文件失败如何处理？

A：专业版默认`--fail-on-error false`，单个文件失败不影响整体流程。失败列表记录在`--report`指定的JSON报告中，可据此修复后单独重转。

### Q2：API服务如何做鉴权？

A：通过Bearer Token鉴权，Token通过`--auth-token`参数或`API_TOKEN`环境变量配置。建议在生产环境配合API网关做更细粒度的权限控制。

### Q3：自定义样式不生效？

A：(1) 检查CSS路径是否正确；(2) 确认CSS语法无错误；(3) 部分格式（如DOCX）使用模板而非CSS，需通过`--template`指定；(4) 使用`--debug`参数查看样式加载日志。

### Q4：PDF加密后无法打开？

A：确认密码正确，且PDF阅读器支持加密算法。专业版默认使用AES-256加密，部分老旧阅读器可能不兼容，可通过`--encryption-algorithm aes-128`降级。

### Q5：模板云端同步占用空间大？

A：模板文件通常不大（DOCX约100KB），主要占用来自历史版本。建议定期清理旧版本：`markdown-exporter-pro template prune --keep-latest 5`。

### Q6：版本差异导出如何处理删除的内容？

A：删除的内容在差异PDF中以红色删除线标记，新增内容以绿色背景标记，修改内容以红绿对比显示。

### Q7：API服务如何水平扩展？

A：专业版支持多实例部署，通过Redis共享任务队列。建议前置Nginx做负载均衡，后端实例数根据QPS动态调整。

### Q8：如何与CI/CD流水线集成？

A：在CI/CD流水线中调用命令行或API，将构建产物中的Markdown自动转换为分发格式。GitHub Actions示例：

```yaml
- name: Convert docs
  run: |
    pip install md-exporter-pro
    markdown-exporter-pro batch docs/**/*.md \
      --output-dir publish \
      --formats pdf,html \
      --watermark "Build $相关信息"
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
