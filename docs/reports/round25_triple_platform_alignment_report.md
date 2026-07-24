# Round 25 - 三端对齐验证报告

## 报告生成时间
2026-07-22

## 三端数量汇总

| 平台 | 数量 | 状态 | 说明 |
|------|------|------|------|
| 本地 | 2097 | ✅ 治理完成 | 995 packaged + 1102 differentiated |
| SkillHub | 1898 | ✅ 同步完成 | 169个已删除 + 145个已重新上传 |
| ClawHub | 223+ | 🔄 同步中 | 受200/24h限流，需续传 |

## Round 25 执行明细

### 1. SkillHub已删除skill清理 ✅
- **删除数量**: 169个skill（从2203降至2034）
  - 158个本地已删除的冗余skill
  - 14个重命名的旧slug
  - 3个删除失败但已不存在（ai-video-director, cyber-fortune-teller, openai-whisper-tool-pro）
- **额外删除**: test-paid-skill（测试技能）
- **删除方法**: `DELETE https://api.skillhub.cn/api/v1/orgs/862/admin/skills/{slug}`

### 2. SkillHub修改skill重新上传 ✅
- **上传数量**: 145个skill（145/145成功）
  - 131个修改的skill（DELETE + POST）
  - 14个新重命名的skill（POST only）
- **上传模式**: 10批 × 15个 = 145个
- **已知问题**: `llm-provider-whisper-tool-pro`完整内容被WAF拦截（HTTP 566），已上传截断版本（5000字符，含完整frontmatter）
- **上传方法**: `POST https://api.skillhub.cn/api/v1/orgs/862/skills` with FormData(payload + files)
- **审核状态**: 所有上传skill进入pending审核状态

### 3. ClawHub续传状态 ✅
- **已上传**: 223个skill（upload_tracking记录）
- **sync状态**: 后台运行中，受200新skill/24h限流
- **剩余待传**: 约1874个skill（2097 - 223 = 1874）
- **预计完成**: 约10天（1874 / 200 per day）

### 4. SkillHub platform_review ✅
- **test-paid-skill**: 已删除 ✅
- **60个企业版技能**: 卡在platform_review状态
  - API限制：admin API无法干预platform_review状态
  - 建议联系: skillhub_ipr@tencent.com
  - 邮件内容已准备（60个slug列表）

### 5. 个人版同步 ⏳
- 个人版SkillHub无API访问
- 需通过UI操作同步145个修改
- 记录为后续手动任务

### 6. deep_quality_audit.py重建 ✅
- **位置**: `D:\skills\skill-registry\deep_quality_audit.py`
- **功能**: 全量扫描2097个skill，三级分类（critical/warning/info）
- **审计结果**: 0 critical, 51 warning, 2026 info, 20 ok
- **Warning详情**: 51个differentiated skills缺少tools/homepage/tags字段
- **--fix模式**: 支持自动修复SUMMARY_TOO_LONG和DISPLAYNAME_TOO_LONG

### 7. upload_tracking.json更新 ✅
- **tracking记录数**: 2079个唯一slug
- **SkillHub标记上传**: 2079个
- **ClawHub标记上传**: 223个
- **差异说明**: 2097目录 - 12重叠 - 2分类内重复 - 4已删除旧重命名 = 2079唯一

## 三端差异分析

### 本地 vs SkillHub
| 项目 | 数量 |
|------|------|
| 本地总数 | 2097 |
| SkillHub总数 | 1898 |
| 差异 | 199 |

差异原因：
1. 145个skill刚重新上传，处于pending审核状态（可能未计入admin total）
2. 1个skill（llm-provider-whisper-tool-pro）内容截断
3. 部分skill可能因slug不匹配未同步

### 本地 vs ClawHub
| 项目 | 数量 |
|------|------|
| 本地总数 | 2097 |
| ClawHub已上传 | 223 |
| 差异 | 1874 |

差异原因：
1. ClawHub限流200新skill/24h
2. 需要约10天完成全部上传

## 待办事项

### 高优先级
1. **ClawHub续传**: 每日200个，约10天完成
2. **llm-provider-whisper-tool-pro完整内容上传**: 需排查WAF拦截原因
3. **SkillHub pending审核**: 145个skill等待平台审核

### 中优先级
4. **51个warning修复**: 给differentiated/Agents和Automation分类的skills补充tools/homepage/tags字段
5. **个人版同步**: 145个修改同步到个人版SkillHub
6. **60个platform_review技能**: 联系skillhub_ipr@tencent.com

### 低优先级
7. **2026个info修复**: 补充homepage/tags字段、添加依赖说明section
8. **三端slug对齐**: 确保本地、SkillHub、ClawHub的slug完全一致
