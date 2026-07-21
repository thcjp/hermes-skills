#!/usr/bin/env python3
"""
智能定价引擎 v1.0
================
基于全球skill市场研究数据(Coze/Zapier/GPT Store/Replit等)，
为每个skill自动计算最优定价。

定价模型: 基于类别×市场大小×复杂度×使用频次×竞品价格的多维矩阵

参考数据:
- Coze: 0.002-0.5元/次, 29-99元/月
- Zapier: $19.99-69/月
- Replit Bounties: $4.50-45/任务
- AI Agent To C: $0.01-50/月
- AI Agent To B: $100-5000/月
- SkillHub官方推荐: 10-100元

Usage:
    python pricing_engine.py price <skill_dir>          # 计算单个skill定价
    python pricing_engine.py price-all                   # 计算所有skill定价
    python pricing_engine.py report                      # 生成定价报告
    python pricing_engine.py update-db                   # 更新数据库中的定价
"""

import json
import re
import sqlite3
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# 导入统一配置（修复U-21硬编码路径、U-07事务保护、U-08备份机制）
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR,
    BACKUP_DIR, create_backup, is_paid_skill, BATCH_BACKUP_ENABLED
)

# ============ 定价矩阵 ============

# 类别基础价（基于市场研究）
# 参考: Coze图生视频0.5元/次, Bot调用0.002元/次, 专业Agent $0.10-10/次
CATEGORY_BASE_PRICE = {
    '文案创作': {'min': 1.0, 'max': 5.0, 'base': 3.0, 'rationale': '高频通用工具,大市场,低单价走量'},
    '数据分析': {'min': 5.0, 'max': 15.0, 'base': 9.9, 'rationale': '中频专业工具,中等市场'},
    'SEO优化': {'min': 5.0, 'max': 19.9, 'base': 9.9, 'rationale': '效果可量化,企业刚需'},
    '编程开发': {'min': 3.0, 'max': 15.0, 'base': 6.9, 'rationale': '开发者付费意愿高,但竞品多'},
    '设计创作': {'min': 3.0, 'max': 12.0, 'base': 6.9, 'rationale': '创作类工具,中等频次'},
    '营销推广': {'min': 5.0, 'max': 19.9, 'base': 12.0, 'rationale': '直接关联收入,付费意愿强'},
    '效率工具': {'min': 1.0, 'max': 5.0, 'base': 2.9, 'rationale': '高频低价值,走量为主'},
    '安全合规': {'min': 15.0, 'max': 50.0, 'base': 29.0, 'rationale': '低频高价值,专业壁垒高'},
    '翻译': {'min': 1.0, 'max': 5.0, 'base': 2.9, 'rationale': '高频通用,竞品多(DeepL等免费)'},
    '数据库': {'min': 5.0, 'max': 19.9, 'base': 9.9, 'rationale': '中频专业工具'},
    'API集成': {'min': 5.0, 'max': 19.9, 'base': 9.9, 'rationale': '集成类工具,企业需求'},
    '文件处理': {'min': 1.0, 'max': 5.0, 'base': 3.0, 'rationale': '高频通用工具'},
    '视频音频': {'min': 5.0, 'max': 19.9, 'base': 9.9, 'rationale': '算力消耗大,参考Coze 0.5元/次'},
    '通信消息': {'min': 3.0, 'max': 12.0, 'base': 5.9, 'rationale': '中频工具'},
    '项目管理': {'min': 5.0, 'max': 19.9, 'base': 9.9, 'rationale': '企业团队工具'},
    'AI模型': {'min': 3.0, 'max': 15.0, 'base': 6.9, 'rationale': 'AI辅助工具,中等频次'},
    '监控运维': {'min': 9.9, 'max': 29.0, 'base': 15.0, 'rationale': '企业级运维,低频高价值'},
    '电商': {'min': 5.0, 'max': 19.9, 'base': 12.0, 'rationale': '直接关联收入,付费意愿强'},
}

