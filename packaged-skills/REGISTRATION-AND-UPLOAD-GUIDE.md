# Skill 商业化注册与上传完全指南

> 更新时间: 2026-07-17
> 适用范围: 60个已包装Skill (20个JueJin改造 + 40个开源改造)
> 本指南覆盖: 12平台注册地址/方式 + Trae Work上传流程 + 每个Skill的具体上传说明

---

## 目录

- [一、第一步内容在哪里](#一第一步内容在哪里)
- [二、SkillHub 注册与上传(主战场)](#二skillhub-注册与上传主战场)
- [三、Coze 扣子注册与上传](#三coze-扣子注册与上传)
- [四、其他平台注册与上传](#四其他平台注册与上传)
- [五、Trae Work 上传流程](#五trae-work-上传流程)
- [六、60个Skill的依赖与上传说明](#六60个skill的依赖与上传说明)
- [七、合并方案的上传说明](#七合并方案的上传说明)

---

## 一、第一步内容在哪里

第一步(12平台注册地址与自动化上传)的内容在以下位置:

| 文档 | 路径 | 内容 |
|:-----|:-----|:-----|
| 商业化全流程执行手册 | `d:\skills\skillhub-master-plan\skillhub-master-plan.html` | 4步完整策略,含12平台注册详情 |
| 渠道分析报告 | `d:\skills\skillhub-channel-analysis\skillhub-channel-analysis.html` | 12平台对比分析 |
| 包装策略 | `d:\skills\skillhub-packaging-strategy\skillhub-packaging-strategy.html` | 4层去标识化+包装方案 |
| 变现分析 | `d:\skills\skillhub-monetization-analysis\skillhub-monetization-analysis.html` | 20 Skill清单+3梯队 |
| 总索引 | `d:\skills\packaged-skills\INDEX.md` | 45个Skill完整清单 |
| 审查报告 | `d:\skills\packaged-skills\audit-report.md` | 60个Skill依赖与可用性审查 |

**用浏览器打开HTML文件即可查看完整内容。**

---

## 二、SkillHub 注册与上传(主战场)

### 2.1 注册地址

| 项目 | 地址 |
|:-----|:-----|
| 官网 | https://skillhub.cn |
| 教程 | https://skillhub.cloud.tencent.com/tutorials |
| CLI发布教程 | https://skillhub.cloud.tencent.com/tutorials#publish-via-cli |
| Agent发布指南 | https://skillhub.cn/ai/release.md |

### 2.2 注册方式(5步,15分钟)

**第1步: 注册账号**
1. 浏览器打开 https://skillhub.cn
2. 右上角「登录/注册」
3. 手机号验证码登录(6位短信验证码)
4. 首次登录自动注册

**第2步: 实名认证**
1. 右上角头像 → 个人中心
2. 找到「实名认证」入口
3. 人脸核身(手机扫码刷脸)
4. 状态变为「已认证」

**第3步: 创建 API Token**
1. 个人中心 → 左侧菜单「API keys」(直链 `/dashboard/keys`)
2. 点「创建 API key」
3. 填名称(如`Trae-Work`)
4. 复制保存 Token(格式: `skh_xxx`)— **仅显示一次!**

**第4步: 安装 CLI**
```bash
# Mac/Linux
curl -fsSL https://skillhub.cn/install/install.sh | bash -s -- --cli-only

# Windows (使用 Git Bash)
# 已安装: skillhub 2026.7.7,路径 ~/.local/bin/skillhub
# 便捷脚本: d:\skills\skillhub.ps1
```

**第5步: 登录**
```bash
skillhub login --key skh_你的Token --host https://api.skillhub.cn
# 看到 ✓ Logged in as @你的handle 即成功
```

### 2.3 已配置状态

| 项目 | 状态 |
|:-----|:-----|
| 账号 | ✅ @user_cb75122a (userId=600324) |
| API Key | ✅ 已保存到 `d:\skills\.skillhub-credentials\api-key.txt` |
| CLI | ✅ skillhub 2026.7.7 (Git Bash) |
| 便捷脚本 | ✅ `d:\skills\skillhub.ps1` |

### 2.4 上传方式

#### 方式A: Trae Work 对话上传(推荐)

在 Trae Work 中直接发送指令:

```
根据 https://skillhub.cn/ai/release.md 把 d:\skills\packaged-skills\skillhub\ai-writing-style-cloner 发布到 SkillHub。
```

Agent会自动:
1. 读取发布规范
2. 校验SKILL.md格式
3. 登录(使用已保存的API Key)
4. 执行 dry-run 预检
5. 正式发布

#### 方式B: CLI 命令上传

```bash
# 使用便捷脚本(PowerShell)
cd d:\skills
.\skillhub.ps1 publish .\packaged-skills\skillhub\ai-writing-style-cloner --dry-run
.\skillhub.ps1 publish .\packaged-skills\skillhub\ai-writing-style-cloner --changelog "首次发布"

# 使用 Git Bash 直接执行
skillhub publish /d/skills/packaged-skills/skillhub/ai-writing-style-cloner --dry-run
skillhub publish /d/skills/packaged-skills/skillhub/ai-writing-style-cloner --changelog "首次发布"
```

#### 方式C: 批量上传脚本

```powershell
# PowerShell 批量上传所有 Skill
$skills = Get-ChildItem -Path 'd:\skills\packaged-skills\skillhub' -Directory
foreach ($skill in $skills) {
    Write-Host "正在上传: $($skill.Name)..."
    cd d:\skills
    .\skillhub.ps1 publish $skill.FullName --dry-run
    if ($LASTEXITCODE -eq 0) {
        .\skillhub.ps1 publish $skill.FullName --changelog "首次发布"
    }
}
```

#### 方式D: 网页上传

1. 登录 https://skillhub.cn
2. 个人中心 → 我的Skill → 发布新Skill
3. 上传SKILL.md文件或填写表单

### 2.5 发布后状态

| 状态 | 说明 |
|:-----|:-----|
| `pending_review` | 审核中(三线并行安全审核) |
| `published` | 审核通过,已上架 |
| `rejected` | 审核未通过,需修改 |

审核时间: 通常几分钟到几小时。审核通过后详情页自动可见。

### 2.6 SkillPay 付费Skill

如需设置付费Skill:
1. 完成企业认证(营业执照)
2. 商户入驻 + 微信商户号绑定
3. 发布Pay Skill,设置按次计费价格
4. 基于微信支付 Agent Pay X402协议自动结算

---

## 三、Coze 扣子注册与上传

### 3.1 注册地址

| 项目 | 地址 |
|:-----|:-----|
| 中文版 | https://www.coze.cn |
| 国际版 | https://www.coze.com |
| 开发者文档 | https://www.coze.cn/open/developer |

### 3.2 注册方式

1. 打开 https://www.coze.cn
2. 手机号/抖音扫码/微信登录
3. 无需实名认证
4. 进入「工作台」即可开始创建

### 3.3 上传方式

Coze不支持直接上传SKILL.md,需要手动创建Bot:

1. **创建Bot**: 工作台 → 创建Bot → 填写名称和描述
2. **编写提示词**: 将SKILL.md的正文内容粘贴到Bot的「人设与回复逻辑」中
3. **添加插件**: 根据Skill的依赖说明,添加对应插件:
   - 需要搜索 → 添加「必应搜索」插件
   - 需要画图 → 添加「图像生成」插件
   - 需要代码执行 → 添加「代码执行」插件
4. **配置知识库**: 上传相关文档作为知识库
5. **发布Bot**: 测试通过后发布

### 3.4 自动化方式

```bash
# 安装Coze Python SDK
pip install cozepy

# 使用API创建和管理Bot
# 需要在「个人设置→开发者令牌」创建PAT
# API地址: https://api.coze.cn/v3/chat
```

### 3.5 变现方式

- 免费Bot引流 → 付费会员订阅
- 开放「复制权限」 → 别人付费copy工作流
- 接商单定制Bot

---

## 四、其他平台注册与上传

### 4.1 速查表

| 平台 | 注册地址 | 注册方式 | 上传方式 | 自动化 |
|:-----|:---------|:---------|:---------|:-------|
| **Dify** | https://cloud.dify.ai | GitHub/Google登录 | Plugin SDK打包 → GitHub仓库URL安装 | SDK+签名认证 |
| **FastGPT** | https://fastgpt.cn | 手机号/邮箱 | API Key接入,自托管Docker部署 | OpenAI兼容API |
| **Agent.ai** | https://agent.ai | 网页注册 | Agent Builder无代码创建 | 无CLI |
| **AI Agents Dir** | https://aiagentsdirectory.com | 网页表单 | 表单提交Agent信息 | 不支持 |
| **Stammer.ai** | https://app.stammer.ai/accounts/signup/ | 邮箱注册 | Rebrandable API集成 | API |
| **SwarmZero** | https://swarmzero.ai | 网页注册 | Python SDK部署 | `pip install swarmzero` |
| **PromptBase** | https://promptbase.com | 邮箱注册 | 网页表单+Stripe | 不支持 |
| **FlowGPT** | https://flowgpt.com | Google/邮箱 | 网页Prompt编辑器 | 不支持 |
| **GPT Store** | https://chat.openai.com/gpts | OpenAI账号+Plus订阅 | GPT Builder网页操作 | 不支持 |

### 4.2 Dify 插件上传

1. 注册 https://cloud.dify.ai (GitHub登录)
2. 安装Dify Plugin SDK: `pip install difine`
3. 创建插件项目,编写SKILL.md
4. 打包: `dify plugin package ./my-plugin`
5. 发布: 通过GitHub仓库URL+版本号安装到Dify

### 4.3 PromptBase 上传

1. 注册 https://promptbase.com (邮箱)
2. 连接Stripe账户(收款)
3. 点「Sell a prompt」
4. 选择类型(ChatGPT/Midjourney/SD等)
5. 填写标题、描述、Prompt内容、价格($1.99起)
6. 平台抽成10%,卖家保留90%

### 4.4 GPT Store 上传

1. 订阅ChatGPT Plus ($20/月)
2. 创建GPT: https://chat.openai.com/gpts/editor
3. 在GPT Builder中编写指令(将SKILL.md正文粘贴)
4. 保存为「Everyone」
5. 验证Builder Profile(域名DNS TXT验证)
6. 等待审核

---

## 五、Trae Work 上传流程

### 5.1 方式A: 对话指令上传(最简单)

在Trae Work对话中直接发送:

```
请帮我将以下Skill发布到SkillHub:
d:\skills\packaged-skills\skillhub\ai-writing-style-cloner

发布规范参考: https://skillhub.cn/ai/release.md
API Key已保存在: d:\skills\.skillhub-credentials\api-key.txt
Host: https://api.skillhub.cn

请先执行 dry-run 预检,通过后再正式发布。
```

Trae Work Agent会自动完成:
1. 读取SKILL.md验证frontmatter
2. 登录SkillHub
3. 执行dry-run预检
4. 正式发布
5. 返回发布结果和URL

### 5.2 方式B: 批量对话指令

```
请帮我批量发布以下20个Skill到SkillHub:
目录: d:\skills\packaged-skills\skillhub\

每个Skill目录下都有SKILL.md文件。
请逐个执行 dry-run 预检,通过后正式发布。
如果某个Skill发布失败,记录错误并继续下一个。

API Key: d:\skills\.skillhub-credentials\api-key.txt
Host: https://api.skillhub.cn
```

### 5.3 方式C: 使用便捷脚本

在Trae Work终端中执行:

```powershell
# 单个上传
cd d:\skills
.\skillhub.ps1 publish .\packaged-skills\skillhub\ai-writing-style-cloner --dry-run
.\skillhub.ps1 publish .\packaged-skills\skillhub\ai-writing-style-cloner --changelog "首次发布"

# 查看登录状态
.\skillhub.ps1 auth whoami

# 搜索已有Skill
.\skillhub.ps1 search writing
```

### 5.4 发布前检查清单

每个Skill发布前,确认:

- [ ] SKILL.md存在且frontmatter完整(slug/name/version/displayName/summary/license)
- [ ] slug为kebab-case,2-128字符,全网唯一
- [ ] version为合法SemVer(如1.0.0)
- [ ] 正文包含:使用场景、工作流、输入格式、输出格式、依赖说明、异常处理、示例
- [ ] 无残留禁止关键词(JueJin/dailyhot/narrato/fishclaw/PostgreSQL/PG/MCP/tenant/xianyu等)
- [ ] 依赖说明章节清晰标注了所需LLM、API Key、运行环境

---

## 六、60个Skill的依赖与上传说明

### 6.1 JueJin改造Skill (20个)

每个Skill的上传目标平台和依赖要求:

| # | Skill | 上传平台 | 依赖类型 | 需要 | 上传内容 |
|:--|:------|:---------|:---------|:-----|:---------|
| 1 | ai-writing-style-cloner | SkillHub+Coze | LLM + JSON | LLM API | 直接上传SKILL.md |
| 2 | viral-prophet | SkillHub+Coze | LLM + JSON | LLM API | 直接上传SKILL.md |
| 3 | drama-hit-producer | SkillHub | LLM + TTS + 图像API | LLM API + TTS API + 图像生成API | 上传SKILL.md,需说明TTS和图像API依赖 |
| 4 | ecommerce-pricing-strategist | SkillHub+Coze | LLM + 电商API | LLM API + 电商数据API | 直接上传SKILL.md |
| 5 | intel-sentinel | SkillHub+Coze | LLM + 新闻源 | LLM API + RSS/热搜API | 上传SKILL.md,需说明新闻数据源 |
| 6 | novel-autopilot | SkillHub | LLM + 发布API | LLM API | 直接上传SKILL.md |
| 7 | ai-artist-workstation | SkillHub | LLM + 绘画引擎 | LLM API + AI绘画API | 上传SKILL.md,需说明绘画引擎依赖 |
| 8 | ai-video-director | SkillHub | LLM + TTS + 视频API + ffmpeg | LLM API + TTS + 视频 + ffmpeg | 上传SKILL.md,需说明视频生成依赖 |
| 9 | topic-hunter | SkillHub+Coze | LLM + 热榜源 | LLM API + 热搜API | 直接上传SKILL.md |
| 10 | stealth-browser-assistant | SkillHub | Chrome + CDP | Chrome浏览器 + CDP协议 | 上传SKILL.md,需说明浏览器依赖 |
| 11 | cyber-fortune-teller | SkillHub+Coze | LLM + 命理引擎 | LLM API + 命理排盘API | 上传SKILL.md,需说明命理引擎依赖 |
| 12 | ebook-factory | SkillHub+Coze | LLM + 封面图 + PDF | LLM API + 图像API + PDF工具 | 上传SKILL.md,需说明PDF生成依赖 |
| 13 | poetry-craftsman | SkillHub+Coze | LLM + 诗词库 | LLM API | 直接上传SKILL.md |
| 14 | title-hook-factory | SkillHub+Coze+PromptBase | LLM | LLM API | 直接上传SKILL.md |
| 15 | sales-copy-writer | SkillHub+Coze+PromptBase | LLM | LLM API | 直接上传SKILL.md |
| 16 | seo-doctor | SkillHub+Coze | LLM + BERT + 搜索API | LLM API + 搜索API | 上传SKILL.md,需说明搜索API依赖 |
| 17 | hook-retention-master | SkillHub+Coze+PromptBase | LLM | LLM API | 直接上传SKILL.md |
| 18 | content-refiner | SkillHub+Coze+PromptBase | LLM(可选) + SimHash | LLM API(可选) | 直接上传SKILL.md |
| 19 | seo-rank-monopolizer | SkillHub+Coze | LLM | LLM API | 直接上传SKILL.md |
| 20 | viral-decoder | SkillHub+Coze+PromptBase | LLM + 内容数据 | LLM API | 直接上传SKILL.md |

**说明**: "直接上传SKILL.md"意味着只需将文件夹上传到SkillHub,平台会自动处理。LLM能力由Agent内置提供,用户无需额外配置LLM API Key。

### 6.2 开源改造Skill (40个)

| # | Skill | 上传平台 | 依赖类型 | 需要 | 直接可用 |
|:--|:------|:---------|:---------|:-----|:---------|
| 21 | api-design-architect | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |
| 22 | auth-security-architect | SkillHub+Coze | LLM + 数据库 | LLM API + 数据库 | 需配置数据库 |
| 23 | azure-cloud-automator | SkillHub | Azure CLI + Bicep | Azure账号 + CLI | 需Azure环境 |
| 24 | brainstorm-facilitator | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |
| 25 | brand-identity-creator | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |
| 26 | canvas-art-designer | SkillHub+Coze | Canvas/SVG + Python | Python(可选) | 基本可用 |
| 27 | clickhouse-analytics | SkillHub | ClickHouse | ClickHouse实例 | 需ClickHouse |
| 28 | cloudflare-edge-developer | SkillHub | Cloudflare Workers | Node.js + wrangler + CF账号 | 需CF环境 |
| 29 | code-review-sentinel | SkillHub+Coze | Git + LLM | Git + LLM API | 基本可用 |
| 30 | competitive-ad-spy | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |
| 31 | compliance-manager | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |
| 32 | content-cms-architect | SkillHub | Sanity Studio | Node.js + Sanity CLI | 需Sanity账号 |
| 33 | copywriting-master | SkillHub+Coze+PromptBase | 无(纯方法论) | 无 | ✅ 零依赖 |
| 34 | csv-insight-miner | SkillHub+Coze | Python + pandas | Python 3.8+ + pandas | 需Python |
| 35 | debug-doctor | SkillHub+Coze | LLM + 调试工具 | LLM API | 基本可用 |
| 36 | deep-research-engine | SkillHub+Coze | LLM + 联网搜索 | LLM API + 搜索API | 基本可用 |
| 37 | docx-document-master | SkillHub+Coze | Python + python-docx | Python 3.8+ + python-docx | 需Python |
| 38 | duckdb-analytics-engine | SkillHub | DuckDB | Python/Node + duckdb | 需DuckDB |
| 39 | lead-research-hunter | SkillHub+Coze | LLM + 联网搜索 | LLM API + 搜索API | 基本可用 |
| 40 | legal-assistant-pro | SkillHub+Coze | LLM + 联网搜索 | LLM API + 搜索API | 基本可用 |
| 41 | mcp-server-builder | SkillHub | Python/Node | Python(FastMCP) 或 Node(MCP SDK) | 需开发环境 |
| 42 | nextjs-fullstack-guide | SkillHub | Node.js + Next.js | Node.js 18+ + Next.js 14+ | 需Node环境 |
| 43 | pdf-toolkit-pro | SkillHub+Coze | Python + PyPDF2 | Python 3.8+ + PyPDF2/reportlab | 需Python |
| 44 | performance-optimizer-pro | SkillHub+Coze | LLM + 分析工具 | LLM API | 基本可用 |
| 45 | plan-architect | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |
| 46 | pptx-presentation-pro | SkillHub+Coze | Node/Python | Node.js(PptxGenJS) 或 Python(python-pptx) | 需Node或Python |
| 47 | remotion-video-studio | SkillHub | Node.js + Remotion | Node.js + Remotion | 需Node环境 |
| 48 | research-article-crafter | SkillHub+Coze | LLM + 联网搜索 | LLM API + 搜索API | 基本可用 |
| 49 | scientific-research-assistant | SkillHub | LLM + 科研工具 | Python 3.11+ + uv | 需Python |
| 50 | security-hardening-shield | SkillHub+Coze | LLM + 安全工具 | LLM API | 基本可用 |
| 51 | seo-audit-master | SkillHub+Coze | LLM + 联网搜索 | LLM API + 搜索API | 基本可用 |
| 52 | stripe-payment-integrator | SkillHub | Stripe API | Stripe API Key + Node/Python | 需Stripe账号 |
| 53 | terraform-iac-architect | SkillHub | Terraform | Terraform CLI + HCL | 需Terraform |
| 54 | test-driven-coder | SkillHub+Coze | LLM + 测试框架 | LLM API + 测试框架 | 基本可用 |
| 55 | theme-stylist | SkillHub+Coze | LLM + CSS | LLM API | 基本可用 |
| 56 | twitter-viral-optimizer | SkillHub+Coze | LLM + 联网搜索 | LLM API + 搜索API | 基本可用 |
| 57 | web-artifact-studio | SkillHub | Node.js + React | Node.js + React/Vite/Tailwind | 需Node环境 |
| 58 | web-scraper-engine | SkillHub | Firecrawl API | Firecrawl API Key | 需Firecrawl |
| 59 | xlsx-data-wizard | SkillHub+Coze | Python + openpyxl | Python 3.8+ + openpyxl/pandas | 需Python |
| 60 | c-suite-advisor | SkillHub+Coze | 无(纯方法论) | 无 | ✅ 零依赖 |

### 6.3 按可用性分类上传建议

#### 零依赖直接上传 (8个,优先上传)
```
api-design-architect, brainstorm-facilitator, brand-identity-creator,
competitive-ad-spy, compliance-manager, copywriting-master,
plan-architect, c-suite-advisor
```
这8个纯方法论Skill无需任何外部依赖,任何平台直接加载即可使用。

#### 只需LLM即可使用 (28个,第二批上传)
```
ai-writing-style-cloner, viral-prophet, novel-autopilot, topic-hunter,
poetry-craftsman, title-hook-factory, sales-copy-writer, hook-retention-master,
content-refiner, seo-rank-monopolizer, viral-decoder,
code-review-sentinel, debug-doctor, deep-research-engine,
lead-research-hunter, legal-assistant-pro, performance-optimizer-pro,
research-article-crafter, security-hardening-shield, seo-audit-master,
test-driven-coder, theme-stylist, twitter-viral-optimizer,
ecommerce-pricing-strategist, intel-sentinel, cyber-fortune-teller,
seo-doctor, canvas-art-designer
```
这些Skill的LLM能力由Agent内置提供,用户无需额外配置。

#### 需要特定API/工具 (24个,第三批上传)
```
drama-hit-producer(TTS+图像), ai-artist-workstation(绘画API),
ai-video-director(TTS+视频+ffmpeg), stealth-browser-assistant(Chrome+CDP),
ebook-factory(图像+PDF), ai-artist-workstation(绘画引擎),
csv-insight-miner(Python+pandas), docx-document-master(Python),
pdf-toolkit-pro(Python), pptx-presentation-pro(Node/Python),
xlsx-data-wizard(Python), stripe-payment-integrator(Stripe API),
terraform-iac-architect(Terraform), azure-cloud-automator(Azure CLI),
cloudflare-edge-developer(Cloudflare), mcp-server-builder(Python/Node),
nextjs-fullstack-guide(Node.js), remotion-video-studio(Node.js),
web-artifact-studio(Node.js), web-scraper-engine(Firecrawl),
clickhouse-analytics(ClickHouse), duckdb-analytics-engine(DuckDB),
auth-security-architect(数据库), content-cms-architect(Sanity)
```
这些Skill需要在依赖说明中清楚标注所需环境,用户按需配置。

---

## 七、合并方案的上传说明

### 7.1 合并方案概述

根据 `d:\skills\opensource-skills\merge-plan.md`,共有24组合并方案 + 17个独立产品。

### 7.2 合并方案上传策略

合并方案不是上传"合并后的文件",而是:

1. **在SkillHub上分别上传各子Skill**
2. **在Skill的description中互相引用** (如"建议配合xxx-skill一起使用")
3. **创建一个「套装」Skill** 作为入口,description中列出所有子Skill

### 7.3 具体合并方案上传

#### 合并组1: AI视频导演工作室 Pro
| 上传内容 | SkillHub | Coze |
|:---------|:---------|:-----|
| ai-video-director | ✅ 上传SKILL.md | ✅ 创建Bot |
| remotion-video-studio | ✅ 上传SKILL.md | - |
| 合并说明 | 在description中写"建议配合remotion-video-studio使用,实现代码化视频生成" | - |

#### 合并组2: AI艺术家工作站 Pro
| 上传内容 | SkillHub | Coze |
|:---------|:---------|:-----|
| ai-artist-workstation | ✅ 上传SKILL.md | ✅ 创建Bot |
| canvas-art-designer | ✅ 上传SKILL.md | ✅ 创建Bot |
| 合并说明 | 在description中写"配合canvas-art-designer可扩展为静态视觉创作" | - |

#### 合并组3: 内容质量全能顾问
| 上传内容 | SkillHub | Coze |
|:---------|:---------|:-----|
| viral-prophet | ✅ 上传SKILL.md | ✅ 创建Bot |
| viral-decoder | ✅ 上传SKILL.md | ✅ 创建Bot |
| 合并说明 | "viral-prophet负责预测,viral-decoder负责拆解,配合使用形成闭环" | - |

#### 合并组4: SEO+CRO全能顾问
| 上传内容 | SkillHub | Coze |
|:---------|:---------|:-----|
| seo-doctor | ✅ 上传SKILL.md | ✅ 创建Bot |
| seo-audit-master | ✅ 上传SKILL.md | - |
| seo-rank-monopolizer | ✅ 上传SKILL.md | ✅ 创建Bot |
| 合并说明 | "三件套:seo-doctor诊断 → seo-audit-master审计 → seo-rank-monopolizer占位" | - |

#### 合并组5: 竞品情报雷达
| 上传内容 | SkillHub | Coze |
|:---------|:---------|:-----|
| ecommerce-pricing-strategist | ✅ 上传SKILL.md | ✅ 创建Bot |
| competitive-ad-spy | ✅ 上传SKILL.md | - |
| 合并说明 | "竞品监控+广告提取+定价建议三合一" | - |

#### 合并组6: 卖货文案+着陆页优化套装
| 上传内容 | SkillHub | Coze | PromptBase |
|:---------|:---------|:-----|:----------|
| sales-copy-writer | ✅ 上传SKILL.md | ✅ 创建Bot | ✅ 拆Prompt |
| copywriting-master | ✅ 上传SKILL.md | ✅ 创建Bot | ✅ 拆Prompt |
| 合并说明 | "sales-copy-writer侧重FAB+CTA,copywriting-master侧重标题+正文+CTA全流程" | - | - |

#### 合并组7: 浏览器自动化专家
| 上传内容 | SkillHub | Coze |
|:---------|:---------|:-----|
| stealth-browser-assistant | ✅ 上传SKILL.md | - |
| web-scraper-engine | ✅ 上传SKILL.md | - |
| 合并说明 | "stealth-browser-assistant负责反检测浏览,web-scraper-engine负责数据抓取" | - |

### 7.4 独立产品上传

17个独立产品(不合并)直接上传SKILL.md到对应平台即可:

```
api-design-architect → SkillHub+Coze
brainstorm-facilitator → SkillHub+Coze
brand-identity-creator → SkillHub+Coze
compliance-manager → SkillHub+Coze
plan-architect → SkillHub+Coze
c-suite-advisor → SkillHub+Coze
debug-doctor → SkillHub+Coze
stripe-payment-integrator → SkillHub
terraform-iac-architect → SkillHub
cloudflare-edge-developer → SkillHub
clickhouse-analytics → SkillHub
duckdb-analytics-engine → SkillHub
deep-research-engine → SkillHub+Coze
legal-assistant-pro → SkillHub+Coze
mcp-server-builder → SkillHub
nextjs-fullstack-guide → SkillHub
remotion-video-studio → SkillHub
```

### 7.5 上传优先级

| 优先级 | 批次 | 数量 | 内容 |
|:-------|:-----|:-----|:-----|
| P0 | 第1批 | 8个 | 零依赖纯方法论Skill(立即上传) |
| P1 | 第2批 | 5个 | 第一梯队冲奖Skill |
| P2 | 第3批 | 3个 | 第二梯队获奖Skill |
| P3 | 第4批 | 12个 | 第三梯队赚钱Skill(只需LLM) |
| P4 | 第5批 | 16个 | 只需LLM的开源Skill |
| P5 | 第6批 | 16个 | 需特定API/工具的Skill |

### 7.6 上传命令模板

```bash
# P0: 零依赖Skill(8个)
for skill in api-design-architect brainstorm-facilitator brand-identity-creator competitive-ad-spy compliance-manager copywriting-master plan-architect c-suite-advisor; do
  skillhub publish d:/skills/opensource-skills/packaged/$skill --dry-run
  skillhub publish d:/skills/opensource-skills/packaged/$skill --changelog "首次发布"
done

# P1: 冲奖Skill(5个)
for skill in ai-writing-style-cloner viral-prophet drama-hit-producer ecommerce-pricing-strategist intel-sentinel; do
  skillhub publish d:/skills/packaged-skills/skillhub/$skill --dry-run
  skillhub publish d:/skills/packaged-skills/skillhub/$skill --changelog "首次发布"
done
```

---

## 附录: 常见问题

### Q1: SkillHub上传失败怎么办?

| 错误 | 原因 | 解决方案 |
|:-----|:-----|:---------|
| `401 invalid api key` | Token失效 | 重新创建API Key |
| `403 请先完成实名认证` | 未实名 | 完成人脸核身 |
| `409 slug已被占用` | slug冲突 | 修改slug(加前缀) |
| `429 请求过于频繁` | 限频 | 等待1分钟后重试 |
| `SKILL.md 缺少xxx` | frontmatter不完整 | 补全缺失字段 |

### Q2: Coze上如何使用这些Skill?

Coze不支持直接上传SKILL.md。需要:
1. 创建Bot
2. 将SKILL.md正文粘贴到Bot的「人设与回复逻辑」
3. 根据依赖说明添加对应插件
4. 测试并发布Bot

### Q3: 哪些Skill可以直接在Trae Work中使用?

所有60个Skill都可以在Trae Work中使用:
1. 将SKILL.md文件放入Trae Work的skills目录
2. Trae Work会自动识别并加载
3. 根据SKILL.md的description中的触发关键词自动触发

### Q4: 如何设置付费Skill?

1. 完成SkillHub企业认证(营业执照)
2. 商户入驻 + 微信商户号绑定
3. 发布时选择Pay Skill
4. 设置按次计费价格
5. 基于微信支付 Agent Pay X402协议自动结算
