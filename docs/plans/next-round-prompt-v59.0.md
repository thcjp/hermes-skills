# 第59轮提示词 (v59.0) — 批量重传持续 + 审核闭环 + DisplayName中文化 + categoryIds验证

> **日期**: 2026-07-25
> **上一轮完成**: V58 — 审核工作流修复(发现正确API: POST /admin/skills/{slug}/approve {versionId}) + 385个admin_review审核通过(0失败) + 121个-sk幻影slug清理 + visibility:public验证通过(100/100) + iconUrl 100%覆盖 + ai-artist-workstation-pro slug修复 + 批量重传493/1938(27%)
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 继续批量重传剩余1295个skill + 持续审核新admin_review + 处理41个rejected

## V58完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| 企业Cookie认证 | ✅ | check-auth返回✅, 平台skill从1739增至1933 |
| 审核工作流修复 | ✅ | 发现正确API: POST /admin/skills/{slug}/approve with {"versionId": vid}，仅对admin_review状态有效 |
| 批量审核admin_review | ✅ | 385个审核通过(230+80+75)，0失败 |
| -sk后缀幻影slug清理 | ✅ | 121个SKILL.md未找到记录清除 |
| visibility:public验证 | ✅ | 第一页100/100 public，所有重传skill均public |
| iconUrl覆盖验证 | ✅ | 第一页100/100有iconUrl |
| ai-artist-workstation-pro修复 | ✅ | 创建本地目录+修改slug为ai-artist-workstation-pro |
| 批量重传 | ⏳ | 493/1938完成(27%)，进程运行中 |
| pending审核处理 | ⏳ | 156个pending等待平台转为admin_review |
| rejected审核处理 | ❌ | 41个rejected需DELETE+重传 |
| Git提交 | ❌ | 本轮执行 |

## 关键API发现（V58核心突破）

### 审核API工作流
```
上传skill(POST) → 创建版本 → reviewStatus=pending
    ↓ (平台自动处理，不可API控制)
reviewStatus=admin_review ← 可被管理员审核
    ↓ POST /api/v1/orgs/{ORG_ID}/admin/skills/{slug}/approve {"versionId": vid}
reviewStatus=approved ← 审核通过，skill变为published
```

### 关键端点
| 操作 | 端点 | 方法 | Body | 状态要求 |
|------|------|------|------|---------|
| 获取审核列表 | `/orgs/{ORG_ID}/admin/skills/reviews` | GET | - | - |
| 审核通过 | `/orgs/{ORG_ID}/admin/skills/{slug}/approve` | POST | `{"versionId": 168087}` | admin_review |
| 获取skill列表 | `/orgs/{ORG_ID}/admin/skills` | GET | - | - |
| 上传skill | `/orgs/{ORG_ID}/skills` | POST | FormData | - |
| 删除skill | `/orgs/{ORG_ID}/admin/skills/{slug}` | DELETE | - | - |

### 不存在的端点（404）
- `/admin/skills/{slug}/submit` — 无submit API
- `/admin/skills/{slug}/visibility` — 无visibility修改 API
- `/admin/skills/{slug}` PUT/PATCH — 无非破坏性更新 API
- `/admin/skills/reviews/{vid}/approve` — 无按versionId审核

### 核心约束
- **pending → admin_review转换不可API控制** — 平台自动处理，需等待
- **visibility修改只能DELETE+重传** — 无PATCH/PUT API
- **categoryIds/tags/summary_zh修改只能DELETE+重传** — 无非破坏性更新

## 平台当前状态（V58结束）

### 审核状态
| 状态 | 数量 | 说明 |
|------|------|------|
| approved | 1933 | ✅ 已审核通过 |
| pending | 156 | ⏳ 等待平台转为admin_review |
| admin_review | 1 | 🔔 可立即审核 |
| rejected | 41 | ❌ 需DELETE+重传 |
| platform_review | 20 | ⏳ 平台处理中 |

### Skill状态
| 指标 | 值 | 说明 |
|------|------|------|
| 平台skill总数 | 1933 | 从1739增至1933(+194) |
| 重传成功 | 493 | 携带visibility:public+categoryIds+iconUrl+tags+summary_zh |
| 重传剩余 | 1295 | 进程运行中 |
| 第一页visibility | 100% public | ✅ |
| 第一页iconUrl | 100% | ✅ |

## 实施任务

### 任务1: 持续批量重传剩余1295个skill (P0 — 进程运行中)

**当前状态**: 493/1938完成，进程运行中

```bash
cd D:\skills\tools
python batch_field_fix.py reupload-all-batch
```

**断点续传**: 从`data/reports/batch_reupload_progress.json`读取已完成slug

**验证**:
- 重传完成后，平台skill总数应接近1938
- 抽样10个skill通过API GET检查 categoryIds, iconUrl, summary_zh, tags
- `/admin/skills/categories` 分类不再为0

### 任务2: 持续审核新admin_review (P0 — 循环执行)

**机制**: 平台会自动将pending转为admin_review，需定期审核

```bash
python c:\Users\thcd\.trae-cn\work\6a6322fd6711a0efa7a6c030\batch_approve_admin_review.py
```

**断点续传**: 从`data/reports/batch_approve_progress_v2.json`读取已完成

