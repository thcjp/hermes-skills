#!/usr/bin/env python3
"""
Fix MISSING_TOOLS / MISSING_TAGS / MISSING_SLUG / MISSING_VERSION / MISSING_NAME
 across all 3 directories.

Scans all SKILL.md files, detects missing frontmatter fields, and adds them
with inferred values based on content analysis.
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR, DATA_DIR, DB_PATH
# === End Phase 1 ===

import re
import json
import sqlite3
from pathlib import Path
from datetime import datetime

SCAN_DIRS = [
    Path(r"d:\skills\packaged-skills\skillhub"),
    Path(r"d:\skills\opensource-skills\packaged"),
    DIFFERENTIATED_DIR,
]

# Default tools by category keywords in slug/path
TOOL_CATEGORIES = {
    "code": ["read", "write", "exec", "glob", "grep"],
    "git": ["read", "write", "exec"],
    "docker": ["read", "write", "exec"],
    "aws": ["read", "write", "exec"],
    "azure": ["read", "write", "exec"],
    "cloud": ["read", "write", "exec"],
    "api": ["read", "write", "exec"],
    "web": ["read", "write", "exec", "glob"],
    "data": ["read", "write", "exec", "glob"],
    "image": ["read", "write", "exec"],
    "video": ["read", "write", "exec"],
    "audio": ["read", "write", "exec"],
    "music": ["read", "write", "exec"],
    "design": ["read", "write", "exec"],
    "ui": ["read", "write", "exec"],
    "finance": ["read", "write", "exec"],
    "email": ["read", "write", "exec"],
    "social": ["read", "write", "exec"],
    "automation": ["read", "write", "exec"],
    "workflow": ["read", "write", "exec"],
    "agent": ["read", "write", "exec", "glob", "grep"],
    "memory": ["read", "write", "exec"],
    "context": ["read", "write", "exec"],
    "task": ["read", "write", "exec"],
    "schedule": ["read", "write", "exec"],
    "monitor": ["read", "exec"],
    "security": ["read", "exec"],
    "network": ["read", "exec"],
    "database": ["read", "write", "exec"],
    "redis": ["read", "write", "exec"],
    "search": ["read", "exec", "glob", "grep"],
    "translate": ["read", "write", "exec"],
    "document": ["read", "write", "exec"],
    "markdown": ["read", "write", "exec"],
    "rss": ["read", "exec"],
    "news": ["read", "exec"],
    "discord": ["read", "write", "exec"],
    "telegram": ["read", "write", "exec"],
    "slack": ["read", "write", "exec"],
    "whatsapp": ["read", "write", "exec"],
    "bilibili": ["read", "write", "exec"],
    "youtube": ["read", "write", "exec"],
    "podcast": ["read", "write", "exec"],
}

# Default tags by category
TAG_CATEGORIES = {
    "code": "开发工具,代码生成,编程辅助",
    "git": "版本控制,Git,开发工具",
    "docker": "容器,Docker,DevOps",
    "aws": "AWS,云计算,DevOps",
    "azure": "Azure,云计算,DevOps",
    "cloud": "云计算,DevOps,基础设施",
    "api": "API,接口,开发工具",
    "web": "Web开发,前端,开发工具",
    "data": "数据处理,数据分析,工具",
    "image": "图像处理,AI绘图,创意",
    "video": "视频处理,媒体,创意",
    "audio": "音频处理,媒体,创意",
    "music": "音乐生成,音频,创意",
    "design": "设计,UI/UX,创意",
    "ui": "UI设计,前端,设计",
    "finance": "金融,财务,数据",
    "email": "邮件,通信,工具",
    "social": "社交媒体,营销,通信",
    "automation": "自动化,工作流,效率",
    "workflow": "工作流,自动化,效率",
    "agent": "AI代理,自动化,智能",
    "memory": "记忆管理,上下文,AI",
    "context": "上下文管理,AI,工具",
    "task": "任务管理,效率,工具",
    "schedule": "定时任务,调度,自动化",
    "monitor": "监控,运维,工具",
    "security": "安全,加密,工具",
    "network": "网络,DNS,工具",
    "database": "数据库,存储,工具",
    "redis": "Redis,缓存,数据库",
    "search": "搜索,检索,工具",
    "translate": "翻译,语言,工具",
    "document": "文档处理,工具,效率",
    "markdown": "Markdown,文档,工具",
    "rss": "RSS,订阅,信息",
    "news": "新闻,信息,资讯",
    "discord": "Discord,社交,通信",
    "telegram": "Telegram,社交,通信",
    "slack": "Slack,社交,通信",
    "whatsapp": "WhatsApp,社交,通信",
    "bilibili": "B站,视频,媒体",
    "youtube": "YouTube,视频,媒体",
    "podcast": "播客,音频,媒体",
}

DEFAULT_TOOLS = ["read", "write", "exec"]
DEFAULT_TAGS = "工具,效率,自动化"

# Tag关键词到category的映射（14个有效category）
TAG_TO_CATEGORY_MAP = {
    # Agents
    "AI代理": "Agents", "agent": "Agents", "智能体": "Agents", "AI助手": "Agents",
    "自动化助手": "Agents", "自主代理": "Agents", "记忆管理": "Agents", "上下文": "Agents",
    "self-evolving": "Agents", "memory": "Agents", "orchestrator": "Agents",
    # Automation
    "自动化": "Automation", "工作流": "Automation", "workflow": "Automation",
    "定时任务": "Automation", "调度": "Automation", "批处理": "Automation",
    "RPA": "Automation", "流程": "Automation", "recipe": "Automation",
    # Communication
    "通信": "Communication", "邮件": "Communication", "email": "Communication",
    "社交": "Communication", "Discord": "Communication", "Telegram": "Communication",
    "Slack": "Communication", "WhatsApp": "Communication", "消息": "Communication",
    "calendar": "Communication", "日历": "Communication", "提醒": "Communication",
    # Creative
    "创意": "Creative", "图像": "Creative", "视频": "Creative", "音频": "Creative",
    "音乐": "Creative", "设计": "Creative", "UI": "Creative", "art": "Creative",
    "drawing": "Creative", "绘画": "Creative", "写作": "Creative", "content": "Creative",
    "bilibili": "Creative", "youtube": "Creative", "podcast": "Creative", "媒体": "Creative",
    # Development
    "开发": "Development", "代码": "Development", "code": "Development", "编程": "Development",
    "git": "Development", "docker": "Development", "API": "Development", "web": "Development",
    "前端": "Development", "后端": "Development", "database": "Development", "redis": "Development",
    "markdown": "Development", "测试": "Development", "debug": "Development",
    # Finance
    "金融": "Finance", "财务": "Finance", "会计": "Finance", "finance": "Finance",
    "accounting": "Finance", "交易": "Finance", "投资": "Finance", "pricing": "Finance",
    # Integrations
    "集成": "Integrations", "integration": "Integrations", "第三方": "Integrations",
    "对接": "Integrations", "webhook": "Integrations", "sync": "Integrations",
    "连接器": "Integrations", "bridge": "Integrations",
    # Knowledge
    "知识": "Knowledge", "文档": "Knowledge", "knowledge": "Knowledge",
    "笔记": "Knowledge", "wiki": "Knowledge", "搜索": "Knowledge",
    "translate": "Knowledge", "翻译": "Knowledge", "PDF": "Knowledge",
    "RSS": "Knowledge", "新闻": "Knowledge", "学习": "Knowledge",
    # Lifestyle
    "生活": "Lifestyle", "健康": "Lifestyle", "美食": "Lifestyle", "旅行": "Lifestyle",
    "购物": "Lifestyle", "电商": "Lifestyle", "娱乐": "Lifestyle", "游戏": "Lifestyle",
    # Operations
    "运维": "Operations", "监控": "Operations", "部署": "Operations", "security": "Operations",
    "网络": "Operations", "DNS": "Operations", "aws": "Operations", "azure": "Operations",
    "cloud": "Operations", "基础设施": "Operations", "DevOps": "Operations",
    # Productivity
    "效率": "Productivity", "productivity": "Productivity", "任务": "Productivity",
    "task": "Productivity", "管理": "Productivity", "SEO": "Productivity",
    "营销": "Productivity", "文案": "Productivity", "电商": "Productivity",
    "小说": "Productivity", "写作": "Productivity", "电子书": "Productivity",
    # Research
    "研究": "Research", "分析": "Research", "research": "Research", "数据": "Research",
    "调研": "Research", "报告": "Research", "统计": "Research", "调研": "Research",
    # Security
    "安全": "Security", "加密": "Security", "防护": "Security", "firewall": "Security",
    "密码": "Security", "漏洞": "Security", "privacy": "Security", "隐私": "Security",
}

# 无效category值需要修复
INVALID_CATEGORIES = {"", "packaged", "null", "None", "NULL"}


def extract_frontmatter(content):
    """Parse frontmatter and return (fm_dict, fm_text, body, full_content)"""
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith("---"):
        return {}, "", content, content
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) >= 3:
        fm_text = parts[1]
        body = parts[2]
        fm = {}
        for line in fm_text.split("\n"):
            m = re.match(r'^(\w+):\s*(.*)$', line)
            if m:
                key = m.group(1)
                val = m.group(2).strip().strip('"').strip("'")
                if val:
                    fm[key] = val
        return fm, fm_text, body, content
    return {}, "", content, content


def infer_tools(slug, path, body):
    """Infer tools field based on slug and content"""
    slug_lower = slug.lower()
    for keyword, tools in TOOL_CATEGORIES.items():
        if keyword in slug_lower or keyword in str(path).lower():
            return tools
    # Check body for hints
    if "grep" in body.lower() or "search" in body.lower():
        return ["read", "exec", "glob", "grep"]
    if "write" in body.lower() or "create" in body.lower() or "generate" in body.lower():
        return ["read", "write", "exec"]
    return DEFAULT_TOOLS


def infer_tags(slug, path, body):
    """Infer tags field based on slug and content"""
    slug_lower = slug.lower()
    for keyword, tags in TAG_CATEGORIES.items():
        if keyword in slug_lower or keyword in str(path).lower():
            return tags
    return DEFAULT_TAGS


def infer_category(slug, path, body, tags=None):
    """Infer category field based on tags, slug, path, and body content.
    
    Priority:
    1. Match tags against TAG_TO_CATEGORY_MAP
    2. Match slug/path keywords against TAG_TO_CATEGORY_MAP
    3. Match body content keywords against TAG_TO_CATEGORY_MAP
    4. Fall back to 'Other'
    """
    # 1. Try tags first
    if tags:
        tags_lower = tags.lower() if isinstance(tags, str) else " ".join(str(t) for t in tags).lower()
        for keyword, category in TAG_TO_CATEGORY_MAP.items():
            if keyword.lower() in tags_lower:
                return category
    
    # 2. Try slug and path
    slug_lower = slug.lower()
    path_lower = str(path).lower()
    for keyword, category in TAG_TO_CATEGORY_MAP.items():
        if keyword.lower() in slug_lower or keyword.lower() in path_lower:
            return category
    
    # 3. Try body content (first 2000 chars for performance)
    body_lower = body[:2000].lower()
    category_scores = {}
    for keyword, category in TAG_TO_CATEGORY_MAP.items():
        count = body_lower.count(keyword.lower())
        if count > 0:
            category_scores[category] = category_scores.get(category, 0) + count
    
    if category_scores:
        return max(category_scores, key=category_scores.get)
    
    # 4. Fall back to 'Other'
    return "Other"


def update_db_category(slug, category):
    """Update the skills.category field in the SQLite database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE skills SET category = ?, updated_at = ? WHERE slug = ?", 
                  (category, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), slug))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False


