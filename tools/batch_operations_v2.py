#!/usr/bin/env python3
"""
SkillHub批量审核+删除重传脚本 v2
================================
增强版：支持多种认证方式 + 批量审核 + 删除重传 + 进度跟踪

使用方式:
    python batch_operations_v2.py check-auth         # 检查认证状态
    python batch_operations_v2.py approve-all         # 生成批量审核JS
    python batch_operations_v2.py delete-rejected     # 删除被拒skill(38个)
    python batch_operations_v2.py reupload-rejected   # 删除+重传被拒skill(38个)
    python batch_operations_v2.py reupload-deleted    # 重传已删除skill
    python batch_operations_v2.py delete-banned       # 删除被封禁skill(5个VPN)
    python batch_operations_v2.py publish-org-only    # 对外发布4个org_only skill
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# 添加工具目录到路径
TOOLS_DIR = Path(__file__).parent
sys.path.insert(0, str(TOOLS_DIR))

from config import DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR

# ============ 配置 ============
ORG_ID = 862
API_BASE = "https://api.skillhub.cn/api/v1"

# Cookie文件路径
COOKIE_FILE = Path(os.environ.get(
    'SKILLHUB_COOKIE_FILE',
    os.path.join(os.path.expanduser('~'), '.skillhub_cookies.txt')
))

# 被拒绝的skill slug列表 (38个 — 旧版本Proprietary license残留)
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

# 被封禁的skill slug列表 (5个 — VPN/翻墙内容)
BANNED_SLUGS = [
    'v2ray-proxy-tool-free', 'v2ray-proxy-tool-pro', 'universal-proxy-pro',
    'vpn-toolkit-free', 'vpn-toolkit-pro'
]

# 4个org_only skill (未对外发布)
ORG_ONLY_SLUGS = [
    'ai-artist-workstation-pro', 'clickhouse-olap-expert',
    'requirement-explorer-pro', 'lead-research-hunter'
]

# 被删除需要重新上传的skill
DELETED_SLUGS = ['memory-orchestrator-sk']


def load_cookies():
    """加载浏览器cookie"""
    if COOKIE_FILE.exists():
        cookies = COOKIE_FILE.read_text(encoding='utf-8').strip()
        if cookies:
            return cookies

    env_cookies = os.environ.get('SKILLHUB_SESSION_COOKIE', '')
    if env_cookies:
        return env_cookies

    return None


def make_request(url, method='GET', data=None, headers=None):
    """发送HTTP请求"""
    cookies = load_cookies()
    default_headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0',
    }
    if cookies:
        default_headers['Cookie'] = cookies
    if headers:
        default_headers.update(headers)

    req = Request(url, data=data, headers=default_headers, method=method)
    try:
        with urlopen(req, timeout=30) as resp:
            body = resp.read().decode('utf-8')
            return json.loads(body) if body else {}
    except HTTPError as e:
        body = e.read().decode('utf-8') if e.fp else ''
        try:
            return json.loads(body)
        except:
            return {'error': f'HTTP {e.code}', 'body': body[:500]}
    except Exception as e:
        return {'error': str(e)}


def check_auth():
    """检查认证状态"""
    print("=== 检查认证状态 ===\n")

    cookies = load_cookies()
    if not cookies:
        print("❌ 无认证cookie")
        print(f"   请设置cookie文件: {COOKIE_FILE}")
        print("   或设置环境变量: SKILLHUB_SESSION_COOKIE")
        return False

    print(f"Cookie文件: {COOKIE_FILE}")
    print(f"Cookie长度: {len(cookies)}")
    print(f"Cookie前50字符: {cookies[:50]}...")

    # 尝试获取admin skill列表
    print("\n尝试获取admin skill列表...")
    result = make_request(f"{API_BASE}/orgs/{ORG_ID}/admin/skills?page=1&pageSize=1")

    if 'error' in result:
        print(f"❌ Admin API认证失败: {result['error']}")
        if 'enterprise authentication required' in str(result.get('body', '')):
            print("\n   原因: cookie过期或不是企业账号")
            print("   解决方案:")
            print("   1. 在浏览器中登录skillhub.cn企业账号")
            print("   2. 从浏览器开发者工具 > Application > Cookies 复制完整cookie")
            print("   3. 保存到 ~/.skillhub_cookies.txt")
        return False

    total = result.get('total', 0)
    print(f"✅ 认证成功! Skill总数: {total}")
    return True


def delete_skill(slug):
    """删除skill"""
    url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}"
    result = make_request(url, method='DELETE')

    if 'error' in result:
        print(f"  ❌ 删除 {slug} 失败: {result['error']}")
        return False

    # 检查删除是否成功
    if result.get('deleted') or result.get('ok') or result.get('success'):
        return True

    # 有些API删除成功返回空body
    if not result:
        return True

    print(f"  ⚠️ 删除 {slug} 返回: {json.dumps(result)[:200]}")
    return True  # 假设成功


def reupload_skill(slug):
    """重新上传skill"""
    # 导入上传函数
    try:
        from enterprise_uploader import upload_skill
    except ImportError as e:
        print(f"  ❌ 无法导入upload_skill: {e}")
        return {'success': False, 'slug': slug, 'message': f'导入失败: {e}'}

    # 1. 先删除
    print(f"  1. 删除旧版本...")
    delete_skill(slug)
    time.sleep(1)

    # 2. 重新上传
    print(f"  2. 重新上传...")
    result = upload_skill(slug, dry_run=False)
    return result


def batch_reupload(slugs, operation_name="重传"):
    """批量删除+重新上传"""
    results = {'success': [], 'failed': []}

    print(f"\n=== 批量{operation_name} ({len(slugs)}个) ===\n")

    for i, slug in enumerate(slugs):
        print(f"[{i+1}/{len(slugs)}] {slug}")
        result = reupload_skill(slug)

        if result.get('success'):
            print(f"  ✅ 成功")
            results['success'].append(slug)
        else:
            msg = result.get('message', '未知错误')
            print(f"  ❌ 失败: {msg}")
            results['failed'].append({'slug': slug, 'error': msg})

        if i + 1 < len(slugs):
            time.sleep(2)

    # 保存结果
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_file = REPORT_DIR / f"batch_{operation_name}_{timestamp}.json"
    with open(result_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n=== {operation_name}结果 ===")
    print(f"✅ 成功: {len(results['success'])}")
    print(f"❌ 失败: {len(results['failed'])}")
    print(f"结果保存: {result_file}")

    return results


def generate_approve_js():
    """生成批量审核JS脚本"""
    js_code = """// SkillHub 批量审核通过脚本 v2