# 市场大小系数（市场越大，单价越低，走量）
MARKET_SIZE_FACTOR = {
    'large': 0.6,      # 大市场(文案/翻译/文件处理) → 降价走量
    'medium': 1.0,     # 中等市场 → 标准定价
    'small': 1.5,      # 小市场(安全/合规) → 提价补偿
    'niche': 2.0,      # 极小众市场 → 高溢价
}

# 复杂度系数（基于代码量、依赖数、流程步骤数）
COMPLEXITY_FACTOR = {
    'simple': 0.8,     # 单文件,无外部依赖
    'moderate': 1.0,   # 多文件,1-2个依赖
    'complex': 1.3,    # 多文件,3+依赖,多步骤
    'enterprise': 1.6, # 企业级,多系统集成
}

# 使用频次系数（高频低价,低频高价）
FREQUENCY_FACTOR = {
    'daily': 0.7,      # 每日使用 → 低价走量
    'weekly': 1.0,     # 每周使用 → 标准定价
    'monthly': 1.4,    # 每月使用 → 中高价
    'rare': 1.8,       # 偶尔使用 → 高价补偿
}

# 关键词分类
MARKETING_KEYWORDS = {
    '文案创作': ['文案', '写作', '内容创作', '爆款', '标题', '钩子', 'copywriting', 'writer', 'content'],
    '数据分析': ['分析', '报表', '统计', '可视化', '洞察', '数据', 'analytics', 'data', 'report', 'chart'],
    'SEO优化': ['SEO', '排名', '关键词', '搜索', '流量', '收录', 'search', 'rank', 'traffic'],
    '编程开发': ['代码', '编程', '开发', '调试', '测试', '部署', 'code', 'dev', 'debug', 'test', 'deploy'],
    '设计创作': ['设计', '海报', '图标', 'UI', '配色', '排版', 'design', 'poster', 'icon', 'theme'],
    '营销推广': ['营销', '推广', '广告', '转化', '获客', '裂变', 'marketing', 'ad', 'conversion', 'growth'],
    '效率工具': ['效率', '自动化', '批量', '快捷', '省时', '提速', 'automation', 'batch', 'productivity'],
    '安全合规': ['安全', '加密', '合规', '审计', '防护', '检测', 'security', 'crypto', 'compliance', 'audit'],
    '翻译': ['翻译', 'translate', '语言', 'language', '多语言', 'i18n'],
    '数据库': ['数据库', 'database', 'SQL', 'DB', '查询', 'query', '存储'],
    'API集成': ['API', '集成', 'integration', '接口', 'webhook', '连接'],
    '文件处理': ['文件', 'file', '文档', 'document', 'PDF', 'Word', 'Excel', '转换'],
    '视频音频': ['视频', 'video', '音频', 'audio', '音乐', 'music', '配音', 'voice'],
    '通信消息': ['消息', 'message', '通知', 'notify', '邮件', 'email', '短信', 'SMS'],
    '项目管理': ['项目', 'project', '任务', 'task', '管理', 'manage', '计划', 'plan'],
    'AI模型': ['AI', 'LLM', 'GPT', '模型', 'model', '智能', 'agent', '助手'],
    '监控运维': ['监控', 'monitor', '运维', 'ops', '日志', 'log', '告警', 'alert'],
    '电商': ['电商', 'ecommerce', '商品', 'product', '店铺', 'shop', '订单', 'order', '支付'],
}

# 市场大小判断关键词
LARGE_MARKET_KEYWORDS = ['文案', '写作', '翻译', '文件', '转换', '格式', '效率', '自动化', '批量']
NICHE_MARKET_KEYWORDS = ['安全', '合规', '审计', '加密', '漏洞', '渗透', '金融', '税务', '法律', '医疗']

# 使用频次判断关键词
DAILY_USE_KEYWORDS = ['文案', '写作', '翻译', '文件', '转换', '格式', '效率', '快捷', '自动']
RARE_USE_KEYWORDS = ['安全', '审计', '合规', '迁移', '部署', '监控', '灾备', '恢复']


def categorize_skill(slug, display_name, summary, description, body):
    """根据关键词分类skill"""
    all_text = f"{slug} {display_name} {summary} {description} {body[:500]}".lower()
    scores = {}
    for cat, keywords in MARKETING_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in all_text)
        if score > 0:
            scores[cat] = score
    
    return max(scores, key=scores.get) if scores else '效率工具'


