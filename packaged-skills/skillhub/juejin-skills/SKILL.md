---
slug: "juejin-skills"
name: "juejin-skills"
version: "1.0.8"
displayName: "掘金技能集"
summary: "掘金技术社区一站式操作技能，支持热门文章排行榜查询。"
license: "MIT"
description: |-
  掘金技术社区一站式操作技能，支持热门文章排行榜查询。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Other
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 掘金技能集

## 核心能力

### 📊 功能一：热门文章排行榜
| 子功能 | 说明 |
| --- | --- |
| 获取分类列表 | 获取掘金所有文章分类（前端、后端、Android、iOS、人工智能等） |
| 热门文章排行 | 获取指定分类或全部分类的热门文章排行榜 |
| 文章趋势分析 | 按时间维度（3天/7天/30天/历史）查看文章热度趋势 |
| 排行榜筛选 | 支持按分类、时间范围、排序方式筛选 |

**API 接口**：

* 分类列表：`GET https://api.juejin.cn/tag_api/v1/query_category_briefs`
* 热门文章：`POST https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed`
* 分类文章：`POST https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed`
* 标签列表：`POST https://api.juejin.cn/tag_api/v1/query_category_tags`

**输入**: 用户提供📊 功能一：热门文章排行榜所需的指令和必要参数。
**输出**: 返回📊 功能一：热门文章排行榜的执行结果,包含操作状态和输出数据。### 📝 功能二：文章自动发布

| 子功能 | 说明 |
| --- | --- |
| 浏览器登录 | 通过 Playwright 打开掘金登录页面，用户扫码或密码登录后自动获取 Cookie |
| Cookie 管理 | 保存、加载、验证 Cookie 状态 |
| Markdown 解析 | 读取本地 Markdown 文件，提取标题、正文内容 |
| 文章发布 | 通过掘金 API 创建草稿并发布，支持设置分类、标签、摘要、封面图 |
| 草稿管理 | 支持保存为草稿而不立即发布 |

**API 接口**：

* 创建草稿：`POST https://api.juejin.cn/content_api/v1/article_draft/create`
* 发布文章：`POST https://api.juejin.cn/content_api/v1/article/publish`
* 获取标签：`POST https://api.juejin.cn/tag_api/v1/query_category_tags`

**鉴权方式**：Cookie 鉴权（通过 Playwright 浏览器登录获取）

### 📥 功能三：文章下载

| 子功能 | 说明 |
| --- | --- |
| 单篇下载 | 通过文章 URL 下载单篇文章，保存为 Markdown |
| 批量下载 | 下载指定作者的所有/部分文章 |
| 格式转换 | 将掘金文章 HTML 内容转换为标准 Markdown |
| 图片处理 | 可选下载文章中的图片到本地 |
| 元数据保留 | 保留文章标题、作者、发布时间、标签等元信息 |

**API 接口**：

* 文章详情：`POST https://api.juejin.cn/content_api/v1/article/detail`
* 用户文章列表：`POST https://api.juejin.cn/content_api/v1/article/query_list`
### 子功能

执行子功能操作,处理用户输入并返回结果。

**输入**: 用户提供子功能所需的参数和指令。

**输出**: 返回子功能的处理结果。

- 执行`子功能`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`子功能`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 掘金技术社区一站、式操作技能、支持热门文章排行、榜查询、核心能力。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

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

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

```text
用户：帮我获取掘金前端分类的热门文章排行榜
AI：正在获取掘金前端分类的热门文章...

用户：把 ./my-article.md 发布到掘金，分类选前端，标签加上 Vue.js 和 TypeScript
AI：正在登录掘金账号并发布文章...

用户：下载这篇掘金文章 https://juejin.cn/post/7300000000000000000
AI：正在下载文章并转换为 Markdown 格式...
```

## 常见问题

### Q1: 如何开始使用掘金技能集？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: 掘金技能集有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

### 本地文件写入安全限制（`filesystem_write`）

* `download_article(...)`、`download_user_articles(...)` 以及内部的
  `_write_markdown_file` / `_download_images` 在写入磁盘之前都会调用
  `juejin_skill.downloader._validate_output_dir()`：
  + 写入路径必须位于 `./output`（或 `$JUEJIN_OUTPUT_ROOT`）之下；
  + 使用 `os.path.realpath` 解析后再比对，可抵御符号链接、`..` 馑越，
    以及伪造后缀绕过检查。
* 任何越出根目录的 `output_dir` 传入都会被以
  `{"success": False, "message": ...}` 形式拒绝，不会创建目录也不会调用 open()。
* 这保证了 SKILL.md 中 `filesystem_write` 边界与代码实际行为一致。

### 批量下载安全限制（`bulk_download_policy`）

* `download_user_articles()` 需要显式 `confirm_bulk=True` 才会执行；
* `max_count` 默认 20、硬上限 `BULK_DOWNLOAD_HARD_CAP=50`，超出会被静默降级；
* 防止在用户仅下载一两篇文章时被意外启动为全量抓取，控制运营风险与平台合规风险。

### 本地文件读取安全限制（`filesystem_read`）

* `publish_markdown(filepath=...)` 会经过
  `juejin_skill.publisher._validate_markdown_path()` 校验，仅接受：
  + 位于当前工作目录（或 `$JUEJIN_MD_ROOT`）之下的 `.md` / `.markdown` 文件；
  + 文件大小 ≤ 2 MiB；
  + 不在 `/etc`、`/var`、`/proc`、`/sys`、`/dev`、`/root`、`/boot`、
    `[REDACTED_SSH_PATH] 等敏感前缀下的文件。
* 路径会使用 `os.path.realpath` 解析后再比对，以防止符号链接逃逸、
  `..` 路径馑越、以及伪造后缀绕过检查。
* 违反任一规则都会抩出 `ValueError`，不会走到 `open()`，也不会被填到
  草稿 / 发布 / 任何外发请求中。

### 图片下载安全限制

* 图片下载功能仅允许下载来自掘金官方域名的图片
* 支持的域名：juejin.cn, p1-juejin.byteimg.com, p3-juejin.byteimg.com, p6-juejin.byteimg.com, p9-juejin.byteimg.com
* 其他域名的图片将被自动跳过，防止SSRF攻击和未经授权的出站请求

### 发布安全机制

* 默认只创建草稿，不公开发布
* 公开发布需要双重确认：`save_draft_only=False` 和 `allow_public_publish=True`
* 命令行工具需要额外的环境变量和交互式确认

### 网络访问限制

* 仅允许访问 juejin.cn 和 api.juejin.cn 域名
* 图片下载有严格的域名白名单限制
* 防止潜在的策略绕过和跟踪风险
