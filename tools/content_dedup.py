#!/usr/bin/env python3
"""
内容指纹去重工具 (v1.0)
======================
上传前检测SKILL.md内容是否与已上传的skill重复，
防止相同内容以不同slug上传触发平台反垃圾系统。

根因: 2026-07-24批量上传中大量近似重复内容被封禁(93.4%封禁率)
修复: 在上传路径增加内容指纹预检，相同内容的skill不允许重复上传
"""

import hashlib
import sqlite3
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DB_PATH = str(_PROJECT_ROOT / "skill-registry.db")


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