def assess_market_size(category, slug, display_name, summary):
    """评估市场大小"""
    all_text = f"{slug} {display_name} {summary}".lower()
    
    # 检查小众市场关键词
    niche_score = sum(1 for kw in NICHE_MARKET_KEYWORDS if kw.lower() in all_text)
    if niche_score >= 2:
        return 'niche'
    if niche_score >= 1 or category in ['安全合规', '监控运维']:
        return 'small'
    
    # 检查大市场关键词
    large_score = sum(1 for kw in LARGE_MARKET_KEYWORDS if kw.lower() in all_text)
    if large_score >= 2 or category in ['文案创作', '翻译', '文件处理', '效率工具']:
        return 'large'
    
    return 'medium'


def assess_complexity(body, fm):
    """评估复杂度"""
    # 代码块数量
    code_blocks = len(re.findall(r'```[\s\S]*?```', body))
    # 依赖数量
    deps = len(re.findall(r'pip install|npm install|require\(|import ', body))
    # 步骤数量
    steps = len(re.findall(r'###\s*Step\s*\d|##\s*步骤|##\s*流程', body))
    # 文件行数
    lines = len(body.split('\n'))
    
    score = code_blocks * 2 + deps + steps * 3 + lines / 50
    
    if score >= 30 or '企业' in body or 'enterprise' in body.lower():
        return 'enterprise'
    elif score >= 15:
        return 'complex'
    elif score >= 5:
        return 'moderate'
    else:
        return 'simple'


def assess_frequency(category, slug, display_name, summary):
    """评估使用频次"""
    all_text = f"{slug} {display_name} {summary}".lower()
    
    rare_score = sum(1 for kw in RARE_USE_KEYWORDS if kw.lower() in all_text)
    if rare_score >= 2 or category in ['安全合规', '监控运维']:
        return 'rare'
    
    daily_score = sum(1 for kw in DAILY_USE_KEYWORDS if kw.lower() in all_text)
    if daily_score >= 2 or category in ['文案创作', '翻译', '文件处理', '效率工具']:
        return 'daily'
    
    if category in ['数据分析', '编程开发', '设计创作', '营销推广', '电商']:
        return 'weekly'
    
    return 'monthly'


