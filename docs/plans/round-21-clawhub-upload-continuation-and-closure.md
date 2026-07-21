# Round 21: ClawHub上传续传 + 旧skill撤回 + 最终闭环

## 背景与上下文

### Round 20 完成情况

| 任务 | 状态 | 结果 |
|------|------|------|
| SkillHub企业版上传 | ✅ 完成 | 1925成功/70失败/138跳过 |
| ClawHub认证修复 | ✅ 完成 | registry从mirror-cn改为clawhub.ai, whoami返回thcjp |
| ClawHub slug冲突修复 | ✅ 完成 | 3个slug重命名: api→rest-api-reference, agent-browser-clawdbot→agent-browser-automation, clawhub-jira-pat-skill→jira-pat-toolkit |
| ClawHub旧skill撤回 | ❌ 平台限制 | CLI delete/hide需要moderator权限; delete --version调用assertCanManageOwnedResource也返回Forbidden |
| ClawHub上传 | ⏳ 限流中 | 232已同步, ~785待上传, 限流200/24h |
| 旧skill识别 | ✅ 完成 | 455个已发布skill中221个为旧skill(本地不存在) |
| Git commit | ✅ 完成 | 本轮变更已提交 |

### 关键技术发现

1. **ClawHub认证修复**:
   - 配置文件`clawhub-config.json`中的registry URL错误(`https://mirror-cn.clawhub.com`)
   - 正确的registry是`https://clawhub.ai`
   - 使用`--registry "https://clawhub.ai"`标志或设置`$env:CLAWHUB_REGISTRY`
   - `whoami`返回`thcjp`,认证正常

2. **ClawHub slug保护机制**:
   - 保留slug: `api` (系统保留)
   - 保护命名空间: `clawdbot-*`, `*-clawdbot`, `clawhub-*`, `*-clawhub`
   - 冲突解决: 重命名文件夹+更新SKILL.md中的slug和name字段

3. **ClawHub删除限制**:
   - `delete`命令调用`setSkillSoftDeletedByActor` → 需要`assertModerator`
   - `hide`命令同样需要`assertModerator`
   - `delete --version`调用`deleteOwnedSkillVersionForUser` → 需要`assertCanManageOwnedResource`
   - 当前用户`thcjp`无moderator权限,无法通过CLI删除任何skill
   - Web Dashboard显示31个skill(仅最近更新),无法管理全部455个
   - 需要联系ClawHub支持团队或获取moderator权限

4. **ClawHub限流机制**:
   - 每日最多200个新skill
   - 限流重置时间: 约24小时滑动窗口
   - 已同步: 232个skill (Round 19上传)
   - 待上传: ~785个skill (修复slug冲突后)

5. **ClawHub已发布skill盘点**:
   - 通过API `https://clawhub.ai/api/v1/skills?owner=thcjp`获取
   - 总计455个skill (含`latestVersion: null`的未发布版本)
   - 其中221个在本地不存在(旧skill)
   - 234个在本地存在(当前有效skill)

### 当前资产盘点

| 资产 | 数量 | 位置 | 状态 |
|------|------|------|------|
| Packaged skills (已验证) | 1017 | `D:\skills\packaged-skills\skillhub\` | 100%通过 |
| 差异化skills (已修复) | 1251 | `D:\skills\differentiated-skills\` | 98.7%通过 |
| ClawHub已同步 | 232 | https://clawhub.ai/@thcjp | 含3个重命名skill |
| ClawHub待上传 | ~785 | 本地 | 限流200/24h |
| ClawHub旧skill | 221 | ClawHub平台 | 无法删除(需moderator) |
| SkillHub企业版 | 1925 | org 862 | 已上传 |
| SkillHub已发布 | 6 | 公开可见 | 选题捕手等 |

## Round 21 目标

1. **完成ClawHub上传** (785个skill, 分4天完成, 每天200个)
2. **解决旧skill撤回问题** (联系ClawHub支持或获取moderator权限)
3. **差异化skill上传到ClawHub** (1251个, 同样分批)
4. **全量验证报告** (双平台最终状态)
5. **SkillHub monetization配置** (如需要)

## 执行步骤

### Step 21.1: ClawHub上传续传 (785个packaged skills)

**背景**: 限流已部分重置, 可继续上传

**执行**:
1. 确认限流状态: `npx clawhub --registry "https://clawhub.ai" publish [skill-path] --changelog "Quality verified"`
2. 如限流已重置, 执行批量同步:
   ```powershell
   npx clawhub --registry "https://clawhub.ai" sync --root "D:\skills\packaged-skills\skillhub" --all --changelog "Quality verified - L3+L4+SF passed" --concurrency 5
   ```
3. 注意: concurrency设为5(降低并发避免限流)
4. 预计需要4天完成(785/200≈4天)
5. 每天记录上传进度

**关键文件**:
- `D:\skills\skill-registry\clawhub_published_slugs.json` - 已发布skill列表
- `D:\skills\skill-registry\clawhub_withdrawal_list.json` - 待撤回skill列表(221个)

### Step 21.2: 处理版本冲突

**背景**: 部分skill可能已上传旧版本, 需递增版本号

**执行**:
1. 对sync中"Version 1.0.0 already exists"的skill, 递增版本号到1.0.1
2. 修改SKILL.md中的`version`字段
3. 重新上传

### Step 21.3: 旧skill撤回方案

**背景**: CLI无法删除, 需要替代方案

**方案A: 联系ClawHub支持**:
- 通过Discord/GitHub联系ClawHub团队
- 请求批量删除221个旧skill
- 提供slug列表: `D:\skills\skill-registry\clawhub_withdrawal_list.json`

**方案B: 获取moderator权限**:
- 申请成为ClawHub moderator
- 获取权限后使用CLI批量删除

**方案C: 覆盖更新**:
- 对221个旧slug重新上传新版本(覆盖旧内容)
- 这不能删除skill, 但可以更新内容

### Step 21.4: 差异化skill上传到ClawHub

**背景**: 1251个差异化skill需上传到ClawHub

**执行**:
1. 检查差异化skill的slug是否与packaged skill冲突
2. 对冲突的slug添加`-diff`后缀
3. 分批上传(每天200个, 预计7天)

### Step 21.5: 全量验证报告

**执行**:
1. 生成ClawHub上传状态报告
2. 生成SkillHub上传状态报告
3. 对比双平台skill数量
4. 验证skill内容一致性

## 注意事项

1. **ClawHub registry**: 必须使用`--registry "https://clawhub.ai"`标志, 配置文件中的URL可能不被自动加载
2. **Slug保护**: 避免使用`api`, `clawhub-*`, `clawdbot-*`等保留/保护slug
3. **限流策略**: 每日最多200个新skill, 需合理规划上传批次
4. **删除限制**: 当前用户无moderator权限, 无法通过CLI删除skill
5. **版本冲突**: 已上传的skill需递增版本号才能重新上传
