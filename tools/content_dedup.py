#!/usr/bin/env python3
"""
内容指纹去重工具 (v2.0)
======================
上传前检测SKILL.md内容是否与已上传的skill重复，
防止相同内容以不同slug上传触发平台反垃圾系统。

v2.0: 增加SimHash近似去重(check_approximate_dedup)
根因: 2026-07-24批量上传中大量近似重复内容被封禁(93.4%封禁率)
修复: 在上传路径增加内容指纹预检 + SimHash近似去重
"""

import hashlib
import re
import sqlite3
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DB_PATH = str(_PROJECT_ROOT / "skill-registry.db")

# SimHash参数
_SIMHASH_BITS = 64
_HAMMING_THRESHOLD = 6  # Hamming距离<=6视为近似重复(64位SimHash)


def compute_content_hash(content: str) -> str:
    """计算内容的SHA-256哈希"""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def check_content_dedup(slug: str, content: str, db_path: str = None) -> dict:
    """
    检查内容指纹是否与已上传的skill重复
    
    参数:
        slug: 当前skill的slug
        content: SKILL.md文件内容
        db_path: 数据库路径
    
    返回:
        {
            'duplicate': bool,         # 是否重复
            'existing_slug': str,      # 重复的已有slug
            'content_hash': str,       # 内容哈希
            'reason': str,             # 原因说明
        }
    """
    if db_path is None:
        db_path = _DB_PATH
    
    content_hash = compute_content_hash(content)
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # 查找相同content_hash且已成功上传的其他skill
    # 检查条件: content_hash相同 + slug不同 + 有成功的上传记录
    c.execute("""
        SELECT s.slug, s.local_path, s.skillhub_sync_status
        FROM skills s
        WHERE s.content_hash = ?
        AND s.slug != ?
        AND s.skillhub_sync_status = 'synced'
        LIMIT 1
    """, (content_hash, slug))
    
    row = c.fetchone()
    conn.close()
    
    if row:
        return {
            'duplicate': True,
            'existing_slug': row[0],
            'existing_path': row[1],
            'content_hash': content_hash,
            'reason': f"内容与已上传skill '{row[0]}'完全相同(哈希匹配)",
        }
    
    return {
        'duplicate': False,
        'content_hash': content_hash,
        'reason': '内容唯一',
    }


# ============ SimHash 近似去重 (v2.0) ============

def _tokenize(content: str) -> list:
    """将内容分词为特征列表(用于SimHash计算)

    采用3-gram shingling: 将文本按连续3个词为一组切分,
    对中文按字符切分, 对英文按空格切分后取3-gram。
    """
    # 移除frontmatter(YAML) — 只比较正文内容
    parts = content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else content

    # 按非字母数字汉字切分
    tokens = re.findall(r'[\w\u4e00-\u9fff]+', body.lower())
    if len(tokens) < 3:
        return tokens

    # 3-gram shingling
    shingles = []
    for i in range(len(tokens) - 2):
        shingles.append(tokens[i] + ' ' + tokens[i + 1] + ' ' + tokens[i + 2])
    return shingles if shingles else tokens


def compute_simhash(content: str) -> int:
    """计算内容的64位SimHash值

    算法:
    1. 将内容分词为特征(shingles)
    2. 对每个特征计算MD5哈希(128位), 取前64位
    3. 对每一位累加: 该位为1则+1, 为0则-1
    4. 最终: 累加值>0的位为1, 否则为0

    Args:
        content: 文本内容

    Returns:
        64位SimHash值(int)
    """
    tokens = _tokenize(content)
    if not tokens:
        return 0

    # 统计token频率作为权重
    from collections import Counter
    token_weights = Counter(tokens)

    # 每一位的累加器
    v = [0] * _SIMHASH_BITS

    for token, weight in token_weights.items():
        # MD5哈希取前8字节(64位)
        h = hashlib.md5(token.encode('utf-8')).digest()
        hash_val = int.from_bytes(h[:8], 'big')

        for i in range(_SIMHASH_BITS):
            bit = (hash_val >> i) & 1
            if bit:
                v[i] += weight
            else:
                v[i] -= weight

    # 生成最终SimHash
    simhash = 0
    for i in range(_SIMHASH_BITS):
        if v[i] > 0:
            simhash |= (1 << i)

    return simhash


