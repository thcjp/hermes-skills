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
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===

import re
import json
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
    report_path = Path(r"D:\skills\skill-registry\reports\fix_missing_fields_v36.json")
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
