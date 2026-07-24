# Round 20: 上传完成 + 残留修复 + 旧skill撤回

## 背景与上下文

### Round 19 完成情况

Round 19 的核心任务已全部完成:

| 任务 | 状态 | 结果 |
|------|------|------|
| 1017 packaged skills 验证 | ✅ 完成 | L3=100%, L4=100%, SF=100%, Combined=100% |
| 1251 差异化 skills 验证与修复 | ✅ 完成 | L3=100%, L4=98.9%, SF=99.8%, Combined=98.7% |
| 差异化skill L3批量修复 | ✅ 完成 | 3轮修复: 核心能力格式标准化+关键词对齐+内容实质性 |
| 差异化skill L4批量修复 | ✅ 完成 | 5维度修复: 用户体验+命令执行+输出标准+错误恢复+依赖闭环 |
| SkillHub企业版上传 | ✅ 完成 | 1925成功/70失败/138跳过(已存在), 用户命名空间@user_cb75122a/ |
| clawhub上传 | ❌ 阻塞 | 认证token过期,whoami返回"invalid value" |
| 51个旧skill撤回 | ❌ 阻塞 | 依赖clawhub认证 |
| monetization配置 | ❌ 未开始 | 需要企业认证+微信支付商户绑定 |

### SkillHub 上传最终结果 (Round 19 完成)

- **总上传**: 2233个skill (1014 packaged + 1219 differentiated)
- **成功**: 1925个 (HTTP 200/201)
- **跳过**: 138个 (HTTP 409, 已存在)
- **失败**: 70个 (slug格式无效或其他错误)
- **命名空间**: `@user_cb75122a/` (用户个人命名空间)
- **已发布(公开可见)**: 6个 (选题捕手等, org 862 published)
- **验证**: agent-copilot-pro, aws-cloud-architect, code-review-expert 等可通过 `/api/v1/skills/{slug}` 访问(200)

### Round 19 关键修复

#### 差异化skill L3修复 (3轮)

1. **第一轮 (diff_batch_fix.py)**: 
   - 核心能力编号列表 → ###标题格式
   - 使用流程步骤格式标准化 (步骤N → Step N)
   - 补充缺失章节 (FAQ/已知限制/输出格式)
   - free版本升级提示
   - 修复1044/1251个文件

2. **第二轮 (diff_batch_fix2.py)**:
   - description关键词对齐到核心能力章节
   - 能力点详细指示符补充 (动作动词+代码引用)
   - 模板套话清除
   - 使用流程/示例/已知限制章节补充

3. **第三轮 (diff_batch_fix3.py)**:
   - NON_CAPABILITY_HEADINGS同步 (7个新条目)
   - L3-5错误处理章节补充
   - 关键词对齐替换修复
   - 最终L3 PASS: 1251/1251 (100%)

#### 差异化skill L4修复 (diff_l4_batch_fix.py)

1. **L4-6 用户体验完整性**: 使用流程线性化+FAQ+已知限制+free版升级提示
2. **L4-5 输出标准明确性**: 输出格式章节+能力点输出描述+使用流程结果处理
3. **L4-2 命令可执行性**: 脚本获取说明+命令参数解释
4. **L4-3 错误恢复可操作性**: VAGUE_TO_ACTION替换+表头修复
5. **L4-4 依赖闭环性**: LLM能力描述+API Key获取/配置+运行环境
6. 最终L4 PASS+WARN: 1237/1251 (98.9%), 仅剩14个L4-1失败

### 当前资产盘点