def hamming_distance(hash1: int, hash2: int) -> int:
    """计算两个SimHash值的Hamming距离

    V152-R1修复: 使用异或+bit_count避免bin()对负数的问题
    Python bin()对负数返回'-0b...'格式,导致count('1')结果错误
    """
    xor_val = hash1 ^ hash2
    # 使用int.bit_count()(Python 3.10+)或fallback
    if hasattr(int, 'bit_count'):
        return xor_val.bit_count()
    # Fallback for Python < 3.10
    return bin(xor_val).count('1') if xor_val >= 0 else bin(xor_val & ((1 << _SIMHASH_BITS) - 1)).count('1')


def simhash_similarity(hash1: int, hash2: int) -> float:
    """计算两个SimHash值的相似度(0.0~1.0)"""
    dist = hamming_distance(hash1, hash2)
    return 1.0 - (dist / _SIMHASH_BITS)


def _to_signed_64(val: int) -> int:
    """将无符号64位整数转为有符号64位整数(SQLite INTEGER兼容)

    SQLite INTEGER类型为有符号64位(-2^63 ~ 2^63-1),
    而SimHash计算结果为无符号64位(0 ~ 2^64-1),
    超过2^63-1时需转换否则触发溢出异常。
    """
    if val >= (1 << 63):
        return val - (1 << 64)
    return val


def _to_unsigned_64(val) -> int:
    """将有符号64位整数转回无符号64位整数(用于Hamming距离计算)"""
    if val is None:
        return 0
    val = int(val)
    if val < 0:
        return val + (1 << 64)
    return val


def update_simhash(slug: str, simhash: int, content_hash: str = None, db_path: str = None):
    """更新数据库中skill的simhash和content_hash

    Args:
        slug: skill slug
        simhash: SimHash值(无符号64位)
        content_hash: SHA-256内容哈希(可选)
        db_path: 数据库路径
    """
    if db_path is None:
        db_path = _DB_PATH

    # 转换为有符号64位以兼容SQLite INTEGER类型
    simhash_signed = _to_signed_64(simhash)

    conn = sqlite3.connect(db_path)
    if content_hash:
        conn.execute(
            "UPDATE skills SET simhash = ?, content_hash = ? WHERE slug = ?",
            (simhash_signed, content_hash, slug)
        )
    else:
        conn.execute(
            "UPDATE skills SET simhash = ? WHERE slug = ?",
            (simhash_signed, slug)
        )
    conn.commit()
    conn.close()


def find_approximate_duplicates(slug: str, simhash: int, threshold: int = None,
                                db_path: str = None) -> list:
    """在数据库中查找与给定SimHash近似重复的skill

    Args:
        slug: 当前skill的slug(排除自身)
        simhash: 当前skill的SimHash值
        threshold: Hamming距离阈值, 默认使用_HAMMING_THRESHOLD
        db_path: 数据库路径

    Returns:
        list of dict: [{slug, simhash, distance, similarity, sync_status}, ...]
    """
    if threshold is None:
        threshold = _HAMMING_THRESHOLD
    if db_path is None:
        db_path = _DB_PATH

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # 查询所有已上传的skill(simhash != 0 且 slug不同)
    rows = conn.execute("""
        SELECT slug, simhash, skillhub_sync_status, clawhub_sync_status
        FROM skills
        WHERE simhash != 0 AND slug != ?
    """, (slug,)).fetchall()

    conn.close()

    duplicates = []
    for row in rows:
        row_simhash = _to_unsigned_64(row['simhash'])
        dist = hamming_distance(simhash, row_simhash)
        if dist <= threshold:
            duplicates.append({
                'slug': row['slug'],
                'simhash': row_simhash,
                'distance': dist,
                'similarity': round(simhash_similarity(simhash, row_simhash), 4),
                'skillhub_sync_status': row['skillhub_sync_status'],
                'clawhub_sync_status': row['clawhub_sync_status'],
            })

    # 按距离排序(距离越小越相似)
    duplicates.sort(key=lambda x: x['distance'])
    return duplicates


