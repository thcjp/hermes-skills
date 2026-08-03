"""
skill_core.parser - frontmatter解析(单一来源)

从quality_gate.py迁移, 消除quality_gate.py和update_mechanism.py的重复实现
支持三种值模式: 普通键值对 / 块标量(|-) / 列表(- item)
V126 W5: 新增 extract_source_license, 统一 auto_differentiate/finance_differentiate 的重复实现(TD-185)
"""

import re
from pathlib import Path

# [V132 C1a] 章节标题正则(统一3处重复定义: generate_skill, l2_capability_checker, source_fidelity_checker)
CHAPTER_HEADING_PATTERN = re.compile(r'^## (.+)$', re.MULTILINE)


def extract_source_license(source_content: str) -> str:
    """从源skill内容中提取license字段，默认返回MIT。

    V126 W5: 统一 auto_differentiate.py._extract_source_license 和
    finance_differentiate.py.extract_source_license 的重复实现(TD-185)。
    """
    if not source_content:
        return 'MIT'
    content = source_content
    if content.startswith('\ufeff'):
        content = content[1:]
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm = parts[1]
            match = re.search(r'^license:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if match:
                return match.group(1).strip()
    return 'MIT'


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
        # 在块标量模式: 收集缩进行和空行(YAML |- 允许空行)
        if mode == 'block':
            if line.startswith(' ') or line.strip() == '':
                # 空行也属于块标量,保留为空字符串
                block_lines.append(line.strip())
                continue
            else:
                flush()
                # 继续处理当前行(非缩进行)

        # 在列表模式: 收集 - item
        # V181修复: \s+ → \s* 允许无缩进列表项(如 "tools:\n- read\n- exec")
        # 原正则要求至少1个空格在前,导致153个skill的tools字段解析失败
        if mode == 'list':
            if re.match(r'^\s*-\s+', line):
                item = re.sub(r'^\s*-\s+', '', line).strip()
                # V181修复: 递归剥离多层引号(与键值对处理一致)
                while len(item) >= 2 and \
                      ((item.startswith('"') and item.endswith('"')) or \
                       (item.startswith("'") and item.endswith("'"))):
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
            # V181修复: 递归剥离所有层级的引号(处理 name: '"slug"' 等多层引号问题)
            while len(value) >= 2 and \
                  ((value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'"))):
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


def extract_section(content: str, section_name: str) -> str:
    """提取 ## 级别章节内容 (单一来源, 支持章节名变体匹配)

    从markdown正文中按章节标题提取内容, 返回该 `## <section_name>` 标题
    与下一个同级或更高级 `## ` 标题之间的正文(不含标题行); 未找到返回空字符串。
    `###` 等更低级别标题被视为该章节的子内容, 一并包含在返回结果中。

    支持章节名变体匹配(与原 l3_function_checker / l4_task_gate 等实现完全一致):
      - '核心能力' → 核心(能力|功能|规则|概念|原则|工作流|操作)
      - '错误处理' → (错误|异常)处理
      - 其他       → 精确匹配 `## <section_name>`

    Args:
        content: markdown正文(完整markdown亦可, frontmatter不影响匹配)
        section_name: 章节名称

    Returns:
        章节正文(已strip), 未找到返回''
    """
    if section_name == '核心能力':
        pattern = r'##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n(.*?)(?=\n## |\Z)'
    elif section_name == '错误处理':
        pattern = r'##\s+(?:错误|异常)处理\s*\n(.*?)(?=\n## |\Z)'
    else:
        pattern = rf'## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


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
            ENTERPRISE_UPLOAD_DIR, DIFFERENTIATED_DIR, CLAWHUB_DOWNLOADED_DIR,
            DB_PATH,  # V118 W2: 新增DB_PATH(替代硬编码路径)
            PROJECT_ROOT,  # V120 W3: 从project_config导入(替代函数级Path(__file__))
            PLUGS_DIR,  # V147 R2.1: 新增PLUGS_DIR(Plug发布阶段find_skill_md搜索路径)
        )
    except ImportError as e:
        # V143 F2.2: 添加警告日志(保留降级行为,但不再静默)
        print(f"[WARN] project_config不可用,使用本地计算路径回退: {e}")
        PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # V120 W3: 仅project_config不可用时本地计算回退
        PACKAGED_SKILLS_DIR = PROJECT_ROOT / "packaged-skills" / "skillhub"
        OPENSOURCE_SKILLS_DIR = PROJECT_ROOT / "opensource-skills" / "packaged"
        ENTERPRISE_UPLOAD_DIR = PROJECT_ROOT / "enterprise-upload"
        DIFFERENTIATED_DIR = PROJECT_ROOT / "differentiated-skills"
        CLAWHUB_DOWNLOADED_DIR = PROJECT_ROOT / "clawhub-skills" / "downloaded"
        DB_PATH = PROJECT_ROOT / "skill-registry.db"  # V118 W2: 降级DB_PATH
        PLUGS_DIR = PROJECT_ROOT / "packaged-skills" / "plugs"  # V147 R2.1: 降级PLUGS_DIR

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
        PLUGS_DIR / slug,  # V147 R2.1: 新增Plug搜索路径(修复Plug发布阶段find_skill_md找不到SKILL.md)
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
    for base_dir in [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, ENTERPRISE_UPLOAD_DIR, CLAWHUB_DOWNLOADED_DIR, PLUGS_DIR]:
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
    # V118 W2: 使用DB_PATH+get_db(),替代硬编码路径+直连DB
    try:
        from skill_core import db as db_module
        _conn = db_module.get_db()
        _c = _conn.cursor()
        _c.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,))
        _row = _c.fetchone()
        _conn.close()
        if _row and _row['local_path']:
            _p = Path(_row['local_path'])
            _md = _p if _p.name == 'SKILL.md' and _p.exists() else _p / "SKILL.md"
            if _md.exists():
                return _md
    except Exception as e:  # [V130 A1] 宽泛捕获: DB查询失败时回退到None  [V132 C2] 有意降级  V144 G1: 添加警告日志
        print(f"[WARN] DB查询local_path失败,返回None: {e}")

    return None


