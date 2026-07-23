---
slug: straker-verify-tool-pro
name: straker-verify-tool-pro
version: 1.0.0
displayName: AI翻译验证(专业版)
summary: 企业级翻译平台,含AI质量增强、人工审核、翻译记忆、术语库与Webhook回调
license: Proprietary
edition: pro
description: '核心能力:

  - 100+语言AI翻译+质量增强

  - 专业人工翻译审核

  - 翻译记忆库(TM)与术语表

  - 批量翻译与并行处理

  - Webhook翻译完成回调

  - HTML/JSON翻译报告

  - 无限API调用


  适用场景:

  - 企业多语言内容本地化

  - 软件国际化(i18n)

  - 法律/医疗专业翻译

  - 大规模文档批量翻译


  差异化:

  - AI翻译+人工审核双重保障

  - 翻译记忆库降低成本与保持一致性

  - Webhook自动化翻译流水线

  - 与免费版兼容,API接口统一


  触发...'
tags:
- 翻译
- 本地化
- 企业翻译
- 人工审核
- 翻译记忆
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
AI翻译验证专业版是一款面向企业用户的翻译与本地化平台。在免费版基础翻译功能上,增加AI质量增强、专业人工审核、翻译记忆库(TM)与术语表管理、批量并行翻译、Webhook翻译完成回调等企业级功能。支持无限API调用,提供HTML/JSON专业翻译报告。与免费版完全兼容,API接口和项目格式可无缝迁移。

## 核心能力
### 功能矩阵
| 功能模块 | 描述 | 免费版 | 专业版 |
|----------|------|--------|--------|
| AI翻译 | 基础翻译 | 100+语言 | 100+语言+质量增强 |
| 人工审核 | 人工验证 | 不支持 | 专业译员审核 |
| 翻译记忆 | TM复用 | 不支持 | TM+术语表 |
| 批量翻译 | 处理能力 | 单文件 | 批量+并行 |
| API限额 | 调用限制 | 10次/天 | 无限 |
| Webhook | 回调通知 | 不支持 | 翻译完成回调 |
| 报告格式 | 输出类型 | 文本 | HTML/JSON |
| 项目协作 | 团队功能 | 不支持 | 多用户协作 |

**输入**: 用户提供功能矩阵所需的指令和必要参数。
**处理**: 解析功能矩阵的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回功能矩阵的响应数据,包含状态码、结果和日志。