// 在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行
(async function() {
  let totalApproved = 0;
  let totalFailed = 0;
  let currentPage = 1;
  let totalPages = 271;

  // 从localStorage恢复进度
  const saved = localStorage.getItem('sh_approve_progress');
  if (saved) {
    const p = JSON.parse(saved);
    totalApproved = p.approved || 0;
    totalFailed = p.failed || 0;
    currentPage = p.page || 1;
    console.log(`恢复进度: 通过${totalApproved}, 失败${totalFailed}, 页${currentPage}`);
  }

  console.log("=== SkillHub 批量审核通过 v2 ===");

  function getApproveButtons() {
    return Array.from(document.querySelectorAll('button')).filter(b => b.textContent.trim() === '审核通过');
  }

  async function goToPage(pageNum) {
    const pageBtns = document.querySelectorAll('button');
    const targetBtn = Array.from(pageBtns).find(b => b.textContent.trim() === String(pageNum));
    if (targetBtn) {
      targetBtn.click();
      await new Promise(r => setTimeout(r, 1500));
      return true;
    }
    // 尝试下一页按钮
    const nextBtn = Array.from(pageBtns).find(b => b.textContent.includes('下一页'));
    if (nextBtn && !nextBtn.disabled) {
      nextBtn.click();
      await new Promise(r => setTimeout(r, 1500));
      return true;
    }
    return false;
  }

  for (let page = currentPage; page <= totalPages; page++) {
    console.log(`\\n--- 第 ${page}/${totalPages} 页 ---`);
    await new Promise(r => setTimeout(r, 500));

    let buttons = getApproveButtons();
    console.log(`找到 ${buttons.length} 个审核按钮`);

    for (let i = 0; i < buttons.length; i++) {
      try {
        buttons[i].click();
        totalApproved++;
        await new Promise(r => setTimeout(r, 300));
      } catch(e) {
        totalFailed++;
      }

      if ((totalApproved + totalFailed) % 10 === 0) {
        localStorage.setItem('sh_approve_progress', JSON.stringify({
          approved: totalApproved, failed: totalFailed, page: page
        }));
        console.log(`进度: 通过${totalApproved}, 失败${totalFailed}`);
      }
    }

    // 翻页
    if (page < totalPages) {
      const moved = await goToPage(page + 1);
      if (!moved) {
        console.log('无法翻页，结束');
        break;
      }
    }
  }

  localStorage.removeItem('sh_approve_progress');
  console.log(`\\n=== 完成 ===`);
  console.log(`总通过: ${totalApproved}`);
  console.log(`总失败: ${totalFailed}`);
})();
"""

    js_file = REPORT_DIR / "batch_approve_v2.js"
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"批量审核JS脚本已生成: {js_file}")
    print("请在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == 'check-auth':
        check_auth()

    elif cmd == 'approve-all':
        generate_approve_js()

    elif cmd == 'delete-rejected':
        if not check_auth():
            return
        print("\n删除被拒skill...")
        for slug in REJECTED_SLUGS:
            print(f"  删除 {slug}...")
            delete_skill(slug)
            time.sleep(0.5)

    elif cmd == 'reupload-rejected':
        if not check_auth():
            return
        batch_reupload(REJECTED_SLUGS, "重传被拒skill")

    elif cmd == 'reupload-deleted':
        if not check_auth():
            return
        batch_reupload(DELETED_SLUGS, "重传已删除skill")

    elif cmd == 'delete-banned':
        if not check_auth():
            return
        print("\n删除被封禁skill...")
        for slug in BANNED_SLUGS:
            print(f"  删除 {slug}...")
            delete_skill(slug)
            time.sleep(0.5)

    elif cmd == 'publish-org-only':
        """对外发布4个org_only skill"""
        if not check_auth():
            return
        print("\n对外发布org_only skill...")
        for slug in ORG_ONLY_SLUGS:
            print(f"  发布 {slug}...")
            result = make_request(
                f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}/publish",
                method='POST'
            )
            if 'error' in result:
                print(f"    ❌ 失败: {result['error']}")
            else:
                print(f"    ✅ 成功")
            time.sleep(1)

    elif cmd == 'approve-v3':
        """生成v3审核JS脚本"""
        js_file = REPORT_DIR / "batch_approve_v3.js"
        if js_file.exists():
            print(f"v3审核JS脚本已存在: {js_file}")
            print("请在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行")
        else:
            print("请运行生成脚本")

    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()
