#!/usr/bin/env python3
"""
定价模型校准 v34.0 任务3 (P1) - 生产脚本
==========================================
6维度评分模型: complexity + frequency + value + cost + uniqueness - alternative - penalty
校准阈值: >=18→L4, >=13→L3, >=8→L2, <8→L1
新增LOW_VALUE_KEYWORDS降低简单工具评分
slug-based简单工具惩罚

操作:
1. 评分全部付费skill
2. 更新DB skills表 (pricing_tier, pricing_model, suggested_price, is_paid)
3. 更新DB pricing表 (edition, price_amount, price_model)
4. 更新SKILL.md frontmatter (suggested_price, pricing_tier, pricing_model)
5. 报告分布
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
# === End Phase 1 ===

import re
import sqlite3
import shutil
from pathlib import Path
from datetime import datetime
from collections import Counter

# DB_PATH imported from config

# ============ 评分维度关键词 ============

HIGH_VALUE_KEYWORDS = [
    '企业', 'enterprise', '商业', '营收', '收入', '转化', 'ROI', '安全', '合规', '审计',
    '金融', '支付', '加密', '区块链', 'blockchain', 'crypto', 'AI', 'LLM', 'GPT', 'agent',
    '自动化', '集成', 'integration', 'API', '数据库', 'database', 'cloud', '云', 'k8s',
    'kubernetes', 'docker', '监控', 'monitor', '运维', 'devops', 'CI/CD', '部署', 'deploy',
    '机器学习', '深度学习', '神经网络', 'NLP', '计算机视觉', '推荐系统', '大数据', '实时',
    '高并发', '分布式', '微服务', '架构', 'pipeline', '工作流', 'workflow', '编排',
    '安全审计', '漏洞', '渗透', 'pentest', '防火墙', 'firewall', '加密', 'encryption',
]

# 低价值关键词 (含v34.0新增基础工具关键词)
LOW_VALUE_KEYWORDS = [
    '格式化', 'format', 'beautify', 'prettify', 'lint', '计数', 'count',
    '排序', 'sort', '过滤', 'filter', '搜索', 'search', '替换', 'replace',
    '转换', 'convert', 'transform', '解析', 'parse', '验证', 'validate',
    '生成', 'generate', '模板', 'template', '示例', 'example', 'demo',
    '基础', 'basic', 'simple', '简单', '入门', 'beginner', 'starter',
    '工具', 'tool', 'utility', 'helper', '助手', '辅助',
    # v34.0新增基础工具关键词
    '随机', '生成器', 'generator', '计算器', 'calculator',
    '合并', 'merge', '分割', 'split', '压缩', 'compress', 'zip',
    '美化', '校验', 'checksum', '解码', 'decode', '编码', 'encode',
    '计数器', 'counter', '清单', 'checklist', '速查', 'cheat',
]

ALTERNATIVE_KEYWORDS = [
    '格式化', 'format', 'beautify', 'prettify', 'lint', '计数', 'count',
    '排序', 'sort', '过滤', 'filter', '转换', 'convert', 'transform',
    '解析', 'parse', '验证', 'validate', '生成器', 'generator', '计算器',
    'calculator', '合并', 'merge', '分割', 'split', '压缩', 'compress',
    '美化', '校验', '解码', 'decode', '编码', 'encode', 'base64', 'hex',
    'json', 'yaml', 'csv', 'xml', 'markdown', 'text', 'txt',
    'converter', 'formatter', 'parser', 'validator', '随机', 'random',
    'password', '密码', 'uuid', 'hash', '基础', 'basic', 'simple', '简单',
]

HIGH_FREQUENCY_KEYWORDS = [
    '每日', '日常', 'daily', '实时', 'real-time', '自动', 'auto', '批量', 'batch',
    '监控', 'monitor', '通知', 'notify', '提醒', 'remind', '定时', 'schedule',
    'cron', '定时任务', '同步', 'sync', '推送', 'push', '订阅', 'subscribe',
    '高频', '常用', '必备', '核心', 'essential', 'core',
]

LOW_FREQUENCY_KEYWORDS = [
    '迁移', 'migrate', '灾备', 'disaster', '恢复', 'recover', '归档', 'archive',
    '审计', 'audit', '合规', 'compliance', '一次', '偶尔', 'rare', '初始化', 'init',
]

HIGH_COST_KEYWORDS = [
    'API', '密钥', 'key', 'token', '认证', 'auth', 'oauth', '数据库', 'database',
    'SQL', '云服务', 'cloud', 'docker', 'kubernetes', 'k8s', '部署', 'deploy',
    '集成', 'integration', 'webhook', 'SDK', '框架', 'framework', '服务器', 'server',
    '集群', 'cluster', '分布式', 'distributed', '微服务', 'microservice',
    '机器学习', 'ML', '深度学习', 'DL', '模型', 'model', '训练', 'train',
    '实时', 'stream', '流式', 'pipeline', 'ETL', '消息队列', 'queue', 'kafka',
]

UNIQUENESS_KEYWORDS = [
    '专有', 'proprietary', '独家', '专利', 'patent', '唯一', '稀缺', 'rare',
    '专业', 'professional', '企业级', 'enterprise', 'blockchain', '区块链',
    '加密', 'crypto', '安全', 'security', '审计', 'audit', '合规', 'compliance',
    '金融', 'finance', '医疗', 'healthcare', '法律', 'legal', '税务', 'tax',
    'AI', 'LLM', 'GPT', 'agent', '智能',
    '区块链', '智能合约', 'smart-contract', 'DeFi', 'NFT',
]

SIMPLE_TOOL_SLUG_PATTERNS = [
    'format', 'beautify', 'lint', 'parse', 'validate', 'convert', 'transform',
    'merge', 'split', 'compress', 'encode', 'decode', 'count', 'sort', 'filter',
    'random', 'generator', 'calculator', 'checksum', 'hash', 'uuid', 'password',
    'base64', 'hex', 'json', 'yaml', 'csv', 'xml', 'markdown-formatter',
    'beautifier', 'formatter', 'parser', 'validator', 'converter',
]


# ============ 评分函数 ============

def parse_frontmatter(content):
    if content.startswith('\ufeff'):
        content = content[1:]
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return '', content


def extract_field(fm, field):
    m = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(rf'{field}:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if m:
        return m.group(1).strip()
    return ''


def score_complexity(body):
    code_blocks = len(re.findall(r'```[\s\S]*?```', body))
    deps = len(re.findall(r'pip install|npm install|require\(|import |from ', body))
    steps = len(re.findall(r'###\s*Step\s*\d|##\s*步骤|##\s*流程|##\s*使用|##\s*核心|##\s*功能', body))
    lines = len(body.split('\n'))
    tables = len(re.findall(r'^\|.*\|', body, re.MULTILINE))
    raw = code_blocks * 1.2 + deps * 0.4 + steps * 1.0 + lines / 120 + tables * 0.2
    if raw >= 18: return 5
    elif raw >= 11: return 4
    elif raw >= 6: return 3
    elif raw >= 3: return 2
    elif raw >= 1: return 1
    else: return 0


def score_frequency(text):
    text_lower = text.lower()
    high_score = sum(1 for kw in HIGH_FREQUENCY_KEYWORDS if kw.lower() in text_lower)
    low_score = sum(1 for kw in LOW_FREQUENCY_KEYWORDS if kw.lower() in text_lower)
    raw = high_score - low_score * 0.5
    if raw >= 4: return 5
    elif raw >= 3: return 4
    elif raw >= 2: return 3
    elif raw >= 1: return 2
    elif raw >= 0: return 1
    else: return 0


def score_value(text):
    text_lower = text.lower()
    high_score = sum(1 for kw in HIGH_VALUE_KEYWORDS if kw.lower() in text_lower)
    low_score = sum(1 for kw in LOW_VALUE_KEYWORDS if kw.lower() in text_lower)
    raw = high_score - low_score * 0.6
    if raw >= 6: return 5
    elif raw >= 4: return 4
    elif raw >= 2: return 3
    elif raw >= 1: return 2
    elif raw >= 0: return 1
    else: return 0


def score_cost(text):
    text_lower = text.lower()
    cost_score = sum(1 for kw in HIGH_COST_KEYWORDS if kw.lower() in text_lower)
    if cost_score >= 6: return 5
    elif cost_score >= 4: return 4
    elif cost_score >= 3: return 3
    elif cost_score >= 2: return 2
    elif cost_score >= 1: return 1
    else: return 0


def score_uniqueness(text):
    text_lower = text.lower()
    uniq_score = sum(1 for kw in UNIQUENESS_KEYWORDS if kw.lower() in text_lower)
    if uniq_score >= 7: return 5
    elif uniq_score >= 5: return 4
    elif uniq_score >= 3: return 3
    elif uniq_score >= 2: return 2
    elif uniq_score >= 1: return 1
    else: return 0


def score_alternative(text):
    text_lower = text.lower()
    alt_score = sum(1 for kw in ALTERNATIVE_KEYWORDS if kw.lower() in text_lower)
    if alt_score >= 8: return 5
    elif alt_score >= 6: return 4
    elif alt_score >= 4: return 3
    elif alt_score >= 2: return 2
    elif alt_score >= 1: return 1
    else: return 0


def simple_tool_penalty(slug):
    slug_lower = slug.lower()
    for pattern in SIMPLE_TOOL_SLUG_PATTERNS:
        if slug_lower == pattern or slug_lower.startswith(pattern + '-') or slug_lower.endswith('-' + pattern):
            return 4
    matches = sum(1 for p in SIMPLE_TOOL_SLUG_PATTERNS if p in slug_lower)
    if matches >= 2:
        return 3
    return 0


def calculate_pricing_score(slug, display_name, summary, description, body):
    all_text = f"{slug} {display_name} {summary} {description} {body[:2000]}"
    complexity = score_complexity(body)
    frequency = score_frequency(all_text)
    value = score_value(all_text)
    cost = score_cost(all_text)
    uniqueness = score_uniqueness(all_text)
    alternative = score_alternative(all_text)
    penalty = simple_tool_penalty(slug)
    total = complexity + frequency + value + cost + uniqueness - alternative - penalty
    return {
        'complexity': complexity, 'frequency': frequency, 'value': value,
        'cost': cost, 'uniqueness': uniqueness, 'alternative': alternative,
        'penalty': penalty, 'total': total,
    }


def calculate_pricing_score_slug_only(slug):
    """对没有SKILL.md的skill,仅基于slug评分"""
    all_text = slug.replace('-', ' ')
    complexity = max(1, score_complexity(all_text))
    frequency = score_frequency(all_text)
    value = score_value(all_text)
    cost = score_cost(all_text)
    uniqueness = score_uniqueness(all_text)
    alternative = score_alternative(all_text)
    penalty = simple_tool_penalty(slug)
    total = complexity + frequency + value + cost + uniqueness - alternative - penalty
    return {
        'complexity': complexity, 'frequency': frequency, 'value': value,
        'cost': cost, 'uniqueness': uniqueness, 'alternative': alternative,
        'penalty': penalty, 'total': total,
    }


# ============ 阈值与价格映射 ============

# 校准后阈值 (基于dry-run累积分布校准)
TIER_THRESHOLDS = {'L4': 18, 'L3': 13, 'L2': 8, 'L1': 0}

TIER_PRICE_MAP = {
    'L1': {'price': 9.9, 'model': 'per_use', 'name': 'L1-入门级', 'desc': '基础工具'},
    'L2': {'price': 19.9, 'model': 'per_use', 'name': 'L2-标准级', 'desc': '标准工具'},
    'L3': {'price': 29.9, 'model': 'per_use', 'name': 'L3-专业级', 'desc': '专业工具'},
    'L4': {'price': 99.9, 'model': 'monthly', 'name': 'L4-企业级', 'desc': '企业级'},
}


def score_to_tier(score):
    if score >= TIER_THRESHOLDS['L4']: return 'L4'
    elif score >= TIER_THRESHOLDS['L3']: return 'L3'
    elif score >= TIER_THRESHOLDS['L2']: return 'L2'
    else: return 'L1'


# ============ 路径映射 ============

def build_slug_to_path():
    slug_to_path = {}
    skills_dirs = [
        Path(r'd:\skills\packaged-skills\skillhub'),
        Path(r'd:\skills\opensource-skills\packaged'),
    ]
    for sd in skills_dirs:
        if not sd.exists(): continue
        for d in sorted(sd.iterdir()):
            if d.is_dir() and (d / 'SKILL.md').exists():
                content = (d / 'SKILL.md').read_text(encoding='utf-8')
                if content.startswith('\ufeff'): content = content[1:]
                if content.startswith('---'):
                    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                    if len(parts) >= 3:
                        fm = parts[1]
                        m = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                        if m:
                            slug_to_path[m.group(1).strip()] = d / 'SKILL.md'
    return slug_to_path


# ============ SKILL.md frontmatter 更新 ============

def update_skill_md_frontmatter(skill_md_path, tier, price, model):
    """更新SKILL.md frontmatter中的定价字段"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    if not content.startswith('---'):
        return False

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return False

    fm = parts[1]
    body = parts[2]

    # 移除旧的定价字段
    fm = re.sub(r'^#?\s*定价元数据\s*\n?', '', fm, flags=re.MULTILINE)
    fm = re.sub(r'^suggested_price:.*$\n?', '', fm, flags=re.MULTILINE)
    fm = re.sub(r'^pricing_tier:.*$\n?', '', fm, flags=re.MULTILINE)
    fm = re.sub(r'^pricing_model:.*$\n?', '', fm, flags=re.MULTILINE)
    fm = re.sub(r'^pricing_rationale:.*$\n?', '', fm, flags=re.MULTILINE)

    tier_name = TIER_PRICE_MAP[tier]['name']
    price_str = f"{price} CNY/{model}"

    # 添加新的定价字段
    fm = fm.rstrip() + f"\n# 定价元数据"
    fm += f"\nsuggested_price: \"{price_str}\""
    fm += f"\npricing_tier: \"{tier_name}\""
    fm += f"\npricing_model: \"{model}\""
    fm += "\n"

    new_content = f"---\n{fm.strip()}\n---\n{body.lstrip()}"
    skill_md_path.write_text(new_content, encoding='utf-8')
    return True