**验证**: approved数量持续增长，pending数量持续减少

### 任务3: 处理41个rejected审核 (P0)

**执行方案**: rejected的skill需DELETE+重传

```bash
cd D:\skills\tools
python batch_field_fix.py reupload-rejected
```

**41个rejected slugs**:
api-doc-writer, aegis-security-tool-pro, whatsapp-styler, web-vulnerability-assessment, web-content-fetcher, text-rpg-arcade-v3, tardis, secure-api-calls, qq-zone-photo, productivity-improving, okx-dex-token-paid, logo-design-guide, docker-ctl, data-analysis-litiao, audio-upload-aioz-stream-free, audio-stream-upload, audio-upload-aioz-stream, aegis-security-tool-free, audio-stream-upload-free, xml-reader, video-upload-aioz-stream, ui-ux-dev, trade-with-taro, text-game-arcade-universe-v3, rho-telegram-alerts, read-github, python-data-analysis, podcast-downloader, ocean-chat, obsidian-official-cli, netpad, moltbook-firewall, markdown-converter, jellyfin-control, git-workflows, file-browser, feishu-calendar, doc, compress-pdf, baoyu-format-markdown, ai-artist-workstation-pro

**验证**: 41个rejected skill DELETE+重传成功，重新进入审核队列

### 任务4: categoryIds/tags/summary_zh字段验证 (P1)

**问题**: 列表API不返回categoryIds/tags字段，需通过详情API验证

**执行方案**:
1. 编写验证脚本，抽样20个已重传skill
2. 通过详情API GET检查字段完整性
3. 统计categoryIds/tags/summary_zh覆盖率

**验证标准**:
- categoryIds: 非空数组，包含正确的团队分类数字ID
- tags: 非空数组，包含1-5个标签
- summary_zh: 非空字符串
- iconUrl: 非空URL

### 任务5: DisplayName中文化 (P1)

**问题**: 约40%的skill displayName仍为英文

**执行方案**:
1. 扫描所有SKILL.md的displayName字段
2. 对英文displayName生成中文翻译
3. 保持语义一致，不改变技能原有含义
4. DELETE+重传修改后的skill

**验证标准**:
- 100%的displayName为中文
- 翻译准确，无机器翻译痕迹
- 无虚假功能描述

### 任务6: 处理156个pending审核 (P1 — 等待平台)

**机制**: pending状态不可API控制，需等待平台自动转为admin_review

**执行方案**:
1. 定期运行batch_approve_admin_review.py
2. 监控pending数量变化
3. 当pending转为admin_review后立即审核

**验证**: pending数量持续减少，approved数量持续增长

### 任务7: Git提交与下一轮提示词生成

```bash
cd D:\skills
git add -A
git commit -m "fix: V58-59 — 审核工作流修复(385个admin_review通过) + 批量重传493/1938 + visibility:public验证 + ai-artist-workstation-pro slug修复 + -sk幻影清理"
git push origin master
git push hermes-skills master
```

生成 `next-round-prompt-v60.0.md`，包含:
- P0: 继续批量重传(如未完成)
- P0: 持续审核新admin_review
- P1: Verified认证申请
- P1: Downloads/stars积累策略
- P2: 所有权认领
- P2: 搜索排名优化

## 任务执行顺序

```
任务1 (批量重传1295个) ──────────────────────┐
                                              │
任务2 (持续审核admin_review) ── 循环执行 ─────┤
                                              ├──→ 任务7 (Git提交)
任务3 (处理41个rejected) ── 需任务1空闲 ──────┤
                                              │
任务4 (字段验证) ── 需任务1部分完成 ──────────┤
                                              │
任务5 (DisplayName中文化) ── 可并行 ──────────┤
                                              │
任务6 (等待pending转admin_review) ── 循环 ────┘
```

## 验证检查清单

- [ ] 1295个skill重传完成(总计1938/1938)
- [ ] `/admin/skills/categories` 分类不再为0
- [ ] 抽样20个skill的 categoryIds, iconUrl, summary_zh, tags 字段正确
- [ ] 41个rejected skill DELETE并重新上传成功
- [ ] 156个pending审核全部转为admin_review并审核通过
- [ ] 100%的displayName为中文
- [ ] 平台skill总数 ≈ 1938
- [ ] approved审核数 ≈ 2100+
- [ ] Git提交并推送
- [ ] 下一轮提示词v60.0生成

## 约束

1. **增强已有代码** — 不创建碎片化新文件，所有修复功能集成到现有工具脚本
2. **不模拟/mock** — 所有操作必须真实执行
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏enterprise_uploader.py现有功能
5. **企业账号** — 所有API操作必须使用企业团队账号Cookie
6. **categoryIds** — 所有上传必须包含categoryIds数字ID数组
7. **visibility:public** — 所有上传必须包含visibility:public
8. **断点续传** — 全量重传支持从报告文件恢复进度
9. **内容保真** — DisplayName翻译不得改变技能原有语义
10. **分类统一** — 本地分类=skillhub分类=clawhub分类
11. **审核工作流** — admin_review状态才能approve，pending需等待平台
12. **非破坏性更新不可用** — categoryIds/tags/summary_zh修改只能DELETE+重传
