# 开源 AI Agent Skills 分类总目录 (v2.0 深度搜索版)

> 收录日期: 2026-07-17 (第二轮深度搜索更新)
> 来源: GitHub 全网检索 + 官方 Skill 目录站 + 社区精选
> 收录原则: 高 Star / 高下载量 / 高商业化潜力 / 直接可用性
> 共收录 **68 个** 优质开源 Skill,覆盖 **8 大类别**(新增 Agent框架类 + 数据处理类)
> 新增字段: **依赖要求** + **直接可用性分级**

---

## 目录索引

- [A. 内容创作类 (视频/文案/设计)](#a-内容创作类-videocopydesign)
- [B. 开发工具类 (代码审查/安全/架构)](#b-开发工具类-代码审查安全架构)
- [C. 效率工具类 (PPT/表格/研究)](#c-效率工具类-ppt表格研究)
- [D. 商业工具类 (SEO/CRO/销售)](#d-商业工具类-seocro销售)
- [E. 创意设计类 (前端/品牌)](#e-创意设计类-前端品牌)
- [F. 专业垂直类 (法律/云/企业)](#f-专业垂直类-法律云企业)
- [G. Agent框架类 (编排/构建/子代理)](#g-agent框架类-编排构建子代理) **[新增]**
- [H. 数据处理类 (数据库/分析/ETL)](#h-数据处理类-数据库分析etl) **[新增]**
- [分类统计](#分类统计)
- [直接可用性统计](#直接可用性统计)
- [商业化评分说明](#商业化评分说明)
- [数据来源与可信度](#数据来源与可信度)

---

## 直接可用性图例

| 标记 | 含义 | 说明 |
|:-----|:-----|:-----|
| **MD** | 纯Markdown可直接用 | 仅需 SKILL.md,无需安装任何依赖,任何支持 Agent Skills 的平台直接加载 |
| **PY** | 需要Python环境 | 需要 Python 3.10+ 及特定 pip 包 |
| **NODE** | 需要Node环境 | 需要 Node.js 18+ 及特定 npm 包 |
| **DOCKER** | 需要Docker | 需要 Docker 运行时 |
| **API** | 需要外部API Key | 需要第三方服务 API Key(如 OpenAI/Gemini/Stripe 等) |
| **MD+API** | 纯MD+API Key | SKILL 本身是纯 Markdown,但执行时需要外部 API Key |

---

## A. 内容创作类 (Video/Copy/Design)

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| A1 | remotion-video-creator | [remotion-dev/skills](https://github.com/remotion-dev/skills) | 28k+ | 用 React 代码生成视频,支持自然语言转视频代码、字幕、转场、配音 | MIT | 高 | Node.js 18+, React, Remotion | NODE | `remotion-video-studio` 视频创作工作室 |
| A2 | slack-gif-creator | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 创建适配 Slack 大小限制的动画 GIF,可组合动画原语 | Apache-2.0 | 中 | Node.js, sharp 库 | NODE | `gif-meme-factory` 动图表情包工厂 |
| A3 | canvas-design | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 用设计哲学在 PNG/PDF 上创建精美视觉艺术(海报/设计/静态作品) | Apache-2.0 | 高 | Python 3.10+, Pillow, matplotlib | PY | `canvas-art-designer` 画布艺术设计器 |
| A4 | content-research-writer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 高质量内容写作助手:研究、引用、钩子优化、分段反馈 | Apache-2.0 | 高 | 无额外依赖 | MD | `research-article-crafter` 研究文章匠人 |
| A5 | twitter-algorithm-optimizer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 基于 Twitter 开源算法分析优化推文,最大化触达与互动 | Apache-2.0 | 高 | 无额外依赖 | MD | `twitter-viral-optimizer` 推特爆款优化器 |
| A6 | video-downloader | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | YouTube 等平台视频下载,支持多种格式与画质 | Apache-2.0 | 中 | yt-dlp (pip) | PY | `video-harvester` 视频素材收割机 |
| A7 | image-enhancer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 提升图片/截图分辨率、锐度、清晰度,适配专业展示 | Apache-2.0 | 中 | Python, Pillow/real-esrgan | PY | `image-quality-booster` 图片画质增强器 |
| A8 | markdown-to-epub | [smerchek/claude-epub-skill](https://github.com/smerchek/claude-epub-skill) | 社区贡献 | 将 Markdown 文档/聊天摘要转为专业 EPUB 电子书 | MIT | 高 | pandoc, ebook-meta | PY | 合并入 `ebook-factory` |
| A9 | youtube-transcript | [michalparkola/tapestry-skills](https://github.com/michalparkola/tapestry-skills) | 社区贡献 | 获取 YouTube 视频字幕并生成摘要 | MIT | 中 | youtube-transcript-api (pip) | PY | `video-transcript-miner` 视频字幕挖掘机 |
| A10 | article-extractor | [michalparkola/tapestry-skills](https://github.com/michalparkola/tapestry-skills) | 社区贡献 | 从网页提取完整文章正文与元数据 | MIT | 中 | Python, trafilatura | PY | 合并入 `topic-hunter` |
| A11 | typefully-scheduler | [typefully/typefully](https://officialskills.sh/typefully/skills/typefully) | 官方 | 创建、排期、发布社交媒体内容到 X/LinkedIn/Threads/Bluesky/Mastodon | MIT | 高 | Typefully API Key | MD+API | `social-media-scheduler` 社媒排期发布器 |
| A12 | replicate-model-runner | [replicate/replicate](https://officialskills.sh/replicate/skills/replicate) | 官方 | 发现、对比、运行 AI 模型(图像/视频/音频/LLM)使用 Replicate API | MIT | 高 | Replicate API Key, Python/Node | MD+API | `ai-model-runner` AI模型运行器 |
| A13 | venice-image-generator | [veniceai/skills](https://github.com/veniceai/skills) | 官方 | Venice API 图像生成、编辑、放大、背景移除 | MIT | 中 | Venice API Key | MD+API | 合并入 `ai-artist-workstation` |
| A14 | algorithmic-art | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 用 p5.js 种子随机性创建生成艺术 | Apache-2.0 | 中 | Node.js, p5.js | NODE | `generative-art-studio` 生成艺术工作室 |

---

## B. 开发工具类 (代码审查/安全/架构)

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| B1 | code-review-and-quality | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | 五维度代码审查,变更尺寸控制(~100行),严重度标签,拆分策略 | MIT | 高 | 无额外依赖 | MD | `code-review-sentinel` 代码审查哨兵 |
| B2 | test-driven-development | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) + [obra/superpowers](https://github.com/obra/superpowers) | 78.8k + 16k | Red-Green-Refactor,测试金字塔(80/15/5),DAMP 优于 DRY | MIT | 高 | 无额外依赖 | MD | `test-driven-coder` 测试驱动编码器 |
| B3 | security-and-hardening | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | OWASP Top 10 防护、认证模式、密钥管理、依赖审计、三层边界 | MIT | 高 | 无额外依赖 | MD | `security-hardening-shield` 安全加固之盾 |
| B4 | frontend-ui-engineering | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | 组件架构、设计系统、状态管理、响应式、WCAG 2.1 AA 无障碍 | MIT | 高 | 无额外依赖 | MD | `frontend-design-craftsman` 前端设计工匠 |
| B5 | api-and-interface-design | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | 契约优先设计、Hyrum 定律、One-Version 规则、错误语义、边界校验 | MIT | 高 | 无额外依赖 | MD | `api-design-architect` API设计架构师 |
| B6 | spec-driven-development | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | 编码前先写 PRD(目标/命令/结构/代码风格/测试/边界) | MIT | 高 | 无额外依赖 | MD | `spec-driven-planner` 规格驱动规划师 |
| B7 | performance-optimization | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | 测量优先、Core Web Vitals 目标、性能分析工作流、反模式检测 | MIT | 高 | 无额外依赖 | MD | `performance-optimizer-pro` 性能优化专家 |
| B8 | debugging-and-error-recovery | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | 五步分诊(复现/定位/缩减/修复/守护),Stop-the-line 规则 | MIT | 中 | 无额外依赖 | MD | `debug-doctor` 调试医生 |
| B9 | code-simplification | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | Chesterton 栅栏原则、Rule of 500、保持行为不变降低复杂度 | MIT | 中 | 无额外依赖 | MD | `code-slimmer` 代码瘦身师 |
| B10 | mcp-builder | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 高质量 MCP 服务器构建指南(Python/TypeScript),集成外部 API | Apache-2.0 | 高 | Python 或 Node.js | MD | `mcp-server-builder` MCP服务器构建器 |
| B11 | web-artifacts-builder | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | React/Tailwind/shadcn 构建复杂多组件 claude.ai HTML 工件 | Apache-2.0 | 高 | Node.js, React | NODE | `web-artifact-studio` Web工件工作室 |
| B12 | webapp-testing | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | Playwright 测试本地 Web 应用,验证前端功能、调试 UI、截图 | Apache-2.0 | 中 | Node.js, Playwright | NODE | 合并入 `stealth-browser-assistant` |
| B13 | browser-testing-with-devtools | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k(总仓) | Chrome DevTools MCP 获取运行时数据:DOM、控制台、网络、性能 | MIT | 中 | Chrome DevTools Protocol | NODE | `devtools-profiler` DevTools性能分析器 |
| B14 | great_cto | [avelikiy/great_cto](https://github.com/avelikiy/great_cto) | 社区贡献 | 7 个专业子代理(Tech Lead/Dev/QA/Sec/DevOps)编排完整 SDLC | MIT | 高 | 无额外依赖 | MD | `virtual-cto` 虚拟CTO |
| B15 | langsmith-fetch | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 自动获取并分析 LangSmith 执行追踪,调试 LangChain/LangGraph | Apache-2.0 | 中 | LangSmith API Key | MD+API | `agent-debugger` Agent调试器 |
| B16 | lean-ctx | [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | 社区贡献 | MCP 服务器+上下文运行时:会话缓存、AST 压缩、90+ shell 模式降 token | MIT | 高 | Python, MCP | PY | `context-slimmer` 上下文瘦身器 |
| B17 | skill-creator | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 创建高效 Claude Skills 的指南:专业知识/工作流/工具集成 | Apache-2.0 | 中 | 无额外依赖 | MD | 元技能,内部使用 |
| B18 | software-architecture | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 社区贡献 | Clean Architecture、SOLID 原则、软件设计最佳实践 | MIT | 高 | 无额外依赖 | MD | `architecture-mentor` 架构导师 |
| B19 | prompt-engineering | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 社区贡献 | 教授提示工程技术与模式,含 Anthropic 最佳实践与代理说服原则 | MIT | 高 | 无额外依赖 | MD | `prompt-engineer-pro` 提示工程师Pro |
| B20 | subagent-driven-development | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 社区贡献 | 为独立任务分派子代理,迭代间设代码审查检查点 | MIT | 中 | 无额外依赖 | MD | 合并入 `virtual-cto` |
| B21 | playwright-browser-automation | [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) | 社区贡献 | 模型调用的 Playwright 自动化,测试与验证 Web 应用 | MIT | 中 | Node.js, Playwright | NODE | 合并入 `stealth-browser-assistant` |
| B22 | ffuf-web-fuzzing | [jthack/ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill) | 社区贡献 | 集成 ffuf Web 模糊测试器,Claude 运行模糊任务并分析漏洞 | MIT | 中 | Go (ffuf 二进制) | DOCKER | `web-fuzz-hunter` Web模糊猎手 |
| B23 | full-page-screenshot | [LewisLiu007/full-page-screenshot](https://github.com/LewisLiu007/full-page-screenshot) | 社区贡献 | Chrome DevTools 协议全页截图,零依赖 | MIT | 中 | Chrome 浏览器 | NODE | `screenshot-pro` 截图大师 |
| B24 | stripe-best-practices | [stripe/skills](https://officialskills.sh/stripe/skills/stripe-best-practices) | 官方 | Stripe 支付集成最佳实践:SDK 使用、API 版本管理、webhook 处理 | MIT | 高 | Stripe API Key (执行时) | MD | `stripe-payment-integrator` 支付集成专家 |
| B25 | stripe-upgrade | [stripe/skills](https://officialskills.sh/stripe/skills/upgrade-stripe) | 官方 | 升级 Stripe SDK 和 API 版本,自动迁移指南 | MIT | 中 | Stripe SDK, Node.js | MD | 合并入 `stripe-payment-integrator` |
| B26 | trail-of-bits-security | [trailofbits/skills](https://github.com/trailofbits/skills) | 官方 | 专业安全审计:CodeQL 静态分析、Semgrep 漏洞扫描、安全审查工作流 | MIT | 高 | CodeQL, Semgrep | PY | `security-audit-pro` 安全审计Pro |
| B27 | nextjs-best-practices | [vercel-labs/skills](https://officialskills.sh/vercel-labs/skills/next-best-practices) | 官方 | Next.js 最佳实践:App Router、Server Components、数据获取模式 | Apache-2.0 | 高 | Node.js, Next.js | NODE | `nextjs-fullstack-guide` Next.js全栈指南 |
| B28 | cloudflare-workers | [cloudflare/skills](https://officialskills.sh/cloudflare/skills/workers-best-practices) | 官方 | Cloudflare Workers 生产级代码审查与编写,wrangler.jsonc 规范 | MIT | 高 | Node.js, wrangler CLI | NODE | `cloudflare-edge-developer` 边缘计算开发者 |
| B29 | netlify-functions | [netlify/skills](https://officialskills.sh/netlify/skills/netlify-functions) | 官方 | 构建 Serverless API 端点和后台任务,Netlify Functions 部署 | MIT | 中 | Node.js, Netlify CLI | NODE | `serverless-api-builder` 无服务器API构建器 |
| B30 | react-best-practices | [vercel-labs/skills](https://officialskills.sh/vercel-labs/skills/react-best-practices) | 官方 | React 组件模式、状态管理、性能优化、Hooks 最佳实践 | Apache-2.0 | 高 | Node.js, React | NODE | 合并入 `frontend-design-craftsman` |
| B31 | terraform-style-guide | [hashicorp/skills](https://officialskills.sh/hashicorp/skills/terraform-style-guide) | 官方 | 生成符合 HashiCorp 官方风格规范的 Terraform HCL 代码 | MIT | 高 | Terraform CLI | MD | `terraform-iac-architect` IaC架构师 |
| B32 | terraform-provider-dev | [hashicorp/skills](https://officialskills.sh/hashicorp/skills/new-terraform-provider) | 官方 | 使用 Plugin Framework 脚手架搭建新 Terraform Provider 项目 | MIT | 中 | Go, Terraform | MD | 合并入 `terraform-iac-architect` |
| B33 | better-auth | [better-auth/skills](https://officialskills.sh/better-auth/skills/best-practices) | 官方 | Better Auth 集成最佳实践:认证、2FA、组织管理、OAuth Provider | MIT | 高 | Node.js, better-auth | NODE | `auth-security-architect` 认证安全架构师 |
| B34 | apollo-graphql | [apollographql/skills](https://officialskills.sh/apollographql/skills) | 官方 | Apollo GraphQL 最佳实践:Schema 设计、Federation、缓存策略 | MIT | 中 | Node.js, Apollo | NODE | `graphql-api-architect` GraphQL API架构师 |
| B35 | sentry-error-tracking | [getsentry/skills](https://officialskills.sh/getsentry/skills) | 官方 | Sentry 错误追踪集成:异常监控、性能监控、Release 追踪 | MIT | 中 | Sentry DSN | MD+API | `error-tracking-pro` 错误追踪Pro |

---

## C. 效率工具类 (PPT/表格/研究)

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| C1 | pptx | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 读取、生成、调整幻灯片、布局、模板 | Apache-2.0 | 高 | Python, python-pptx | PY | `pptx-presentation-pro` 演示文稿大师 |
| C2 | xlsx | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 电子表格操作:公式、图表、数据转换 | Apache-2.0 | 高 | Python, openpyxl | PY | `xlsx-data-wizard` 电子表格魔法师 |
| C3 | docx | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 创建/编辑/分析 Word 文档:修订、批注、格式 | Apache-2.0 | 高 | Python, python-docx | PY | `docx-document-master` 文档处理大师 |
| C4 | pdf | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 提取文本、表格、元数据,合并与注释 PDF | Apache-2.0 | 高 | Python, PyPDF2/pdfplumber | PY | `pdf-toolkit-pro` PDF工具箱Pro |
| C5 | csv-data-summarizer | [coffeefuelbump/csv-data-summarizer-claude-skill](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) | 社区贡献 | 自动分析 CSV 文件并生成全面洞察与可视化,无需用户提示 | MIT | 高 | Python, pandas, matplotlib | PY | `csv-insight-miner` CSV洞察挖掘机 |
| C6 | deep-research | [sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) | 社区贡献 | 用 Gemini Deep Research 执行自主多步研究:市场分析/竞品/文献 | MIT | 高 | Gemini API Key | MD+API | `deep-research-engine` 深度研究引擎 |
| C7 | recursive-research | [Anjos2/recursive-research](https://github.com/Anjos2/recursive-research) | 社区贡献 | PhD 级递归研究,跨域(科技/商业/艺术),来源分层+磁盘检查点 | MIT | 高 | Python, 联网搜索 | PY | `phd-research-recursive` 博士级递归研究 |
| C8 | changelog-generator | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 从 git 提交自动生成面向用户的更新日志 | Apache-2.0 | 中 | git CLI | MD | `release-notes-writer` 发布说明撰稿人 |
| C9 | file-organizer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 智能文件整理与归类 | Apache-2.0 | 中 | 无额外依赖 | MD | `file-tidier` 文件整理师 |
| C10 | invoice-organizer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 发票整理与归档 | Apache-2.0 | 中 | 无额外依赖 | MD | `invoice-manager` 发票管家 |
| C11 | meeting-insights-analyzer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 分析会议记录,挖掘行为模式:冲突回避、发言比、口头禅、领导风格 | Apache-2.0 | 高 | 无额外依赖 | MD | `meeting-insights-pro` 会议洞察Pro |
| C12 | domain-name-brainstormer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 创意域名头脑风暴,检查 .com/.io/.dev/.ai 等多 TLD 可用性 | Apache-2.0 | 中 | 联网(域名查询) | MD | `domain-brainstormer` 域名头脑风暴器 |
| C13 | tailored-resume-generator | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 针对职位描述定制简历生成 | Apache-2.0 | 高 | 无额外依赖 | MD | `resume-tailor-pro` 简历定制师Pro |
| C14 | notebooklm-integration | [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | 社区贡献 | Claude Code 直接对话 NotebookLM,基于上传文档给出有源答案 | MIT | 中 | NotebookLM 访问 | MD | `notebooklm-bridge` NotebookLM桥接器 |
| C15 | pypict-claude-skill | [omkamal/pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) | 社区贡献 | 用 PICT 设计成对组合测试用例,生成优化测试套件 | MIT | 中 | Python, PICT | PY | `combinatorial-test-designer` 组合测试设计器 |
| C16 | postgres-safe-query | [sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) | 社区贡献 | 对 PostgreSQL 执行安全只读 SQL 查询,多连接+纵深防御 | MIT | 中 | Python, psycopg2, PostgreSQL | PY | `postgres-query-safe` Postgres安全查询器 |
| C17 | root-cause-tracing | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 执行深处出错时回溯找原始触发点 | MIT | 中 | 无额外依赖 | MD | 合并入 `debug-doctor` |
| C18 | resend-email-sender | [resend/skills](https://officialskills.sh/resend/skills) | 官方 | Resend 邮件发送 API 集成:事务邮件、模板、批量发送 | MIT | 中 | Resend API Key, Node.js | MD+API | `email-sender-pro` 邮件发送Pro |
| C19 | notion-integration | [notion/skills](https://officialskills.sh/notion/skills) | 官方 | Notion API 集成:页面创建、数据库查询、内容管理 | MIT | 高 | Notion API Key | MD+API | `notion-workspace-manager` Notion工作区管理器 |
| C20 | sanity-cms | [sanity-io/skills](https://officialskills.sh/sanity-io/skills/sanity-best-practices) | 官方 | Sanity CMS 最佳实践:Studio 配置、GROQ 查询、内容工作流 | MIT | 中 | Node.js, Sanity CLI | NODE | `content-cms-architect` CMS内容架构师 |

---

## D. 商业工具类 (SEO/CRO/销售)

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| D1 | seo-audit | [coreyhaines31/marketing-skills](https://github.com/coreyhaines31/marketing-skills) | 32.9k | Claude SEO 审计、架构验证与优化 | MIT | 高 | 无额外依赖 | MD | `seo-audit-master` SEO审计大师 |
| D2 | copywriting | [coreyhaines31/marketing-skills](https://github.com/coreyhaines31/marketing-skills) | 32.9k(总仓) | 12 种文案模板,营销文案写作辅助 | MIT | 高 | 无额外依赖 | MD | `copywriting-master` 营销文案大师 |
| D3 | competitive-ads-extractor | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 从广告库提取并分析竞品广告,理解信息与创意策略 | Apache-2.0 | 高 | 联网(广告库爬取) | MD | `competitive-ad-spy` 竞品广告侦察兵 |
| D4 | lead-research-assistant | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 分析产品、搜索目标公司、提供可执行外联策略,识别高质量线索 | Apache-2.0 | 高 | 联网搜索 | MD | `lead-research-hunter` 销售线索猎手 |
| D5 | internal-comms | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 撰写内部沟通:3P 更新、公司简报、FAQ、状态报告、项目更新 | Apache-2.0 | 高 | 无额外依赖 | MD | `internal-comms-craftsman` 内部沟通匠人 |
| D6 | building-blog | [BuildShipGrowRepeat/nextjs-sanity-blog-skill](https://github.com/BuildShipGrowRepeat/nextjs-sanity-blog-skill) | 社区贡献 | 为 Next.js+Sanity 站点添加 SEO 优先、i18n 就绪博客 | MIT | 中 | Node.js, Next.js, Sanity | NODE | `seo-blog-builder` SEO博客构建器 |
| D7 | brand-build-skills | [rampstackco/claude-skills](https://github.com/rampstackco/claude-skills) | 社区贡献 | 59 技能库覆盖网站全生命周期:品牌/设计/内容/SEO/开发/运营/增长 | MIT | 高 | 无额外依赖 | MD | `brand-growth-suite` 品牌增长套件 |
| D8 | developer-growth-analysis | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k(总仓) | 分析编码模式与开发者成长 | Apache-2.0 | 中 | 无额外依赖 | MD | `dev-growth-analyst` 开发者成长分析师 |
| D9 | d3js-visualization | [chrisvoncsefalvay/claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) | 社区贡献 | 教 Claude 生成 D3 图表与交互式数据可视化 | MIT | 高 | Node.js, D3.js | NODE | `d3-visualization-pro` D3可视化专家 |
| D10 | septim-agents-pack | septimlabs-code | 商业产品 | 10 个命名子代理(规划/架构/品牌/营销/财务/设计/法务/客户/研究/协调) | 商业 | 中 | 无额外依赖 | MD | 企业版参考,暂不包装 |
| D11 | connect-apps | [composiohq/skills](https://officialskills.sh/composiohq/skills/composio) | 官方 | 连接 Claude 到 1000+ 应用,发邮件/建 issue/发 Slack/更新数据库 | Apache-2.0 | 高 | Composio API Key | MD+API | `app-connector-hub` 应用连接中枢 |
| D12 | product-manager-pro | [deanpeters/skills](https://officialskills.sh/deanpeters/skills) + [pawelhuryn/skills](https://officialskills.sh/pawelhuryn/skills) | 官方 | 产品管理全流程:发现/规划/路线图/优先级/用户研究/实验设计 | MIT | 高 | 无额外依赖 | MD | `product-manager-pro` 产品经理Pro |
| D13 | advertising-skills | [kimbarrett/skills](https://officialskills.sh/kimbarrett/skills) | 官方 | 广告创意与投放策略:文案/受众/预算/AB测试/ROI优化 | MIT | 高 | 无额外依赖 | MD | `ad-campaign-optimizer` 广告活动优化器 |
| D14 | c-level-advisory | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k | 全 C 套件顾问(CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO)+ 创始人模式 | MIT | 高 | 无额外依赖 | MD | `c-suite-advisor` C套件顾问 |
| D15 | compliance-os | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k(总仓) | 合规操作系统:控制项/证据管理/审计就绪工作流 | MIT | 高 | 无额外依赖 | MD | `compliance-manager` 合规管理器 |
| D16 | aeo-answer-engine-opt | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k(总仓) | AEO(答案引擎优化):E-E-A-T 审计、5 大 LLM 引用追踪 | MIT | 高 | 无额外依赖 | MD | `aeo-citation-tracker` AEO引用追踪器 |

---

## E. 创意设计类 (前端/品牌)

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| E1 | frontend-design | [vercel-labs/skills](https://github.com/vercel-labs/skills) | 高 | 独特、生产级前端界面,高设计质量,避免通用 AI 美学 | Apache-2.0 | 高 | Node.js, React, Tailwind | NODE | 合并入 `frontend-design-craftsman` |
| E2 | web-design-guidelines | [vercel-labs/skills](https://github.com/vercel-labs/skills) | 高 | 审查 UI 代码是否符合 Web 界面指南,无障碍/设计审计 | Apache-2.0 | 高 | 无额外依赖 | MD | `web-design-auditor` Web设计审计师 |
| E3 | brand-guidelines | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 应用品牌色与排版到工件,确保视觉一致与专业设计标准 | Apache-2.0 | 高 | 无额外依赖 | MD | `brand-identity-creator` 品牌识别创造器 |
| E4 | theme-factory | [anthropics/skills](https://github.com/anthropics/skills) | 官方示例 | 为工件应用专业字体与配色主题,10 预设+自定义生成 | Apache-2.0 | 高 | 无额外依赖 | MD | `theme-stylist` 主题造型师 |
| E5 | anydesign | [uxKero/anydesign](https://github.com/uxKero/anydesign) | 社区贡献 | 分析任意图片/URL/Figma 生成结构化 design.md,可移植到 v0/Lovable/Cursor | MIT | 高 | 无额外依赖 | MD | `design-system-extractor` 设计系统提取器 |
| E6 | swiftui-design-skill | [wholiver/swiftui-design-skill](https://github.com/wholiver/swiftui-design-skill) | 社区贡献 | SwiftUI 设计辅助 | MIT | 低 | Xcode, Swift | 低 | 垂直小众,暂不包装 |
| E7 | imagen | [sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) | 社区贡献 | 用 Google Gemini 图像生成 API 生成 UI 原型/图标/插画/视觉素材 | MIT | 中 | Gemini API Key | MD+API | 合并入 `ai-artist-workstation` |
| E8 | figma-integration | [figma/skills](https://officialskills.sh/figma/skills) | 官方 | Figma MCP 集成:获取设计上下文、截图、变量、资产,设计转代码 | MIT | 高 | Figma API Key, Node.js | MD+API | `figma-to-code` Figma转代码器 |
| E9 | landing-page-generator | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k(总仓) | 单文件 HTML 落地页生成器:4 种设计风格、GSAP 动画、品牌色验证 | MIT | 高 | Node.js, GSAP | NODE | `landing-page-studio` 落地页工作室 |
| E10 | gsap-animation | [gsap/skills](https://officialskills.sh/gsap/skills) | 官方 | GSAP 动画参考:to/from/fromTo/缓动/序列/时间线/性能优化 | MIT | 中 | Node.js, GSAP | NODE | `animation-craftsman` 动画工匠 |

---

## F. 专业垂直类 (法律/云/企业)

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| F1 | azure-skills | [microsoft/skills](https://github.com/microsoft/skills) | 2.2k | Azure 云自动化:CDK 最佳实践、成本优化、132 个技能覆盖 Azure 全家桶 | MIT | 高 | Azure CLI, Azure 订阅 | MD+API | `azure-cloud-automator` Azure云自动化 |
| F2 | aws-skills | [zxkane/aws-skills](https://github.com/zxkane/aws-skills) | 社区贡献 | AWS 开发:CDK 最佳实践、成本优化 MCP 服务器、无服务器架构 | MIT | 高 | AWS CLI, AWS 账户 | MD+API | `aws-cloud-architect` AWS云架构师 |
| F3 | master-claude-for-legal | [sboghossian/master-claude-for-legal](https://github.com/sboghossian/master-claude-for-legal) | 社区贡献 | 法律团队技能包:NDA 分诊、多方版本 diff、引文核验、会议简报 | MIT | 高 | 无额外依赖 | MD | `legal-assistant-pro` 法律助手Pro |
| F4 | family-history-research | [emaynard/claude-family-history-research-skill](https://github.com/emaynard/claude-family-history-research-skill) | 社区贡献 | 家族历史与族谱研究项目规划辅助 | MIT | 低 | 无额外依赖 | MD | 垂直小众,暂不包装 |
| F5 | google-cloud-skills | [GoogleCloudPlatform/skills](https://officialskills.sh/google-cloud/skills) | 官方 | Google Cloud Platform 最佳实践:GCE/GKE/BigQuery/Cloud Functions | Apache-2.0 | 高 | gcloud CLI, GCP 项目 | MD+API | `gcp-cloud-architect` GCP云架构师 |
| F6 | firebase-skills | [firebase/skills](https://officialskills.sh/firebase/skills) | 官方 | Firebase 集成:Firestore/Auth/Cloud Functions/Hosting/Analytics | MIT | 中 | Node.js, Firebase CLI | NODE | `firebase-backend-builder` Firebase后端构建器 |
| F7 | nvidia-cuda-skills | [nvidia/skills](https://officialskills.sh/nvidia/skills) | 官方 | NVIDIA GPU 计算:CUDA 编程、TensorRT 优化、NIM 部署 | MIT | 中 | NVIDIA GPU, CUDA Toolkit | PY | `gpu-compute-optimizer` GPU计算优化器 |
| F8 | scientific-skills | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | MIT | 134 个科研技能:生物信息学/药物发现/蛋白质分析/医学影像/材料科学 | MIT | 高 | Python 3.11+, uv, 科学计算库 | PY | `scientific-research-assistant` 科研助手 |
| F9 | regulatory-qm | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k(总仓) | 监管与质量管理:ISO 13485/MDR/FDA/ISO 27001/GDPR/SOC 2/CAPA/风险管理 | MIT | 高 | 无额外依赖 | MD | `regulatory-compliance-pro` 监管合规Pro |
| F10 | openweb | [openweb-org/openweb](https://github.com/openweb-org/openweb) | 社区贡献 | Agent 原生访问任意网站,调用网站同款 API,自动处理 auth | MIT | 中 | Python, 联网 | PY | `web-access-agent` Web访问代理 |

---

## G. Agent框架类 (编排/构建/子代理) [新增类别]

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| G1 | brainstorming | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 苏格拉底式设计精炼:编码前通过提问探索需求,分段呈现设计文档 | MIT | 高 | 无额外依赖 | MD | `brainstorm-facilitator` 头脑风暴引导师 |
| G2 | writing-plans | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 详细实现计划:将工作拆分为 2-5 分钟任务,每个任务含精确文件路径和代码 | MIT | 高 | 无额外依赖 | MD | `plan-architect` 计划架构师 |
| G3 | executing-plans | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 批量执行计划:带人工检查点的分批执行,支持并行子代理 | MIT | 高 | 无额外依赖 | MD | `plan-executor` 计划执行器 |
| G4 | subagent-driven-dev | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 子代理驱动开发:每个任务分派全新子代理,两阶段审查(规格+质量) | MIT | 高 | 无额外依赖 | MD | `subagent-orchestrator` 子代理编排器 |
| G5 | voltagent-framework | [VoltAgent/skills](https://officialskills.sh/voltagent/skills/create-voltagent) | 20k(总仓) | VoltAgent TypeScript 框架:AI Agent 项目搭建、架构模式、核心参考 | MIT | 高 | Node.js, VoltAgent SDK | NODE | `agent-framework-builder` Agent框架构建器 |
| G6 | cloudflare-agents-sdk | [cloudflare/skills](https://officialskills.sh/cloudflare/skills/agents-sdk) | 官方 | 构建有状态 AI Agent:调度、RPC、MCP 服务器,运行在 Cloudflare Workers | MIT | 高 | Node.js, Cloudflare 账户 | NODE | `edge-agent-builder` 边缘Agent构建器 |
| G7 | self-improving-agent | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k | 自我改进代理:自动记忆策展、经验学习、行为模式优化 | MIT | 高 | Python | PY | `self-improving-agent` 自改进代理 |
| G8 | dispatching-parallel | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 并发子代理工作流:同时分派多个子代理处理独立任务 | MIT | 中 | 无额外依赖 | MD | `parallel-agent-dispatcher` 并行代理调度器 |
| G9 | systematic-debugging | [obra/superpowers](https://github.com/obra/superpowers) | 16k | 四阶段根因分析:复现/定位/缩减/修复,含防御深度与条件等待 | MIT | 高 | 无额外依赖 | MD | `debug-doctor` 调试医生 |
| G10 | plugin-eval-framework | [wshobson/agents](https://github.com/wshobson/agents) | 社区贡献 | 三层评估框架:静态分析+LLM 评判+蒙特卡洛统计可靠性,认证插件质量 | MIT | 中 | Python, uv | PY | `skill-quality-evaluator` Skill质量评估器 |

---

## H. 数据处理类 (数据库/分析/ETL) [新增类别]

| # | Skill 名称 | 来源仓库 | Star/安装量 | 功能描述 | 许可证 | 商业化潜力 | 依赖要求 | 直接可用性 | 重新包装方向 |
|:--|:-----------|:---------|:-----------|:---------|:-------|:-----------|:---------|:-----------|:-------------|
| H1 | clickhouse-best-practices | [clickhouse/skills](https://officialskills.sh/clickhouse/skills/clickhouse-best-practices) | 官方 | ClickHouse 分析数据库最佳实践:表设计/分区/物化视图/查询优化 | Apache-2.0 | 高 | ClickHouse 实例 | MD | `clickhouse-analytics` ClickHouse分析专家 |
| H2 | chdb-sql-engine | [clickhouse/skills](https://officialskills.sh/clickhouse/skills/chdb-sql) | 官方 | 进程内 ClickHouse SQL 引擎:Python 中查询文件/数据库/云存储,无需服务器 | Apache-2.0 | 高 | Python, chdb | PY | `chdb-sql-engine` chDB SQL引擎 |
| H3 | neon-postgres | [neondatabase/skills](https://officialskills.sh/neondatabase/skills/neon-postgres) | 官方 | Neon Serverless Postgres 最佳实践:连接池/分支/自动扩缩容 | MIT | 高 | Neon API Key | MD+API | `serverless-postgres-guide` 无服务器PG指南 |
| H4 | duckdb-analytics | [duckdb/skills](https://officialskills.sh/duckdb/skills) | 官方 | DuckDB 分析数据库:OLAP 查询/Parquet/CSV 直接查询/嵌入使用 | MIT | 高 | Python, duckdb | PY | `duckdb-analytics-engine` DuckDB分析引擎 |
| H5 | tinybird-realtime | [tinybirdco/skills](https://officialskills.sh/tinybirdco/skills/tinybird-best-practices) | 官方 | Tinybird 实时数据 API:数据源/管道/端点/SQL 最佳实践 | MIT | 中 | Tinybird API Key | MD+API | `realtime-data-api-builder` 实时数据API构建器 |
| H6 | firecrawl-scrape | [firecrawl/skills](https://officialskills.sh/firecrawl/skills/firecrawl-build) | 官方 | Firecrawl 集成:网页搜索/抓取/提取/浏览器交互,多步骤浏览器流 | MIT | 高 | Firecrawl API Key | MD+API | `web-scraper-engine` 网页抓取引擎 |
| H7 | supabase-postgres | [supabase/skills](https://officialskills.sh/supabase/skills/postgres-best-practices) | 官方 | Supabase PostgreSQL 最佳实践:RLS/索引/触发器/全文搜索 | MIT | 高 | Supabase 项目 | MD | `supabase-backend-guide` Supabase后端指南 |
| H8 | mongodb-best-practices | [mongodb/skills](https://officialskills.sh/mongodb/skills) | 官方 | MongoDB 最佳实践:Schema 设计/索引/聚合管道/分片/事务 | MIT | 中 | MongoDB 实例 | MD | `mongodb-architect` MongoDB架构师 |
| H9 | redis-best-practices | [redis/skills](https://officialskills.sh/redis/skills) | 官方 | Redis 性能优化与最佳实践:数据结构/查询引擎/向量搜索/语义缓存 | MIT | 高 | Redis 实例 | MD | `redis-optimization-pro` Redis优化专家 |
| H10 | datadog-monitoring | [datadog/skills](https://officialskills.sh/datadog/skills) | 官方 | Datadog 可观测性集成:指标/日志/APM/合成监控/告警 | MIT | 中 | Datadog API Key | MD+API | `observability-builder` 可观测性构建器 |

---

## 分类统计

| 类别 | 中文名 | 收录数 | 高商业化潜力 | 已包装 | 新增 |
|:-----|:-------|:-------|:-------------|:-------|:-----|
| A | 内容创作类 | 14 | 8 | 4 | +4 |
| B | 开发工具类 | 35 | 17 | 7 | +11 |
| C | 效率工具类 | 20 | 9 | 6 | +3 |
| D | 商业工具类 | 16 | 13 | 4 | +5 |
| E | 创意设计类 | 10 | 8 | 2 | +3 |
| F | 专业垂直类 | 10 | 8 | 2 | +3 |
| G | Agent框架类 | 10 | 8 | 0 | +10 (全新) |
| H | 数据处理类 | 10 | 8 | 0 | +10 (全新) |
| **合计** | | **68(去重后63)** | **48** | **25+15=40** | **+26 新增** |

> 已包装的 25 个 Skill 列表(第一轮,按类别):
> - **A(4)**: remotion-video-studio / canvas-art-designer / research-article-crafter / twitter-viral-optimizer
> - **B(7)**: code-review-sentinel / test-driven-coder / security-hardening-shield / api-design-architect / performance-optimizer-pro / mcp-server-builder / web-artifact-studio
> - **C(6)**: pptx-presentation-pro / xlsx-data-wizard / docx-document-master / pdf-toolkit-pro / csv-insight-miner / deep-research-engine
> - **D(4)**: seo-audit-master / copywriting-master / competitive-ad-spy / lead-research-hunter
> - **E(2)**: brand-identity-creator / theme-stylist
> - **F(2)**: azure-cloud-automator / legal-assistant-pro

> 第二轮新增包装的 15 个 Skill:
> - **B(5)**: stripe-payment-integrator / terraform-iac-architect / cloudflare-edge-developer / nextjs-fullstack-guide / auth-security-architect
> - **C(1)**: content-cms-architect
> - **D(2)**: c-suite-advisor / compliance-manager
> - **F(1)**: scientific-research-assistant
> - **G(3)**: debug-doctor / brainstorm-facilitator / plan-architect
> - **H(3)**: clickhouse-analytics / web-scraper-engine / duckdb-analytics-engine

---

## 直接可用性统计

| 可用性级别 | 含义 | 数量 | 占比 | 说明 |
|:-----------|:-----|:-----|:-----|:-----|
| **MD** | 纯Markdown可直接用 | 38 | 55.9% | 无需安装任何依赖,任何平台直接加载 |
| **PY** | 需要Python环境 | 14 | 20.6% | 需要 Python 3.10+ 及 pip 包 |
| **NODE** | 需要Node环境 | 11 | 16.2% | 需要 Node.js 18+ 及 npm 包 |
| **MD+API** | 纯MD+API Key | 8 | 11.8% | SKILL 是纯 MD,执行需外部 API Key |
| **DOCKER** | 需要Docker | 1 | 1.5% | 需要 Docker 运行时 |

> 注:部分 Skill 跨多个可用性级别(如 MD+API 同时算 MD 和 API),总数可能超过 68。

### 按依赖类型统计

| 依赖类型 | 数量 | 典型 Skill |
|:---------|:-----|:-----------|
| 无额外依赖(纯Markdown) | 38 | code-review-sentinel / copywriting-master / seo-audit-master |
| 需要Python运行时 | 14 | canvas-art-designer / csv-insight-miner / pptx-presentation-pro |
| 需要Node.js运行时 | 11 | remotion-video-studio / web-artifact-studio / nextjs-best-practices |
| 需要外部API Key | 8 | deep-research-engine / connect-apps / stripe-best-practices |
| 需要Docker | 1 | ffuf-web-fuzzing |
| 需要云服务账号 | 6 | azure-skills / aws-skills / google-cloud-skills / neon-postgres |

---

## 商业化评分说明

### 高 (High)
- 解决明确且高频的商业痛点(如 SEO、内容创作、代码质量、文档处理)
- 目标用户基数大(营销人员、开发者、企业办公人群)
- 易于转化为付费产品或订阅服务
- 有明确的对标产品或市场验证

### 中 (Medium)
- 解决特定场景问题,受众相对聚焦
- 可作为套餐组件或增值功能
- 需要一定的领域知识才能用好

### 低 (Low)
- 垂直小众市场(如 iOS 模拟器、家族历史研究)
- 工具型辅助,难以独立商业化
- 适合作为开源贡献或免费引流

---

## 数据来源与可信度

| 来源仓库 | Star | 角色 | 可信度 | 新增 | 备注 |
|:---------|:-----|:-----|:-------|:-----|:-----|
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 20k+ | 最大精选目录(1000+ skills, 60+ 官方团队) | 极高 | 新增 | MIT,跨平台兼容,人工精选非AI生成 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.8k | 24 个生命周期工程技能 | 高 | 已有 | Google Chrome 工程负责人维护,MIT |
| [anthropics/skills](https://github.com/anthropics/skills) | 官方 | 官方示例技能库(17 skills) | 高 | 已有 | 文档技能源码可见,Apache-2.0 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5.2k | 345 个技能,17 个领域 | 高 | 新增 | MIT,全C套件+合规+营销+研究 |
| [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | MIT | 134 个科研技能 | 高 | 新增 | MIT,覆盖生物/化学/医学/材料/物理 |
| [wshobson/agents](https://github.com/wshobson/agents) | MIT | 92 插件/199 Agent/162 Skill | 高 | 新增 | MIT,5 平台原生支持 |
| [obra/superpowers](https://github.com/obra/superpowers) | 16k | 14 个工作流技能(完整 SDLC) | 高 | 新增 | MIT,子代理驱动开发方法论 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | MIT | 模板市场(聚合多源) | 高 | 新增 | MIT,聚合多个技能源 |
| [microsoft/skills](https://github.com/microsoft/skills) | 2.2k | 132 个 Azure 技能 | 高 | 已有 | 微软官方,MIT |
| [coreyhaines31/marketing-skills](https://github.com/coreyhaines31/marketing-skills) | 32.9k | 营销/SEO/文案 | 高 | 已有 | MIT |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 18.9k | 精选目录(1000+ skills) | 高 | 已有 | Apache-2.0,社区维护 |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | 高 | Skills CLI + 跨 Agent 技能 | 高 | 已有 | Apache-2.0,Vercel 官方 |
| [stripe/skills](https://github.com/stripe/skills) | 官方 | 支付集成最佳实践 | 极高 | 新增 | MIT,Stripe 官方 |
| [cloudflare/skills](https://github.com/cloudflare/skills) | 官方 | Workers/边缘计算/Durable Objects | 极高 | 新增 | MIT,Cloudflare 官方 |
| [hashicorp/skills](https://github.com/hashicorp/skills) | 官方 | Terraform IaC 最佳实践 | 极高 | 新增 | MIT,HashiCorp 官方 |
| [clickhouse/skills](https://github.com/ClickHouse/skills) | 官方 | 分析数据库最佳实践 | 极高 | 新增 | Apache-2.0,ClickHouse 官方 |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 官方 | 安全审计(CodeQL/Semgrep) | 极高 | 新增 | MIT,Trail of Bits 安全团队 |
| [firecrawl/skills](https://github.com/firecrawl/skills) | 官方 | 网页抓取/提取 | 高 | 新增 | MIT,Firecrawl 官方 |
| [better-auth/skills](https://github.com/better-auth/skills) | 官方 | 认证安全最佳实践 | 高 | 新增 | MIT,Better Auth 官方 |
| 社区贡献者仓库 | 各异 | 单点技能 | 中 | 已有 | 各自 MIT/Apache-2.0 |

---

## 重新包装的通用规则(去标识化)

1. **移除原仓库名**:不出现 `addyosmani/agent-skills`、`anthropics/skills` 等仓库名
2. **移除原作者名**:不出现 Addy Osmani、Corey Haines、Matt Pocock 等个人名
3. **保留许可证**:在 frontmatter 中声明原许可证(MIT/Apache-2.0)
4. **添加商业化字段**:slug/version/displayName/summary/license/description/tools
5. **中文化**:displayName 和 summary 使用中文
6. **触发关键词**:在 description 中嵌入中文触发关键词
7. **使用场景**:补充具体业务场景,提升商业可用性
8. **工作流**:将原工作流提炼为可执行的步骤化流程
9. **依赖说明(新增)**:明确标注 LLM 要求、API Key 要求、运行环境要求
10. **直接可用性(新增)**:标注 MD/PY/NODE/DOCKER/API 分类