def find_skill_md_multi(slug: str, local_path: str = None) -> Path:
    """向后兼容wrapper: 调用find_skill_md(slug, local_path)

    保留此函数是为了兼容batch_l3_trial.py等历史调用方
    新代码应直接使用find_skill_md
    """
    return find_skill_md(slug, local_path)


# ============================================================
# V101 W1/W2: 章节定位与代码块检测 (从l3/l4/sf_batch等文件统一)
# ============================================================

def find_section_position(content: str, section_name: str) -> tuple:
    """找到##章节的起始和结束位置 (支持变体匹配, 跳过代码块内的##)
    
    V101 W1: 从6个文件统一到此实现,采用diff_l4_batch_fix的代码块跳过逻辑(最完善版本)
    
    Returns: (header_start, header_end, body_start, body_end) or None
    """
    if section_name == '核心能力':
        pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)'
    elif section_name == '错误处理':
        pattern = r'(##\s+(?:错误|异常)处理\s*\n)'
    else:
        pattern = rf'(## {re.escape(section_name)}\s*\n)'
    match = re.search(pattern, content)
    if not match:
        return None
    header_start = match.start()
    body_start = match.end()
    # 找到下一个##章节 (跳过代码块内的##)
    pos = body_start
    while pos < len(content):
        next_section = re.search(r'\n## ', content[pos:])
        if not next_section:
            body_end = len(content)
            break
        candidate_end = pos + next_section.start()
        # 检查是否在代码块内
        if is_in_code_block(content, candidate_end):
            pos = candidate_end + next_section.end()
            continue
        body_end = candidate_end
        break
    else:
        body_end = len(content)
    return (header_start, match.end(), body_start, body_end)


def is_in_code_block(content: str, position: int) -> bool:
    """检查给定位置是否在代码块内 (通过计算```出现次数)

    V101 W2: 从3个文件统一到此实现
    """
    before = content[:position]
    return before.count('```') % 2 == 1


def split_frontmatter(text: str) -> tuple:
    """将SKILL.md文本拆分为frontmatter和正文

    V103 W2: 从deduplicate_blocks.py统一到此实现
    Returns: (frontmatter_str, body_str)
    """
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", text
