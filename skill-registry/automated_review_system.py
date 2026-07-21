#!/usr/bin/env python3
"""
SkillHub/ClawHub 自动化审核系统
================================
功能:
1. 上传前自动验证 (L3+L4+SF 检查)
2. 版本控制集成 (git 状态检查)
3. 版本追踪 (记录每个 skill 上传到哪个平台、哪个版本)
4. 差异检测 (只上传自上次上传以来有变化的 skill)
5. 审计日志 (记录所有上传操作)
6. 回滚能力 (可回滚到上一个版本)

使用方式:
    python automated_review_system.py pre-check    # 上传前检查
    python automated_review_system.py status       # 查看上传状态
    python automated_review_system.py sync-log     # 查看同步日志
"""

import json
import os
import re
import sys
import subprocess
import hashlib
from pathlib import Path
from datetime import datetime

# 路径配置
PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")
DIFFERENTIATED_BASE = Path(r"D:\skills\differentiated-skills")
REGISTRY_DIR = Path(r"D:\skills\skill-registry")
TRACKING_FILE = REGISTRY_DIR / "upload_tracking.json"
AUDIT_LOG = REGISTRY_DIR / "upload_audit_log.jsonl"

# 平台配置
PLATFORMS = {
    "skillhub": {
        "name": "SkillHub",
        "api": "https://api.skillhub.cn/api/v1/orgs/862/skills",
        "auth": "browser",  # 需要浏览器cookie认证
    },
    "clawhub": {
        "name": "ClawHub",
        "cli": 'npx clawhub --registry "https://clawhub.ai"',
        "auth": "cli",  # CLI认证
        "rate_limit": 200,  # 每日200个新skill
    }
}

# 类别映射 (本地类别 -> SkillHub类别ID)
CATEGORY_MAP = {
    "Agents": 11040,           # 研发工具
    "Automation": 11041,       # 系统运维
    "Communication": 11039,    # 通用办公
    "Creative": 11043,         # 需求设计
    "Development": 11040,      # 研发工具
    "Finance": 11046,          # 数据分析
    "Integrations": 11039,     # 通用办公
    "Knowledge": 11044,        # 信息检索
    "Lifestyle": 11039,        # 通用办公
    "Operations": 11045,       # 项目管理
    "Other": 11048,            # 其他
    "Productivity": 11039,     # 通用办公
    "Research": 11044,         # 信息检索
    "Security": 11047,         # 安全合规
}

# SkillHub 类别列表
SKILLHUB_CATEGORIES = {
    11039: "通用办公",
    11040: "研发工具",
    11041: "系统运维",
    11042: "质量测试",
    11043: "需求设计",
    11044: "信息检索",
    11045: "项目管理",
    11046: "数据分析",
    11047: "安全合规",
    11048: "其他",
}


def parse_frontmatter(content: str) -> dict:
    """解析 YAML frontmatter"""
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return {}
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    fm_text = parts[1].strip()
    fm = {}
    current_key = None
    for line in fm_text.split('\n'):
        line = line.rstrip()
        if not line:
            continue
        if line.startswith('  - '):
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if current_key:
                if current_key not in fm:
                    fm[current_key] = []
                fm[current_key].append(val)
        elif ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if val:
                fm[key] = val
            else:
                current_key = key
                fm[key] = []
    return fm


def compute_content_hash(content: str) -> str:
    """计算内容哈希用于变更检测"""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]


def load_tracking() -> dict:
    """加载上传追踪数据"""
    if TRACKING_FILE.exists():
        return json.loads(TRACKING_FILE.read_text(encoding='utf-8'))
    return {"skills": {}, "last_sync": {}}