def calculate_price(skill_md_path):
    """计算单个skill的最优定价"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    # 解析frontmatter
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        fm = parts[1] if len(parts) >= 3 else ''
        body = parts[2] if len(parts) >= 3 else content
    else:
        fm = ''
        body = content
    
    # 提取元数据
    slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    slug = slug_match.group(1).strip() if slug_match else skill_md_path.parent.name
    
    display_match = re.search(r'^displayName:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    display_name = display_match.group(1).strip() if display_match else slug
    
    summary_match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    summary = summary_match.group(1).strip() if summary_match else ''
    
    desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if desc_match:
        description = desc_match.group(1).strip()
    else:
        desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        description = desc_match.group(1).strip() if desc_match else ''
    
    edition_match = re.search(r'^edition:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    edition = edition_match.group(1).strip() if edition_match else ''

    # 检查license字段判断付费意图
    license_match = re.search(r'^license:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    license_val = license_match.group(1).strip() if license_match else ''

    # 判断是否为付费skill
    # 1. edition明确标注pro/paid/enterprise → 付费
    # 2. license为Proprietary/Commercial/Paid → 付费（即使edition缺失或为free）
    # 3. edition为free/community且license为MIT/Apache等开源协议 → 免费
    PAID_LICENSES = ['proprietary', 'commercial', 'paid', 'pro', 'enterprise', 'custom']
    OPEN_LICENSES = ['mit', 'apache', 'gpl', 'bsd', 'mpl', 'unlicense', 'cc0', 'cc-by']

    is_paid_intent = False
    if edition.lower() in ['pro', 'paid', 'enterprise', 'commercial', 'standard', 'premium']:
        is_paid_intent = True
    elif license_val and any(pl in license_val.lower() for pl in PAID_LICENSES):
        is_paid_intent = True
    elif edition.lower() in ['free', 'community', 'opensource', 'open-source']:
        is_paid_intent = False
    elif license_val and any(ol in license_val.lower() for ol in OPEN_LICENSES):
        is_paid_intent = False
    else:
        # 默认：有Proprietary license倾向则付费
        is_paid_intent = False

    # 确定edition显示值
    if not edition:
        edition = 'pro' if is_paid_intent else 'free'
    
    # 分类
    category = categorize_skill(slug, display_name, summary, description, body)
    market_size = assess_market_size(category, slug, display_name, summary)
    complexity = assess_complexity(body, fm)
    frequency = assess_frequency(category, slug, display_name, summary)
    
    # 计算定价
    base = CATEGORY_BASE_PRICE.get(category, {'base': 9.9, 'min': 1.0, 'max': 50.0, 'rationale': '默认定价'})
    market_factor = MARKET_SIZE_FACTOR[market_size]
    complexity_factor = COMPLEXITY_FACTOR[complexity]
    frequency_factor = FREQUENCY_FACTOR[frequency]
    
    # 基础价格 × 各系数
    raw_price = base['base'] * market_factor * complexity_factor * frequency_factor
    
    # 限定在类别价格范围内
    min_price = base['min']
    max_price = base['max']
    
    # 定价分层
    if not is_paid_intent:
        final_price = 0.0
        billing_type = 'free'
        tier = 'free'
    else:
        # 四舍五入到合理的价格点
        price_points = [0.99, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9, 7.9, 8.9, 9.9, 
                       12.0, 15.0, 19.0, 19.9, 25.0, 29.0, 39.0, 49.0, 69.0, 99.0]
        
        # 找到最接近的价格点
        final_price = min(price_points, key=lambda x: abs(x - raw_price))
        final_price = max(min_price, min(max_price, final_price))
        billing_type = 'per_call'
        
        # 分层
        if final_price <= 3.9:
            tier = 'standard'    # 高频走量
        elif final_price <= 9.9:
            tier = 'professional' # 中频创作
        elif final_price <= 19.9:
            tier = 'business'     # 中高频专业
        elif final_price <= 49.0:
            tier = 'premium'      # 低频高价值
        else:
            tier = 'enterprise'   # 企业级
    
    return {
        'slug': slug,
        'display_name': display_name,
        'edition': edition,
        'license': license_val,
        'is_paid': is_paid_intent,
        'tier': tier,
        'category': category,
        'market_size': market_size,
        'complexity': complexity,
        'frequency': frequency,
        'base_price': base['base'],
        'market_factor': market_factor,
        'complexity_factor': complexity_factor,
        'frequency_factor': frequency_factor,
        'raw_price': round(raw_price, 2),
        'final_price': final_price,
        'billing_type': billing_type,
        'rationale': f"{category}类, {market_size}市场, {complexity}复杂度, {frequency}频次, {tier}层 → {base['rationale']}",
        'price_range': f"{min_price}-{max_price}元",
    }


def cmd_price(skill_dir):
    """计算单个skill定价"""
    skill_md = Path(skill_dir) / "SKILL.md"
    if not skill_md.exists():
        skill_md = Path(skill_dir)
    
    result = calculate_price(skill_md)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 更新SKILL.md中的定价信息
    if result['final_price'] > 0:
        print(f"\n建议定价: {result['final_price']}元/次")
        print(f"定价依据: {result['rationale']}")


def cmd_price_all():
    """计算所有packaged skill的定价"""
    skills_dirs = [
        Path(r"d:\skills\packaged-skills\skillhub"),
        Path(r"d:\skills\opensource-skills\packaged"),
    ]
    
    all_results = []
    for skills_dir in skills_dirs:
        if not skills_dir.exists():
            continue
        for d in sorted(skills_dir.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                result = calculate_price(d / "SKILL.md")
                all_results.append(result)
    
    # 按价格排序
    all_results.sort(key=lambda x: x['final_price'], reverse=True)
    
    print(f"\n{'='*120}")
    print(f"智能定价报告 - {len(all_results)}个Packaged Skills")
    print(f"{'='*120}")
    print(f"{'Slug':<40} {'Tier':<14} {'类别':<12} {'市场':<8} {'复杂度':<10} {'频次':<10} {'定价':>8} {'范围'}")
    print(f"{'-'*120}")
    
    for r in all_results:
        print(f"{r['slug']:<40} {r['tier']:<14} {r['category']:<12} {r['market_size']:<8} {r['complexity']:<10} {r['frequency']:<10} {r['final_price']:>7.1f}元 {r['price_range']}")
    
    # 统计
    free_count = sum(1 for r in all_results if r['final_price'] == 0)
    paid_results = [r for r in all_results if r['final_price'] > 0]
    avg_price = sum(r['final_price'] for r in paid_results) / len(paid_results) if paid_results else 0
    
    print(f"\n{'='*60}")
    print(f"统计:")
    print(f"  免费版: {free_count}")
    print(f"  付费版: {len(paid_results)}")
    print(f"  平均价格: {avg_price:.1f}元/次")
    
    # Tier分布
    tier_counts = {}
    for r in paid_results:
        tier_counts[r['tier']] = tier_counts.get(r['tier'], 0) + 1
    print(f"\n分层分布:")
    for tier in ['standard', 'professional', 'business', 'premium', 'enterprise']:
        count = tier_counts.get(tier, 0)
        if count > 0:
            print(f"  {tier:<14}: {count:>3} ({count/len(paid_results)*100:.0f}%)")
    
    # 价格分布
    price_ranges = {'0.99-3.9': 0, '4.9-9.9': 0, '12-19.9': 0, '25-49': 0, '50+': 0}
    for r in paid_results:
        p = r['final_price']
        if p <= 3.9: price_ranges['0.99-3.9'] += 1
        elif p <= 9.9: price_ranges['4.9-9.9'] += 1
        elif p <= 19.9: price_ranges['12-19.9'] += 1
        elif p <= 49: price_ranges['25-49'] += 1
        else: price_ranges['50+'] += 1
    
    print(f"\n价格分布:")
    for rng, count in price_ranges.items():
        pct = count/len(paid_results)*100 if paid_results else 0
        bar = '█' * int(pct/2)
        print(f"  {rng:>10}元: {count:>3} ({pct:.0f}%) {bar}")
    
    # 保存结果
    output_path = REPORT_DIR / "pricing_report.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"\n定价报告保存到: {output_path}")


def cmd_apply():
    """将智能定价写回SKILL.md frontmatter（添加suggested_price和pricing_tier字段）
    
    修复U-07：添加备份机制，文件写入失败时回滚
    修复U-21：使用config路径常量
    """
    pricing_report = REPORT_DIR / "pricing_report.json"
    if not pricing_report.exists():
        print("请先运行 price-all 生成定价报告")
        return
    
    with open(pricing_report, 'r', encoding='utf-8') as f:
        all_results = json.load(f)
    
    # 构建slug到SKILL.md路径的映射（通过读取每个SKILL.md的slug字段）
    skills_dirs = [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR]
    
    slug_to_path = {}
    for sd in skills_dirs:
        if not sd.exists():
            continue
        for d in sd.iterdir():
            if d.is_dir() and (d / "SKILL.md").exists():
                content = (d / "SKILL.md").read_text(encoding='utf-8')
                if content.startswith('\ufeff'):
                    content = content[1:]
                if content.startswith('---'):
                    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                    if len(parts) >= 3:
                        fm = parts[1]
                        slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                        if slug_match:
                            slug_to_path[slug_match.group(1).strip()] = d / "SKILL.md"
    
    updated = 0
    skipped = 0
    failed = 0
    backups = {}
    
    # 备份阶段：先备份所有待修改的文件
    if BATCH_BACKUP_ENABLED:
        print("备份待修改的SKILL.md文件...")
        for result in all_results:
            slug = result['slug']
            skill_md = slug_to_path.get(slug)
            if skill_md and skill_md.exists():
                backup_path = create_backup(skill_md)
                if backup_path:
                    backups[slug] = backup_path
        print(f"已备份 {len(backups)} 个文件")
    
    # 写入阶段
    for result in all_results:
        slug = result['slug']
        skill_md = slug_to_path.get(slug)
        
        if not skill_md:
            skipped += 1
            continue
        
        try:
            content = skill_md.read_text(encoding='utf-8')
            if content.startswith('\ufeff'):
                content = content[1:]
            
            # 解析frontmatter
            if content.startswith('---'):
                parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                if len(parts) >= 3:
                    fm = parts[1]
                    body = parts[2]
                else:
                    skipped += 1
                    continue
            else:
                skipped += 1
                continue
            
            # 移除旧的定价字段
            fm = re.sub(r'^suggested_price:.*$\n?', '', fm, flags=re.MULTILINE)
            fm = re.sub(r'^pricing_tier:.*$\n?', '', fm, flags=re.MULTILINE)
            fm = re.sub(r'^pricing_rationale:.*$\n?', '', fm, flags=re.MULTILINE)
            
            # 添加新的定价字段
            price_str = f"{result['final_price']:.2f}" if result['final_price'] > 0 else "0"
            fm = fm.rstrip() + f"\nsuggested_price: \"{price_str}\""
            fm += f"\npricing_tier: \"{result['tier']}\""
            fm += f"\npricing_rationale: \"{result['rationale']}\""
            fm += "\n"
            
            # 重建文件
            new_content = f"---\n{fm.strip()}\n---\n{body.lstrip()}"
            skill_md.write_text(new_content, encoding='utf-8')
            updated += 1
        except Exception as e:
            print(f"  写入失败 {slug}: {e}")
            failed += 1
            # 回滚：从备份恢复
            if slug in backups:
                import shutil
                try:
                    shutil.copy2(backups[slug], skill_md)
                    print(f"  已从备份恢复 {slug}")
                except Exception:
                    print(f"  警告：恢复失败 {slug}")
    
    print(f"已更新 {updated} 个SKILL.md的定价字段, 跳过 {skipped} 个, 失败 {failed} 个")
    if failed > 0:
        print(f"失败文件可从 {BACKUP_DIR} 手动恢复")


def cmd_update_db():
    """更新数据库中的定价信息
    
    修复U-07：使用事务保护，全部成功才提交，失败回滚
    修复U-21：使用config路径常量
    """
    pricing_report = REPORT_DIR / "pricing_report.json"
    if not pricing_report.exists():
        print("请先运行 price-all 生成定价报告")
        return
    
    with open(pricing_report, 'r', encoding='utf-8') as f:
        all_results = json.load(f)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 确保列存在
    c.execute("PRAGMA table_info(skills)")
    columns = [row[1] for row in c.fetchall()]
    
    for col, col_type in [('suggested_price', 'REAL'), ('pricing_category', 'TEXT'), 
                          ('pricing_rationale', 'TEXT'), ('pricing_tier', 'TEXT'),
                          ('is_paid', 'INTEGER')]:
        if col not in columns:
            c.execute(f"ALTER TABLE skills ADD COLUMN {col} {col_type}")
    
    conn.commit()
    
    # 使用事务保护（修复U-07：全部成功才提交）
    updated = 0
    try:
        for result in all_results:
            c.execute("""
                UPDATE skills 
                SET suggested_price = ?, pricing_category = ?, pricing_rationale = ?, 
                    pricing_tier = ?, is_paid = ?
                WHERE slug = ?
            """, (result['final_price'], result['category'], result['rationale'],
                  result['tier'], 1 if result['is_paid'] else 0, result['slug']))
            
            if c.rowcount > 0:
                updated += 1
        
        conn.commit()
        print(f"已更新 {updated} 个skill的定价信息")
    except Exception as e:
        conn.rollback()
        print(f"数据库更新失败，已回滚: {e}")
    finally:
        conn.close()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    if cmd == 'price' and len(sys.argv) > 2:
        cmd_price(sys.argv[2])
    elif cmd == 'price-all':
        cmd_price_all()
    elif cmd == 'report':
        cmd_price_all()
    elif cmd == 'apply':
        cmd_apply()
    elif cmd == 'update-db':
        cmd_update_db()
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
