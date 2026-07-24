# SkillHub 可见性根因分析与修复方案

> **日期**: 2026-07-24
> **问题**: 1120个标记为"success"的skill在SkillHub前台完全不可见
> **状态**: 根因已确认，修复方案已制定

## 一、根因分析

### 1.1 核心发现

通过对数据库状态、CLI能力、平台API、实际搜索验证的交叉分析，确认以下根因：

| 根因 | 证据 | 影响 |
|------|------|------|
| **skillhub CLI无publish命令** | v0.4.1只有install/search/list/config/uninstall/update | 无法通过CLI上传skill |
| **数据库标记≠平台实际状态** | 1120条记录的community_published=1和visibility=public是V45在本地DB设置的 | DB状态不代表平台状态 |
| **download_ready全部为NULL** | 1120条success记录的download_ready均为NULL | 从未验证平台是否处理了版本 |
| **实际搜索验证失败** | `npx skillhub search "ad-insight-hub"`无法找到我们的skill | 确认前台不可见 |
| **上传日期异常** | 1100/1120条记录的upload_date=2026-07-24（V45 DB迁移日） | 非实际平台上传时间 |

### 1.2 排除的因素

| 因素 | 排除理由 |
|------|----------|
| WAF拦截 | 无566错误记录 |
| 内容过长 | 已在V36修复，所有SKILL.md < 5800字符 |
| 安全审核拒绝 | L8安全审计100%通过 |
| Slug冲突 | 无409 SLUG_CONFLICT错误 |
| 版本冲突 | 无409 VERSION_EXISTS错误 |

### 1.3 根因链路

```
V36-V37: 尝试通过 npx skillhub publish 上传
    ↓
CLI v0.4.1 无 publish 命令 → 全部返回 CLI_NO_PUBLISH
    ↓
V45: 在数据库中设置 community_published=1, visibility=public
    ↓ (仅修改本地DB，未联系平台)
平台侧: skill从未实际上传/发布到社区
    ↓
前台搜索: 找不到任何我们的skill
```

## 二、SkillHub上传方式分析

### 2.1 当前CLI能力 (v0.4.1)

```
Commands:
  install [options] <skill-id>      Install a skill from the registry
  search [options] <query>          Search for skills in the registry
  list [options]                    List installed skills
  config [options]                  Manage CLI configuration
  uninstall [options] <skill-name>  Uninstall a skill
  update [options] [skill-name]     Update installed skills
```

**结论**: CLI仅支持消费端（搜索/安装），不支持生产端（发布/上传）。

### 2.2 Admin API (需浏览器cookie)

- **端点**: `https://api.skillhub.cn/api/v1/orgs/862/admin/skills`
- **认证**: 浏览器cookie（Bearer Token sk-ent-/skh_ 无法访问admin端点）
- **操作**: 
  - `GET /admin/skills` — 列出所有skill
  - `POST /admin/skills` — 创建新skill
  - `POST /admin/skills/{slug}/publish-to-community` — 发布到社区
  - `PUT /admin/skills/{slug}/rename-slug` — 重命名slug

### 2.3 浏览器端社区发布流程

已生成 `community_publish.js` 脚本，功能包括：
1. 获取所有skill（含visibility/download_ready/namespace信息）
2. 生成可见性诊断报告
3. 筛选 org_only + NULL visibility 的skill
4. 批量调用 publish-to-community API
5. 处理slug冲突（自动追加-sk后缀）
6. 输出JSON格式结果供数据库同步

**使用步骤**:
1. 打开 https://skillhub.cn/admin/skills
2. 按F12打开浏览器开发者工具
3. 切换到Console标签
4. 粘贴 `d:\skills\tools\community_publish.js` 的内容并回车执行
5. 执行完成后运行: `JSON.stringify(window.__publishResults)`
6. 将结果保存为JSON文件
7. 运行: `python tools/auto_publish.py sync-platform-status <results.json>`

## 三、修复方案

### 3.1 短期方案（立即可执行）

**方案A: 浏览器端批量发布**
- 执行 `community_publish.js` 脚本
- 验证1120个skill的实际平台状态
- 对不可见skill调用 publish-to-community API
- 同步结果到数据库

**方案B: 逐个浏览器上传**
- 登录 https://www.skillhub.cn
- 导航到"发布Skill"页面
- 逐个上传8个retry_pending技能的SKILL.md文件
- 上传成功后更新数据库

### 3.2 中期方案（需平台配合）

**方案C: 寻找SkillHub发布API**
- 调查SkillHub是否有Web端上传API（非Admin API）
- 检查是否有第三方发布工具
- 联系SkillHub平台获取发布API文档

**方案D: 使用npx skillhub的config命令配置发布凭证**
- `npx skillhub config` 可能支持设置API Key
- 配置后可能解锁publish功能

### 3.3 长期方案

**方案E: 多平台发布策略调整**
- 将SkillHub定位为"手动发布"平台
- 将ClawHub作为"自动发布"主平台（CLI支持publish）
- GitHub双仓库作为代码备份和引流
- 开发自动化浏览器发布工具（Puppeteer/Playwright）

## 四、验证检查清单

- [ ] 用户在浏览器执行 community_publish.js
- [ ] 验证平台侧 visibility/download_ready/namespace 状态
- [ ] 不可见skill调用 publish-to-community
- [ ] sync-platform-status 同步结果到数据库
- [ ] 8个retry_pending技能浏览器上传
- [ ] `npx skillhub search` 能找到我们的skill

## 五、数据库字段说明

| 字段 | 含义 | 当前状态 |
|------|------|----------|
| upload_status | 上传状态 | success=1120 (本地标记) |
| visibility | 可见性 | public=1120 (本地标记) |
| community_published | 社区发布 | 1=1120 (本地标记) |
| download_ready | 下载就绪 | NULL=1120 (未验证) |
| http_status | HTTP状态码 | 200=1120 (本地标记) |

**关键**: visibility/community_published/download_ready 三个字段的值均为本地设置，未经SkillHub平台确认。