| 资产 | 数量 | 位置 | 状态 |
|------|------|------|------|
| Packaged skills (已验证) | 1017 | `D:\skills\packaged-skills\skillhub\` | 100%通过 |
| 差异化skills (已修复) | 1251 | `D:\skills\differentiated-skills\` | 98.7%通过 |
| 差异化skills (未通过) | 16 | `D:\skills\differentiated-skills\` | 14个L4-1+2个SF |
| clawhub已上传 | ~170 | https://clawhub.ai/@thcjp | 认证过期 |
| SkillHub企业版已上传 | 6+188+ | org 862 | 后台上传中 |
| SkillHub已发布 | 6 | 公开可见 | 选题捕手等 |

### 关键技术发现

1. **SkillHub企业版API**:
   - POST https://api.skillhub.cn/api/v1/orgs/862/skills
   - 需要FormData: `payload`(JSON) + `files`(SKILL.md文件blob)
   - tags和tools必须是数组(不能是字符串)
   - slug必须匹配 `^[a-z0-9][a-z0-9-]*[a-z0-9]$`
   - 已存在的slug返回409
   - Python requests无法认证(401),必须通过浏览器fetch+credentials:'include'

2. **clawhub CLI认证**:
   - token已过期,whoami返回"invalid value"
   - 需要重新登录: `clawhub login`
   - 限流: 每日最多200个新skill
   - 已上传skill重复上传返回"Version 1.0.0 already exists"

3. **L3/L4检查器函数签名**:
   - `parse_frontmatter()` 返回dict(不是tuple)
   - L3-1/L3-3/L3-6接受(content, fm_data), L3-2/L3-4/L3-5/L3-7接受(content)
   - 所有L3/L4函数返回Tuple[str, List[str]] = (status, errors)
   - L4所有函数都接受(content, fm_data)

## Round 20 目标

1. **完成SkillHub企业版上传** (当前进行中,目标2233个)
2. **修复clawhub认证并完成上传** (1017 packaged + 1235 differentiated)
3. **撤回51个旧skill** (需先确定具体列表)
4. **修复16个未通过差异化skill** (14个L4-1+2个SF)
5. **SkillHub monetization配置** (定价、分类)
6. **全量验证报告** (双平台上传状态+质量验证状态)

## 执行步骤

### Step 20.1: SkillHub上传失败skill重试

**背景**: Round 19后台上传已完成,1925个成功,70个失败(主要是slug格式无效)

**执行**:
1. 从 `window._uploadProgress` 获取失败列表(如有)
2. 分析70个失败skill的失败原因(slug格式/内容问题)
3. 修复slug格式问题(移除中文括号等非法字符)
4. 重新上传修复后的skill
5. 验证SkillHub用户命名空间下的skill总数达到2000+

### Step 20.2: 修复clawhub认证

**背景**: clawhub CLI token已过期

**执行**:
1. 运行 `clawhub login` 重新认证
2. 验证 `clawhub whoami` 返回正确用户
3. 如无法通过CLI登录,通过浏览器获取cookie

### Step 20.3: 完成clawhub上传

**背景**: 1017个packaged skill需上传到clawhub,当前约170个已上传

**执行**:
1. 检查已上传skill列表
2. 对未上传的skill执行clawhub sync
3. 注意每日200个新skill限制
4. 对差异化skill也执行上传
5. 处理"Version 1.0.0 already exists"错误(递增版本号)

**命令**:
```bash
$env:CLAWHUB_SITE="https://clawhub.ai"
npx clawhub sync --root "D:\skills\packaged-skills\skillhub" --all --changelog "Quality verified skills" --concurrency 15 --json
```

### Step 20.4: 撤回51个旧skill

**背景**: 项目记忆记录"Clawhub upload of 51 skills must be撤回"

**执行**:
1. 通过 `clawhub list` 获取所有已上传skill
2. 对比当前1017个packaged skill slug
3. 找出不在当前列表中的旧skill(可能是第一批低质量上传)
4. 使用 `clawhub delete <slug> --yes` 批量撤回
5. 验证撤回结果

### Step 20.5: 修复16个未通过差异化skill

**背景**: 14个L4-1失败(核心能力标题缺少输入/输出/处理描述), 2个SF<70

**执行**:
1. 从 `D:\skills\skill-registry\differentiated_verification_results.json` 获取16个失败skill列表
2. 逐个检查L4-1失败原因(核心能力标题格式问题)
3. 手动修复或编写针对性修复脚本
4. 重新验证修复后的skill
5. 将修复后的skill上传到SkillHub

### Step 20.6: SkillHub monetization配置

**背景**: SkillHub有SkillPay机制(per_call/monthly/one_time)

**执行**:
1. 检查企业认证状态(四川云物益邦科技有限公司)
2. 配置微信支付商户绑定(如未配置)
3. 为已上传skill设置定价:
   - 通用工具类: 按次1.9-9.9 CNY
   - 专业工具类: 按次9.9-29.9 CNY
   - 企业级工具: 月度29.9-99.0 CNY
4. 配置skill分类和标签

### Step 20.7: 全量验证报告

**执行**:
1. 生成Round 20全量验证报告:
   - SkillHub上传状态 (org 862的skill总数)
   - clawhub上传状态 (packaged + differentiated)
   - 质量验证状态 (L3+L4+SF通过率)
   - 旧skill撤回状态
   - monetization配置状态
2. 更新项目记忆

### Step 20.8: 生成Round 21提示词

**执行**:
1. 分析Round 20完成情况
2. 生成Round 21提示词文档

## 关键文件索引

### 验证与修复脚本
- `c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\verify_differentiated.py` - 差异化验证脚本(已修复)
- `D:\skills\skill-registry\diff_batch_fix.py` - L3第一轮修复(格式标准化)
- `D:\skills\skill-registry\diff_batch_fix2.py` - L3第二轮修复(关键词对齐)
- `D:\skills\skill-registry\diff_batch_fix3.py` - L3第三轮修复(NON_CAP同步)
- `D:\skills\skill-registry\diff_l4_batch_fix.py` - L4批量修复(5维度)

### 验证结果
- `D:\skills\skill-registry\differentiated_verification_results.json` - 差异化验证结果
- `D:\skills\skill-registry\full_verification_results.json` - Packaged验证结果
- `D:\skills\skill-registry\diff_fix_report.json` - L3修复报告
- `D:\skills\skill-registry\diff_l4_fix_report.json` - L4修复报告

### 上传相关
- `c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\skillhub_upload_server.py` - SkillHub上传辅助服务器
- `c:\Users\thcd\.trae-cn\work\6a5e1d47ef5f370fd441a912\skills_to_upload.json` - 待上传skill数据
- `D:\skills\skill-registry\enterprise_uploader.py` - 企业版上传脚本(需更新认证方式)

### 检查器
- `D:\skills\skill-registry\l3_function_checker.py` - L3检查器(7维度,已更新NON_CAPABILITY_HEADINGS)
- `D:\skills\skill-registry\l4_task_gate.py` - L4检查器(6维度)
- `D:\skills\skill-registry\source_fidelity_checker.py` - SF检查器

## 注意事项

1. **SkillHub API认证**: 必须通过浏览器fetch+credentials:'include',Python requests无法认证
2. **clawhub限流**: 每日最多200个新skill,已上传skill会返回version冲突
3. **slug格式**: 必须匹配 `^[a-z0-9][a-z0-9-]*[a-z0-9]$` (小写字母数字和连字符)
4. **tags/tools格式**: API要求数组,不能是逗号分隔字符串
5. **文件上传**: SkillHub API需要FormData包含payload(JSON)+files(SKILL.md文件)
6. **不要降低标准**: 所有skill必须通过L3+L4+SF验证才能上传
7. **使用git-commit skill**: 每完成一个步骤后提交代码
8. **使用dogfood skill**: 对样本skill进行实际任务测试
9. **使用brainstorming skill**: 在关键决策点确认策略
