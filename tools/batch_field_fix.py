#!/usr/bin/env python3
"""
SkillHub批量字段修复脚本
========================
因PUT API不可用，需要DELETE+重新上传来更新tags/summary_zh/categoryIds等字段。
本脚本支持：
1. 批量审核通过待审版本（通过浏览器JS）
2. 批量删除+重新上传skill（补全categoryIds/tags/summary_zh/iconUrl等字段）
3. 重新上传被删除的skill
4. 全量DELETE+重传所有skill（带断点续传）
5. org_only skill对外发布
6. 企业认证状态检查

使用方式:
    python batch_field_fix.py check              # 检查哪些skill需要修复
    python batch_field_fix.py check-auth         # 检查企业认证状态
    python batch_field_fix.py reupload <slug>    # 重新上传单个skill
    python batch_field_fix.py batch <n>          # 批量修复前n个skill
    python batch_field_fix.py reupload-all-batch # 全量DELETE+重传所有skill
    python batch_field_fix.py reupload-deleted   # 重新上传被删除的skill
    python batch_field_fix.py reupload-rejected  # 重新上传38个被拒绝的skill
    python batch_field_fix.py publish-org-only   # 4个org_only skill对外发布
    python batch_field_fix.py gen-approve-js     # 生成批量审核通过JS脚本
"""

import json
import os
import re
import sys
import time
import sqlite3
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR
)
from skill_core.parser import parse_frontmatter as _parse_fm
from enterprise_uploader import (
    upload_skill, find_skill_md, parse_frontmatter,
    get_platform_category, get_team_category_id, get_subcategories,
    parse_tags, generate_summary_zh,
    load_cookies, ORG_ID, API_BASE, ORG_SKILLS_API,
    CATEGORY_ICONS, DEFAULT_ICON
)

# 被拒绝的skill slug列表（38个，从通知中提取）
REJECTED_SLUGS = [
    'ai-writing-style-cloner', 'api-design-architect', 'auth-security-architect',
    'azure-cloud-automator', 'brand-identity-creator', 'c-suite-advisor',
    'canvas-art-designer', 'clickhouse-olap-expert', 'cloudflare-edge-developer',
    'code-review-sentinel', 'competitive-ad-spy', 'compliance-manager',
    'content-cms-architect', 'content-refiner', 'copywriting-master',
    'csv-insight-miner', 'drama-hit-producer', 'ebook-factory',
    'ecommerce-pricing-strategist', 'geo-rank-architect', 'hook-retention-master',
    'intel-sentinel', 'novel-autopilot', 'poetry-craftsman', 'requirement-explorer-pro',
    'sales-copy-writer', 'seo-doctor', 'seo-rank-monopolizer', 'stealth-browser-assistant',
    'title-hook-factory', 'topic-hunter', 'viral-decoder', 'viral-prophet',
    'ai-artist-workstation-pro', 'lead-research-hunter', 'duckdb-analytics-engine',
    'docx-document-master', 'debug-doctor'
]

# 被删除需要重新上传的skill
DELETED_SLUGS = ['memory-orchestrator-sk']

# org_only需要对外发布的skill
ORG_ONLY_SLUGS = [
    'ai-artist-workstation-pro', 'clickhouse-olap-expert',
    'requirement-explorer-pro', 'lead-research-hunter'
]


