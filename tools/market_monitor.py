#!/usr/bin/env python3
"""
市场监控功能 v1.0
==================
监控SkillHub和Coze等平台的竞品skill数据，包括：
1. 竞品定价、销量、下载量、评分
2. 按类别分析市场趋势
3. 生成对比报告和定价建议
4. 指导新skill开发方向

Usage:
    python market_monitor.py scan-skillhub          # 扫描SkillHub公开skill
    python market_monitor.py scan-coze              # 扫描Coze商店
    python market_monitor.py report                 # 生成市场分析报告
    python market_monitor.py recommend              # 生成定价和开发建议
    python market_monitor.py compare                # 对比我们的skill与竞品
    python market_monitor.py trending               # 发现热门类别和趋势
"""

import json
import re
import sqlite3
import sys
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# 导入统一配置（修复U-21硬编码路径、U-27无限循环、U-05分类归一化）
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from config import (
    DB_PATH, MARKET_DATA_DIR, MAX_SCAN_PAGES, safe_float, safe_int,
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR
)

MARKET_DATA_DIR.mkdir(parents=True, exist_ok=True)

# SkillHub API endpoints
SKILLHUB_API_BASE = "https://api.skillhub.cn/api/v1"
SKILLHUB_PUBLIC_SKILLS = f"{SKILLHUB_API_BASE}/skills"  # 公开skill列表
SKILLHUB_CATEGORIES = f"{SKILLHUB_API_BASE}/categories"

# Coze API endpoints  
COZE_STORE_URL = "https://www.coze.cn/store"

# 类别映射（统一分类，修复U-05：扩展中文关键词支持）
CATEGORY_MAPPING = {
    # 英文 → 标准类别
    'writing': '文案创作', 'copywriting': '文案创作', 'content': '文案创作',
    'code': '编程开发', 'development': '编程开发', 'programming': '编程开发',
    'design': '设计创作', 'ui': '设计创作', 'creative': '设计创作',
    'marketing': '营销推广', 'seo': 'SEO优化', 'advertising': '营销推广',
    'data': '数据分析', 'analytics': '数据分析',
    'security': '安全合规', 'compliance': '安全合规',
    'automation': '效率工具', 'productivity': '效率工具', 'workflow': '效率工具',
    'video': '视频音频', 'media': '视频音频', 'audio': '视频音频',
    'translation': '翻译', 'language': '翻译', 'i18n': '翻译',
    'database': '数据库', 'sql': '数据库',
    'api': 'API集成', 'integration': 'API集成', 'webhook': 'API集成',
    'file': '文件处理', 'document': '文件处理', 'pdf': '文件处理',
    'message': '通信消息', 'notification': '通信消息', 'email': '通信消息',
    'project': '项目管理', 'task': '项目管理',
    'ai': 'AI模型', 'llm': 'AI模型', 'gpt': 'AI模型', 'agent': 'AI模型',
    'monitor': '监控运维', 'ops': '监控运维',
    'ecommerce': '电商', 'shop': '电商',
    'finance': '财务法务', 'legal': '财务法务',
    'education': '教育学习', 'research': '教育学习',
    # 中文 → 标准类别（新增，修复48/54竞品归"其他"的问题）
    '文案': '文案创作', '写作': '文案创作', '内容创作': '文案创作', '爆款': '文案创作',
    '编程': '编程开发', '开发': '编程开发', '代码': '编程开发', '调试': '编程开发',
    '设计': '设计创作', '海报': '设计创作', '配色': '设计创作', '排版': '设计创作',
    '营销': '营销推广', '推广': '营销推广', '广告': '营销推广', '转化': '营销推广',
    '数据': '数据分析', '分析': '数据分析', '统计': '数据分析', '报表': '数据分析',
    '安全': '安全合规', '合规': '安全合规', '审计': '安全合规', '加密': '安全合规',
    '效率': '效率工具', '自动化': '效率工具', '批量': '效率工具', '快捷': '效率工具',
    '视频': '视频音频', '音频': '视频音频', '配音': '视频音频', '音乐': '视频音频',
    '翻译': '翻译', '多语言': '翻译', '语言': '翻译',
    '数据库': '数据库', '存储': '数据库', '查询': '数据库',
    '集成': 'API集成', '接口': 'API集成', '连接': 'API集成',
    '文件': '文件处理', '文档': '文件处理', '转换': '文件处理', '格式': '文件处理',
    '消息': '通信消息', '通知': '通信消息', '邮件': '通信消息', '短信': '通信消息',
    '项目': '项目管理', '任务': '项目管理', '管理': '项目管理', '计划': '项目管理',
    '模型': 'AI模型', '智能': 'AI模型', '助手': 'AI模型',
    '监控': '监控运维', '运维': '监控运维', '告警': '监控运维', '日志': '监控运维',
    '电商': '电商', '商品': '电商', '订单': '电商', '店铺': '电商',
    '财务': '财务法务', '法律': '财务法务', '税务': '财务法务',
    '教育': '教育学习', '学习': '教育学习', '研究': '教育学习',
}