def add_field_to_frontmatter(content, field_name, field_value):
    """Add a field to the frontmatter, preserving structure"""
    if content.startswith('\ufeff'):
        bom = '\ufeff'
        content = content[1:]
    else:
        bom = ''

    if not content.startswith("---"):
        # No frontmatter, create one
        if isinstance(field_value, list):
            val_str = "[" + ", ".join(f'"{v}"' for v in field_value) + "]"
        else:
            val_str = f'"{field_value}"'
        new_fm = f"---\n{field_name}: {val_str}\n---\n"
        return bom + new_fm + content

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) >= 3:
        fm_text = parts[1]
        body = parts[2]

        # Format the value
        if isinstance(field_value, list):
            val_str = "[" + ", ".join(f'"{v}"' for v in field_value) + "]"
        else:
            val_str = f'"{field_value}"'

        # Add field at the end of frontmatter
        new_fm = fm_text.rstrip() + f"\n{field_name}: {val_str}\n"
        return bom + "---" + new_fm + "---" + body
    return content


def scan_directory(base_dir):
    """Scan a directory for SKILL.md files"""
    if not base_dir.exists():
        return []
    files = []
    if base_dir.name == "differentiated-skills":
        for cat_dir in sorted(base_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            for skill_dir in sorted(cat_dir.iterdir()):
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    files.append(skill_dir / "SKILL.md")
    else:
        for skill_dir in sorted(base_dir.iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                files.append(skill_dir / "SKILL.md")
    return files


def main():
    stats = {
        'started_at': datetime.now().isoformat(),
        'total_files': 0,
        'files_modified': 0,
        'fixes': {
            'MISSING_SLUG': 0,
            'MISSING_VERSION': 0,
            'MISSING_NAME': 0,
            'MISSING_TOOLS': 0,
            'MISSING_TAGS': 0,
            'MISSING_CATEGORY': 0,
            'INVALID_CATEGORY': 0,
        },
        'modified_files': []
    }

    for base_dir in SCAN_DIRS:
        skill_files = scan_directory(base_dir)
        print(f"\nScanning: {base_dir} ({len(skill_files)} files)")

        for skill_md in skill_files:
            stats['total_files'] += 1
            content = skill_md.read_text(encoding='utf-8', errors='replace')
            original = content

            fm, fm_text, body, full = extract_frontmatter(content)
            dir_name = skill_md.parent.name
            slug = fm.get('slug', '')

            fixes_applied = []

            # Fix MISSING_SLUG
            if not slug:
                slug = dir_name
                content = add_field_to_frontmatter(content, 'slug', slug)
                fixes_applied.append('MISSING_SLUG')
                stats['fixes']['MISSING_SLUG'] += 1

            # Fix MISSING_VERSION
            if not fm.get('version'):
                content = add_field_to_frontmatter(content, 'version', '1.0.0')
                fixes_applied.append('MISSING_VERSION')
                stats['fixes']['MISSING_VERSION'] += 1

            # Fix MISSING_NAME
            if not fm.get('name'):
                # Use displayName or slug as name
                name = fm.get('displayName', slug.replace('-', ' ').title())
                content = add_field_to_frontmatter(content, 'name', name)
                fixes_applied.append('MISSING_NAME')
                stats['fixes']['MISSING_NAME'] += 1

            # Re-parse after potential additions
            fm, fm_text, body, full = extract_frontmatter(content)

            # Fix MISSING_TOOLS
            tools_val = fm.get('tools', None)
            if tools_val is None or (isinstance(tools_val, str) and not tools_val.strip()):
                inferred_tools = infer_tools(slug, skill_md.parent, body)
                content = add_field_to_frontmatter(content, 'tools', inferred_tools)
                fixes_applied.append('MISSING_TOOLS')
                stats['fixes']['MISSING_TOOLS'] += 1

            # Re-parse
            fm, fm_text, body, full = extract_frontmatter(content)

            # Fix MISSING_TAGS
            tags_val = fm.get('tags', None)
            if not tags_val or (isinstance(tags_val, str) and not tags_val.strip()):
                inferred_tags = infer_tags(slug, skill_md.parent, body)
                content = add_field_to_frontmatter(content, 'tags', inferred_tags)
                fixes_applied.append('MISSING_TAGS')
                stats['fixes']['MISSING_TAGS'] += 1

            # Re-parse after tags fix
            fm, fm_text, body, full = extract_frontmatter(content)

            # Fix MISSING_CATEGORY or INVALID_CATEGORY
            cat_val = fm.get('category', None)
            current_tags = fm.get('tags', '')
            if not cat_val or cat_val.strip() in INVALID_CATEGORIES:
                inferred_cat = infer_category(slug, skill_md.parent, body, current_tags)
                content = add_field_to_frontmatter(content, 'category', inferred_cat)
                if not cat_val:
                    fixes_applied.append('MISSING_CATEGORY')
                    stats['fixes']['MISSING_CATEGORY'] += 1
                else:
                    fixes_applied.append('INVALID_CATEGORY')
                    stats['fixes']['INVALID_CATEGORY'] += 1
                # Also update database
                update_db_category(slug, inferred_cat)

            # Save if modified
            if content != original:
                skill_md.write_text(content, encoding='utf-8')
                stats['files_modified'] += 1
                stats['modified_files'].append({
                    'file': str(skill_md),
                    'fixes': fixes_applied
                })

    stats['completed_at'] = datetime.now().isoformat()

    # Save report
    report_path = DATA_DIR / "reports" / "fix_missing_fields_v36.json"
    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Fix Missing Fields Complete")
    print(f"{'='*60}")
    print(f"  Files scanned: {stats['total_files']}")
    print(f"  Files modified: {stats['files_modified']}")
    print(f"  Fixes applied:")
    for fix, count in stats['fixes'].items():
        print(f"    {fix}: {count}")
    print(f"  Report: {report_path}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
