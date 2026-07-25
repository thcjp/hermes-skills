# 第7轮提示词：数据库裸SQL收口 + E2E遗留问题修复 + 批量处理验证

> 基于skill-automation-comprehensive-fix-plan-v4.md中的剩余待优化项
> 前序：第1-6轮修复已完成，E2E全流程测试已通过（3个skill，6次上传，TRACE评分均≥4.5）

---

## 本轮目标

修复v4计划中标记的4个剩余优化项，并启动60个skill的批量处理验证流程。

---

## 任务清单

### R7-1: 数据库裸SQL收口（D4延续，第1批5个文件）

**背景**: v3第4轮修复了3个文件的裸SQL，剩余15个文件中约40处裸INSERT/UPDATE需要收口为db.py业务函数调用。

**执行步骤**:

1. 使用以下命令定位剩余的裸SQL文件：
```
cd d:\skills\tools
grep -rn "INSERT INTO\|UPDATE.*SET\|DELETE FROM" *.py --include="*.py" | grep -v "db.py" | grep -v "__pycache__" | grep -v "test_"
```

2. 取前5个文件（按裸SQL数量降序排列），逐个修改：
   - 将裸`INSERT INTO skills`替换为`db.register_skill()`
   - 将裸`UPDATE skills SET`替换为`db.update_skill()`
   - 将裸`INSERT INTO scores`替换为`db.save_score()`
   - 将裸`DELETE FROM`替换为`UPDATE ... SET is_current=0`（如适用）

3. 每个文件修改后立即验证：
```
python -c "import py_compile; py_compile.compile(r'<文件路径>', doraise=True); print('OK')"
```

4. 全部修改后运行回归测试：
```
cd d:\skills\tools
python quality_gate.py "D:\skills\packaged-skills\skillhub\cron-precision-scheduler" --json
python quality_gate.py "D:\skills\packaged-skills\skillhub\logo-design-guide" --json
python quality_gate.py "D:\skills\packaged-skills\skillhub\git-essentials" --json
```

**约束**:
- 禁止mock/TODO/pass/fallback
- 保持db.py业务函数的参数签名不变
- 如遇db.py缺少对应业务函数，先在db.py中添加再调用
- 每个文件修改后立即py_compile验证

---

### R7-2: ClawHub搜索DNS问题修复

**背景**: E2E步骤7中`registry.clawhub.io`DNS解析失败，导致ClawHub源搜索不可用。

**执行步骤**:

1. 检查ClawHub注册表地址：
```
cd d:\skills
grep -r "registry.clawhub" tools/ config/ --include="*.py"
```

2. 测试DNS解析：
```
nslookup registry.clawhub.io
nslookup clawhub.io
```

3. 如果DNS解析失败：
   - 检查`d:\skills\config\platform_config.py`中的REGISTRY配置
   - 尝试使用替代域名（如`registry.npmmirror.com`或直接IP）
   - 如果是临时DNS问题，在`platform_config.py`中添加DNS缓存和重试机制

4. 验证修复：
```
python -c "
from urllib.request import urlopen, Request
import json
url = 'https://<修复后的REGISTRY>/api/v1/skills?search=cron&limit=3'
req = Request(url, headers={'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'})
with urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read())
    print(f'成功: 找到 {len(data) if isinstance(data, list) else len(data.get(\"skills\", data.get(\"items\", [])))} 个结果')
"
```

**约束**:
- 不修改ClawHub CLI本身（`npx clawhub`）
- 只修改项目配置中的REGISTRY地址
- 如果是网络环境问题（如防火墙），记录问题并跳过

---

### R7-3: SkillHub审核状态和AI评分验证

**背景**: 3个E2E技能上传后reviewStatus为pending，需验证审核是否通过及AI评分。

**执行步骤**:

1. 查询审核状态：
```python
# 使用cookie认证查询
import json, os
from pathlib import Path
from urllib.request import urlopen, Request

HOST = "https://api.skillhub.cn"
ORG_ID = 862
COOKIES = Path(os.path.expanduser("~")).joinpath(".skillhub_cookies.txt").read_text(encoding='utf-8').strip()

for slug in ["cron-precision-scheduler", "logo-design-guide", "git-essentials"]:
    url = f"{HOST}/api/v1/orgs/{ORG_ID}/skills/{slug}"
    req = Request(url, headers={"Cookie": COOKIES, "Accept": "application/json"})
    with urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
        lv = data.get('latestVersion', {})
        print(f"{slug}: v{lv.get('version','?')}, review={lv.get('reviewStatus','?')}")
```

2. 如果审核通过，查找AI评分字段：
   - 检查`latestVersion`中的所有字段
   - 检查全局`/api/v1/skills/{slug}`端点
   - 如果API未暴露评分，尝试通过Web界面查看

3. 如果审核未通过：
   - 查看拒绝原因
   - 根据原因修复skill内容
   - 重新上传新版本

4. 如果AI评分 < 4.5：
   - 分析低分维度
   - 针对性优化skill内容（补充FAQ、错误码、能力边界等）
   - 重新上传并再次验证