def fetch_json(url: str, headers: dict = None, timeout: int = 30) -> Optional[dict]:
    """获取JSON数据"""
    try:
        req = Request(url)
        if headers:
            for k, v in headers.items():
                req.add_header(k, v)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Accept', 'application/json')
        
        with urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except (URLError, HTTPError, json.JSONDecodeError) as e:
        print(f"  获取数据失败: {url} - {e}")
        return None


def scan_skillhub():
    """扫描SkillHub公开skill数据
    
    修复U-27：添加MAX_PAGES安全阀，防止无限循环
    修复U-17：使用safe_float/safe_int安全转换
    """
    print("=" * 80)
    print("扫描SkillHub公开skill市场...")
    print("=" * 80)
    
    all_skills = []
    page = 1
    total = 0
    
    while page <= MAX_SCAN_PAGES:  # 修复U-27：替换 while True
        url = f"{SKILLHUB_PUBLIC_SKILLS}?page={page}&page_size=50&sort=downloads&order=desc"
        print(f"  获取第 {page} 页...")
        
        data = fetch_json(url)
        if not data:
            # 尝试不同的API路径
            url2 = f"{SKILLHUB_API_BASE}/public/skills?page={page}&page_size=50"
            data = fetch_json(url2)
        
        if not data:
            print(f"  无法获取第 {page} 页数据，停止扫描")
            break
        
        # 解析数据（兼容不同的API响应格式）
        skills = data.get('data', {}).get('items', []) or data.get('data', {}).get('list', []) or data.get('items', []) or data.get('list', [])
        
        if not skills:
            break
        
        for skill in skills:
            parsed = {
                'platform': 'skillhub',
                'slug': skill.get('slug', ''),
                'name': skill.get('name', skill.get('displayName', '')),
                'display_name': skill.get('displayName', skill.get('name', '')),
                'summary': skill.get('summary', ''),
                'category': skill.get('category', skill.get('tags', '')),
                'price': safe_float(skill.get('price', 0) or skill.get('pricePerCall', 0)),
                'billing_type': skill.get('billingType', skill.get('billing_type', 'free')),
                'downloads': safe_int(skill.get('downloadCount', skill.get('downloads', 0))),
                'calls': safe_int(skill.get('callCount', skill.get('calls', 0))),
                'rating': safe_float(skill.get('rating', skill.get('avgRating', 0))),
                'rating_count': safe_int(skill.get('ratingCount', skill.get('reviewCount', 0))),
                'author': skill.get('author', skill.get('publisher', '')),
                'created_at': skill.get('createdAt', skill.get('created_at', '')),
                'updated_at': skill.get('updatedAt', skill.get('updated_at', '')),
                'scanned_at': datetime.now().isoformat(),
            }
            all_skills.append(parsed)
        
        total = data.get('data', {}).get('total', data.get('total', len(all_skills)))
        print(f"  获取 {len(skills)} 个skill，累计 {len(all_skills)}/{total}")
        
        if len(skills) < 50 or len(all_skills) >= total:
            break
        
        page += 1
    
    if page > MAX_SCAN_PAGES:
        print(f"  警告：达到最大页数限制 {MAX_SCAN_PAGES}，可能未获取全部数据")
    
    # 保存数据
    output_path = MARKET_DATA_DIR / f"skillhub_{datetime.now().strftime('%Y%m%d')}.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_skills, f, ensure_ascii=False, indent=2)
    
    print(f"\n扫描完成: {len(all_skills)} 个skill")
    print(f"数据保存到: {output_path}")
    
    # 更新最新数据
    latest_path = MARKET_DATA_DIR / "skillhub_latest.json"
    with open(latest_path, 'w', encoding='utf-8') as f:
        json.dump(all_skills, f, ensure_ascii=False, indent=2)
    
    return all_skills


