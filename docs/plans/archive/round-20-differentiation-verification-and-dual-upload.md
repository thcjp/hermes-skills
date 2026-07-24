# Round 20: 差异化skill质量验证 + 双平台上传 + 旧skill撤回

## 背景与上下文

Round 19 完成了全部 1017 个 packaged skill 的质量闭环:

| 指标 | Round 18 | Round 19 | 目标 | 状态 |
|------|----------|----------|------|------|
| L3 PASS | 100% | **100%** | ≥50% | ✅ |
| L4 PASS+WARN | 97% | **100%** | ≥70% | ✅ |
| SF≥70 | 94% | **100%** | ≥80% | ✅ |
| 三关全通过 | 94% | **100%** | ≥90% | ✅ 超额 |

**1017/1017 skills 全部通过 L3+L4+SF 三关验证 (100%)。**

### Round 19 关键修复

1. **L4-2 exec移除** (19 skills): MD-only skill误标exec → 从tools中移除exec
2. **L4-3 空话替换** (21 skills): "重试"等空话 → 具体可执行操作描述
3. **L4-5+L4-6 使用流程** (4 skills): timer/whatsapp → 添加结果处理+线性步骤
4. **L4-1 标题修复** (1 skill): pg-job-queue → "依赖说明"改名为"环境配置与依赖管理"
5. **L4-2 日期格式误报** (1 skill): iris-code-formatter → YYYY-MM-DD改为YYYYMMDD
6. **SF checker修复**: 原创注册表检查优先于源skill加载
7. **SF=0修复** (61 skills): 加入原创注册表获得SF=100
8. **L3-6修复** (1 skill): pg-job-queue → 补充LLM/环境/API Key/分类

### 当前资产盘点

| 资产 | 数量 | 位置 |
|------|------|------|
| Packaged skills (已验证) | 1017 | `D:\skills\packaged-skills\skillhub\` |
| 下载的clawhub源skill | 600 | `D:\skills\clawhub-skills\downloaded\` |
| 差异化skill | 1251 | `D:\skills\differentiated-skills\` (14个类别) |
| 原创skill注册表 | 522 | `D:\skills\skill-registry\original_skills_registry.json` |
| clawhub已上传 | ~165 | https://clawhub.ai/@thcjp |
| SkillHub企业版已上传 | 60 | 企业版 (org 862) |

### 差异化skill分类分布

| 类别 | 数量 | 类别 | 数量 |
|------|------|------|------|
| Agents | 73 | Knowledge | 64 |
| Automation | 106 | Lifestyle | 36 |
| Communication | 76 | Operations | 28 |
| Creative | 130 | Other | 180 |
| Development | 100 | Productivity | 78 |
| Finance | 24 | Research | 116 |
| Integrations | 192 | Security | 48 |

### 关键代码文件

- `D:\skills\skill-registry\l3_function_checker.py` - L3检查器(7维度)
- `D:\skills\skill-registry\l4_task_gate.py` - L4检查器(6维度)
- `D:\skills\skill-registry\source_fidelity_checker.py` - SF检查器(已修复注册表优先)
- `D:\skills\skill-registry\quality_gate.py` - L1格式检查器
- `D:\skills\skill-registry\upload_gate.py` - 上传关卡
- `D:\skills\skill-registry\original_skills_registry.json` - 原创skill注册表(522个)
- `D:\skills\skill-registry\full_verification_results.json` - 全量验证结果

### 已建立的架构原则

1. **4层质量门**: L1(格式) → L2(SF+Cap) → L3(功能) → L4(任务) → 上传
2. **SF checker注册表优先**: 先检查原创注册表,再加载源skill
3. **NON_CAPABILITY_HEADINGS**: 元信息标题在L3-2/L4-1/L4-5中统一过滤
4. **原创skill注册表**: 无clawhub源的skill自动获得SF=100
5. **clawhub CLI上传**: `npx clawhub sync --root <dir> --all --changelog "<text>" --concurrency 15 --json`
6. **SkillHub CLI无publish**: 需通过Trae Work对话命令或企业版API上传

## Round 20 目标

1. **完成1017个packaged skill的clawhub上传** (当前~165/1017)
2. **验证1251个差异化skill的质量** (L1+L2+L3+L4+SF)
3. **差异化skill双平台上传** (clawhub + SkillHub)
4. **撤回51个旧skill** (需先确定具体列表)
5. **SkillHub企业版 monetization配置** (定价、分类)

## 执行步骤

### Step 20.1: 完成clawhub上传 (1017 skills)

**背景**: Round 19启动的clawhub sync正在后台运行,当前已上传约165个

**执行**:
1. 检查clawhub sync进程状态
2. 如进程已退出,检查输出JSON确认上传结果
3. 如有失败,重试上传失败的skill
4. 通过浏览器验证clawhub.ai/@thcjp的skill数量达到1017
5. 抽样检查10个skill的displayName/summary/description显示正确

**验证命令**:
```bash
# 检查上传结果
cat D:\skills\skill-registry\upload_results_round19.json | python -m json.tool