def check_skills_needing_fix():
    """检查哪些skill需要修复tags/summary_zh"""
    cookies = load_cookies()
    if not cookies:
        print("错误：无认证cookie，请先设置SKILLHUB_SESSION_COOKIE")
        return
    
    # 获取所有skill
    all_skills = []
    page = 1
    while True:
        url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills?page={page}&pageSize=100"
        req = Request(url, headers={
            'Cookie': cookies,
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        try:
            with urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if not data.get('skills'):
                    break
                all_skills.extend(data['skills'])
                if len(all_skills) >= data.get('total', 0):
                    break
                page += 1
        except Exception as e:
            print(f"获取skill列表失败: {e}")
            break
    
    print(f"总共 {len(all_skills)} 个skill")
    
    # 检查每个skill的详情
    needs_fix = []
    has_tags = 0
    has_summary_zh = 0
    has_icon = 0
    
    for i, skill in enumerate(all_skills):
        slug = skill['slug']
        try:
            detail_url = f"{API_BASE}/skills/{slug}"
            req = Request(detail_url, headers={
                'Cookie': cookies,
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0'
            })
            with urlopen(req, timeout=15) as resp:
                detail = json.loads(resp.read().decode('utf-8'))
            
            skill_data = detail.get('skill', {})
            tags = skill_data.get('tags', {})
            summary_zh = skill_data.get('summary_zh', '')
            icon_url = skill_data.get('iconUrl', None)
            category = skill_data.get('category', '')
            
            needs_tags = not tags or (isinstance(tags, dict) and len(tags) == 0)
            needs_summary_zh = not summary_zh or not summary_zh.strip()
            needs_icon = not icon_url
            
            if needs_tags or needs_summary_zh:
                needs_fix.append({
                    'slug': slug,
                    'name': skill.get('displayName', slug),
                    'needs_tags': needs_tags,
                    'needs_summary_zh': needs_summary_zh,
                    'needs_icon': needs_icon,
                    'category': category,
                    'stars': skill.get('stars', 0),
                    'downloads': skill.get('downloads', 0),
                })
            
            if not needs_tags:
                has_tags += 1
            if not needs_summary_zh:
                has_summary_zh += 1
            if not needs_icon:
                has_icon += 1
            
            if (i + 1) % 50 == 0:
                print(f"  已检查 {i+1}/{len(all_skills)}...")
                time.sleep(0.5)
                
        except Exception as e:
            print(f"  获取 {slug} 详情失败: {e}")
    
    print(f"\n=== 检查结果 ===")
    print(f"总skill数: {len(all_skills)}")
    print(f"已有tags: {has_tags}")
    print(f"已有summary_zh: {has_summary_zh}")
    print(f"已有icon: {has_icon}")
    print(f"需要修复: {len(needs_fix)}")
    
    # 保存需要修复的列表
    fix_file = REPORT_DIR / "skills_needing_fix.json"
    with open(fix_file, 'w', encoding='utf-8') as f:
        json.dump(needs_fix, f, ensure_ascii=False, indent=2)
    print(f"\n需要修复的skill列表已保存到: {fix_file}")
    
    return needs_fix


def delete_skill(slug: str) -> bool:
    """删除skill — 尝试多个端点（admin/skills和skills）"""
    cookies = load_cookies()
    if not cookies:
        print("错误：无认证cookie")
        return False
    
    # 尝试多个DELETE端点（不同API版本可能路径不同）
    delete_urls = [
        f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}",
        f"{API_BASE}/orgs/{ORG_ID}/skills/{slug}",
    ]
    
    for url in delete_urls:
        req = Request(url, method='DELETE', headers={
            'Cookie': cookies,
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        try:
            with urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                return data.get('deleted', False) or data.get('ok', False)
        except HTTPError as e:
            if e.code == 404:
                continue  # 尝试下一个端点
            # 其他错误也继续尝试
            continue
        except Exception:
            continue
    
    # DELETE失败不阻塞重传 — POST端点支持upsert（同名slug自动创建新版本）
    return False


def reupload_skill(slug: str, skip_gate: bool = True) -> dict:
    """删除并重新上传skill（带完整字段）
    
    Args:
        slug: skill slug
        skip_gate: 跳过门控检查（默认True，用于已发布skill的元数据修复重传）
    """
    print(f"\n处理 {slug}...")
    
    # 1. 先尝试删除（如果已存在）
    print(f"  1. 尝试删除已有版本...")
    delete_skill(slug)
    time.sleep(0.5)
    
    # 2. 使用增强后的upload_skill重新上传
    print(f"  2. 重新上传（含tags/summary_zh/category/categoryIds/iconUrl等完整字段）...")
    result = upload_skill(slug, dry_run=False, skip_gate=skip_gate)
    
    if result['success']:
        print(f"  ✅ {slug} 重新上传成功")
    else:
        print(f"  ❌ {slug} 重新上传失败: {result['message']}")
    
    return result


def batch_reupload(slugs: list, delay: float = 1.5):
    """批量删除+重新上传（统一进度文件，支持断点续传）"""
    results = {'success': [], 'failed': []}
    progress_file = REPORT_DIR / "batch_reupload_progress.json"
    
    # 加载已有进度（断点续传）
    if progress_file.exists():
        try:
            old = json.loads(progress_file.read_text(encoding='utf-8'))
            results['success'] = old.get('success', [])
            results['failed'] = old.get('failed', [])
            print(f"断点续传: 已有成功 {len(results['success'])} 个，失败 {len(results['failed'])} 个")
        except Exception:
            pass
    
    for i, slug in enumerate(slugs):
        # 跳过已完成的
        if slug in results['success']:
            continue
            
        print(f"\n[{i+1}/{len(slugs)}] {slug}")
        result = reupload_skill(slug)
        
        if result['success']:
            results['success'].append(slug)
        else:
            # 替换已有的失败记录
            results['failed'] = [f for f in results['failed'] if f.get('slug') != slug]
            results['failed'].append({'slug': slug, 'error': result['message']})
        
        # 每5个保存一次进度
        if (i + 1) % 5 == 0:
            with open(progress_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"  [进度已保存: 成功{len(results['success'])}, 失败{len(results['failed'])}]")
        
        if i + 1 < len(slugs):
            time.sleep(delay)
    
    # 最终保存
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 批量重新上传结果 ===")
    print(f"✅ 成功: {len(results['success'])}")
    print(f"❌ 失败: {len(results['failed'])}")
    
    if results['failed']:
        print("\n失败详情:")
        for f in results['failed'][:20]:
            print(f"  {f['slug']}: {f['error']}")
    
    print(f"\n进度文件: {progress_file}")
    
    return results


def generate_approval_js():
    """[已废弃] 生成批量审核通过的浏览器JS脚本

    请使用: python platform_ops.py batch-approve
    统一入口直接通过API调用完成审核, 无需浏览器JS中转
    """
    print("⚠ 已废弃: 此命令已被 platform_ops.py batch-approve 替代")
    print("  请使用: python platform_ops.py batch-approve")
    print("  直接通过API调用完成审核, 无需浏览器JS中转\n")
    js_code = """// SkillHub 批量审核通过脚本 v2
// 在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  const BATCH_SIZE = 5;
  let approved = 0;
  let failed = 0;
  let totalProcessed = 0;

  // localStorage进度持久化
  const STORAGE_KEY = 'skillhub_approve_progress';
  let progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  let startPage = progress.lastPage || 1;

  console.log("=== SkillHub 批量审核通过 v2 ===");
  console.log(`从第 ${startPage} 页开始（已处理 ${progress.totalProcessed || 0} 个）`);

  function saveProgress(page, processed) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      lastPage: page,
      totalProcessed: processed
    }));
  }

  const allButtons = document.querySelectorAll('button');
  const approveButtons = Array.from(allButtons).filter(b => b.textContent.trim() === '审核通过');
  const totalPages = document.querySelectorAll('[class*="page"], [class*="Page"]');

  console.log(`当前页面有 ${approveButtons.length} 个审核按钮`);

  for (let i = 0; i < approveButtons.length; i++) {
    try {
      approveButtons[i].click();
      approved++;
      totalProcessed++;
      console.log(`  [${totalProcessed}] 审核通过已点击`);

      await new Promise(r => setTimeout(r, 500));

      const newButtons = document.querySelectorAll('button');
      const newApproveButtons = Array.from(newButtons).filter(b => b.textContent.trim() === '审核通过');
      if (newApproveButtons.length > 0 && i < approveButtons.length - 1) {
        approveButtons.length = 0;
        approveButtons.push(...newApproveButtons);
        i = -1;
      }
    } catch(e) {
      failed++;
      console.error(`  审核失败: ${e.message}`);
    }

    if (totalProcessed % BATCH_SIZE === 0) {
      console.log(`已处理 ${totalProcessed} 个, 成功 ${approved}, 失败 ${failed}`);
      saveProgress(startPage, totalProcessed);
      await new Promise(r => setTimeout(r, 1000));
    }
  }

  saveProgress(startPage + 1, totalProcessed);
  console.log(`\\n=== 完成 ===`);
  console.log(`总计处理: ${totalProcessed}`);
  console.log(`成功: ${approved}`);
  console.log(`失败: ${failed}`);
  console.log(`\\n请刷新页面继续处理下一页`);
})();
"""

    js_file = REPORT_DIR / "batch_approve_reviews_v2.js"
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"批量审核JS脚本已生成: {js_file}")
    print("请在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行")


def check_auth():
    """检查企业认证状态"""
    cookies = load_cookies()
    if not cookies:
        print("错误：无认证cookie，请先设置 ~/.skillhub_cookies.txt")
        print("  用户需在浏览器登录企业团队账号，导出cookie到文件")
        return False

    url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills?page=1&pageSize=1"
    req = Request(url, headers={
        'Cookie': cookies,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    })
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            total = data.get('total', 0)
            print(f"✅ 认证成功! Skill总数: {total}")
            return True
    except HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        if 'enterprise authentication required' in body.lower():
            print("❌ 认证失败: 当前cookie为个人账号，需要企业团队账号cookie")
            print("  请在浏览器登录企业团队账号，导出cookie到 ~/.skillhub_cookies.txt")
        else:
            print(f"❌ 认证失败: HTTP {e.code} - {body[:200]}")
        return False
    except Exception as e:
        print(f"❌ 认证失败: {e}")
        return False


def publish_org_only():
    """[已废弃] 将org_only skill切换为public对外发布

    请使用: python platform_ops.py batch-republish
    统一入口: platform_ops.publish_to_community() 处理完整的发布流程
    (approve → publish_to_community → star → DB更新)
    """
    print("⚠ 已废弃: 此命令已被 platform_ops.py batch-republish 替代")
    print("  请使用: python platform_ops.py batch-republish")
    print("  统一入口支持: approve → publish_to_community → star → DB更新")
    print("  且自动处理slug冲突和改名逻辑\n")

    # 向后兼容: 仍可执行, 但建议迁移
    cookies = load_cookies()
    if not cookies:
        print("错误：无认证cookie")
        return

    print(f"准备发布 {len(ORG_ONLY_SLUGS)} 个org_only skill为public...")
    for slug in ORG_ONLY_SLUGS:
        url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}/visibility"
        payload = json.dumps({'visibility': 'public'}).encode('utf-8')
        req = Request(url, data=payload, method='PATCH', headers={
            'Cookie': cookies,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        try:
            with urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                print(f"  ✅ {slug} 已发布为public")
        except Exception as e:
            print(f"  ❌ {slug} 发布失败: {e}")
        time.sleep(1)


def scan_all_differentiated_slugs():
    """扫描differentiated-skills目录获取所有skill slug"""
    diff_dir = Path(__file__).parent.parent / "differentiated-skills"
    all_slugs = []

    if diff_dir.exists():
        for cat_dir in diff_dir.iterdir():
            if cat_dir.is_dir():
                for skill_dir in cat_dir.iterdir():
                    if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                        content = (skill_dir / "SKILL.md").read_text(encoding='utf-8')
                        if content.startswith('\ufeff'):
                            content = content[1:]
                        if content.startswith('---'):
                            parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                            if len(parts) >= 3:
                                slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', parts[1], re.MULTILINE)
                                if slug_match:
                                    all_slugs.append(slug_match.group(1).strip())
    return all_slugs


def reupload_all_batch():
    """全量DELETE+重传所有skill（带断点续传）
    
    优先从 reupload_plan.json 加载SkillHub上已有的skill slug列表（覆盖3个目录），
    回退到 scan_all_differentiated_slugs()。
    """
    if not check_auth():
        return

    # 优先从reupload_plan.json加载（覆盖packaged/opensource/differentiated三个目录）
    plan_file = REPORT_DIR / "reupload_plan.json"
    if plan_file.exists():
        try:
            plan = json.loads(plan_file.read_text(encoding='utf-8'))
            all_slugs = plan.get('reupload_all_slugs', [])
            print(f"\n从 reupload_plan.json 加载: {len(all_slugs)} 个skill（覆盖packaged/opensource/differentiated）")
        except Exception as e:
            print(f"加载reupload_plan.json失败: {e}，回退到扫描differentiated-skills")
            all_slugs = scan_all_differentiated_slugs()
    else:
        all_slugs = scan_all_differentiated_slugs()
        print(f"\n扫描到 {len(all_slugs)} 个skill待重传（仅differentiated-skills）")

    print(f"待重传: {len(all_slugs)} 个skill")

    # 断点续传：从已有报告中读取已完成的slug
    completed = set()
    progress_file = REPORT_DIR / "batch_reupload_progress.json"
    if progress_file.exists():
        try:
            data = json.loads(progress_file.read_text(encoding='utf-8'))
            completed.update(data.get('success', []))
        except Exception:
            pass
    # 兼容旧格式报告
    for report_file in REPORT_DIR.glob("batch_reupload_*.json"):
        try:
            data = json.loads(report_file.read_text(encoding='utf-8'))
            completed.update(data.get('success', []))
        except Exception:
            pass

    if completed:
        print(f"断点续传: 已完成 {len(completed)} 个，剩余 {len(all_slugs) - len(completed)} 个")
        all_slugs = [s for s in all_slugs if s not in completed]

    batch_reupload(all_slugs, delay=0.8)


# ============ 非破坏性元数据更新（Phase 2/3核心功能） ============

def build_metadata_payload(slug: str) -> dict:
    """为指定skill构建元数据更新payload（复用enterprise_uploader.py的函数）

    Returns:
        包含categoryIds, tags, summary_zh, iconUrl, category, subCategories, changelog的dict
    """
    skill_md = find_skill_md(slug)
    if not skill_md:
        return {'error': f'SKILL.md文件未找到: {slug}'}

    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm = parse_frontmatter(content)
    body = fm.get('_body', '')

    platform_category = get_platform_category(slug, fm, body)
    team_category_id = get_team_category_id(platform_category)
    tags_list = parse_tags(fm, body)
    if isinstance(tags_list, str):
        tags_list = [t.strip() for t in tags_list.split(',') if t.strip()]
    if not tags_list:
        tags_list = ['工具', '效率']

    summary_zh = fm.get('summary_zh', '')
    if not summary_zh or not summary_zh.strip():
        summary_zh = generate_summary_zh(fm, body)

    from enterprise_uploader import CATEGORY_ICONS, DEFAULT_ICON  # 已在顶部导入，此行保留向后兼容
    icon_url = CATEGORY_ICONS.get(platform_category, DEFAULT_ICON)
    subcategories = get_subcategories(platform_category, fm, body)
    version = fm.get('version', '1.0.0')
    changelog = fm.get('changelog', f'v{version} - 元数据更新: 分类={platform_category}')

    return {
        'categoryIds': [team_category_id],
        'category': platform_category,
        'tags': tags_list,
        'summary_zh': summary_zh,
        'iconUrl': icon_url,
        'subCategories': subcategories,
        'changelog': changelog,
    }


def test_metadata_patch(slug: str) -> dict:
    """测试PATCH/PUT端点是否可用于非破坏性更新skill元数据

    测试步骤:
    1. GET基线: 获取当前字段
    2. PATCH尝试: 发送元数据更新
    3. 若PATCH失败(405), 尝试PUT
    4. GET验证: 检查字段是否更新
    5. 返回测试结果

    Returns:
        dict with keys: method, status, success, before, after, message
    """
    cookies = load_cookies()
    if not cookies:
        return {'success': False, 'message': '无认证cookie'}

    # 构建认证头
    if cookies.startswith('BEARER:'):
        api_key = cookies[len('BEARER:'):]
        auth_headers = {'Authorization': f'Bearer {api_key}'}
    else:
        auth_headers = {'Cookie': cookies}

    base_headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        **auth_headers,
    }

    # 1. GET基线
    detail_url = f"{API_BASE}/skills/{slug}"
    try:
        req = Request(detail_url, headers=base_headers)
        with urlopen(req, timeout=15) as resp:
            before_data = json.loads(resp.read().decode('utf-8'))
        before = before_data.get('skill', before_data)
    except Exception as e:
        return {'success': False, 'message': f'GET基线失败: {e}'}

    # 构建更新payload
    payload = build_metadata_payload(slug)
    if 'error' in payload:
        return {'success': False, 'message': payload['error']}

    payload_json = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    update_url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}"

    # 2. 尝试PATCH
    result = {'slug': slug, 'before': {
        'categoryIds': before.get('categoryIds'),
        'category': before.get('category', ''),
        'tags': before.get('tags'),
        'summary_zh': before.get('summary_zh', ''),
        'iconUrl': before.get('iconUrl', ''),
    }}

    patch_headers = {'Content-Type': 'application/json', **base_headers}
    try:
        req = Request(update_url, data=payload_json, method='PATCH', headers=patch_headers)
        with urlopen(req, timeout=15) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
        result['method'] = 'PATCH'
        result['status'] = resp.status if hasattr(resp, 'status') else resp.getcode()
        result['patch_response'] = resp_data
    except HTTPError as e:
        error_body = e.read().decode('utf-8', errors='replace')
        result['patch_error'] = f'HTTP {e.code}: {error_body[:200]}'

        # 3. PATCH失败, 尝试PUT
        try:
            req = Request(update_url, data=payload_json, method='PUT', headers=patch_headers)
            with urlopen(req, timeout=15) as resp:
                resp_data = json.loads(resp.read().decode('utf-8'))
            result['method'] = 'PUT'
            result['status'] = resp.status if hasattr(resp, 'status') else resp.getcode()
            result['put_response'] = resp_data
        except HTTPError as e2:
            error_body2 = e2.read().decode('utf-8', errors='replace')
            result['method'] = 'NONE'
            result['status'] = e2.code
            result['message'] = f'PATCH和PUT均失败。PATCH: HTTP {e.code}, PUT: HTTP {e2.code}'
            return result
        except Exception as e2:
            result['method'] = 'NONE'
            result['message'] = f'PUT异常: {e2}'
            return result
    except Exception as e:
        result['method'] = 'NONE'
        result['message'] = f'PATCH异常: {e}'
        return result

    # 4. GET验证
    time.sleep(1)
    try:
        req = Request(detail_url, headers=base_headers)
        with urlopen(req, timeout=15) as resp:
            after_data = json.loads(resp.read().decode('utf-8'))
        after = after_data.get('skill', after_data)
        result['after'] = {
            'categoryIds': after.get('categoryIds'),
            'category': after.get('category', ''),
            'tags': after.get('tags'),
            'summary_zh': after.get('summary_zh', ''),
            'iconUrl': after.get('iconUrl', ''),
        }

        # 判断是否更新成功
        cat_updated = result['after']['categoryIds'] != result['before']['categoryIds']
        tags_updated = result['after']['tags'] != result['before']['tags']
        summary_updated = result['after']['summary_zh'] != result['before']['summary_zh']
        icon_updated = result['after']['iconUrl'] != result['before']['iconUrl']

        result['success'] = cat_updated or tags_updated or summary_updated or icon_updated
        result['message'] = f"categoryIds更新={cat_updated}, tags更新={tags_updated}, summary_zh更新={summary_updated}, iconUrl更新={icon_updated}"
    except Exception as e:
        result['success'] = False
        result['message'] = f'GET验证失败: {e}'

    return result


def update_metadata_batch(delay: float = 1.0):
    """批量使用PATCH/PUT非破坏性更新所有skill的元数据

    - 不触发新审核
    - 不丢失downloads/stars
    - 支持断点续传
    - 每个skill间隔1秒（PATCH比POST轻量）
    """
    if not check_auth():
        print("认证失败，无法执行批量更新")
        return

    # 先测试单个skill
    test_slugs = ['ad-creative-intel-free']
    print("\n=== Phase 2: 测试非破坏性元数据更新 ===")
    print(f"测试样本: {test_slugs[0]}")
    test_result = test_metadata_patch(test_slugs[0])
    print(f"  方法: {test_result.get('method', 'N/A')}")
    print(f"  状态: {test_result.get('status', 'N/A')}")
    print(f"  成功: {test_result.get('success', False)}")
    print(f"  消息: {test_result.get('message', 'N/A')}")

    if not test_result.get('success'):
        print("\n❌ 非破坏性更新不可用，需要使用Path B (DELETE+重传)")
        print("  请使用: python batch_field_fix.py reupload-all-batch")
        # 保存测试结果
        test_file = REPORT_DIR / "metadata_patch_test_result.json"
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_result, f, ensure_ascii=False, indent=2)
        print(f"  测试结果已保存: {test_file}")
        return

    print(f"\n✅ 非破坏性更新可用! 方法: {test_result['method']}")
    print("\n=== Phase 3: 批量更新所有skill元数据 ===")

    # 扫描所有skill
    all_slugs = scan_all_differentiated_slugs()
    print(f"扫描到 {len(all_slugs)} 个skill")

    # 断点续传：从已有报告中读取已完成的slug
    completed = set()
    metadata_report = REPORT_DIR / "metadata_update_progress.json"
    if metadata_report.exists():
        try:
            data = json.loads(metadata_report.read_text(encoding='utf-8'))
            completed.update(data.get('success', []))
        except Exception:
            pass

    if completed:
        print(f"断点续传: 已完成 {len(completed)} 个，剩余 {len(all_slugs) - len(completed)} 个")
        all_slugs = [s for s in all_slugs if s not in completed]

    results = {'success': [], 'failed': []}
    method = test_result['method']  # PATCH 或 PUT

    cookies = load_cookies()
    if cookies.startswith('BEARER:'):
        api_key = cookies[len('BEARER:'):]
        auth_headers = {'Authorization': f'Bearer {api_key}'}
    else:
        auth_headers = {'Cookie': cookies}

    base_headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        **auth_headers,
    }

    for i, slug in enumerate(all_slugs):
        print(f"\n[{i+1}/{len(all_slugs)}] {slug}")

        payload = build_metadata_payload(slug)
        if 'error' in payload:
            print(f"  ❌ {payload['error']}")
            results['failed'].append({'slug': slug, 'error': payload['error']})
            continue

        payload_json = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        update_url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}"
        patch_headers = {'Content-Type': 'application/json', **base_headers}

        try:
            req = Request(update_url, data=payload_json, method=method, headers=patch_headers)
            with urlopen(req, timeout=15) as resp:
                resp_data = json.loads(resp.read().decode('utf-8'))
            print(f"  ✅ 更新成功 ({method})")
            results['success'].append(slug)
        except HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            print(f"  ❌ HTTP {e.code}: {error_body[:100]}")
            results['failed'].append({'slug': slug, 'error': f'HTTP {e.code}: {error_body[:200]}'})
        except Exception as e:
            print(f"  ❌ {e}")
            results['failed'].append({'slug': slug, 'error': str(e)})

        # 每10个保存一次进度
        if (i + 1) % 10 == 0:
            with open(metadata_report, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"  [进度已保存: 成功{len(results['success'])}, 失败{len(results['failed'])}]")

        if i + 1 < len(all_slugs):
            time.sleep(delay)

    # 最终保存
    with open(metadata_report, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n=== 批量元数据更新结果 ===")
    print(f"✅ 成功: {len(results['success'])}")
    print(f"❌ 失败: {len(results['failed'])}")
    print(f"进度报告: {metadata_report}")

    if results['failed']:
        print("\n失败详情:")
        for f in results['failed'][:20]:
            print(f"  {f['slug']}: {f['error']}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n可用命令:")
        print("  check              检查哪些skill需要修复")
        print("  check-auth         检查企业认证状态")
        print("  reupload <slug>    重新上传单个skill")
        print("  batch <n>          批量修复前n个skill")
        print("  reupload-all-batch 全量DELETE+重传所有skill(带断点续传)")
        print("  reupload-deleted   重新上传被删除的skill")
        print("  reupload-rejected  重新上传38个被拒绝的skill")
        print("  publish-org-only   [已废弃] 请用 platform_ops.py batch-republish")
        print("  gen-approve-js     [已废弃] 请用 platform_ops.py batch-approve")
        print("  test-metadata-patch <slug>  测试PATCH/PUT非破坏性元数据更新")
        print("  update-metadata-batch       批量非破坏性更新所有skill元数据(Phase 3)")
        return

    cmd = sys.argv[1]

    if cmd == 'check':
        check_skills_needing_fix()
    elif cmd == 'check-auth':
        check_auth()
    elif cmd == 'reupload':
        if len(sys.argv) < 3:
            print("用法: python batch_field_fix.py reupload <slug>")
            return
        reupload_skill(sys.argv[2])
    elif cmd == 'batch':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        needs_fix = check_skills_needing_fix()
        if needs_fix:
            slugs = [s['slug'] for s in needs_fix[:n]]
            batch_reupload(slugs)
    elif cmd == 'reupload-all-batch':
        reupload_all_batch()
    elif cmd == 'reupload-deleted':
        batch_reupload(DELETED_SLUGS)
    elif cmd == 'reupload-rejected':
        batch_reupload(REJECTED_SLUGS)
    elif cmd == 'publish-org-only':
        publish_org_only()
    elif cmd == 'gen-approve-js':
        generate_approval_js()
    elif cmd == 'test-metadata-patch':
        if len(sys.argv) < 3:
            print("用法: python batch_field_fix.py test-metadata-patch <slug>")
            print("  默认测试slug: ad-creative-intel-free")
            test_slug = 'ad-creative-intel-free'
        else:
            test_slug = sys.argv[2]
        result = test_metadata_patch(test_slug)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        # 保存测试结果
        test_file = REPORT_DIR / "metadata_patch_test_result.json"
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"\n测试结果已保存: {test_file}")
    elif cmd == 'update-metadata-batch':
        update_metadata_batch()
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()