def check_approximate_dedup(slug: str, content: str, db_path: str = None) -> dict:
    """内容去重预检(精确+近似双重检测)

    组合SHA-256精确匹配和SimHash近似匹配:
    1. 精确去重: SHA-256哈希完全相同 → exact_duplicate=True
    2. 近似去重: SimHash Hamming距离<=阈值 → approximate_duplicate=True

    防止相同或高度相似的内容以不同slug上传触发平台反垃圾系统。
    根因: 2026-07-24批量上传990个近似重复skill导致封禁(93.4%封禁率)。

    Args:
        slug: 当前skill的slug
        content: SKILL.md文件内容
        db_path: 数据库路径(可选)

    Returns:
        {
            'exact_duplicate': bool,       # 是否完全相同(SHA-256匹配)
            'approximate_duplicate': bool,  # 是否高度相似(SimHash匹配)
            'existing_slug': str,          # 重复的已有slug(空字符串表示无)
            'content_hash': str,           # SHA-256哈希
            'simhash': int,                # SimHash值
            'similarity': float,           # 与最相似skill的相似度
            'reason': str,                 # 原因说明
        }
    """
    if db_path is None:
        db_path = _DB_PATH

    content_hash = compute_content_hash(content)
    simhash = compute_simhash(content)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # 1. 精确去重: 检查是否有相同content_hash且已上传的其他skill
    c.execute("""
        SELECT s.slug, s.skillhub_sync_status, s.clawhub_sync_status
        FROM skills s
        WHERE s.content_hash = ?
        AND s.slug != ?
        AND (s.skillhub_sync_status = 'synced' OR s.clawhub_sync_status = 'synced')
        LIMIT 1
    """, (content_hash, slug))
    exact_row = c.fetchone()
    conn.close()

    if exact_row:
        existing_slug = exact_row[0]
        # 更新当前skill的simhash供未来比对
        update_simhash(slug, simhash, content_hash, db_path)
        return {
            'exact_duplicate': True,
            'approximate_duplicate': False,
            'existing_slug': existing_slug,
            'content_hash': content_hash,
            'simhash': simhash,
            'similarity': 1.0,
            'reason': f"内容与已上传skill '{existing_slug}'完全相同(SHA-256匹配)",
        }

    # 2. 近似去重: 检查SimHash Hamming距离
    # 更新当前skill的simhash(供未来比对)
    update_simhash(slug, simhash, content_hash, db_path)

    duplicates = find_approximate_duplicates(slug, simhash, db_path=db_path)
    if duplicates:
        dup = duplicates[0]  # 距离最小的
        return {
            'exact_duplicate': False,
            'approximate_duplicate': True,
            'existing_slug': dup['slug'],
            'content_hash': content_hash,
            'simhash': simhash,
            'similarity': dup['similarity'],
            'reason': f"内容与已上传skill '{dup['slug']}'高度相似"
                      f"(Hamming距离={dup['distance']}, 相似度={dup['similarity']:.1%})",
        }

    return {
        'exact_duplicate': False,
        'approximate_duplicate': False,
        'existing_slug': '',
        'content_hash': content_hash,
        'simhash': simhash,
        'similarity': 0.0,
        'reason': '内容唯一(精确+近似双重检测通过)',
    }


def check_content_dedup_by_hash(slug: str, content_hash: str, db_path: str = None) -> dict:
    """
    通过已有哈希检查重复（避免重复计算哈希）
    """
    if db_path is None:
        db_path = _DB_PATH
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute("""
        SELECT s.slug, s.local_path, s.skillhub_sync_status
        FROM skills s
        WHERE s.content_hash = ?
        AND s.slug != ?
        AND s.skillhub_sync_status = 'synced'
        LIMIT 1
    """, (content_hash, slug))
    
    row = c.fetchone()
    conn.close()
    
    if row:
        return {
            'duplicate': True,
            'existing_slug': row[0],
            'existing_path': row[1],
            'content_hash': content_hash,
            'reason': f"内容与已上传skill '{row[0]}'完全相同(哈希匹配)",
        }
    
    return {
        'duplicate': False,
        'content_hash': content_hash,
        'reason': '内容唯一',
    }