# 重新上传失败的skill(如有)
$env:CLAWHUB_SITE="https://clawhub.ai"
npx clawhub sync --root "D:\skills\packaged-skills\skillhub" --all --changelog "Retry failed uploads" --concurrency 15 --json
```

### Step 20.2: 差异化skill质量验证

**背景**: 1251个差异化skill需要通过L1+L2+L3+L4+SF验证

**执行**:
1. 将差异化skill从 `D:\skills\differentiated-skills\` 各类别子目录汇总
2. 对全部1251个差异化skill运行L1+L2+L3+L4+SF检查
3. 记录验证结果,分类失败维度
4. 对失败skill进行批量修复
5. 确保差异化skill的三关通过率≥90%

**验证脚本**:
```python
# 需要创建 differentiate_verification.py
# 遍历 D:\skills\differentiated-skills\ 下所有类别子目录
# 对每个skill运行L3+L4+SF检查
# 输出结果到 D:\skills\skill-registry\differentiated_verification_results.json
```

### Step 20.3: 差异化skill深度差异化验证

**背景**: 项目记忆要求"深度差异化必须提升质量、实用性、可用性,或降低LLM成本、提升效率或性能"

**执行**:
1. 对比差异化skill与源skill,确认差异化程度:
   - 能力增强(新增功能/参数)
   - 成本降低(减少LLM调用/简化流程)
   - 体验优化(更好的错误处理/更清晰指令)
   - 性能提升(更快的处理/更少资源)
2. 检查差异化skill是否移除了原项目烙印(narrato/fishclaw/xianyu等)
3. 检查差异化skill的slug是否全局唯一(与packaged-skills不冲突)
4. 为每个差异化skill编写差异化说明(changelog)

### Step 20.4: 差异化skill上传到clawhub

**执行**:
1. 将验证通过的差异化skill准备上传
2. 解决slug冲突(差异化skill vs packaged skill)
3. 按类别分批上传到clawhub
4. 验证上传结果

**命令**:
```bash
$env:CLAWHUB_SITE="https://clawhub.ai"
npx clawhub sync --root "D:\skills\differentiated-skills" --all --changelog "Differentiated skills with quality enhancement" --concurrency 15 --json
```

### Step 20.5: 差异化skill上传到SkillHub

**背景**: SkillHub CLI无publish命令,需通过Trae Work对话命令或企业版API上传

**执行**:
1. 检查SkillHub企业版API (org 862)是否可用
2. 使用企业版API批量上传差异化skill
3. 配置定价(per_call/monthly/one_time)
4. 配置分类(通用办公/研发工具/系统运维等)

**企业版API**:
```python
# POST https://api.skillhub.cn/api/v1/orgs/862/skills with FormData
# 参考 D:\skills\skill-registry\enterprise_uploader.py
```

### Step 20.6: 确定并撤回51个旧skill

**背景**: 项目记忆记录"Clawhub upload of 51 skills must be撤回"

**执行**:
1. 通过clawhub API或浏览器获取当前已上传的所有skill列表
2. 对比当前1017个packaged skill,找出不在列表中的旧skill
3. 或者查找上传时间最早的51个skill(可能是第一批低质量上传)
4. 使用 `npx clawhub delete <skill> --reason "Replaced by quality-verified version" --yes` 批量撤回
5. 验证撤回结果

### Step 20.7: SkillHub企业版 monetization配置

**背景**: SkillHub有SkillPay monetization机制(企业认证、微信支付商户绑定)

**执行**:
1. 检查企业认证状态(四川云物益邦科技有限公司, org 862)
2. 配置微信支付商户绑定
3. 为已上传的60+差异化skill设置定价:
   - 按次付费 (per_call): 1.9-50.0 CNY
   - 月度订阅 (monthly): 9.9-99.0 CNY
   - 一次性购买 (one_time): 19.9-199.0 CNY
4. 配置skill分类和标签

### Step 20.8: 全量验证报告

**执行**:
1. 生成Round 20全量验证报告:
   - clawhub上传状态 (1017 packaged + N differentiated)
   - SkillHub上传状态 (60+ enterprise)
   - 质量验证状态 (L3+L4+SF通过率)
   - 旧skill撤回状态
   - monetization配置状态
2. 更新项目记忆

### Step 20.9: 生成Round 21提示词

**执行**:
1. 分析Round 20完成情况
2. 生成Round 21提示词文档

## 验证命令

```bash
# 全量验证(packaged skills)
python c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\full_verification.py

# 差异化skill验证(需创建脚本)
python c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\differentiate_verification.py

# clawhub上传
$env:CLAWHUB_SITE="https://clawhub.ai"
npx clawhub sync --root "D:\skills\packaged-skills\skillhub" --all --changelog "Round 20 upload" --concurrency 15 --json

# SkillHub企业版上传
python D:\skills\skill-registry\enterprise_uploader.py

# clawhub skill撤回
npx clawhub delete <skill-slug> --reason "Replaced by quality-verified version" --yes
```

## 注意事项

1. **不要降低标准**: 差异化skill必须通过L3+L4+SF验证才能上传
2. **slug全局唯一**: 差异化skill的slug不能与packaged skill冲突
3. **移除项目烙印**: 差异化skill的名称/介绍/触发词不能包含narrato/fishclaw/xianyu等
4. **差异化深度**: 每个差异化skill必须有实质性改进,不是简单改名
5. **上传前验证**: 每个skill上传前必须确认已通过L1+L2+L3+L4全部门
6. **使用brainstorming skill**: 在开始差异化验证前,先用brainstorming skill确认验证策略
7. **使用dogfood skill**: 对样本差异化skill进行实际任务测试
8. **使用git-commit skill**: 每完成一个步骤后提交代码
9. **clawhub CLI认证**: 需设置 `$env:CLAWHUB_SITE="https://clawhub.ai"` 和有效token
10. **SkillHub上传**: CLI无publish命令,需通过企业版API或Trae Work对话命令上传