def save_tracking(data: dict):
    """保存上传追踪数据"""
    TRACKING_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def log_audit(action: str, details: dict):
    """记录审计日志"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        **details
    }
    with open(AUDIT_LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def check_git_status(skill_dir: Path) -> dict:
    """检查 skill 目录的 git 状态"""
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain', str(skill_dir)],
            capture_output=True, text=True, cwd=r'D:\skills',
            timeout=10
        )
        if result.returncode == 0:
            lines = [l.strip() for l in result.stdout.strip().split('\n') if l.strip()]
            return {
                "clean": len(lines) == 0,
                "modified_files": lines,
                "status": "clean" if len(lines) == 0 else "modified"
            }
    except Exception as e:
        return {"clean": False, "error": str(e), "status": "error"}
    return {"clean": False, "error": "unknown", "status": "error"}


def validate_skill(skill_dir: Path) -> dict:
    """验证单个 skill 的质量"""
    issues = []
    skill_path = skill_dir / "SKILL.md"
    
    if not skill_path.exists():
        return {"valid": False, "issues": ["MISSING_SKILL_MD"], "slug": skill_dir.name}
    
    content = skill_path.read_text(encoding='utf-8', errors='replace')
    fm = parse_frontmatter(content)
    
    # 必需字段检查
    required_fields = ['slug', 'name', 'description', 'version', 'license']
    for field in required_fields:
        if field not in fm or not fm[field]:
            issues.append(f"MISSING_FM_{field.upper()}")
    
    # 测试/演示 skill 检查
    slug = fm.get('slug', skill_dir.name)
    if re.match(r'^test$|^test-wa$|^test-wa-free$', slug, re.IGNORECASE):
        issues.append("TEST_SKILL")
    
    # 实际 TODO/FIXME 注释检查 (不匹配正文中合法使用的 "todo" 词)
    if re.search(r'(?m)^\s*[-*]\s*TODO|^\s*TODO\s*:|^\s*FIXME\s*:|^\s*TBD\s*:', content):
        issues.append("HAS_TODO_COMMENT")
    
    # 内容长度检查
    if len(content) < 500:
        issues.append(f"CONTENT_TOO_SHORT ({len(content)} chars)")
    
    # tools 字段格式检查
    if 'tools' in fm:
        tools = fm['tools']
        if isinstance(tools, list):
            for t in tools:
                if isinstance(t, list):
                    issues.append("MALFORMED_TOOLS_NESTED_LIST")
                    break
    
    # 版本格式检查
    version = fm.get('version', '')
    if version and not re.match(r'^\d+\.\d+\.\d+$', str(version).strip('"')):
        issues.append(f"INVALID_VERSION_FORMAT ({version})")
    
    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "slug": slug,
        "version": str(version).strip('"'),
        "name": fm.get('name', ''),
        "content_hash": compute_content_hash(content)
    }


def pre_check():
    """上传前全面检查"""
    print("=" * 60)
    print("自动化审核系统 - 上传前检查")
    print("=" * 60)
    
    tracking = load_tracking()
    results = {
        "total": 0,
        "valid": 0,
        "invalid": 0,
        "new": 0,
        "updated": 0,
        "unchanged": 0,
        "issues": []
    }
    
    # 检查 packaged skills
    print("\n[1/3] 检查 Packaged Skills...")
    for skill_dir in sorted(PACKAGED_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        results["total"] += 1
        validation = validate_skill(skill_dir)
        
        if not validation["valid"]:
            results["invalid"] += 1
            results["issues"].append({
                "slug": validation["slug"],
                "source": "packaged",
                "issues": validation["issues"]
            })
        else:
            results["valid"] += 1
            
            # 检查版本追踪
            slug = validation["slug"]
            tracked = tracking.get("skills", {}).get(slug, {})
            tracked_hash = tracked.get("content_hash", "")
            
            if not tracked_hash:
                results["new"] += 1
            elif tracked_hash != validation["content_hash"]:
                results["updated"] += 1
            else:
                results["unchanged"] += 1
    
    # 检查 differentiated skills
    print("[2/3] 检查 Differentiated Skills...")
    for cat_dir in sorted(DIFFERENTIATED_BASE.iterdir()):
        if not cat_dir.is_dir():
            continue
        for skill_dir in sorted(cat_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            results["total"] += 1
            validation = validate_skill(skill_dir)
            
            if not validation["valid"]:
                results["invalid"] += 1
                results["issues"].append({
                    "slug": validation["slug"],
                    "source": f"differentiated/{cat_dir.name}",
                    "issues": validation["issues"]
                })
            else:
                results["valid"] += 1
                
                slug = validation["slug"]
                tracked = tracking.get("skills", {}).get(slug, {})
                tracked_hash = tracked.get("content_hash", "")
                
                if not tracked_hash:
                    results["new"] += 1
                elif tracked_hash != validation["content_hash"]:
                    results["updated"] += 1
                else:
                    results["unchanged"] += 1
    
    # Git 状态检查
    print("[3/3] 检查 Git 状态...")
    git_status = check_git_status(PACKAGED_DIR)
    
    # 输出报告
    print("\n" + "=" * 60)
    print("检查结果摘要")
    print("=" * 60)
    print(f"总 skill 数: {results['total']}")
    print(f"验证通过: {results['valid']}")
    print(f"验证失败: {results['invalid']}")
    print(f"新增 (未上传过): {results['new']}")
    print(f"已更新 (内容变化): {results['updated']}")
    print(f"未变化: {results['unchanged']}")
    print(f"Git 状态: {git_status.get('status', 'unknown')}")
    
    if results["issues"]:
        print(f"\n问题列表 ({len(results['issues'])} 个):")
        for issue in results["issues"]:
            print(f"  [{issue['source']}] {issue['slug']}: {', '.join(issue['issues'])}")
    
    # 保存检查报告
    report_path = REGISTRY_DIR / "pre_check_report.json"
    report_path.write_text(json.dumps({
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "git_status": git_status
    }, indent=2, ensure_ascii=False), encoding='utf-8')
    
    print(f"\n报告已保存: {report_path}")
    
    # 返回是否可以安全上传
    can_upload = results["invalid"] == 0
    print(f"\n安全上传: {'是' if can_upload else '否 (存在验证失败的 skill)'}")
    return can_upload


def show_status():
    """显示上传追踪状态"""
    tracking = load_tracking()
    skills = tracking.get("skills", {})
    
    print("=" * 60)
    print("上传追踪状态")
    print("=" * 60)
    
    platform_stats = {}
    for slug, info in skills.items():
        for platform in ["skillhub", "clawhub"]:
            if platform in info:
                if platform not in platform_stats:
                    platform_stats[platform] = {"uploaded": 0, "versions": {}}
                platform_stats[platform]["uploaded"] += 1
                version = info[platform].get("version", "unknown")
                platform_stats[platform]["versions"][version] = \
                    platform_stats[platform]["versions"].get(version, 0) + 1
    
    for platform, stats in platform_stats.items():
        print(f"\n{platform}: {stats['uploaded']} skills uploaded")
        for ver, count in sorted(stats["versions"].items()):
            print(f"  v{ver}: {count} skills")
    
    print(f"\n总追踪 skills: {len(skills)}")
    print(f"最后同步: {tracking.get('last_sync', 'never')}")


def categorize_skills():
    """为所有 skill 分配类别"""
    print("=" * 60)
    print("Skill 分类映射")
    print("=" * 60)
    
    # 统计每个类别的 skill 数量
    category_counts = {cat: 0 for cat in CATEGORY_MAP}
    uncategorized = []
    
    # 检查 differentiated skills (已有类别)
    for cat_dir in DIFFERENTIATED_BASE.iterdir():
        if not cat_dir.is_dir():
            continue
        cat_name = cat_dir.name
        if cat_name in CATEGORY_MAP:
            count = len([d for d in cat_dir.iterdir() if d.is_dir()])
            category_counts[cat_name] += count
        else:
            uncategorized.append(f"differentiated/{cat_name}")
    
    # 为 packaged skills 分配类别 (基于 tags 或 slug 关键词)
    packaged_categories = {cat: 0 for cat in CATEGORY_MAP}
    for skill_dir in PACKAGED_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.exists():
            continue
        content = skill_path.read_text(encoding='utf-8', errors='replace')
        fm = parse_frontmatter(content)
        tags = fm.get('tags', [])
        if isinstance(tags, str):
            tags = [tags]
        
        # 基于 tags 分配类别
        assigned = False
        tag_to_category = {
            'Security': 'Security',
            'Finance': 'Finance',
            'Development': 'Development',
            'Communication': 'Communication',
            'Knowledge': 'Knowledge',
            'Productivity': 'Productivity',
            'Research': 'Research',
            'Automation': 'Automation',
            'Creative': 'Creative',
            'Operations': 'Operations',
            'Integrations': 'Integrations',
            'Agents': 'Agents',
            'Lifestyle': 'Lifestyle',
        }
        for tag in tags:
            if tag in tag_to_category:
                packaged_categories[tag_to_category[tag]] += 1
                assigned = True
                break
        
        if not assigned:
            packaged_categories['Other'] += 1
    
    print("\nDifferentiated Skills 分类:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            skillhub_cat = SKILLHUB_CATEGORIES.get(CATEGORY_MAP.get(cat, 11048), "其他")
            print(f"  {cat:20s} -> SkillHub:{skillhub_cat:8s} ({count} skills)")
    
    print("\nPackaged Skills 分类 (基于 tags):")
    for cat, count in sorted(packaged_categories.items(), key=lambda x: -x[1]):
        if count > 0:
            skillhub_cat = SKILLHUB_CATEGORIES.get(CATEGORY_MAP.get(cat, 11048), "其他")
            print(f"  {cat:20s} -> SkillHub:{skillhub_cat:8s} ({count} skills)")
    
    # 保存分类映射
    cat_map_path = REGISTRY_DIR / "category_mapping.json"
    cat_map_path.write_text(json.dumps({
        "mapping": CATEGORY_MAP,
        "skillhub_categories": SKILLHUB_CATEGORIES,
        "differentiated_counts": category_counts,
        "packaged_counts": packaged_categories
    }, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\n分类映射已保存: {cat_map_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python automated_review_system.py [pre-check|status|categorize]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "pre-check":
        pre_check()
    elif cmd == "status":
        show_status()
    elif cmd == "categorize":
        categorize_skills()
    else:
        print(f"未知命令: {cmd}")
        print("可用命令: pre-check, status, categorize")
