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
