"""
skill_core.parser - frontmatter解析(单一来源)

从quality_gate.py迁移, 消除quality_gate.py和update_mechanism.py的重复实现
支持三种值模式: 普通键值对 / 块标量(|-) / 列表(- item)
"""

import re
from pathlib import Path


def parse_frontmatter(content: str) -> dict:
    """解析SKILL.md的YAML frontmatter

    返回: {'raw': 原始frontmatter文本, 'fields': {字段名: 值}, 'body': 正文}

    支持三种值模式:
        - 普通键值对: key: value
        - 块标量: key: |-  (多行文本)
        - 列表: key: \n  - item1 \n  - item2
    """
    # 去BOM
    if content.startswith('\ufeff'):
        content = content[1:]

    # 匹配 --- ... ---
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not fm_match:
        return {'raw': '', 'fields': {}, 'body': content}

    raw = fm_match.group(1)
    body = content[fm_match.end():]

    # 简单YAML解析(不依赖yaml库, 避免环境问题)
    fields = {}
    mode = None  # None | 'block' | 'list'
    current_key = None
    block_lines = []
    list_items = []

    def flush():
        """结束当前模式, 保存字段"""
        nonlocal mode, current_key, block_lines, list_items
        if mode == 'block' and current_key:
            # 块标量: 合并行, 去公共缩进
            text = '\n'.join(block_lines)
            fields[current_key] = text.strip()
        elif mode == 'list' and current_key:
            fields[current_key] = list_items[:] if list_items else []
        mode = None
        current_key = None
        block_lines = []
        list_items = []

    for line in raw.split('\n'):
        # 在块标量模式: 收集缩进行
        if mode == 'block':
            if line.startswith(' ') and line.strip():
                block_lines.append(line.strip())
                continue
            else:
                flush()
                # 继续处理当前行(非缩进行)

        # 在列表模式: 收集 - item
        if mode == 'list':
            if re.match(r'^\s+-\s+', line):
                item = re.sub(r'^\s+-\s+', '', line).strip()
                if (item.startswith('"') and item.endswith('"')) or \
                   (item.startswith("'") and item.endswith("'")):
                    item = item[1:-1]
                list_items.append(item)
                continue
            else:
                flush()
                # 继续处理当前行

        # 普通模式: 匹配键值对
        kv_match = re.match(r'^(\w+):\s*(.*)$', line)
        if kv_match:
            key = kv_match.group(1)
            value = kv_match.group(2).strip()

            # 块标量 |-
            if value in ('|-', '|', '>', '>-'):
                mode = 'block'
                current_key = key
                block_lines = []
                continue

            # 列表(值为空, 后续行是- item)
            if not value:
                mode = 'list'
                current_key = key
                list_items = []
                continue

            # 普通键值对
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            fields[key] = value

    # 保存最后一个字段
    flush()

    return {'raw': raw, 'fields': fields, 'body': body}


def parse_frontmatter_from_file(skill_md_path: Path) -> dict:
    """从SKILL.md文件读取并解析frontmatter

    便捷函数: 读取文件 + parse_frontmatter
    """
    content = Path(skill_md_path).read_text(encoding='utf-8')
    return parse_frontmatter(content)


