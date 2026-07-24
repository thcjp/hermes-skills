#!/usr/bin/env python3
"""
Round 30 Task 2: 源skill升级检查机制
==================================
功能:
1. 对比本地源skill版本与数据库记录版本
2. 检查ClawHub/GitHub是否有更新
3. 标记needs_upgrade
4. 生成升级报告

使用方式:
    python upgrade_checker.py check          # 执行升级检查
    python upgrade_checker.py report         # 生成升级报告
    python upgrade_checker.py mark-upgraded <slug> [slug...]  # 标记已升级
"""

import os, json, re, hashlib
from datetime import datetime
from pathlib import Path

# === Phase 1: 统一配置导入 ===
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR
from project_config import CLAWHUB_DOWNLOADED_DIR, DIFFERENTIATED_DIR
# === End Phase 1 ===

NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
DB_FILE = TOOLS_DIR / "upload_tracking.json"
REPORT_FILE = TOOLS_DIR / "upgrade_report.json"

def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    db["metadata"]["last_updated"] = NOW
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def read_frontmatter(path):
    """读取SKILL.md的frontmatter"""
    skill_md = os.path.join(path, "SKILL.md") if os.path.isdir(path) else path
    if not os.path.exists(skill_md):
        return {}
    try:
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read(3000)
        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                fm = content[3:end]
                result = {}
                for line in fm.split("\n"):
                    if ":" in line:
                        key, val = line.split(":", 1)
                        result[key.strip()] = val.strip().strip('"').strip("'")
                return result
    except:
        pass
    return {}

def compute_content_hash(path):
    """计算SKILL.md的内容hash"""
    skill_md = os.path.join(path, "SKILL.md") if os.path.isdir(path) else path
    if not os.path.exists(skill_md):
        return None
    try:
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        return hashlib.md5(content.encode("utf-8")).hexdigest()
    except:
        return None

def find_all_skills(base_path):
    result = {}
    if not os.path.exists(base_path):
        return result
    for root, dirs, files in os.walk(base_path):
        if "SKILL.md" in files:
            slug = os.path.basename(root)
            result[slug] = root
    return result

def cmd_check():
    """执行升级检查"""
    db = load_db()
    skills = db["skills"]
    
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
    
    for slug, s in skills.items():
        # 跳过非源skill
        if not s.get("is_source"):
            # 对生产skill也检查版本
            src_path = s.get("source_path", "")
            if not src_path:
                if slug in packaged:
                    src_path = packaged[slug]
                elif slug in diff_skills:
                    src_path = diff_skills[slug]
            
            if src_path and os.path.exists(src_path):
                fm = read_frontmatter(src_path)
                current_version = fm.get("version", "1.0.0")
                current_hash = compute_content_hash(src_path)
                
                ut = s.get("upgrade_tracking", {})
                old_hash = ut.get("content_hash", "")
                
                ut["local_version"] = current_version
                ut["last_checked"] = NOW
                ut["content_hash"] = current_hash
                
                if old_hash and old_hash != current_hash:
                    ut["needs_upgrade"] = True
                    ut["upgrade_reason"] = "本地文件已变更"
                    needs_upgrade += 1
                else:
                    ut["needs_upgrade"] = False
                    up_to_date += 1
                
                s["upgrade_tracking"] = ut
                checked += 1
            else:
                missing_file += 1
            continue
        
        # 源skill升级检查
        src_path = s.get("source_path", "")
        if not src_path:
            if slug in clawhub_source:
                src_path = clawhub_source[slug]
            elif slug in opensource_source:
                src_path = opensource_source[slug]
        
        if src_path and os.path.exists(src_path):
            fm = read_frontmatter(src_path)
            current_version = fm.get("version", "")
            current_hash = compute_content_hash(src_path)
            
            ut = s.get("upgrade_tracking", {})
            old_version = ut.get("source_version", "")
            old_hash = ut.get("content_hash", "")
            
            ut["source_version"] = current_version
            ut["last_checked"] = NOW
            ut["content_hash"] = current_hash
            
            if old_hash and old_hash != current_hash:
                ut["needs_upgrade"] = True
                ut["upgrade_reason"] = "源skill文件已变更"
                needs_upgrade += 1
            elif old_version and current_version and old_version != current_version:
                ut["needs_upgrade"] = True
                ut["upgrade_reason"] = f"版本变更: {old_version} -> {current_version}"
                needs_upgrade += 1
            else:
                ut["needs_upgrade"] = False
                up_to_date += 1
            
            s["upgrade_tracking"] = ut
            checked += 1
        else:
            missing_file += 1
    
    print(f"    检查完成:")
    print(f"    已检查: {checked}")
    print(f"    需升级: {needs_upgrade}")
    print(f"    最新版: {up_to_date}")
    print(f"    文件缺失: {missing_file}")
    
    # 保存检查结果
    save_db(db)
    
    # 生成报告
    report = {
        "check_time": NOW,
        "summary": {
            "checked": checked,
            "needs_upgrade": needs_upgrade,
            "up_to_date": up_to_date,
            "missing_file": missing_file,
        },
        "needs_upgrade_list": [],
    }
    
    for slug, s in skills.items():
        ut = s.get("upgrade_tracking", {})
        if ut.get("needs_upgrade"):
            report["needs_upgrade_list"].append({
                "slug": slug,
                "is_source": s.get("is_source", False),
                "reason": ut.get("upgrade_reason", ""),
                "source_version": ut.get("source_version", ""),
                "local_version": ut.get("local_version", ""),
            })
    
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
    """标记已升级"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            ut = db["skills"][slug].get("upgrade_tracking", {})
            ut["needs_upgrade"] = False
            ut["upgrade_reason"] = ""
            ut["last_upgraded"] = NOW
            db["skills"][slug]["upgrade_tracking"] = ut
            print(f"  ✅ {slug} → 已升级")
    save_db(db)

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
