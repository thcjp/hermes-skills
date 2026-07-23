---
slug: "quark-scan"
name: "quark-scan"
version: "1.0.0"
displayName: "夸克扫描-专业版"
summary: "企业级文件扫描增强工具,支持批量处理、API集成、自定义流水线,适配商业文档数字化。"
license: "Proprietary"
edition: "pro"
description: |-
  夸克扫描专业版,面向企业团队与专业用户的高级文件扫描与图像增强工具。核心能力:
  - 批量图片处理,支持目录扫描与队列处理
  - API 集成,可嵌入企业文档管理系统
  - 自定义处理流水线,串联多个增强场景
  - 优先处理队列与企业级技术支持
  - 处理结果持久化存储与归档

  适用场景:
  - 企业合同/票据批量数字化
  - 教育机构试卷批量电子化
  - 档案馆历史文档批量修复
  - 电商商品图批量去水印

  差异化:专业版在免费版基础上扩展批量处理、API集成与自定义流水线,兼容免费版所有场景,适合商业级文档数字化生产
tags:
  - Creative
  - 图像处理
  - 企业版
  - 商业内容
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# 夸克扫描-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力项 | 支持 | 支持 |
| 专业版 | 不支持 | 支持 |
| :------- | 不支持 | 支持 |
| :----- | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-------|:-------|:-------|:-----|
| 单张图片处理 | 是 | 是 | 全场景支持 |
| 批量处理 | 否 | 是 | 目录/队列处理 |
| API 集成 | 否 | 是 | 程序化调用 |
| 自定义流水线 | 否 | 是 | 多场景串联 |
| 结果持久化 | 临时 | 持久 | 归档存储 |
| 处理优先级 | 普通 | 高优先 | 企业级保障 |
| 调用量配额 | 限制 | 高配额 | 企业级 |
| 技术支持 | 社区 | 专属 | 工单响应 |
| 审计日志 | 否 | 是 | 操作追溯 |
### 能力项

针对能力项,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供能力项相关的配置参数、输入数据和处理选项。

**输出**: 返回能力项的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力项`的配置文档进行参数调优
### 单张图片处理

针对单张图片,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供单张图片处理相关的配置参数、输入数据和处理选项。

**输出**: 返回单张图片处理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`单张图片处理`的配置文档进行参数调优
### 批量处理

支持批量输入处理,自动队列管理,并行执行提高效率,结果统一汇总输出。

**输入**: 用户提供批量处理相关的配置参数、输入数据和处理选项。

**输出**: 返回批量处理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量处理`的配置文档进行参数调优
#
## 适用场景

### 场景一:企业合同批量数字化

企业法务部门需将一批纸质合同照片批量高清化,用于电子归档。

```python
# 批量处理合同图片
python3 （请参考skill目录中的脚本文件） \
  --input ./contracts/ \
  --scene scan-contract \
  --output ./contracts_hd/ \
  --format json \
  --parallel 5

# contracts/ 目录下放置多个合同照片
# 系统并发处理并输出高清版本到 contracts_hd/
```

### 场景二:教育机构试卷批量电子化

教育机构需将一批已作答试卷批量去手写,生成空白版本供复用。

```bash
# 批量去手写
python3 （请参考skill目录中的脚本文件） \
  --input ./exams/ \
  --scene remove-handwriting \
  --output ./exams_blank/ \
  --parallel 10 \
  --format json

# 自定义流水线:去手写 → 去阴影 → 去底色
python3 （请参考skill目录中的脚本文件） \
  --input ./exams/ \
  --pipeline "remove-handwriting,remove-shadow,remove-background-color" \
  --output ./exams_clean/ \
  --parallel 5
```

### 场景三:电商商品图批量去水印

电商团队需将一批商品图批量去除供应商水印,用于自有渠道展示。

```bash
# 批量去水印
python3 （请参考skill目录中的脚本文件） \
  --input ./product_images/ \
  --scene remove-watermark \
  --output ./products_clean/ \
  --parallel 8 \
  --format json

# 处理结果归档与审计
python3 （请参考skill目录中的脚本文件） \
  --input ./products_clean/ \
  --metadata ./metadata.json \
  --output ./archive/
```

### 场景四:API 集成到文档管理系统

企业需将扫描能力集成到内部文档管理系统。

```python
# 示例
from quark_scan import ScanClient

client = ScanClient(api_key="your_pro_key", edition="pro")

# 单张处理
result = client.scan(
    image_path="./document.jpg",
    scene="scan-document",
    output_path="./output/"
)

# 批量处理
results = client.batch_scan(
    input_dir="./documents/",
    scene="scan-contract",
    output_dir="./processed/",
    parallel=5
)
```

## 使用流程

### 优秀步:配置企业 API Key

```bash
# 企业版 Key 享有更高配额与优先级
export SCAN_WEBSERVICE_KEY="your_pro_key"
export SCAN_EDITION="pro"
```

### 第二步:执行批量处理

```bash
python3 （请参考skill目录中的脚本文件） \
  --input ./images/ \
  --scene image-hd-enhance \
  --output ./enhanced/ \
  --parallel 5
```

### 第三步:查看处理报告

```bash
# 生成处理报告
python3 （请参考skill目录中的脚本文件） \
  --input ./enhanced/ \
  --output report.md
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | quark-scan处理的内容输入 |, 默认: 全部维度 |
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
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.9+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 夸克扫描 Pro API | 外部 API | 必需 | 企业服务渠道申请 |
| Python 3.9+ | 运行时 | 必需 | 官方安装 |
| requests | Python 库 | 必需 | pip install requests |
| aiohttp | 异步 HTTP | 推荐 | pip install aiohttp |
| Pillow | 图像处理 | 推荐 | pip install Pillow |

### API Key 配置
- **环境变量名**: `SCAN_WEBSERVICE_KEY`(企业版 Key)
- **附加变量**: `SCAN_EDITION=pro`
- **获取方式**: 通过企业服务渠道申请,享有高优先级处理队列
- **安全建议**: 使用密钥管理服务存储 Key,审计日志记录所有调用
- **隐私提示**: 图片发送至夸克扫描王服务器处理,敏感数据请评估合规风险

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持批量处理、API集成、自定义流水线等企业级文档数字化场景

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

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

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

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

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

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有场景与命令,迁移时仅需更换 API Key 并设置 `SCAN_EDITION=pro`。

### Q2:批量处理支持多少张图片?
A:单批最多 100 张,并发数 1-20 可调。大批量建议分批处理。

### Q3:自定义流水线如何工作?
A:流水线按顺序对每张图片依次应用多个场景处理,前一步的输出作为后一步的输入。

### Q4:处理结果保存多久?
A:专业版支持结果持久化存储,默认保存至 `--output` 指定目录。临时目录的结果可能被系统清理。

### Q5:API 集成支持哪些语言?
A:提供 Python SDK,同时支持 RESTful API 调用,可集成到任意语言系统。

### Q6:能否私有化部署?
A:企业版支持私有化部署方案,数据完全留在企业内网。联系企业服务获取部署文档。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