**约束**:
- 等待审核期间不阻塞其他任务
- 如审核被拒，必须修复后重新上传，不能跳过

---

### R7-4: 启动60个skill批量处理验证

**背景**: E2E测试已验证流程可用，现在需要对P0-P5优先级的60个skill进行批量处理。

**执行步骤**:

1. 获取待处理skill列表：
```
cd d:\skills\tools
python -c "
import sqlite3
conn = sqlite3.connect(r'D:\skills\skill-registry.db')
c = conn.cursor()
# 按edition和workflow_state筛选待处理skill
c.execute('''
    SELECT slug, edition, workflow_state, current_score 
    FROM skills 
    WHERE workflow_state IS NULL OR workflow_state NOT LIKE '%uploaded%'
    ORDER BY 
        CASE edition WHEN 'free' THEN 0 WHEN 'paid' THEN 1 ELSE 2 END,
        slug
    LIMIT 60
''')
for row in c.fetchall():
    print(f'{row[0]} | edition={row[1]} | state={row[2]} | score={row[3]}')
conn.close()
"
```

2. 对前3个skill执行完整E2E流程（小规模验证）：
   - 使用`generate_skill.py --direct`生成/增强
   - 运行`quality_gate.py`验证
   - 运行`skill_batch_upgrader_v3.py`合规检查
   - 上传到ClawHub和SkillHub

3. 如果前3个全部成功，批量处理剩余57个：
   - 使用`clawhub_batch_uploader.py`批量上传ClawHub
   - 使用`upload_to_skillhub_v2.py`批量上传SkillHub
   - 记录每个skill的上传结果

4. 生成批量处理报告：
```
cd d:\skills\tools
python -c "
import sqlite3, json
from datetime import datetime
conn = sqlite3.connect(r'D:\skills\skill-registry.db')
c = conn.cursor()
c.execute('''
    SELECT slug, edition, workflow_state, current_score,
           CASE WHEN workflow_state LIKE '%uploaded%' THEN 1 ELSE 0 END as uploaded
    FROM skills 
    WHERE slug IN (-- 60个skill的slug列表)
    ORDER BY uploaded DESC, slug
''')
results = []
for row in c.fetchall():
    results.append({
        'slug': row[0], 'edition': row[1], 'state': row[2],
        'score': row[3], 'uploaded': bool(row[4])
    })
print(json.dumps({'timestamp': datetime.now().isoformat(), 'total': len(results),
                  'uploaded': sum(1 for r in results if r['uploaded']),
                  'pending': sum(1 for r in results if not r['uploaded'])},
                 ensure_ascii=False, indent=2))
conn.close()
"
```

**约束**:
- 批量处理前必须先通过3个skill的小规模验证
- 上传失败的skill需要记录原因并单独重试
- 每个skill的TRACE评分必须≥4.5才能上传
- 禁止跳过质量门或合规检查

---

### R7-5: 生成第8轮提示词

完成R7-1到R7-4后：
1. 汇总本轮所有修改和验证结果
2. 识别新发现的问题
3. 生成第8轮提示词，保存到`d:\skills\.trae\documents\round8-prompt.md`

---

## 验证标准

| 检查项 | 标准 | 验证方法 |
|--------|------|---------|
| 裸SQL收口 | 5个文件改为db.py业务函数 | py_compile + grep验证 |
| ClawHub搜索 | DNS解析成功，搜索返回结果 | urllib请求测试 |
| SkillHub审核 | reviewStatus=approved或记录拒绝原因 | API查询 |
| AI评分 | ≥4.5/5.0 或记录低分原因 | API查询或Web界面 |
| 批量处理 | 前3个skill完整E2E通过 | 质量门+合规+上传验证 |
| 回归测试 | 3个E2E测试skill无回归 | quality_gate.py验证 |

---

## 文件清单

### 预期修改的文件

| 文件 | 任务 | 变更类型 |
|------|------|---------|
| 5个含裸SQL的文件 | R7-1 | INSERT/UPDATE → db.py函数调用 |
| `config/platform_config.py` | R7-2 | REGISTRY地址修复 |
| `tools/clawhub_batch_uploader.py` | R7-4 | 批量上传参数优化 |
| `tools/upload_to_skillhub_v2.py` | R7-4 | 批量上传支持 |

### 预期新建的文件

| 文件 | 任务 | 说明 |
|------|------|------|
| `d:\skills\.trae\documents\round8-prompt.md` | R7-5 | 第8轮提示词 |

---

## 注意事项

1. **小规模验证优先**: 每个任务都先用3个skill验证，通过后再扩大范围
2. **禁止mock/TODO/pass/fallback**: 所有修复必须是真实实现
3. **保持已有修复**: 不得回退前6轮的任何修复
4. **记录所有变更**: 每个文件的修改都要记录在v4计划的文件变更记录中
5. **版本号管理**: 上传新版本时版本号必须高于当前最新版本
6. **slug冲突处理**: 如遇slug被占用，使用`-pro`后缀重命名
7. **认证管理**: SkillHub使用cookie认证（含skh_ent_token），ClawHub使用CLI认证
8. **错误处理**: 上传失败时记录错误原因，不阻塞后续skill的上传
