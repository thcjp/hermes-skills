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
    get_platform_category, get_subcategories, parse_tags, generate_summary_zh,
    load_cookies, ORG_ID, API_BASE, ORG_SKILLS_API
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
    """删除skill"""
    cookies = load_cookies()
    if not cookies:
        print("错误：无认证cookie")
        return False
    
    url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}"
    req = Request(url, method='DELETE', headers={
        'Cookie': cookies,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    })
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('deleted', False) or data.get('ok', False)
    except Exception as e:
        print(f"  删除 {slug} 失败: {e}")
        return False


def reupload_skill(slug: str) -> dict:
    """删除并重新上传skill（带完整字段）"""
    print(f"\n处理 {slug}...")
    
    # 1. 先尝试删除（如果已存在）
    print(f"  1. 尝试删除已有版本...")
    delete_skill(slug)
    time.sleep(1)
    
    # 2. 使用增强后的upload_skill重新上传
    print(f"  2. 重新上传（含tags/summary_zh/category等完整字段）...")
    result = upload_skill(slug, dry_run=False)
    
    if result['success']:
        print(f"  ✅ {slug} 重新上传成功")
    else:
        print(f"  ❌ {slug} 重新上传失败: {result['message']}")
    
    return result


def batch_reupload(slugs: list, delay: float = 2.0):
    """批量删除+重新上传"""
    results = {'success': [], 'failed': []}
    
    for i, slug in enumerate(slugs):
        print(f"\n[{i+1}/{len(slugs)}] {slug}")
        result = reupload_skill(slug)
        
        if result['success']:
            results['success'].append(slug)
        else:
            results['failed'].append({'slug': slug, 'error': result['message']})
        
        if i + 1 < len(slugs):
            time.sleep(delay)
    
    print(f"\n=== 批量重新上传结果 ===")
    print(f"✅ 成功: {len(results['success'])}")
    print(f"❌ 失败: {len(results['failed'])}")
    
    if results['failed']:
        print("\n失败详情:")
        for f in results['failed']:
            print(f"  {f['slug']}: {f['error']}")
    
    # 保存结果
    result_file = REPORT_DIR / f"batch_reupload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(result_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n结果已保存到: {result_file}")
    
    return results


def generate_approval_js():
    """生成批量审核通过的浏览器JS脚本"""
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
    """将org_only skill切换为public对外发布"""
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
    """全量DELETE+重传所有differentiated-skills下的skill（带断点续传）"""
    if not check_auth():
        return

    all_slugs = scan_all_differentiated_slugs()
    print(f"\n扫描到 {len(all_slugs)} 个skill待重传")

    # 断点续传：从已有报告中读取已完成的slug
    completed = set()
    for report_file in REPORT_DIR.glob("batch_reupload_*.json"):
        try:
            data = json.loads(report_file.read_text(encoding='utf-8'))
            completed.update(data.get('success', []))
        except Exception:
            pass

    if completed:
        print(f"断点续传: 已完成 {len(completed)} 个，剩余 {len(all_slugs) - len(completed)} 个")
        all_slugs = [s for s in all_slugs if s not in completed]

    batch_reupload(all_slugs, delay=2.0)


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
        print("  publish-org-only   4个org_only skill对外发布")
        print("  gen-approve-js     生成批量审核通过JS脚本")
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
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()
