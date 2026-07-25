#!/usr/bin/env python3
"""
SkillHub批量字段修复脚本
========================
因PUT API不可用，需要DELETE+重新上传来更新tags/summary_zh等字段。
本脚本支持：
1. 批量审核通过待审版本（通过浏览器JS）
2. 批量删除+重新上传skill（补全tags/summary_zh/category等字段）
3. 重新上传被删除的skill

使用方式:
    python batch_field_fix.py check          # 检查哪些skill需要修复
    python batch_field_fix.py reupload <slug> # 重新上传单个skill
    python batch_field_fix.py batch <n>       # 批量修复前n个skill
    python batch_field_fix.py gen-approve-js  # 生成批量审核通过JS脚本
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

# 被拒绝的skill slug列表（从通知中提取）
REJECTED_SLUGS = [
    'ai-writing-style-cloner', 'api-design-architect', 'auth-security-architect',
    'azure-cloud-automator', 'brand-identity-creator', 'c-suite-advisor',
    'canvas-art-designer', 'clickhouse-olap-expert', 'cloudflare-edge-developer',
    'code-review-sentinel', 'competitive-ad-spy', 'compliance-manager',
    'content-cms-architect', 'content-refiner', 'copywriting-master',
    'csv-insight-miner', 'drama-hit-producer', 'ebook-factory',
    'ecommerce-pricing-strategist', 'geo-rank-architect'
]

# 被删除需要重新上传的skill
DELETED_SLUGS = ['memory-orchestrator-sk']


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
    js_code = """// SkillHub 批量审核通过脚本
// 在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  const BATCH_SIZE = 5;
  let approved = 0;
  let failed = 0;
  let totalProcessed = 0;
  
  console.log("=== SkillHub 批量审核通过 ===");
  
  // 获取审核列表总数
  const allButtons = document.querySelectorAll('button');
  const approveButtons = Array.from(allButtons).filter(b => b.textContent.trim() === '审核通过');
  const totalPages = document.querySelectorAll('[class*="page"], [class*="Page"]');
  
  console.log(`当前页面有 ${approveButtons.length} 个审核按钮`);
  console.log(`总页数信息:`, totalPages.length);
  
  // 逐个点击审核通过
  for (let i = 0; i < approveButtons.length; i++) {
    try {
      approveButtons[i].click();
      approved++;
      totalProcessed++;
      console.log(`  [${totalProcessed}] 审核通过已点击`);
      
      // 等待页面响应
      await new Promise(r => setTimeout(r, 500));
      
      // 重新获取按钮（DOM可能已更新）
      const newButtons = document.querySelectorAll('button');
      const newApproveButtons = Array.from(newButtons).filter(b => b.textContent.trim() === '审核通过');
      if (newApproveButtons.length > 0 && i < approveButtons.length - 1) {
        approveButtons.length = 0;
        approveButtons.push(...newApproveButtons);
        i = -1; // 重置索引
      }
    } catch(e) {
      failed++;
      console.error(`  审核失败: ${e.message}`);
    }
    
    // 每5个等待1秒
    if (totalProcessed % BATCH_SIZE === 0) {
      console.log(`已处理 ${totalProcessed} 个, 成功 ${approved}, 失败 ${failed}`);
      await new Promise(r => setTimeout(r, 1000));
    }
  }
  
  console.log(`\\n=== 完成 ===`);
  console.log(`总计处理: ${totalProcessed}`);
  console.log(`成功: ${approved}`);
  console.log(`失败: ${failed}`);
  console.log(`\\n请刷新页面继续处理下一页`);
})();
"""
    
    js_file = REPORT_DIR / "batch_approve_reviews.js"
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"批量审核JS脚本已生成: {js_file}")
    print("请在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'check':
        check_skills_needing_fix()
    elif cmd == 'reupload':
        if len(sys.argv) < 3:
            print("用法: python batch_field_fix.py reupload <slug>")
            return
        reupload_skill(sys.argv[2])
    elif cmd == 'batch':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        # 先检查需要修复的skill
        needs_fix = check_skills_needing_fix()
        if needs_fix:
            slugs = [s['slug'] for s in needs_fix[:n]]
            batch_reupload(slugs)
    elif cmd == 'reupload-deleted':
        # 重新上传被删除的skill
        batch_reupload(DELETED_SLUGS)
    elif cmd == 'reupload-rejected':
        # 重新上传被拒绝的skill
        batch_reupload(REJECTED_SLUGS)
    elif cmd == 'gen-approve-js':
        generate_approval_js()
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()
