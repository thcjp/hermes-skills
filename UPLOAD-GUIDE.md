# SkillHub 批量上传指南

## 当前状态

- ✅ 600个ClawHub Skill已下载并深度优化完成
- ✅ 所有文件已推送到GitHub: https://github.com/thcjp/-.git
- ⏳ 等待用户登录后批量上传到SkillHub

## 优化内容

每个SKILL.md已完成以下优化：
1. **修复代码块** - 修复HTML转Markdown导致的代码块格式错误
2. **移除风险代码** - 清除硬编码凭证、eval()、base64解码等危险代码
3. **清除外部引用** - 替换ClawHub/OpenClaw引用为SkillHub
4. **增强Frontmatter** - 添加分类描述、触发关键词、标签
5. **添加依赖说明** - 每个Skill末尾添加标准依赖文档
6. **修复版本号** - 统一版本号格式
7. **清理Markdown** - 移除转换伪影、修复空行

## 分类统计

| 分类 | 数量 | 中文名 |
|------|------|--------|
| Integrations | 96 | 集成工具 |
| Other | 90 | 其他工具 |
| Creative | 65 | 创意设计 |
| Research | 58 | 研究工具 |
| Development | 50 | 开发工具 |
| Automation | 40 | 效率工具 |
| Productivity | 39 | 商业工具 |
| Communication | 38 | 沟通协作 |
| Knowledge | 32 | 知识管理 |
| Security | 24 | 安全工具 |
| Agents | 24 | 智能代理 |
| Lifestyle | 18 | 生活工具 |
| Operations | 14 | 运维工具 |
| Finance | 12 | 金融工具 |
| **合计** | **600** | |

## 上传方法

### 方法一：ClawHub CLI上传（推荐）

```bash
# 1. 安装clawhub CLI
npm install -g clawhub

# 2. 登录（GitHub OAuth）
clawhub login

# 3. 验证登录
clawhub whoami

# 4. 批量上传
cd d:\skills
.\upload-to-skillhub.ps1

# 或先试运行
.\upload-to-skillhub.ps1 -DryRun

# 或从指定分类开始
.\upload-to-skillhub.ps1 -StartCategory "Security"
```

### 方法二：单个上传

```bash
cd d:\skills\clawhub-skills\downloaded\Security\skill-vetter
clawhub publish . --slug skill-vetter --name "Skill Vetter" --changelog "深度优化版" --categories security --json
```

### 方法三：SkillHub网页上传

1. 访问 https://skillhub.cn
2. 微信扫码登录
3. 点击"发布Skill"
4. 上传SKILL.md文件
5. 填写名称、描述、分类
6. 提交审核

## 上传脚本说明

### upload-to-skillhub.ps1 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| -DryRun | 试运行（不实际上传） | $false |
| -StartCategory | 从指定分类开始 | "" (全部) |
| -DelaySeconds | 上传间隔秒数 | 2 |
| -RateLimitWaitSeconds | 429限流等待秒数 | 90 |

### 上传日志

上传日志保存在 `d:\skills\clawhub-skills\upload-log.csv`，包含：
- 时间戳、分类、slug、状态、HTTP状态码、错误信息

## 注意事项

1. **Slug冲突处理**：如果slug已存在，脚本会自动添加 `-pro` 后缀重试
2. **429限流处理**：遇到限流时自动等待90秒后重试，最多重试3次
3. **认证错误**：如果token过期，脚本会提示重新登录
4. **断点续传**：通过 `-StartCategory` 参数可以从指定分类继续上传
5. **审核流程**：上传后Skill会进入pending_review状态，需通过内容合规和安全管理

## 文件结构

```
d:\skills\
├── clawhub-skills\
│   ├── downloaded\           # 600个优化后的Skill
│   │   ├── Agents\           # 24个
│   │   ├── Creative\         # 65个
│   │   ├── Development\      # 50个
│   │   ├── Security\         # 24个
│   │   └── ...               # 共14个分类
│   ├── catalog.md            # 600个Skill目录索引
│   ├── top600.json           # 原始元数据
│   ├── download-log-v2.csv   # 下载日志
│   └── optimization-log.csv # 优化日志
├── opensource-skills\        # 之前40个开源Skill
├── packaged-skills\          # 之前20个掘金Skill
├── upload-to-skillhub.ps1   # 批量上传脚本
├── UPLOAD-GUIDE.md           # 本文档
└── .gitignore
```
