#!/usr/bin/env python3
"""
Round 30 Task 2: 源skill升级检查机制 (V141 D2: SQLite+SHA-256迁移)
==================================
功能:
1. 对比本地源skill版本与数据库记录版本
2. 检查ClawHub/GitHub是否有更新
3. 标记needs_upgrade
4. 生成升级报告

V141 D2变更:
  - 数据源: daily_sync JSON → SQLite upgrade_tracking表
  - 哈希算法: MD5 → SHA-256
  - 权威源: SQLite为唯一权威源(与orchestrator一致)

使用方式:
    python upgrade_checker.py check          # 执行升级检查
    python upgrade_checker.py report         # 生成升级报告
    python upgrade_checker.py mark-upgraded <slug> [slug...]  # 标记已升级
"""

import json, hashlib  # V124 W2: re移除; V141 D2: hashlib保留(SHA-256)
from pathlib import Path

# === Phase 1: 统一配置导入 ===
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, get_timestamp, CLAWHUB_DOWNLOADED_DIR, DIFFERENTIATED_DIR, DATA_DIR  # V124 W1: 合并重复import
# === End Phase 1 ===

# V141 D2: 从JSON存储迁移到SQLite
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_core import db as db_module

NOW = get_timestamp()  # V101 W4: 统一时间戳
REPORT_FILE = DATA_DIR / "reports" / "upgrade_report.json"

def read_frontmatter(path):
    """V100 W1: wrapper调用skill_core.parser.parse_frontmatter_from_file
    
    保留原签名(path→dict)兼容现有调用方
    """
    from skill_core.parser import parse_frontmatter_from_file
    p = Path(path)
    skill_md = p / "SKILL.md" if p.is_dir() else p
    if not skill_md.exists():
        return {}
    try:
        result = parse_frontmatter_from_file(skill_md)
        return result.get('fields', {})
    except Exception:  # [V130 A1] 宽泛捕获: frontmatter解析可能因文件缺失/格式等多种原因失败
        return {}

# V141 D2: MD5→SHA-256 (与content_dedup算法一致,但用途不同:
#   content_dedup用于内容去重(接收content字符串),
#   本函数用于文件变更检测(接收path路径))
def compute_content_hash(path):
    """计算SKILL.md的内容hash (V141 D2: SHA-256)"""
    p = Path(path)
    skill_md = p / "SKILL.md" if p.is_dir() else p
    if not skill_md.exists():
        return None
    try:
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
    except (OSError, UnicodeDecodeError):  # V126 W2: 替换裸except(TD-182)
        return None

def find_all_skills(base_path):
    """递归扫描目录下所有SKILL.md"""
    result = {}
    base = Path(base_path)
    if not base.exists():
        return result
    for skill_md in base.rglob("SKILL.md"):  # V126 W7: os.walk→Path.rglob(TD-187)
        root = skill_md.parent
        slug = root.name
        result[slug] = str(root)
    return result

def _get_upgrade_tracking(c, slug):
    """从SQLite读取upgrade_tracking记录(V141 D2)"""
    c.execute("""
        SELECT source_version, local_version, content_hash,
               needs_upgrade, upgrade_reason, last_checked, last_upgraded
        FROM upgrade_tracking WHERE slug = ?
    """, (slug,))
    row = c.fetchone()
    if not row:
        return {}
    return {
        'source_version': row[0] or '',
        'local_version': row[1] or '',
        'content_hash': row[2] or '',
        'needs_upgrade': bool(row[3]),
        'upgrade_reason': row[4] or '',
        'last_checked': row[5] or '',
        'last_upgraded': row[6] or '',
    }