def find_skill_md(slug: str, local_path: str = None) -> Path:
    """根据slug在所有skill目录中查找SKILL.md文件(统一实现)

    搜索目录(按优先级):
    0. local_path — 调用方指定的路径(可选)
    1. PACKAGED_SKILLS_DIR — 扁平结构: {dir}/{slug}/SKILL.md
    2. OPENSOURCE_SKILLS_DIR — 扁平结构: {dir}/{slug}/SKILL.md
    3. ENTERPRISE_UPLOAD_DIR — 扁平结构: {dir}/{slug}/SKILL.md
    4. DIFFERENTIATED_DIR — 嵌套结构: {dir}/{category}/{slug}/SKILL.md
    5. CLAWHUB_DOWNLOADED_DIR — 扁平/嵌套结构: {dir}/{slug}/SKILL.md

    快速路径: 先按目录名匹配slug(不读文件内容)
    准确路径: 如果快速路径未命中, 读取SKILL.md验证slug字段
    DB回退: 从skills表local_path字段查找

    Args:
        slug: skill的slug标识
        local_path: 可选, 调用方指定的本地路径(向后兼容find_skill_md_multi)

    Returns:
        SKILL.md的Path, 未找到返回None
    """
    import re as _re
    import sys as _sys

    # 延迟导入配置, 避免循环依赖
    _sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "config"))
    try:
        from project_config import (
            PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR,
            ENTERPRISE_UPLOAD_DIR, DIFFERENTIATED_DIR, CLAWHUB_DOWNLOADED_DIR
        )
    except ImportError:
        # 降级: 使用硬编码路径
        _project_root = Path(__file__).resolve().parent.parent.parent
        PACKAGED_SKILLS_DIR = _project_root / "packaged-skills" / "skillhub"
        OPENSOURCE_SKILLS_DIR = _project_root / "opensource-skills" / "packaged"
        ENTERPRISE_UPLOAD_DIR = _project_root / "enterprise-upload"
        DIFFERENTIATED_DIR = _project_root / "differentiated-skills"
        CLAWHUB_DOWNLOADED_DIR = _project_root / "clawhub-skills" / "downloaded"

    # 0. local_path优先(向后兼容find_skill_md_multi)
    if local_path:
        p = Path(local_path) / "SKILL.md"
        if p.exists():
            return p
        p = Path(local_path)
        if p.exists() and p.suffix == '.md':
            return p

    # 快速路径: 按目录名匹配
    fast_dirs = [
        PACKAGED_SKILLS_DIR / slug,
        OPENSOURCE_SKILLS_DIR / slug,
        ENTERPRISE_UPLOAD_DIR / slug,
        CLAWHUB_DOWNLOADED_DIR / slug,
    ]
    for d in fast_dirs:
        if d.is_dir():
            md = d / "SKILL.md"
            if md.exists():
                return md

    # 嵌套结构: differentiated-skills/{category}/{slug}/SKILL.md
    if DIFFERENTIATED_DIR.exists():
        for cat_dir in DIFFERENTIATED_DIR.iterdir():
            if not cat_dir.is_dir():
                continue
            md = cat_dir / slug / "SKILL.md"
            if md.exists():
                return md

    # 嵌套结构: clawhub-skills/downloaded/{category}/{slug}/SKILL.md
    if CLAWHUB_DOWNLOADED_DIR.exists():
        for cat_dir in CLAWHUB_DOWNLOADED_DIR.iterdir():
            if not cat_dir.is_dir():
                continue
            md = cat_dir / slug / "SKILL.md"
            if md.exists():
                return md

    # 准确路径: 读取SKILL.md验证slug字段(慢但可靠)
    for base_dir in [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, ENTERPRISE_UPLOAD_DIR, CLAWHUB_DOWNLOADED_DIR]:
        if not base_dir.exists():
            continue
        for d in base_dir.iterdir():
            if d.is_dir() and (d / "SKILL.md").exists():
                content = (d / "SKILL.md").read_text(encoding='utf-8')
                if content.startswith('\ufeff'):
                    content = content[1:]
                if content.startswith('---'):
                    parts = _re.split(r'^---\s*$', content, maxsplit=2, flags=_re.MULTILINE)
                    if len(parts) >= 3:
                        fm = parts[1]
                        slug_match = _re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, _re.MULTILINE)
                        if slug_match and slug_match.group(1).strip() == slug:
                            return d / "SKILL.md"

    # 嵌套结构准确路径: differentiated-skills + clawhub-skills/downloaded
    for nested_dir in [DIFFERENTIATED_DIR, CLAWHUB_DOWNLOADED_DIR]:
        if not nested_dir.exists():
            continue
        for cat_dir in nested_dir.iterdir():
            if not cat_dir.is_dir():
                continue
            for d in cat_dir.iterdir():
                if d.is_dir() and (d / "SKILL.md").exists():
                    content = (d / "SKILL.md").read_text(encoding='utf-8')
                    if content.startswith('\ufeff'):
                        content = content[1:]
                    if content.startswith('---'):
                        parts = _re.split(r'^---\s*$', content, maxsplit=2, flags=_re.MULTILINE)
                        if len(parts) >= 3:
                            fm = parts[1]
                            slug_match = _re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, _re.MULTILINE)
                            if slug_match and slug_match.group(1).strip() == slug:
                                return d / "SKILL.md"

    # DB local_path 回退 (v2.7新增: 统一skill_batch_upgrader/llm_validator/dependency_verifier的DB回退)
    try:
        import sqlite3 as _sqlite3
        _db_path = Path(__file__).resolve().parent.parent.parent / "skill-registry.db"
        if _db_path.exists():
            _conn = _sqlite3.connect(str(_db_path))
            _conn.row_factory = _sqlite3.Row
            _c = _conn.cursor()
            _c.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,))
            _row = _c.fetchone()
            _conn.close()
            if _row and _row['local_path']:
                _p = Path(_row['local_path'])
                _md = _p if _p.name == 'SKILL.md' and _p.exists() else _p / "SKILL.md"
                if _md.exists():
                    return _md
    except Exception:
        pass

    return None


def find_skill_md_multi(slug: str, local_path: str = None) -> Path:
    """向后兼容wrapper: 调用find_skill_md(slug, local_path)

    保留此函数是为了兼容batch_l3_trial.py等历史调用方
    新代码应直接使用find_skill_md
    """
    return find_skill_md(slug, local_path)