# ============ 主流程 ============

def main():
    print("=" * 70)
    print("定价模型校准 v34.0 任务3 (P1)")
    print("=" * 70)

    # 1. 构建路径映射
    slug_to_path = build_slug_to_path()
    print(f"Packaged SKILL.md: {len(slug_to_path)}")

    # 2. 从DB获取所有需要定价的skill
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("""
        SELECT id, slug, pricing_tier, pricing_model, suggested_price, edition, local_path
        FROM skills
        WHERE slug NOT LIKE '%-free'
          AND pricing_tier != 'free'
    """)
    db_skills = c.fetchall()
    print(f"DB中需要重新定价的skill: {len(db_skills)}")

    # 3. 评分
    results = []
    missing_md = []
    for row in db_skills:
        slug = row['slug']
        skill_md = slug_to_path.get(slug)
        skill_md_str = None

        if not skill_md:
            lp = row['local_path'] or ''
            if lp:
                candidate = Path(lp) / 'SKILL.md'
                if candidate.exists():
                    skill_md = candidate
                    skill_md_str = str(candidate)

        if skill_md and skill_md.exists():
            skill_md_str = str(skill_md)
            content = skill_md.read_text(encoding='utf-8')
            fm, body = parse_frontmatter(content)
            display_name = extract_field(fm, 'displayName')
            summary = extract_field(fm, 'summary')
            description = extract_field(fm, 'description')
            scores = calculate_pricing_score(slug, display_name, summary, description, body)
        else:
            # 没有SKILL.md,仅基于slug评分
            scores = calculate_pricing_score_slug_only(slug)
            missing_md.append(slug)

        new_tier = score_to_tier(scores['total'])
        price_info = TIER_PRICE_MAP[new_tier]

        results.append({
            'id': row['id'],
            'slug': slug,
            'old_tier': row['pricing_tier'],
            'new_tier': new_tier,
            'total_score': scores['total'],
            'scores': scores,
            'price': price_info['price'],
            'model': price_info['model'],
            'tier_name': price_info['name'],
            'skill_md': skill_md_str,
        })

    total = len(results)
    print(f"成功评分: {total}, 缺失SKILL.md(仅slug评分): {len(missing_md)}")

    # 4. 更新DB (事务保护)
    print("\n--- 更新DB ---")
    db_updated = 0
    pricing_updated = 0
    pricing_inserted = 0
    try:
        for r in results:
            # 更新skills表
            c.execute("""
                UPDATE skills
                SET pricing_tier = ?, pricing_model = ?, suggested_price = ?, is_paid = 1
                WHERE id = ?
            """, (r['new_tier'], r['model'], r['price'], r['id']))
            if c.rowcount > 0:
                db_updated += 1

            # 更新/插入pricing表
            c.execute("SELECT id FROM pricing WHERE skill_id = ?", (r['id'],))
            pricing_row = c.fetchone()
            now = datetime.now().strftime('%Y-%m-%d')
            if pricing_row:
                c.execute("""
                    UPDATE pricing
                    SET edition = ?, price_model = ?, price_amount = ?, price_currency = 'CNY'
                    WHERE skill_id = ?
                """, (r['new_tier'], r['model'], r['price'], r['id']))
                pricing_updated += 1
            else:
                c.execute("""
                    INSERT INTO pricing (skill_id, edition, price_model, price_amount, price_currency, effective_date)
                    VALUES (?, ?, ?, ?, 'CNY', ?)
                """, (r['id'], r['new_tier'], r['model'], r['price'], now))
                pricing_inserted += 1

        conn.commit()
        print(f"  skills表更新: {db_updated}")
        print(f"  pricing表更新: {pricing_updated}, 新增: {pricing_inserted}")
    except Exception as e:
        conn.rollback()
        print(f"  DB更新失败,已回滚: {e}")
        conn.close()
        return

    # 5. 更新SKILL.md frontmatter
    print("\n--- 更新SKILL.md ---")
    md_updated = 0
    md_failed = 0
    md_skipped = 0
    for r in results:
        if not r['skill_md']:
            md_skipped += 1
            continue
        try:
            skill_md_path = Path(r['skill_md'])
            if update_skill_md_frontmatter(skill_md_path, r['new_tier'], r['price'], r['model']):
                md_updated += 1
            else:
                md_failed += 1
        except Exception as e:
            print(f"  SKILL.md更新失败 {r['slug']}: {e}")
            md_failed += 1

    print(f"  SKILL.md更新: {md_updated}, 失败: {md_failed}, 跳过(无文件): {md_skipped}")

    conn.close()

    # 6. 报告分布
    print("\n" + "=" * 70)
    print("最终分布报告")
    print("=" * 70)

    tier_counts = Counter(r['new_tier'] for r in results)
    print(f"\n付费skill分布 (共{total}个):")
    print(f"  {'层级':<8} {'数量':>6} {'占比':>8} {'目标':>8} {'偏差':>8}")
    print(f"  {'-'*40}")
    for tier in ['L1', 'L2', 'L3', 'L4']:
        cnt = tier_counts.get(tier, 0)
        pct = cnt / total * 100
        target = {'L1': 10, 'L2': 30, 'L3': 40, 'L4': 20}[tier]
        diff = pct - target
        status = 'OK' if abs(diff) < 5 else 'XX'
        print(f"  {tier:<8} {cnt:>6} {pct:>7.1f}% {target:>7}% {diff:>+7.1f}% {status}")

    # 含-free suffix skill的全局分布
    print(f"\n全局分布 (含-free suffix skill, 未重新定价):")
    conn2 = sqlite3.connect(DB_PATH)
    c2 = conn2.cursor()
    c2.execute("SELECT pricing_tier, COUNT(*) FROM skills GROUP BY pricing_tier ORDER BY pricing_tier")
    all_total = 0
    all_dist = {}
    for tier, cnt in c2.fetchall():
        all_dist[tier] = cnt
        all_total += cnt
    print(f"  {'层级':<8} {'数量':>6} {'占比':>8}")
    print(f"  {'-'*30}")
    for tier in ['L1', 'L2', 'L3', 'L4', 'free']:
        cnt = all_dist.get(tier, 0)
        pct = cnt / all_total * 100 if all_total else 0
        print(f"  {tier:<8} {cnt:>6} {pct:>7.1f}%")
    print(f"  {'总计':<8} {all_total:>6}")
    conn2.close()

    # 迁移矩阵
    print(f"\n层级迁移矩阵 (行=旧层级, 列=新层级):")
    print(f"  {'':>6} {'L1':>6} {'L2':>6} {'L3':>6} {'L4':>6} {'总计':>6}")
    for old_tier in ['L1', 'L2', 'L3', 'L4']:
        row_results = [r for r in results if r['old_tier'] == old_tier]
        counts = Counter(r['new_tier'] for r in row_results)
        print(f"  {old_tier:>6} {counts.get('L1',0):>6} {counts.get('L2',0):>6} {counts.get('L3',0):>6} {counts.get('L4',0):>6} {len(row_results):>6}")

    # 阈值信息
    print(f"\n校准阈值:")
    print(f"  L4: score >= {TIER_THRESHOLDS['L4']} (企业级, 99.9 CNY/monthly)")
    print(f"  L3: score >= {TIER_THRESHOLDS['L3']} (专业级, 29.9 CNY/per_use)")
    print(f"  L2: score >= {TIER_THRESHOLDS['L2']} (标准级, 19.9 CNY/per_use)")
    print(f"  L1: score <  {TIER_THRESHOLDS['L2']} (入门级, 9.9 CNY/per_use)")

    # 各维度平均分
    print(f"\n各维度平均分:")
    for dim in ['complexity', 'frequency', 'value', 'cost', 'uniqueness', 'alternative', 'penalty', 'total']:
        avg = sum(r['scores'][dim] for r in results) / total
        print(f"  {dim:>14}: {avg:.2f}")

    print(f"\n完成! DB备份: d:\\skills\\tools\\backups\\skill-registry_pre_pricing_v34_backup.db")


if __name__ == '__main__':
    main()