def scan_skillhub_via_browser():
    """通过浏览器扫描SkillHub（当API不可用时）"""
    print("API方式不可用，尝试通过浏览器扫描...")
    print("请在浏览器中打开 https://skillhub.cloud.tencent.com/explore")
    print("然后使用browser_evaluate执行以下脚本获取数据:")
    print("""
    // 在浏览器控制台执行
    fetch('/api/v1/skills?page=1&page_size=100&sort=downloads&order=desc')
      .then(r => r.json())
      .then(d => console.log(JSON.stringify(d)))
    """)
    return []


def load_market_data() -> List[dict]:
    """加载最新的市场数据"""
    all_data = []
    seen_names = set()
    
    # 优先加载手动录入的数据（包含竞品数据）
    manual_path = MARKET_DATA_DIR / "manual_entries.json"
    if manual_path.exists():
        with open(manual_path, 'r', encoding='utf-8') as f:
            for entry in json.load(f):
                name = entry.get('name', '')
                if name not in seen_names:
                    all_data.append(entry)
                    seen_names.add(name)
    
    # 加载SkillHub扫描数据（如果有且不重复）
    skillhub_latest = MARKET_DATA_DIR / "skillhub_latest.json"
    if skillhub_latest.exists():
        with open(skillhub_latest, 'r', encoding='utf-8') as f:
            for entry in json.load(f):
                name = entry.get('name', '')
                platform = entry.get('platform', '')
                # 只添加SkillHub扫描的数据（不添加manual_entries已包含的）
                if platform == 'skillhub' and name not in seen_names:
                    all_data.append(entry)
                    seen_names.add(name)
    
    return all_data