def _upsert_upgrade_tracking(c, skill_id, slug, ut):
    """写入或更新upgrade_tracking记录(V141 D2)"""
    c.execute("""
        INSERT OR REPLACE INTO upgrade_tracking
            (skill_id, slug, source_version, local_version, content_hash,
             needs_upgrade, upgrade_reason, last_checked, last_upgraded)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        skill_id, slug,
        ut.get('source_version', ''),
        ut.get('local_version', ''),
        ut.get('content_hash', ''),
        1 if ut.get('needs_upgrade') else 0,
        ut.get('upgrade_reason', ''),
        ut.get('last_checked', ''),
        ut.get('last_upgraded', ''),
    ))

def cmd_check():
    """执行升级检查 (V141 D2: SQLite数据源)"""
    conn = db_module.get_db()
    c = conn.cursor()

    # 确保upgrade_tracking表存在
    c.execute("""
        CREATE TABLE IF NOT EXISTS upgrade_tracking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            slug TEXT NOT NULL,
            source_version TEXT,
            local_version TEXT,
            content_hash TEXT,
            needs_upgrade INTEGER DEFAULT 0,
            upgrade_reason TEXT,
            last_checked TEXT,
            last_upgraded TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id),
            UNIQUE(slug)
        )
    """)

    # 查询所有skill
    c.execute("""
        SELECT id, slug, current_version, source, source_slug, local_path
        FROM skills
    """)
    all_skills = c.fetchall()

    # 扫描源skill目录
    clawhub_source = find_all_skills(str(CLAWHUB_DOWNLOADED_DIR.parent))
    opensource_source = find_all_skills(str(OPENSOURCE_SKILLS_DIR.parent))

    # 扫描生产skill目录
    packaged = find_all_skills(str(PACKAGED_SKILLS_DIR))
    diff_skills = find_all_skills(str(DIFFERENTIATED_DIR))
    
    print(">>> 执行升级检查...")
    
    checked = 0
    needs_upgrade = 0
    up_to_date = 0
    missing_file = 0
    needs_upgrade_list = []
    
    for row in all_skills:
        skill_id = row[0]
        slug = row[1] or ''
        current_db_version = row[2] or '1.0.0'
        source = row[3] or ''
        source_slug = row[4] or ''
        local_path = row[5] or ''

        if not slug:
            continue

        # 判断是否为源skill (有source_slug或source非空)
        is_source = bool(source_slug) or source in ('clawhub', 'github')

        if not is_source:
            # 生产skill: 检查版本变更
            src_path = local_path
            if not src_path or not Path(src_path).exists():
                if slug in packaged:
                    src_path = packaged[slug]
                elif slug in diff_skills:
                    src_path = diff_skills[slug]

            if src_path and Path(src_path).exists():
                fm = read_frontmatter(src_path)
                current_version = fm.get("version", "1.0.0")
                current_hash = compute_content_hash(src_path)

                ut = _get_upgrade_tracking(c, slug)
                old_hash = ut.get('content_hash', '')

                ut['local_version'] = current_version
                ut['last_checked'] = NOW
                ut['content_hash'] = current_hash or ''

                if old_hash and old_hash != current_hash:
                    ut['needs_upgrade'] = True
                    ut['upgrade_reason'] = "本地文件已变更"
                    needs_upgrade += 1
                    needs_upgrade_list.append({
                        'slug': slug, 'is_source': False,
                        'reason': ut['upgrade_reason'],
                        'source_version': '',
                        'local_version': current_version,
                    })
                else:
                    ut['needs_upgrade'] = False
                    up_to_date += 1

                _upsert_upgrade_tracking(c, skill_id, slug, ut)
                checked += 1
            else:
                missing_file += 1
            continue
        
        # 源skill升级检查
        src_path = local_path
        if not src_path or not Path(src_path).exists():
            if slug in clawhub_source:
                src_path = clawhub_source[slug]
            elif slug in opensource_source:
                src_path = opensource_source[slug]
        
        if src_path and Path(src_path).exists():
            fm = read_frontmatter(src_path)
            current_version = fm.get("version", "")
            current_hash = compute_content_hash(src_path)
            
            ut = _get_upgrade_tracking(c, slug)
            old_version = ut.get('source_version', '')
            old_hash = ut.get('content_hash', '')
            
            ut['source_version'] = current_version
            ut['last_checked'] = NOW
            ut['content_hash'] = current_hash or ''
            
            if old_hash and old_hash != current_hash:
                ut['needs_upgrade'] = True
                ut['upgrade_reason'] = "源skill文件已变更"
                needs_upgrade += 1
                needs_upgrade_list.append({
                    'slug': slug, 'is_source': True,
                    'reason': ut['upgrade_reason'],
                    'source_version': current_version,
                    'local_version': '',
                })
            elif old_version and current_version and old_version != current_version:
                ut['needs_upgrade'] = True
                ut['upgrade_reason'] = f"版本变更: {old_version} -> {current_version}"
                needs_upgrade += 1
                needs_upgrade_list.append({
                    'slug': slug, 'is_source': True,
                    'reason': ut['upgrade_reason'],
                    'source_version': current_version,
                    'local_version': '',
                })
            else:
                ut['needs_upgrade'] = False
                up_to_date += 1
            
            _upsert_upgrade_tracking(c, skill_id, slug, ut)
            checked += 1
        else:
            missing_file += 1
    
    conn.commit()
    conn.close()
    
    print(f"    检查完成:")
    print(f"    已检查: {checked}")
    print(f"    需升级: {needs_upgrade}")
    print(f"    最新版: {up_to_date}")
    print(f"    文件缺失: {missing_file}")
    
    # 生成报告(JSON, 向后兼容)
    report = {
        "check_time": NOW,
        "summary": {
            "checked": checked,
            "needs_upgrade": needs_upgrade,
            "up_to_date": up_to_date,
            "missing_file": missing_file,
        },
        "needs_upgrade_list": needs_upgrade_list,
    }
    
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"    报告已保存: {REPORT_FILE}")

def cmd_report():
    """生成升级报告"""
    if not REPORT_FILE.exists():
        print("请先运行: python upgrade_checker.py check")
        return
    
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        report = json.load(f)
    
    print(f"升级检查报告 ({report['check_time']})")
    print(f"{'='*55}")
    s = report["summary"]
    print(f"已检查: {s['checked']}")
    print(f"需升级: {s['needs_upgrade']}")
    print(f"最新版: {s['up_to_date']}")
    print(f"文件缺失: {s['missing_file']}")
    
    if report["needs_upgrade_list"]:
        print(f"\n需升级的skill ({len(report['needs_upgrade_list'])}个):")
        for item in report["needs_upgrade_list"][:20]:
            print(f"  → {item['slug']} ({'源' if item['is_source'] else '生产'}): {item['reason']}")

def cmd_mark_upgraded(slugs):
    """标记已升级 (V141 D2: SQLite更新)"""
    conn = db_module.get_db()
    c = conn.cursor()
    for slug in slugs:
        c.execute("""
            UPDATE upgrade_tracking
            SET needs_upgrade = 0, upgrade_reason = '', last_upgraded = ?
            WHERE slug = ?
        """, (NOW, slug))
        if c.rowcount > 0:
            print(f"  ✅ {slug} → 已升级")
        else:
            print(f"  ⚠ {slug} → 无记录(跳过)")
    conn.commit()
    conn.close()

def main():
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    if cmd == "check":
        cmd_check()
    elif cmd == "report":
        cmd_report()
    elif cmd == "mark-upgraded":
        if len(sys.argv) < 3:
            print("用法: python upgrade_checker.py mark-upgraded <slug> [slug...]")
            return
        cmd_mark_upgraded(sys.argv[2:])
    else:
        print(f"未知命令: {cmd}")

if __name__ == "__main__":
    main()
