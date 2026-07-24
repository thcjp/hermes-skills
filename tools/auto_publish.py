#!/usr/bin/env python3
"""
自动化发布工具 (Auto Publish Tool)
====================================
集成多平台skill发布流程: SkillHub → ClawHub → (Coze评估)

功能:
  1. publish-skillhub <slug>...        — 上传到SkillHub并跟踪状态
  2. publish-clawhub <slug>...         — 上传到ClawHub
  3. publish-all <slug>...             — 按策略上传到所有平台
  4. public-publish <slug>...          — 批量对外发布(已上架→公开)
  5. batch-public-publish              — 批量对外发布所有已上架skill
  6. auto-flow <slug>...               — 完整自动化: 上传→跟踪→对外发布
  7. check-status <slug>...            — 检查skill在所有平台的状态
  8. retry-rejected                    — 重试被拒绝的skill(需先修改内容)
  9. gen-community-publish-js          — 生成浏览器端社区发布JS脚本
 10. retry-cos-failures                — 生成COS失败重试JS脚本
 11. sync-platform-status <results.json> — 根据浏览器返回结果同步数据库
 12. check-visibility                    — 检查所有SkillHub技能可见性状态

重要说明:
  SkillHub Admin API (orgs/862/admin/*) 需要浏览器cookie认证,
  Bearer Token (sk-ent-/skh_) 无法访问admin端点。
  因此社区发布(对外发布)通过生成JS脚本在浏览器控制台执行。

使用方式:
    python auto_publish.py publish-skillhub <slug> [slug...]
    python auto_publish.py batch-public-publish
    python auto_publish.py check-status <slug>
    python auto_publish.py auto-flow <slug> [slug...]
    python auto_publish.py gen-community-publish-js
    python auto_publish.py retry-cos-failures
    python auto_publish.py sync-platform-status <results.json>
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR, DATA_DIR, REGISTRY_DIR, REPORT_DIR, DB_PATH
# === End Phase 1 ===


import json
import subprocess
import time
import sys
import re
import sqlite3
from pathlib import Path
from datetime import datetime

DB_FILE = DATA_DIR / "upload_tracking.json"
PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")
# DIFFERENTIATED_DIR imported from config
COS_FAILURE_FILE = REGISTRY_DIR / "cos_failure_slugs.json"
NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# SkillHub上传限制
MAX_CONTENT_LENGTH = 5800  # WAF限制
RATE_LIMIT_WAIT = 120  # 429限频等待秒数
MAX_RETRIES = 3

# SkillHub Admin API 配置 (需要浏览器cookie认证)
ADMIN_API_HOST = "https://api.skillhub.cn"
ADMIN_ORG_ID = 862
ADMIN_PUBLISHER_ID = 742
ADMIN_SKILLS_LIST = f"/api/v1/orgs/{ADMIN_ORG_ID}/admin/skills"
ADMIN_PUBLISH = f"/api/v1/orgs/{ADMIN_ORG_ID}/admin/skills"
ADMIN_PUBLISHER_PROFILES = f"/api/v1/orgs/{ADMIN_ORG_ID}/admin/publisher-profiles"


def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(db):
    db["metadata"]["last_updated"] = NOW
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)


def find_skill_dir(slug):
    """查找skill的本地目录"""
    # 先查packaged
    p = PACKAGED_DIR / slug
    if p.exists():
        return p
    # 再查differentiated (按类别子目录)
    if DIFFERENTIATED_DIR.exists():
        for cat_dir in DIFFERENTIATED_DIR.iterdir():
            if not cat_dir.is_dir():
                continue
            p = cat_dir / slug
            if p.exists():
                return p
    return None


def publish_to_skillhub(slug, dry_run=False):
    """上传单个skill到SkillHub"""
    skill_dir = find_skill_dir(slug)
    if not skill_dir:
        return {"success": False, "error": f"找不到skill目录: {slug}"}

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {"success": False, "error": f"找不到SKILL.md: {skill_dir}"}

    # 检查内容长度 (WAF限制)
    content = skill_md.read_text(encoding='utf-8', errors='replace')
    if len(content) > MAX_CONTENT_LENGTH:
        return {"success": False, "error": f"内容过长({len(content)}>{MAX_CONTENT_LENGTH}), 需精简"}

    if dry_run:
        return {"success": True, "dry_run": True, "command": f"skillhub publish {skill_dir}"}

    # 执行上传 (使用 npx skillhub 确保 CLI 可用)
    cmd = f'npx skillhub publish "{skill_dir}" --changelog "Automated publish"'
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=120
        )
        output = result.stdout + result.stderr

        # 解析响应
        if result.returncode == 0:
            return {"success": True, "output": output}
        elif "unknown command" in output and "publish" in output:
            return {"success": False, "error": "CLI_NO_PUBLISH", "output": output,
                    "action": "skillhub CLI不支持publish命令,需通过浏览器https://www.skillhub.cn上传"}
        elif "409" in output and "VERSION_EXISTS" in output:
            return {"success": False, "error": "VERSION_EXISTS", "output": output,
                    "action": "需递增版本号"}
        elif "409" in output and ("slug" in output.lower() or "标识符" in output):
            return {"success": False, "error": "SLUG_CONFLICT", "output": output,
                    "action": "需改名为唯一slug"}
        elif "429" in output:
            return {"success": False, "error": "RATE_LIMITED", "output": output,
                    "action": f"等待{RATE_LIMIT_WAIT}秒后重试"}
        elif "566" in output or "WAF" in output.upper():
            return {"success": False, "error": "WAF_BLOCKED", "output": output,
                    "action": "内容触发WAF, 需精简或替换敏感词"}
        elif "401" in output:
            return {"success": False, "error": "AUTH_FAILED", "output": output,
                    "action": "API Key失效, 需重新认证"}
        else:
            return {"success": False, "error": "UNKNOWN", "output": output}
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "TIMEOUT"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def batch_public_publish(dry_run=False):
    """批量对外发布所有已上架skill"""
    db = load_db()
    skills = db["skills"]

    publishable = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        sh = s.get("skillhub", {})
        rs = sh.get("review_status", "")
        # 已上架但未对外发布
        if rs in ("published", "approved") and not sh.get("public_published"):
            publishable.append(slug)

    print(f"可对外发布的skill: {len(publishable)} 个")
    if dry_run:
        for slug in publishable[:20]:
            print(f"  [DRY] {slug}")
        if len(publishable) > 20:
            print(f"  ... 还有 {len(publishable)-20} 个")
        return

    # 批量标记
    success = 0
    failed = 0
    for i, slug in enumerate(publishable):
        # 更新数据库状态
        if slug in skills:
            skills[slug]["skillhub"]["review_status"] = "public_published"
            skills[slug]["skillhub"]["public_published"] = True
            skills[slug]["skillhub"]["public_published_at"] = NOW
            skills[slug]["skillhub"]["last_sync"] = NOW
            skills[slug]["lifecycle"]["stage"] = "public_published"
            skills[slug]["lifecycle"]["last_modified"] = NOW
            success += 1
            if (i + 1) % 100 == 0:
                print(f"  进度: {i+1}/{len(publishable)}")
                save_db(db)  # 每100个保存一次

    save_db(db)
    print(f"\n✅ 已标记 {success} 个skill为对外发布")
    print(f"⚠ 注意: 数据库标记完成, 实际平台发布需运行:")
    print(f"  python auto_publish.py gen-community-publish-js")
    print(f"  然后将生成的JS脚本粘贴到SkillHub管理后台浏览器控制台执行")


def auto_flow(slugs, dry_run=False):
    """完整自动化流程: 上传 → 状态跟踪 → 对外发布"""
    db = load_db()
    results = {"success": [], "failed": [], "pending": [], "already_published": []}

    for slug in slugs:
        s = db["skills"].get(slug)
        if not s:
            results["failed"].append({"slug": slug, "error": "不在数据库中"})
            continue

        if s.get("is_source"):
            results["failed"].append({"slug": slug, "error": "源skill不上传"})
            continue

        sh = s.get("skillhub", {})
        rs = sh.get("review_status", "")

        # 已对外发布
        if rs == "public_published" or sh.get("public_published"):
            results["already_published"].append(slug)
            continue

        # 已上架, 直接对外发布
        if rs in ("published", "approved"):
            if not dry_run:
                sh["review_status"] = "public_published"
                sh["public_published"] = True
                sh["public_published_at"] = NOW
                sh["last_sync"] = NOW
            results["success"].append({"slug": slug, "action": "public_published"})
            continue

        # 需要上传
        if rs in ("not_uploaded", "rejected", "slug_conflict", "deleted", ""):
            result = publish_to_skillhub(slug, dry_run=dry_run)
            if result["success"]:
                if not dry_run:
                    sh["review_status"] = "pending"
                    sh["uploaded"] = True
                    sh["last_sync"] = NOW
                results["pending"].append({"slug": slug, "status": "pending"})
            else:
                results["failed"].append({"slug": slug, "error": result.get("error", "unknown"),
                                         "action": result.get("action", "")})

    if not dry_run:
        save_db(db)

    # 打印结果
    print("="*60)
    print("自动化发布结果")
    print("="*60)
    print(f"  成功对外发布: {len(results['success'])}")
    print(f"  已是公开状态: {len(results['already_published'])}")
    print(f"  上传审核中:   {len(results['pending'])}")
    print(f"  失败:         {len(results['failed'])}")

    if results["failed"]:
        print(f"\n失败详情:")
        for item in results["failed"]:
            print(f"  {item['slug']}: {item['error']}" +
                  (f" → {item['action']}" if item.get("action") else ""))


def check_status(slugs):
    """检查skill在所有平台的状态"""
    db = load_db()
    for slug in slugs:
        s = db["skills"].get(slug)
        if not s:
            print(f"  {slug}: 不在数据库中")
            continue

        sh = s.get("skillhub", {})
        ch = s.get("clawhub", {})
        rs = sh.get("review_status", "not_uploaded")
        ch_st = ch.get("status", "not_uploaded")
        pub = sh.get("public_published", False)

        print(f"  {slug}:")
        print(f"    SkillHub: {rs}" + (" (已对外发布)" if pub else ""))
        print(f"    ClawHub:  {ch_st}")
        print(f"    类型: {'源' if s.get('is_source') else '生产'} | "
              f"{'免费' if s.get('is_free') else '付费'}")


def retry_rejected(dry_run=False):
    """分析并重试被拒绝的skill"""
    db = load_db()
    skills = db["skills"]

    rejected = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        if s.get("skillhub", {}).get("review_status") == "rejected":
            rejected.append(slug)

    print(f"被拒绝的skill: {len(rejected)} 个")
    print()

    # 分析拒绝原因
    categories = {
        "short_name": [],      # 名称太短
        "slug_conflict": [],   # 可能的slug冲突
        "content_issue": [],   # 内容问题
        "unknown": [],         # 未知原因
    }

    for slug in rejected:
        if len(slug) <= 4:
            categories["short_name"].append(slug)
        elif slug in ("copywriting-master", "viral-decoder", "dashboard"):
            categories["slug_conflict"].append(slug)
        else:
            categories["unknown"].append(slug)

    print(f"名称太短 (需改名): {len(categories['short_name'])}")
    for s in categories["short_name"]:
        print(f"  → {s} (建议: {s}-tool 或 {s}-assistant)")

    print(f"\nslug冲突 (需改名): {len(categories['slug_conflict'])}")
    for s in categories["slug_conflict"]:
        print(f"  → {s}")

    print(f"\n其他原因 (需检查内容): {len(categories['unknown'])}")
    for s in categories["unknown"]:
        skill_dir = find_skill_dir(s)
        if skill_dir:
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding='utf-8', errors='replace')
                print(f"  → {s} (内容长度: {len(content)})")
            else:
                print(f"  → {s} (SKILL.md不存在)")
        else:
            print(f"  → {s} (目录不存在)")

    return categories


def generate_community_publish_js():
    """生成浏览器端社区发布JS脚本（增强版 - 含可见性诊断）
    
    SkillHub Admin API需要cookie认证,无法通过Python直接调用。
    此函数生成一个JS脚本,可在SkillHub管理后台(https://skillhub.cn/admin/skills)
    的浏览器控制台中执行,自动完成:
    1. 获取所有skill（含 visibility, download_ready, namespace 信息）
    2. 生成可见性诊断报告（识别不可见原因）
    3. 筛选 org_only + NULL visibility 的skill
    4. 批量调用publish-to-community API
    5. 处理slug冲突(自动追加-sk后缀)
    6. 输出JSON格式结果供数据库同步
    """
    js_code = f"""// SkillHub 批量社区发布脚本 (增强版 - 含可见性诊断)
// 在 https://skillhub.cn/admin/skills 页面控制台执行
(async function() {{
  const API_HOST = "{ADMIN_API_HOST}";
  const ORG_ID = {ADMIN_ORG_ID};
  const PUBLISHER_ID = {ADMIN_PUBLISHER_ID};
  const BATCH_SIZE = 10;  // 每批并发数
  const RESULTS = {{ published: [], failed: [], renamed: [], visibility_report: {{}} }};
  
  console.log("=== SkillHub 批量社区发布 (增强版) ===");
  
  // 1. 获取所有skill
  const allSkills = [];
  let page = 1;
  while (true) {{
    const resp = await fetch(`${{API_HOST}}/api/v1/orgs/${{ORG_ID}}/admin/skills?page=${{page}}&pageSize=100`, {{
      credentials: 'include',
      headers: {{ 'Accept': 'application/json' }}
    }});
    const data = await resp.json();
    if (!data.skills || data.skills.length === 0) break;
    allSkills.push(...data.skills);
    if (allSkills.length >= data.total) break;
    page++;
  }}
  console.log(`总共 ${{allSkills.length}} 个skill`);
  
  // 2. 可见性诊断报告
  const visReport = {{
    total: allSkills.length,
    public: 0,
    org_only: 0,
    null_visibility: 0,
    hidden: 0,
    not_download_ready: 0,
    team_namespace: 0,
    global_namespace: 0,
    invisible_reasons: []
  }};
  
  allSkills.forEach(s => {{
    if (s.visibility === 'public') visReport.public++;
    else if (s.visibility === 'org_only') visReport.org_only++;
    else visReport.null_visibility++;
    
    if (s.hidden === true) {{
      visReport.hidden++;
      visReport.invisible_reasons.push({{ slug: s.slug, reason: 'hidden' }});
    }}
    
    if (s.latestVersion && s.latestVersion.download_ready === false) {{
      visReport.not_download_ready++;
      visReport.invisible_reasons.push({{ slug: s.slug, reason: 'download_not_ready' }});
    }}
    
    if (s.namespace && s.namespace.type === 'TEAM' && s.visibility !== 'public') {{
      visReport.team_namespace++;
      visReport.invisible_reasons.push({{ slug: s.slug, reason: 'team_namespace_not_public' }});
    }} else if (s.namespace && s.namespace.type === 'GLOBAL') {{
      visReport.global_namespace++;
    }}
  }});
  
  console.log("\\n=== 可见性诊断报告 ===");
  console.log(`  public: ${{visReport.public}}`);
  console.log(`  org_only: ${{visReport.org_only}}`);
  console.log(`  null_visibility: ${{visReport.null_visibility}}`);
  console.log(`  hidden: ${{visReport.hidden}}`);
  console.log(`  not_download_ready: ${{visReport.not_download_ready}}`);
  console.log(`  TEAM namespace: ${{visReport.team_namespace}}`);
  console.log(`  GLOBAL namespace: ${{visReport.global_namespace}}`);
  if (visReport.invisible_reasons.length > 0) {{
    console.log(`\\n  不可见原因 (${{visReport.invisible_reasons.length}} 个):`);
    visReport.invisible_reasons.slice(0, 20).forEach(r => 
      console.log(`    ${{r.slug}}: ${{r.reason}}`));
  }}
  RESULTS.visibility_report = visReport;
  
  // 3. 筛选需要发布的skill (org_only + null visibility)
  const toPublish = allSkills.filter(s => 
    s.visibility === 'org_only' || !s.visibility);
  console.log(`\\n需要发布(org_only + null): ${{toPublish.length}} 个`);
  
  if (toPublish.length === 0) {{
    console.log("✅ 所有skill已对外发布!");
    window.__publishResults = RESULTS;
    console.log("结果已保存到 window.__publishResults");
    return;
  }}
  
  // 4. 批量发布
  for (let i = 0; i < toPublish.length; i += BATCH_SIZE) {{
    const batch = toPublish.slice(i, i + BATCH_SIZE);
    console.log(`处理批次 ${{Math.floor(i/BATCH_SIZE)+1}}: ${{i+1}}-${{Math.min(i+BATCH_SIZE, toPublish.length)}}/${{toPublish.length}}`);
    
    const promises = batch.map(async (skill) => {{
      const slug = skill.slug;
      try {{
        // 尝试直接发布
        const resp = await fetch(`${{API_HOST}}/api/v1/orgs/${{ORG_ID}}/admin/skills/${{slug}}/publish-to-community`, {{
          method: 'POST',
          credentials: 'include',
          headers: {{ 'Content-Type': 'application/json', 'Accept': 'application/json' }},
          body: JSON.stringify({{ publisherProfileId: PUBLISHER_ID }})
        }});
        const data = await resp.json().catch(() => ({{}}));
        
        if (resp.status === 200 || resp.status === 201) {{
          RESULTS.published.push(slug);
          return {{ slug, success: true }};
        }} else if (resp.status === 409 && (data.error === 'slug_conflict' || JSON.stringify(data).includes('slug'))) {{
          // slug冲突, 重命名后重试
          const newSlug = slug + '-sk';
          const renameResp = await fetch(`${{API_HOST}}/api/v1/orgs/${{ORG_ID}}/admin/skills/${{slug}}/rename-slug`, {{
            method: 'PUT',
            credentials: 'include',
            headers: {{ 'Content-Type': 'application/json', 'Accept': 'application/json' }},
            body: JSON.stringify({{ newSlug }})
          }});
          
          if (renameResp.ok) {{
            // 用新slug重新发布
            const retryResp = await fetch(`${{API_HOST}}/api/v1/orgs/${{ORG_ID}}/admin/skills/${{newSlug}}/publish-to-community`, {{
              method: 'POST',
              credentials: 'include',
              headers: {{ 'Content-Type': 'application/json', 'Accept': 'application/json' }},
              body: JSON.stringify({{ publisherProfileId: PUBLISHER_ID }})
            }});
            
            if (retryResp.ok) {{
              RESULTS.published.push(newSlug);
              RESULTS.renamed.push({{ original: slug, renamed: newSlug }});
              return {{ slug: newSlug, success: true, renamed_from: slug }};
            }} else {{
              const retryData = await retryResp.json().catch(() => ({{}}));
              RESULTS.failed.push({{ slug, error: retryData.error || `rename_ok_publish_failed_${{retryResp.status}}` }});
              return {{ slug, success: false, error: retryData.error }};
            }}
          }} else {{
            RESULTS.failed.push({{ slug, error: 'rename_failed' }});
            return {{ slug, success: false, error: 'rename_failed' }};
          }}
        }} else {{
          RESULTS.failed.push({{ slug, error: data.error || `HTTP_${{resp.status}}` }});
          return {{ slug, success: false, error: data.error || `HTTP_${{resp.status}}` }};
        }}
      }} catch(e) {{
        RESULTS.failed.push({{ slug, error: e.message }});
        return {{ slug, success: false, error: e.message }};
      }}
    }});
    
    await Promise.all(promises);
    console.log(`  已发布: ${{RESULTS.published.length}}, 失败: ${{RESULTS.failed.length}}`);
    
    // 批次间短暂等待
    if (i + BATCH_SIZE < toPublish.length) {{
      await new Promise(r => setTimeout(r, 500));
    }}
  }}
  
  // 5. 输出结果
  console.log("\\n=== 发布结果 ===");
  console.log(`✅ 成功发布: ${{RESULTS.published.length}}`);
  console.log(`❌ 发布失败: ${{RESULTS.failed.length}}`);
  console.log(`📝 重命名: ${{RESULTS.renamed.length}}`);
  
  if (RESULTS.failed.length > 0) {{
    console.log("\\n失败详情:");
    RESULTS.failed.forEach(f => console.log(`  ${{f.slug}}: ${{f.error}}`));
  }}
  
  // 保存结果到window供复制
  window.__publishResults = RESULTS;
  console.log("\\n结果已保存到 window.__publishResults (含可见性诊断报告)");
  console.log("复制结果: JSON.stringify(window.__publishResults)");
}})();
"""
    
    output_file = REGISTRY_DIR / "community_publish.js"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(js_code)
    
    print(f"✅ 增强版JS脚本已生成: {output_file}")
    print(f"功能: 可见性诊断 + 批量社区发布")
    print(f"使用方法:")
    print(f"  1. 打开 https://skillhub.cn/admin/skills")
    print(f"  2. 按 F12 打开浏览器开发者工具")
    print(f"  3. 切换到 Console 标签")
    print(f"  4. 粘贴 {output_file} 的内容并回车执行")
    print(f"  5. 脚本会先输出可见性诊断报告，然后自动发布不可见技能")
    print(f"  6. 执行完成后, 运行: JSON.stringify(window.__publishResults)")
    print(f"  7. 将结果保存为JSON文件, 然后运行:")
    print(f"     python auto_publish.py sync-platform-status <results.json>")


def retry_cos_failures():
    """生成COS失败重试JS脚本"""
    if not COS_FAILURE_FILE.exists():
        print(f"❌ COS失败列表不存在: {COS_FAILURE_FILE}")
        return
    
    with open(COS_FAILURE_FILE, "r", encoding="utf-8") as f:
        cos_slugs = json.load(f)
    
    js_code = f"""// SkillHub COS失败重试脚本 (自动生成)
// 在 https://skillhub.cn/admin/skills 页面控制台执行
(async function() {{
  const API_HOST = "{ADMIN_API_HOST}";
  const ORG_ID = {ADMIN_ORG_ID};
  const PUBLISHER_ID = {ADMIN_PUBLISHER_ID};
  const COS_FAILURE_SLUGS = {json.dumps(cos_slugs)};
  const RESULTS = {{ published: [], failed: [] }};
  
  console.log(`=== COS失败重试: ${{COS_FAILURE_SLUGS.length}} 个skill ===`);
  
  for (let i = 0; i < COS_FAILURE_SLUGS.length; i++) {{
    const slug = COS_FAILURE_SLUGS[i];
    console.log(`[${{i+1}}/${{COS_FAILURE_SLUGS.length}}] 重试: ${{slug}}`);
    
    try {{
      const resp = await fetch(`${{API_HOST}}/api/v1/orgs/${{ORG_ID}}/admin/skills/${{slug}}/publish-to-community`, {{
        method: 'POST',
        credentials: 'include',
        headers: {{ 'Content-Type': 'application/json', 'Accept': 'application/json' }},
        body: JSON.stringify({{ publisherProfileId: PUBLISHER_ID }})
      }});
      const data = await resp.json().catch(() => ({{}}));
      
      if (resp.ok) {{
        RESULTS.published.push(slug);
        console.log(`  ✅ 成功`);
      }} else {{
        RESULTS.failed.push({{ slug, error: data.error || `HTTP_${{resp.status}}` }});
        console.log(`  ❌ 失败: ${{data.error || resp.status}}`);
      }}
    }} catch(e) {{
      RESULTS.failed.push({{ slug, error: e.message }});
      console.log(`  ❌ 异常: ${{e.message}}`);
    }}
    
    // 请求间隔
    if (i + 1 < COS_FAILURE_SLUGS.length) {{
      await new Promise(r => setTimeout(r, 300));
    }}
  }}
  
  console.log("\\n=== 重试结果 ===");
  console.log(`✅ 成功: ${{RESULTS.published.length}}`);
  console.log(`❌ 失败: ${{RESULTS.failed.length}}`);
  
  if (RESULTS.failed.length > 0) {{
    console.log("\\n仍失败的skill:");
    RESULTS.failed.forEach(f => console.log(`  ${{f.slug}}: ${{f.error}}`));
  }}
  
  window.__cosRetryResults = RESULTS;
  console.log("\\n结果已保存到 window.__cosRetryResults");
}})();
"""
    
    output_file = REGISTRY_DIR / "retry_cos_failures.js"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(js_code)
    
    print(f"✅ COS重试JS脚本已生成: {output_file}")
    print(f"COS失败skill数量: {len(cos_slugs)}")
    print(f"使用方法: 在 https://skillhub.cn/admin/skills 控制台粘贴执行")


def sync_platform_status(results_file):
    """根据浏览器返回的发布结果同步数据库
    
    Args:
        results_file: 浏览器端JS脚本执行后保存的JSON结果文件
    """
    results_path = Path(results_file)
    if not results_path.exists():
        print(f"❌ 结果文件不存在: {results_file}")
        return
    
    with open(results_path, "r", encoding="utf-8") as f:
        results = json.load(f)
    
    published = results.get("published", [])
    failed = results.get("failed", [])
    renamed = results.get("renamed", [])
    
    print(f"发布结果: 成功={len(published)}, 失败={len(failed)}, 重命名={len(renamed)}")
    
    db = load_db()
    skills = db.get("skills", {})
    
    # 处理重命名映射
    rename_map = {r["original"]: r["renamed"] for r in renamed}
    
    # 更新已发布的skill
    success_count = 0
    for slug in published:
        # 检查是否是重命名后的slug
        original_slug = None
        for orig, renamed_slug in rename_map.items():
            if renamed_slug == slug:
                original_slug = orig
                break
        
        # 在数据库中查找 (可能是原始slug或重命名后的slug)
        db_slug = original_slug if original_slug else slug
        if db_slug in skills:
            sh = skills[db_slug].get("skillhub", {})
            sh["public_published"] = True
            sh["public_published_at"] = NOW
            sh["community_published"] = True
            sh["community_slug"] = slug  # 实际在平台上的slug
            sh["last_sync"] = NOW
            if "community_publish_failed" in sh:
                del sh["community_publish_failed"]
            if "community_publish_error" in sh:
                del sh["community_publish_error"]
            
            lifecycle = skills[db_slug].get("lifecycle", {})
            lifecycle["stage"] = "community_published"
            lifecycle["last_modified"] = NOW
            skills[db_slug]["lifecycle"] = lifecycle
            success_count += 1
    
    # 更新失败的skill
    fail_count = 0
    for item in failed:
        slug = item.get("slug", "")
        if slug in skills:
            sh = skills[slug].get("skillhub", {})
            sh["public_published"] = False
            sh["community_publish_failed"] = True
            sh["community_publish_error"] = item.get("error", "unknown")
            sh["community_publish_retry_count"] = sh.get("community_publish_retry_count", 0) + 1
            sh["last_sync"] = NOW
            
            lifecycle = skills[slug].get("lifecycle", {})
            lifecycle["stage"] = "community_publish_failed"
            lifecycle["last_modified"] = NOW
            skills[slug]["lifecycle"] = lifecycle
            fail_count += 1
    
    # 更新统计
    stats = db.get("stats", {})
    stats["community_published"] = success_count
    stats["community_publish_failed"] = fail_count
    db["stats"] = stats
    
    db["metadata"]["last_updated"] = NOW
    db["metadata"]["platform_sync"] = {
        "synced_at": NOW,
        "published_count": len(published),
        "failed_count": len(failed),
        "renamed_count": len(renamed),
        "db_updated_success": success_count,
        "db_updated_failed": fail_count
    }
    
    save_db(db)
    
    print(f"\n=== 数据库同步完成 ===")
    print(f"  已发布(数据库更新): {success_count}")
    print(f"  仍失败(数据库更新): {fail_count}")
    print(f"  重命名: {len(renamed)}")
    if renamed:
        print(f"  重命名详情:")
        for r in renamed:
            print(f"    {r['original']} → {r['renamed']}")


def check_visibility():
    """检查所有SkillHub技能的可见性状态
    
    查询SQLite数据库中platform_uploads表，
    识别不可见技能(org_only/NULL visibility)并生成诊断报告。
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 1. 总体统计
    c.execute("""SELECT upload_status, visibility, COUNT(*) 
                 FROM platform_uploads WHERE platform='skillhub' 
                 GROUP BY upload_status, visibility ORDER BY upload_status""")
    print("=== SkillHub 可见性总体统计 ===")
    stats = []
    for row in c.fetchall():
        vis = row[1] if row[1] else "NULL"
        print(f"  status={row[0]:20s} | visibility={vis:15s} | count={row[2]}")
        stats.append({"status": row[0], "visibility": vis, "count": row[2]})

    # 2. org_only 技能（不可见）
    c.execute("""SELECT s.slug, s.category, pu.upload_status, pu.error_message
                 FROM platform_uploads pu 
                 JOIN skills s ON pu.skill_id = s.id
                 WHERE pu.platform='skillhub' AND pu.visibility='org_only'""")
    org_only_skills = []
    print(f"\n=== org_only 可见性技能 (前台不可见) ===")
    for row in c.fetchall():
        err = str(row[3])[:60] if row[3] else "None"
        print(f"  {row[0]:40s} | cat={str(row[1]):15s} | status={row[2]} | err={err}")
        org_only_skills.append({"slug": row[0], "category": row[1], "status": row[2], "error": row[3]})

    # 3. NULL 可见性技能（状态未知）
    c.execute("""SELECT s.slug, s.category, pu.upload_status
                 FROM platform_uploads pu 
                 JOIN skills s ON pu.skill_id = s.id
                 WHERE pu.platform='skillhub' AND pu.visibility IS NULL""")
    null_vis_skills = []
    print(f"\n=== NULL 可见性技能 (状态未知，可能不可见) ===")
    for row in c.fetchall():
        print(f"  {row[0]:40s} | cat={str(row[1]):15s} | status={row[2]}")
        null_vis_skills.append({"slug": row[0], "category": row[1], "status": row[2]})

    # 4. retry_pending 技能
    c.execute("""SELECT s.slug, s.category, pu.error_message
                 FROM platform_uploads pu 
                 JOIN skills s ON pu.skill_id = s.id
                 WHERE pu.platform='skillhub' AND pu.upload_status='retry_pending'""")
    retry_skills = []
    print(f"\n=== retry_pending 技能 (需重新上传) ===")
    for row in c.fetchall():
        err = str(row[2])[:80] if row[2] else "None"
        print(f"  {row[0]:40s} | cat={str(row[1]):15s} | error={err}")
        retry_skills.append({"slug": row[0], "category": row[1], "error": row[2]})

    # 5. NULL/无效 category 统计
    c.execute("""SELECT COUNT(*) FROM skills WHERE category IS NULL OR category = '' OR category = 'packaged'""")
    null_cat_count = c.fetchone()[0]
    c.execute("""SELECT COUNT(*) FROM skills WHERE category IS NOT NULL AND category != '' AND category != 'packaged'""")
    valid_cat_count = c.fetchone()[0]
    print(f"\n=== Category 统计 ===")
    print(f"  有效 category: {valid_cat_count}")
    print(f"  NULL/无效 category: {null_cat_count}")

    # 6. public + success 技能数量（理论可见）
    c.execute("""SELECT COUNT(*) FROM platform_uploads 
                 WHERE platform='skillhub' AND visibility='public' AND upload_status='success'""")
    public_success = c.fetchone()[0]
    print(f"\n=== 理论可见技能 (public+success): {public_success} ===")
    print(f"  注意: 实际可见性还需验证平台侧 download_ready, namespace.type, hidden 状态")

    conn.close()

    # 7. 生成诊断报告
    report = {
        "generated_at": NOW,
        "summary": {
            "total_skillhub_uploads": sum(s["count"] for s in stats),
            "public_success": public_success,
            "org_only": len(org_only_skills),
            "null_visibility": len(null_vis_skills),
            "retry_pending": len(retry_skills),
            "null_invalid_category": null_cat_count,
        },
        "org_only_skills": org_only_skills,
        "null_visibility_skills": null_vis_skills,
        "retry_pending_skills": retry_skills,
        "stats_breakdown": stats,
        "recommendations": [
            "对 org_only 技能执行 gen-community-publish-js 生成发布脚本",
            "对 NULL visibility 技能执行 gen-community-publish-js (含诊断模式)",
            "对 retry_pending 技能执行 publish-skillhub 重新上传",
            "对 NULL/无效 category 技能执行 fix_missing_fields.py 推断category",
            "在浏览器执行生成的JS脚本后执行 sync-platform-status 同步结果",
        ],
    }

    report_file = REPORT_DIR / "visibility_report.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"\n=== 诊断报告已生成: {report_file} ===")

    # 8. 输出行动建议
    print(f"\n=== 行动建议 ===")
    if org_only_skills:
        print(f"  1. 执行: python tools/auto_publish.py gen-community-publish-js")
        print(f"     → 生成浏览器JS脚本，发布 {len(org_only_skills)} 个 org_only 技能到社区")
    if null_vis_skills:
        print(f"  2. 检查 {len(null_vis_skills)} 个 NULL visibility 技能的平台侧状态")
    if retry_skills:
        print(f"  3. 执行: python tools/auto_publish.py publish-skillhub <slug>")
        print(f"     → 重新上传 {len(retry_skills)} 个 retry_pending 技能")
    if null_cat_count > 0:
        print(f"  4. 执行: python tools/fix_missing_fields.py")
        print(f"     → 修复 {null_cat_count} 个 NULL/无效 category")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]
    dry_run = "--dry-run" in sys.argv

    if cmd == "publish-skillhub":
        slugs = [s for s in sys.argv[2:] if not s.startswith("--")]
        for slug in slugs:
            result = publish_to_skillhub(slug, dry_run=dry_run)
            status = "✅" if result["success"] else "❌"
            print(f"  {status} {slug}: {result.get('error', 'success')}")
            if not result["success"] and result.get("action"):
                print(f"     → {result['action']}")
            time.sleep(2)  # 限频保护

    elif cmd == "batch-public-publish":
        batch_public_publish(dry_run=dry_run)

    elif cmd == "auto-flow":
        slugs = [s for s in sys.argv[2:] if not s.startswith("--")]
        auto_flow(slugs, dry_run=dry_run)

    elif cmd == "check-status":
        slugs = sys.argv[2:]
        check_status(slugs)

    elif cmd == "retry-rejected":
        retry_rejected(dry_run=dry_run)

    elif cmd == "gen-community-publish-js":
        generate_community_publish_js()

    elif cmd == "retry-cos-failures":
        retry_cos_failures()

    elif cmd == "sync-platform-status":
        if len(sys.argv) < 3:
            print("用法: python auto_publish.py sync-platform-status <results.json>")
            return
        sync_platform_status(sys.argv[2])

    elif cmd == "check-visibility":
        check_visibility()

    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
