"""
skill_core.finder - Skill目录查找(单一来源)

V116 W2: 统一 auto_publish.py 和 clawhub_batch_uploader.py 的 find_skill_dir 实现。
查找顺序: DB local_path → dir_mapping → slug变体 → ALT_DIRS文件系统搜索
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent / "config"))
from project_config import (
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, DIFFERENTIATED_DIR,
)
# === End Phase 1 ===

from pathlib import Path
from .db import get_db


# Alternative directory locations to check
ALT_DIRS = [
    PACKAGED_SKILLS_DIR,
    OPENSOURCE_SKILLS_DIR,
    DIFFERENTIATED_DIR,
]


def find_skill_dir(slug, dir_mapping=None):
    """查找skill的本地目录 (统一入口)

    V116 W2: 合并 auto_publish.py(简单版) 和 clawhub_batch_uploader.py(增强版) 的实现。
    auto_publish 调用方只需传 slug, dir_mapping 默认 None 跳过。

    查找顺序:
    1. DB local_path (最可靠, v2.3新增)
    2. dir_mapping (如果提供)
    3. slug变体匹配 (-sk, -free, -paid后缀)
    4. ALT_DIRS 文件系统搜索 (PACKAGED_SKILLS_DIR + OPENSOURCE_SKILLS_DIR + DIFFERENTIATED_DIR)

    Args:
        slug: skill的slug标识
        dir_mapping: 可选的slug→路径映射 (来自批量上传器的found_mapping)

    Returns:
        Path: skill目录路径, 未找到返回None
    """
    # 1. 优先从DB获取local_path (最可靠)
    try:
        conn = get_db()
        row = conn.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,)).fetchone()
        conn.close()
        if row and row["local_path"]:
            local_path = row["local_path"]
            if local_path.startswith("/d/"):
                local_path = "d:" + local_path[2:]
            p = Path(local_path)
            if p.exists() and (p / "SKILL.md").exists():
                return p
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        print(f"  [WARN] find_skill_dir DB查询失败: {e}")

    # 2. Check dir mapping (如果提供)
    if dir_mapping:
        d = dir_mapping.get(slug)
        if d and Path(d).exists() and (Path(d) / "SKILL.md").exists():
            return Path(d)

    # 3. 生成slug变体列表(处理 -sk, -free, -paid 等后缀)
    slug_variants = [slug]
    if slug.endswith('-sk'):
        slug_variants.append(slug[:-3])
    if slug.endswith('-free'):
        slug_variants.append(slug[:-5])
    if slug.endswith('-paid'):
        slug_variants.append(slug[:-5])
    if slug.endswith('-pro-sk'):
        slug_variants.append(slug.replace('-pro-sk', '-pro'))
        slug_variants.append(slug.replace('-pro-sk', ''))
    # 去掉 -sk 后尝试其他变体
    base_slug = slug
    for suffix in ['-sk', '-free', '-paid']:
        if base_slug.endswith(suffix):
            base_slug = base_slug[:-len(suffix)]
            break
    if base_slug != slug:
        slug_variants.append(base_slug)

    # 4. Fallback: search in alternative directories with all slug variants
    for base in ALT_DIRS:
        if not base.exists():
            continue
        for try_slug in slug_variants:
            # Direct match
            p = base / try_slug
            if p.exists() and (p / "SKILL.md").exists():
                return p
            # Search in subdirectories (for differentiated-skills which has category folders)
            if base.name == "differentiated-skills":
                for cat_dir in base.iterdir():
                    if not cat_dir.is_dir():
                        continue
                    p = cat_dir / try_slug
                    if p.exists() and (p / "SKILL.md").exists():
                        return p

    return None