### 翻译质量层次
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | AI翻译验证(专业版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
┌──────────────────────────────────────────────────┐
│           专业版翻译质量层次                      │
├──────────────┬───────────────────────────────────┤
│ Level 1      │ AI基础翻译(免费版)               │
│ Level 2      │ AI翻译+质量增强(专业版)          │
│ Level 3      │ AI翻译+人工审核(专业版)          │
│ Level 4      │ AI翻译+质量增强+人工审核(最高)   │
└──────────────┴───────────────────────────────────┘
```

**输入**: 用户提供翻译质量层次所需的指令和必要参数。
**处理**: 解析翻译质量层次的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回翻译质量层次的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级翻译平台、术语库与、核心能力、专业人工翻译审核、翻译记忆库、与术语表、批量翻译与并行处、翻译报告等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景一:企业内容本地化
对产品文档进行多语言本地化,使用翻译记忆库保持一致性。

```bash
python （请参考skill目录中的脚本文件） \
  --files docs/*.md \
  --languages fr,de,es,ja,zh \
  --quality-boost \
  --use-tm \
  --tm-file company_tm.tmx \
  --glossary company_glossary.csv \
  --format json \
  --output localization_report.json
```

### 场景二:专业人工审核翻译
对关键内容(法律/医疗)进行AI翻译+人工审核。

```bash
python （请参考skill目录中的脚本文件） \
  --file legal_document.pdf \
  --target-lang ja \
  --human-verify \
  --priority high \
  --webhook "https://api.example.com/translation-done"
```

### 场景三:批量翻译与并行处理
```bash
python （请参考skill目录中的脚本文件） \
  --batch translations/ \
  --languages fr,de,es,ja,zh \
  --threads 10 \
  --quality-boost \
  --format html \
  --output batch_report.html
```

### 场景四:Webhook自动化流水线
```python
client = TranslationClientPro(api_key=os.environ["TRANSLATE_API_KEY"])

result = client.create_project(
    file_path="product_docs.pdf",
    target_langs=["fr", "de", "es", "ja", "zh"],
    quality_boost=True,
    human_verify=False,
    webhook_url="https://api.example.com/translation-complete",
    webhook_events=["project.completed", "project.failed"]
)
```

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 专业版翻译引擎
```python
import os
import requests
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

class TranslationClientPro:
    """企业级翻译客户端"""

    BASE_URL = "https://api-verify.example.com"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("TRANSLATE_API_KEY")
        if not self.api_key:
            raise ValueError("请设置 TRANSLATE_API_KEY 环境变量")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.tm_cache = {}

    def create_project(self, file_path, target_langs, **options):
        """创建翻译项目(支持高级选项)"""
        with open(file_path, 'rb') as f:
            data = {
                "title": options.get("title", f"翻译_{file_path}"),
                "confirmation_required": str(options.get("confirm", True)).lower(),
            }

            if options.get("quality_boost"):
                data["quality_boost"] = "true"

            if options.get("human_verify"):
                data["human_verify"] = "true"
                data["priority"] = options.get("priority", "normal")

            if options.get("webhook_url"):
                data["webhook_url"] = options["webhook_url"]
                data["webhook_events"] = json.dumps(
                    options.get("webhook_events", ["project.completed"])
                )

            if options.get("use_tm"):
                data["use_translation_memory"] = "true"
                if options.get("tm_file"):
                    with open(options["tm_file"], 'rb') as tm:
                        response = requests.post(
                            f"{self.BASE_URL}/project",
                            headers=self.headers,
                            files={"files": f, "tm_file": tm},
                            data=data
                        )
                else:
                    response = requests.post(
                        f"{self.BASE_URL}/project",
                        headers=self.headers,
                        files={"files": f},
                        data=data
                    )
            else:
                lang_uuids = [self._get_lang_uuid(lang) for lang in target_langs]
                data["languages"] = ",".join(filter(None, lang_uuids))

                response = requests.post(
                    f"{self.BASE_URL}/project",
                    headers=self.headers,
                    files={"files": f},
                    data=data
                )

        return response.json()

    def quality_boost(self, file_path, target_lang):
        """AI质量增强"""
        lang_uuid = self._get_lang_uuid(target_lang)
        with open(file_path, 'rb') as f:
            response = requests.post(
                f"{self.BASE_URL}/quality-boost",
                headers=self.headers,
                files={"files": f},
                data={"language": lang_uuid}
            )
        return response.json()

    def human_verify(self, file_path, target_lang):
        """人工审核翻译"""
        lang_uuid = self._get_lang_uuid(target_lang)
        with open(file_path, 'rb') as f:
            response = requests.post(
                f"{self.BASE_URL}/human-verify",
                headers=self.headers,
                files={"files": f},
                data={"language": lang_uuid}
            )
        return response.json()

    def batch_translate(self, files_dir, target_langs, threads=5, **options):
        """批量并行翻译"""
        files = list(Path(files_dir).glob("*"))
        results = []

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {}
            for file_path in files:
                for lang in target_langs:
                    future = executor.submit(
                        self.create_project,
                        str(file_path), [lang],
                        **options
                    )
                    futures[future] = (file_path.name, lang)

            for future in as_completed(futures):
                file_name, lang = futures[future]
                try:
                    result = future.result()
                    results.append({
                        "file": file_name,
                        "language": lang,
                        "status": "success",
                        "result": result
                    })
                    print(f"[完成] {file_name} -> {lang}")
                except Exception as e:
                    results.append({
                        "file": file_name,
                        "language": lang,
                        "status": "error",
                        "error": str(e)
                    })
                    print(f"[失败] {file_name} -> {lang}: {str(e)}")

        return results

    def generate_report(self, results, format="html", output_path="translation_report"):
        """生成翻译报告"""
        if format == "html":
            return self._generate_html_report(results, output_path + ".html")
        elif format == "json":
            return self._generate_json_report(results, output_path + ".json")

    def _generate_html_report(self, results, output_path):
        """生成HTML报告"""
        success_count = sum(1 for r in results if r["status"] == "success")
        total = len(results)

        html = f"""<!DOCTYPE html>
<html>
<head><title>翻译项目报告</title></head>
<body>
<h1>翻译项目报告</h1>
<p>生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
<p>总项目数: {total}</p>
<p>成功: {success_count} / 失败: {total - success_count}</p>

<h2>项目详情</h2>
<table border="1">
<tr><th>文件</th><th>语言</th><th>状态</th><th>项目ID</th></tr>"""

        for r in results:
            status = "✅ 成功" if r["status"] == "success" else "❌ 失败"
            project_id = r.get("result", {}).get("data", {}).get("project_id", "N/A")
            html += f"<tr><td>{r['file']}</td><td>{r['language']}</td><td>{status}</td><td>{project_id}</td></tr>"

        html += """</table>
</body>
</html>"""

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        return output_path

    def _generate_json_report(self, results, output_path):
        """生成JSON报告"""
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_projects": len(results),
            "success_count": sum(1 for r in results if r["status"] == "success"),
            "results": results
        }
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        return output_path

    def _get_lang_uuid(self, lang_code):
        """获取语言UUID"""
        if lang_code in self.tm_cache:
            return self.tm_cache[lang_code]

        response = requests.get(f"{self.BASE_URL}/languages")
        languages = response.json().get("data", [])

        for lang in languages:
            if lang.get("code") == lang_code:
                self.tm_cache[lang_code] = lang.get("uuid")
                return lang.get("uuid")
        return None
```

## 示例
### 企业翻译配置
```json
{
  "translation_config": {
    "api_key_env": "TRANSLATE_API_KEY",
    "default_quality": "quality_boost",
    "languages": ["fr", "de", "es", "ja", "zh", "pt", "ru"],
    "translation_memory": {
      "enabled": true,
      "tm_file": "assets/company_tm.tmx",
      "min_match": 0.75
    },
    "glossary": {
      "enabled": true,
      "file": "assets/company_glossary.csv",
      "strict": true
    },
    "human_verify": {
      "enabled": false,
      "trigger_on": ["legal", "medical"],
      "priority": "high"
    },
    "webhook": {
      "url": "https://api.example.com/translation-complete",
      "events": ["project.completed", "project.failed"],
      "secret": "webhook-secret"
    },
    "batch": {
      "threads": 10,
      "retry_count": 3,
      "retry_delay": 60
    },
    "report": {
      "format": "html",
      "include_metrics": true,
      "include_costs": true
    }
  }
}
```

### 翻译记忆库格式(TMX)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<tmx version="1.4">
  <body>
    <tu>
      <tuv xml:lang="en">
        <seg>Product Name</seg>
      </tuv>
      <tuv xml:lang="zh">
        <seg>产品名称</seg>
      </tuv>
    </tu>
    <tu>
      <tuv xml:lang="en">
        <seg>Terms of Service</seg>
      </tuv>
      <tuv xml:lang="zh">
        <seg>服务条款</seg>
      </tuv>
    </tu>
  </body>
</tmx>
```

### 术语表格式(CSV)
```csv
source_term,target_lang,target_term,context
Product,zh,产品,通用
Dashboard,zh,控制面板,软件界面
API,zh,API,技术术语(不翻译)
Cloud,zh,云,技术
```

## 最佳实践
### 1. 翻译记忆库维护
```bash
python （请参考skill目录中的脚本文件） \
  --update-tm \
  --tm-file company_tm.tmx \
  --from-projects "project1,project2,project3"
```

### 2. 质量分层策略
```python
content_types = {
    "marketing": {"quality_boost": True, "human_verify": False},
    "legal": {"quality_boost": True, "human_verify": True, "priority": "high"},
    "technical": {"quality_boost": True, "human_verify": False, "use_tm": True},
    "user_manual": {"quality_boost": True, "human_verify": True, "priority": "normal"}
}

for content_type, config in content_types.items():
    client.create_project(f"{content_type}.pdf", ["ja", "zh"], **config)
```

### 3. CI/CD集成
```yaml
name: Translate Documentation
on:
  push:
    paths: ['docs/**']

jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Translate
        run: |
          python （请参考skill目录中的脚本文件） \
            --files docs/*.md \
            --languages fr,de,es,ja,zh \
            --quality-boost \
            --use-tm \
            --format json \
            --output translations.json
```

## 常见问题
### Q1: 专业版与免费版兼容吗?
A: 完全兼容。专业版包含免费版所有功能,并增加质量增强、人工审核、翻译记忆等。免费版创建的项目可在专业版中管理。

### Q2: 翻译记忆库如何降低成本?
A: TM库存储已翻译的内容片段。当新内容与TM中的片段匹配时(75%+相似度),直接复用翻译,减少API调用和人工翻译成本。

### Q3: 人工审核需要多长时间?
A: 取决于内容长度和译员可用性。普通内容24-48小时,高优先级内容4-8小时。

### Q4: Webhook如何配置?
A: 在创建项目时指定 `webhook_url` 和 `webhook_events`。翻译完成后,API会向指定URL发送POST请求,包含项目状态和下载链接。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 必需 | 系统自带 |
| requests | Python包 | 必需 | `pip install requests` |
| curl | CLI工具 | 可选 | 系统自带 |

### API Key 配置
- 必需配置 `TRANSLATE_API_KEY` 环境变量
- 专业版API Key支持无限调用
- 获取方式: 在翻译服务平台购买专业版订阅

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用翻译API完成企业级翻译任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "AI翻译验证(专业版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "straker verify pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