def load_our_skills() -> List[dict]:
    """从数据库加载我们的skill数据"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 加载所有有定价信息的skill
    c.execute("""
        SELECT slug, current_display_name, suggested_price, pricing_tier, 
               is_paid, pricing_category, local_path
        FROM skills 
        WHERE current_status = 'active' AND suggested_price IS NOT NULL
    """)
    
    our_skills = []
    for row in c.fetchall():
        our_skills.append({
            'slug': row[0],
            'name': row[1],
            'price': row[2] or 0,
            'tier': row[3] or 'free',
            'is_paid': row[4] or 0,
            'category': row[5] or '',
            'platform': 'ours',
        })
    
    conn.close()
    return our_skills


def normalize_category(raw_category: str, name: str, summary: str) -> str:
    """标准化类别（修复U-05：支持中文category直接匹配，不再将中文竞品归为"其他"）"""
    text = f"{raw_category} {name} {summary}".lower()
    
    # 优先匹配精确的中文类别名
    for chn_category in ['文案创作', '数据分析', 'SEO优化', '编程开发', '设计创作',
                          '营销推广', '效率工具', '安全合规', '翻译', '数据库',
                          'API集成', '文件处理', '视频音频', '通信消息', '项目管理',
                          'AI模型', '监控运维', '电商', '财务法务', '教育学习']:
        if chn_category.lower() in text:
            return chn_category
    
    # 再匹配映射表
    for key, chn in CATEGORY_MAPPING.items():
        if key.lower() in text:
            return chn
    
    return '其他'


def generate_report():
    """生成市场分析报告"""
    market_data = load_market_data()
    our_skills = load_our_skills()
    
    if not market_data:
        print("无市场数据，请先运行 scan-skillhub")
        return
    
    print("\n" + "=" * 100)
    print(f"市场分析报告 - 生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 100)
    
    # 1. 总体市场概况
    print(f"\n## 1. 市场概况")
    print(f"  竞品skill总数: {len(market_data)}")
    print(f"  我们的skill总数: {len(our_skills)}")
    
    # 2. 定价分析
    paid_market = [s for s in market_data if s.get('price', 0) > 0]
    free_market = [s for s in market_data if s.get('price', 0) == 0]
    
    print(f"\n## 2. 定价分析")
    print(f"  免费skill: {len(free_market)} ({len(free_market)/len(market_data)*100:.1f}%)")
    print(f"  付费skill: {len(paid_market)} ({len(paid_market)/len(market_data)*100:.1f}%)")
    
    if paid_market:
        prices = [s['price'] for s in paid_market]
        avg_price = sum(prices) / len(prices)
        min_price = min(prices)
        max_price = max(prices)
        median_price = sorted(prices)[len(prices)//2]
        
        print(f"\n  竞品付费skill定价:")
        print(f"    最低: {min_price:.1f}元")
        print(f"    最高: {max_price:.1f}元")
        print(f"    平均: {avg_price:.1f}元")
        print(f"    中位数: {median_price:.1f}元")
    
    our_paid = [s for s in our_skills if s.get('price', 0) > 0]
    if our_paid:
        our_prices = [s['price'] for s in our_paid]
        our_avg = sum(our_prices) / len(our_prices)
        print(f"\n  我们的付费skill定价:")
        print(f"    最低: {min(our_prices):.1f}元")
        print(f"    最高: {max(our_prices):.1f}元")
        print(f"    平均: {our_avg:.1f}元")
        
        if paid_market:
            print(f"\n  对比: 我们平均 {our_avg:.1f}元 vs 竞品平均 {avg_price:.1f}元")
            if our_avg > avg_price:
                print(f"  ⚠ 我们的定价高于市场平均 {(our_avg/avg_price-1)*100:.0f}%")
            else:
                print(f"  ✓ 我们的定价低于市场平均 {(1-our_avg/avg_price)*100:.0f}%")
    
    # 3. 按类别分析
    print(f"\n## 3. 按类别分析")
    
    # 标准化类别
    for s in market_data:
        s['norm_category'] = normalize_category(s.get('category', ''), s.get('name', ''), s.get('summary', ''))
    
    category_stats = {}
    for s in market_data:
        cat = s['norm_category']
        if cat not in category_stats:
            category_stats[cat] = {'count': 0, 'paid': 0, 'free': 0, 'prices': [], 'downloads': 0, 'calls': 0}
        category_stats[cat]['count'] += 1
        if s.get('price', 0) > 0:
            category_stats[cat]['paid'] += 1
            category_stats[cat]['prices'].append(s['price'])
        else:
            category_stats[cat]['free'] += 1
        category_stats[cat]['downloads'] += s.get('downloads', 0)
        category_stats[cat]['calls'] += s.get('calls', 0)
    
    print(f"  {'类别':<12} {'总数':>5} {'付费':>5} {'免费':>5} {'付费率':>7} {'平均价':>7} {'下载量':>8}")
    print(f"  {'-'*70}")
    
    for cat in sorted(category_stats.keys(), key=lambda x: category_stats[x]['count'], reverse=True):
        stats = category_stats[cat]
        paid_rate = stats['paid'] / stats['count'] * 100 if stats['count'] > 0 else 0
        avg_price = sum(stats['prices']) / len(stats['prices']) if stats['prices'] else 0
        print(f"  {cat:<12} {stats['count']:>5} {stats['paid']:>5} {stats['free']:>5} {paid_rate:>6.1f}% {avg_price:>6.1f}元 {stats['downloads']:>8}")
    
    # 4. 下载量TOP 20
    print(f"\n## 4. 下载量TOP 20")
    top_downloads = sorted(market_data, key=lambda x: x.get('downloads', 0), reverse=True)[:20]
    print(f"  {'名称':<40} {'定价':>7} {'下载量':>8} {'调用数':>8} {'评分':>5}")
    print(f"  {'-'*75}")
    for s in top_downloads:
        price_str = f"{s['price']:.1f}元" if s.get('price', 0) > 0 else "免费"
        print(f"  {s.get('name', '')[:38]:<40} {price_str:>7} {s.get('downloads', 0):>8} {s.get('calls', 0):>8} {s.get('rating', 0):>5.1f}")
    
    # 5. 定价TOP 20
    print(f"\n## 5. 定价TOP 20")
    top_priced = sorted([s for s in market_data if s.get('price', 0) > 0], key=lambda x: x['price'], reverse=True)[:20]
    print(f"  {'名称':<40} {'定价':>7} {'下载量':>8} {'调用数':>8}")
    print(f"  {'-'*70}")
    for s in top_priced:
        print(f"  {s.get('name', '')[:38]:<40} {s['price']:>6.1f}元 {s.get('downloads', 0):>8} {s.get('calls', 0):>8}")
    
    # 保存报告
    report_path = MARKET_DATA_DIR / f"market_report_{datetime.now().strftime('%Y%m%d')}.json"
    report_data = {
        'generated_at': datetime.now().isoformat(),
        'market_total': len(market_data),
        'our_total': len(our_skills),
        'category_stats': category_stats,
        'top_downloads': top_downloads,
        'top_priced': top_priced,
    }
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n报告保存到: {report_path}")


def generate_recommendations():
    """生成定价和开发建议"""
    market_data = load_market_data()
    our_skills = load_our_skills()
    
    if not market_data:
        print("无市场数据，请先运行 scan-skillhub")
        return
    
    print("\n" + "=" * 100)
    print(f"定价和开发建议 - 生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 100)
    
    # 1. 定价建议
    print(f"\n## 1. 定价建议")
    
    # 标准化类别
    for s in market_data:
        s['norm_category'] = normalize_category(s.get('category', ''), s.get('name', ''), s.get('summary', ''))
    
    # 按类别计算市场平均价
    category_prices = {}
    for s in market_data:
        if s.get('price', 0) > 0:
            cat = s['norm_category']
            if cat not in category_prices:
                category_prices[cat] = []
            category_prices[cat].append(s['price'])
    
    # 对比我们的定价
    print(f"\n  {'我们的Skill':<35} {'我们的定价':>8} {'市场均价':>8} {'差异':>8} {'建议'}")
    print(f"  {'-'*80}")
    
    overpriced = []
    underpriced = []
    
    for our in sorted(our_skills, key=lambda x: x.get('price', 0), reverse=True):
        if our.get('price', 0) == 0:
            continue
        
        # 找到同类别竞品
        our_cat = our.get('category', '')
        market_prices = category_prices.get(our_cat, [])
        
        if market_prices:
            market_avg = sum(market_prices) / len(market_prices)
            diff = our['price'] - market_avg
            diff_pct = diff / market_avg * 100
            
            if diff_pct > 30:
                suggestion = "↓ 建议降价"
                overpriced.append((our, market_avg, diff_pct))
            elif diff_pct < -30:
                suggestion = "↑ 可考虑涨价"
                underpriced.append((our, market_avg, diff_pct))
            else:
                suggestion = "✓ 定价合理"
            
            print(f"  {our['slug'][:33]:<35} {our['price']:>7.1f}元 {market_avg:>7.1f}元 {diff_pct:>+7.1f}% {suggestion}")
        else:
            print(f"  {our['slug'][:33]:<35} {our['price']:>7.1f}元 {'N/A':>8} {'N/A':>8} 无竞品数据")
    
    # 2. 新skill开发建议
    print(f"\n## 2. 新skill开发建议")
    
    # 找到市场大但我们缺空的类别
    category_stats = {}
    for s in market_data:
        cat = s['norm_category']
        if cat not in category_stats:
            category_stats[cat] = {'count': 0, 'downloads': 0, 'calls': 0, 'paid': 0}
        category_stats[cat]['count'] += 1
        category_stats[cat]['downloads'] += s.get('downloads', 0)
        category_stats[cat]['calls'] += s.get('calls', 0)
        if s.get('price', 0) > 0:
            category_stats[cat]['paid'] += 1
    
    our_categories = set(s.get('category', '') for s in our_skills)
    
    print(f"\n  市场热门但我们缺空的类别:")
    for cat in sorted(category_stats.keys(), key=lambda x: category_stats[x]['downloads'], reverse=True):
        if cat not in our_categories and category_stats[cat]['downloads'] > 100:
            stats = category_stats[cat]
            print(f"    {cat}: {stats['count']}个竞品, {stats['downloads']}下载, {stats['paid']}个付费")
    
    # 3. 热门趋势
    print(f"\n## 3. 热门趋势")
    
    # 下载量增长最快的类别
    recent_skills = sorted(market_data, key=lambda x: x.get('downloads', 0), reverse=True)[:50]
    recent_cats = {}
    for s in recent_skills:
        cat = s['norm_category']
        recent_cats[cat] = recent_cats.get(cat, 0) + 1
    
    print(f"\n  下载量TOP 50中的类别分布:")
    for cat, count in sorted(recent_cats.items(), key=lambda x: x[1], reverse=True):
        bar = '█' * count
        print(f"    {cat:<12}: {count:>3} {bar}")
    
    # 4. 付费转化率分析
    print(f"\n## 4. 付费转化率分析")
    print(f"\n  {'类别':<12} {'付费率':>7} {'平均价':>7} {'说明'}")
    print(f"  {'-'*60}")
    
    for cat in sorted(category_stats.keys(), key=lambda x: category_stats[x]['count'], reverse=True):
        stats = category_stats[cat]
        paid_rate = stats['paid'] / stats['count'] * 100 if stats['count'] > 0 else 0
        cat_prices = [s['price'] for s in market_data if s['norm_category'] == cat and s.get('price', 0) > 0]
        avg_price = sum(cat_prices) / len(cat_prices) if cat_prices else 0
        
        if paid_rate > 30:
            note = "高付费意愿"
        elif paid_rate > 10:
            note = "中等付费意愿"
        else:
            note = "低付费意愿"
        
        print(f"  {cat:<12} {paid_rate:>6.1f}% {avg_price:>6.1f}元 {note}")
    
    # 保存建议
    rec_path = MARKET_DATA_DIR / f"recommendations_{datetime.now().strftime('%Y%m%d')}.json"
    rec_data = {
        'generated_at': datetime.now().isoformat(),
        'overpriced': [(o[0]['slug'], o[0]['price'], o[1], o[2]) for o in overpriced],
        'underpriced': [(u[0]['slug'], u[0]['price'], u[1], u[2]) for u in underpriced],
        'category_stats': category_stats,
    }
    with open(rec_path, 'w', encoding='utf-8') as f:
        json.dump(rec_data, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n建议保存到: {rec_path}")


def compare_with_competitors():
    """对比我们的skill与竞品"""
    market_data = load_market_data()
    our_skills = load_our_skills()
    
    if not market_data:
        print("无市场数据，请先运行 scan-skillhub")
        return
    
    print("\n" + "=" * 100)
    print(f"竞品对比分析 - 生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 100)
    
    # 按类别对比
    our_by_cat = {}
    for s in our_skills:
        cat = s.get('category', '其他')
        if cat not in our_by_cat:
            our_by_cat[cat] = []
        our_by_cat[cat].append(s)
    
    market_by_cat = {}
    for s in market_data:
        cat = normalize_category(s.get('category', ''), s.get('name', ''), s.get('summary', ''))
        if cat not in market_by_cat:
            market_by_cat[cat] = []
        market_by_cat[cat].append(s)
    
    print(f"\n  {'类别':<12} {'我们':>5} {'竞品':>5} {'我们的均价':>10} {'竞品均价':>10} {'竞品下载':>10}")
    print(f"  {'-'*65}")
    
    all_cats = set(list(our_by_cat.keys()) + list(market_by_cat.keys()))
    for cat in sorted(all_cats):
        our_count = len(our_by_cat.get(cat, []))
        market_count = len(market_by_cat.get(cat, []))
        
        our_paid = [s for s in our_by_cat.get(cat, []) if s.get('price', 0) > 0]
        our_avg = sum(s['price'] for s in our_paid) / len(our_paid) if our_paid else 0
        
        market_paid = [s for s in market_by_cat.get(cat, []) if s.get('price', 0) > 0]
        market_avg = sum(s['price'] for s in market_paid) / len(market_paid) if market_paid else 0
        
        market_downloads = sum(s.get('downloads', 0) for s in market_by_cat.get(cat, []))
        
        print(f"  {cat:<12} {our_count:>5} {market_count:>5} {our_avg:>9.1f}元 {market_avg:>9.1f}元 {market_downloads:>10}")


def discover_trending():
    """发现热门类别和趋势"""
    market_data = load_market_data()
    
    if not market_data:
        print("无市场数据，请先运行 scan-skillhub")
        return
    
    print("\n" + "=" * 100)
    print(f"热门趋势发现 - 生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 100)
    
    # 1. 下载量趋势
    print(f"\n## 1. 下载量TOP 30 热门skill")
    top = sorted(market_data, key=lambda x: x.get('downloads', 0), reverse=True)[:30]
    print(f"  {'排名':>3} {'名称':<45} {'定价':>7} {'下载量':>8} {'类别'}")
    print(f"  {'-'*80}")
    for i, s in enumerate(top, 1):
        price_str = f"{s['price']:.1f}元" if s.get('price', 0) > 0 else "免费"
        cat = normalize_category(s.get('category', ''), s.get('name', ''), s.get('summary', ''))
        print(f"  {i:>3} {s.get('name', '')[:43]:<45} {price_str:>7} {s.get('downloads', 0):>8} {cat}")
    
    # 2. 新兴skill（最近创建）
    print(f"\n## 2. 最新上架skill")
    recent = sorted(market_data, key=lambda x: x.get('created_at', ''), reverse=True)[:20]
    for s in recent:
        price_str = f"{s['price']:.1f}元" if s.get('price', 0) > 0 else "免费"
        created = s.get('created_at', '')[:10]
        print(f"  {created} {s.get('name', '')[:40]:<42} {price_str:>7}")
    
    # 3. 高评分skill
    print(f"\n## 3. 高评分skill (评分>=4.0)")
    rated = [s for s in market_data if s.get('rating', 0) >= 4.0]
    rated.sort(key=lambda x: x.get('rating', 0), reverse=True)
    for s in rated[:20]:
        price_str = f"{s['price']:.1f}元" if s.get('price', 0) > 0 else "免费"
        print(f"  {s.get('rating', 0):>3.1f}★ {s.get('name', '')[:40]:<42} {price_str:>7} {s.get('rating_count', 0):>5}评")


def add_manual_entry(name: str, platform: str, price: float, downloads: int, calls: int, rating: float, category: str, summary: str = ''):
    """手动添加竞品数据"""
    manual_path = MARKET_DATA_DIR / "manual_entries.json"
    
    entries = []
    if manual_path.exists():
        with open(manual_path, 'r', encoding='utf-8') as f:
            entries = json.load(f)
    
    entries.append({
        'platform': platform,
        'name': name,
        'price': price,
        'downloads': downloads,
        'calls': calls,
        'rating': rating,
        'category': category,
        'summary': summary,
        'scanned_at': datetime.now().isoformat(),
    })
    
    with open(manual_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    
    print(f"已添加: {name} ({platform}) - {price}元, {downloads}下载")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    if cmd == 'scan-skillhub':
        scan_skillhub()
    elif cmd == 'scan-coze':
        print("Coze扫描功能开发中...")
    elif cmd == 'report':
        generate_report()
    elif cmd == 'recommend':
        generate_recommendations()
    elif cmd == 'compare':
        compare_with_competitors()
    elif cmd == 'trending':
        discover_trending()
    elif cmd == 'add' and len(sys.argv) > 7:
        add_manual_entry(sys.argv[2], sys.argv[3], float(sys.argv[4]), 
                        int(sys.argv[5]), int(sys.argv[6]), float(sys.argv[7]),
                        sys.argv[8] if len(sys.argv) > 8 else '',
                        sys.argv[9] if len(sys.argv) > 9 else '')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
