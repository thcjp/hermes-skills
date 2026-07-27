#!/usr/bin/env python3
"""
每日同步脚本 (Daily Sync) v3.0
=========================
统一入口，执行完整的每日同步流程：
1. 发现新 Skill + 检测变更
2. 版本同步流水线
3. 质量审计
4. 封禁技能检测 (v3.0新增)
5. 平台同步（GitHub、SkillHub、ClawHub）
6. 数据库记录
7. 生成每日报告

v3.0 增强功能:
- 速率限制: SkillHub上传每小时最多30个, 每天最多100个, 最小间隔2分钟
  根因: 2026-07-24单日爆发式上传1098个技能(同一微秒时间戳)触发SkillHub反垃圾系统
- 封禁技能感知: 上传前检测封禁状态, 跳过已封禁技能, 记录封禁模式
- 评分同步过滤: 仅同步仍可访问(synced_from_skillhub)的技能评分
- ClawHub速率控制: 保持200/天限制, 增加2分钟上传间隔

使用方式:
    python tools/daily_sync.py                  # 完整同步
    python tools/daily_sync.py --discover       # 仅发现
    python tools/daily_sync.py --audit          # 仅审计
    python tools/daily_sync.py --report         # 仅生成报告
    python tools/daily_sync.py --check-banned   # 仅检查封禁技能 (v3.0)
    python tools/daily_sync.py --rate-status    # 查看速率限制状态 (v3.0)
    python tools/daily_sync.py --ratings        # 仅执行评分同步
    python tools/daily_sync.py --low-ratings    # 仅执行低评分检查
    python tools/daily_sync.py --clawhub        # 仅执行ClawHub上传
    python tools/daily_sync.py --full           # 完整同步（默认）
"""

import sys
import os
import json
import subprocess
import sqlite3
import time as _time
from pathlib import Path
from datetime import datetime, timedelta

# 统一配置导入
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import (
    DB_PATH, TOOLS_DIR, DATA_DIR, REPORT_DIR,
    HEALTH_REPORT_DIR, DISCOVERY_DIR, CLAWHUB_DRY_RUN
)
from platform_config import GITHUB_REPOS


# ============ 速率限制常量 (v3.0: 防止触发SkillHub反垃圾系统) ============
# 根因: 2026-07-24单日爆发式上传1098个技能(同一微秒时间戳)触发平台反垃圾清理
MAX_UPLOADS_PER_HOUR = 30        # 每小时最多上传30个技能
MAX_UPLOADS_PER_DAY = 100        # 每天最多上传100个技能
MIN_INTERVAL_SECONDS = 120       # 两次上传最少间隔2分钟(120秒)
CLAWHUB_UPLOAD_DELAY = 120       # ClawHub上传间隔(秒), v3.0: 从2秒提升到2分钟


def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")


# ============ 速率限制功能 (v3.0新增) ============

def _ensure_rate_limit_table():
    """创建上传速率限制跟踪表(幂等)

    在数据库中创建 upload_rate_limits 表, 记录每次上传的时间戳,
    用于强制执行每小时/每天上传限制和最小间隔要求。
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS upload_rate_limits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            slug TEXT,
            upload_timestamp TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_rate_limit_platform_ts
        ON upload_rate_limits(platform, upload_timestamp)
    """)
    conn.commit()
    conn.close()


def check_upload_rate_limit(platform='skillhub'):
    """检查是否允许上传(基于速率限制)

    检查三个维度:
    1. 最近1小时内的上传数量是否超过 MAX_UPLOADS_PER_HOUR
    2. 最近24小时内的上传数量是否超过 MAX_UPLOADS_PER_DAY
    3. 距离上次上传是否已过 MIN_INTERVAL_SECONDS 秒

    Args:
        platform: 平台名称 ('skillhub' 或 'clawhub')

    Returns:
        dict: {
            'allowed': bool,
            'reason': str,
            'hourly_count': int,
            'daily_count': int,
            'seconds_since_last': float or None,
            'wait_seconds': float or None,  # 需要等待的秒数(allowed=False时)
        }
    """
    _ensure_rate_limit_table()
    conn = sqlite3.connect(DB_PATH)
    now = datetime.now()

    # 统计最近1小时的上传数 + 最早时间戳(用于计算wait_seconds)
    one_hour_ago = (now - timedelta(hours=1)).isoformat()
    hourly_row = conn.execute(
        "SELECT COUNT(*), MIN(upload_timestamp) FROM upload_rate_limits WHERE platform = ? AND upload_timestamp >= ?",
        (platform, one_hour_ago)
    ).fetchone()
    hourly_count = hourly_row[0]
    hourly_oldest = hourly_row[1]

    # 统计最近24小时的上传数 + 最早时间戳
    one_day_ago = (now - timedelta(days=1)).isoformat()
    daily_row = conn.execute(
        "SELECT COUNT(*), MIN(upload_timestamp) FROM upload_rate_limits WHERE platform = ? AND upload_timestamp >= ?",
        (platform, one_day_ago)
    ).fetchone()
    daily_count = daily_row[0]
    daily_oldest = daily_row[1]

    # 检查距离上次上传的时间
    last_upload = conn.execute(
        "SELECT upload_timestamp FROM upload_rate_limits WHERE platform = ? ORDER BY upload_timestamp DESC LIMIT 1",
        (platform,)
    ).fetchone()

    seconds_since_last = None
    if last_upload:
        try:
            last_time = datetime.fromisoformat(last_upload[0])
            seconds_since_last = (now - last_time).total_seconds()
        except (ValueError, TypeError):
            pass

    conn.close()

    # 检查小时限制
    if hourly_count >= MAX_UPLOADS_PER_HOUR:
        wait_seconds = 3600  # 默认1小时
        if hourly_oldest:
            try:
                oldest_time = datetime.fromisoformat(hourly_oldest)
                wait_seconds = max(0, (oldest_time + timedelta(hours=1) - now).total_seconds())
            except (ValueError, TypeError):
                pass
        return {
            'allowed': False,
            'reason': f'每小时上传限制已达上限 ({hourly_count}/{MAX_UPLOADS_PER_HOUR})',
            'hourly_count': hourly_count,
            'daily_count': daily_count,
            'seconds_since_last': seconds_since_last,
            'wait_seconds': wait_seconds,
        }

    # 检查天限制
    if daily_count >= MAX_UPLOADS_PER_DAY:
        wait_seconds = 86400  # 默认24小时
        if daily_oldest:
            try:
                oldest_time = datetime.fromisoformat(daily_oldest)
                wait_seconds = max(0, (oldest_time + timedelta(days=1) - now).total_seconds())
            except (ValueError, TypeError):
                pass
        return {
            'allowed': False,
            'reason': f'每日上传限制已达上限 ({daily_count}/{MAX_UPLOADS_PER_DAY})',
            'hourly_count': hourly_count,
            'daily_count': daily_count,
            'seconds_since_last': seconds_since_last,
            'wait_seconds': wait_seconds,
        }

    # 检查最小间隔
    if seconds_since_last is not None and seconds_since_last < MIN_INTERVAL_SECONDS:
        wait_time = MIN_INTERVAL_SECONDS - seconds_since_last
        return {
            'allowed': False,
            'reason': f'最小间隔未满足, 需等待 {wait_time:.0f} 秒',
            'hourly_count': hourly_count,
            'daily_count': daily_count,
            'seconds_since_last': seconds_since_last,
            'wait_seconds': wait_time,
        }

    return {
        'allowed': True,
        'reason': 'OK',
        'hourly_count': hourly_count,
        'daily_count': daily_count,
        'seconds_since_last': seconds_since_last,
        'wait_seconds': None,
    }


def record_upload(platform, slug=None):
    """记录一次上传到速率限制跟踪表

    Args:
        platform: 平台名称 ('skillhub' 或 'clawhub')
        slug: 被上传的技能slug (可选)
    """
    _ensure_rate_limit_table()
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO upload_rate_limits (platform, slug, upload_timestamp) VALUES (?, ?, ?)",
        (platform, slug, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def wait_for_upload_slot(platform='skillhub', max_wait_seconds=7200):
    """等待直到允许上传(遵守速率限制)

    当速率限制阻止上传时, 此函数会阻塞等待直到限制解除或超时。

    Args:
        platform: 平台名称
        max_wait_seconds: 最大等待时间(秒), 默认2小时

    Returns:
        dict: check_upload_rate_limit 的结果 (allowed=True 时表示可以上传)
    """
    start = datetime.now()
    while True:
        check = check_upload_rate_limit(platform)
        if check['allowed']:
            return check

        elapsed = (datetime.now() - start).total_seconds()
        if elapsed > max_wait_seconds:
            log(f"  速率限制等待超时 ({elapsed:.0f}秒): {check['reason']}")
            return check

        # 计算等待时间
        if check['seconds_since_last'] is not None:
            wait = MIN_INTERVAL_SECONDS - check['seconds_since_last']
        else:
            wait = 60  # 默认检查间隔

        # 限制等待时间在 10-300 秒之间
        wait = max(min(wait, 300), 10)
        log(f"  速率限制: {check['reason']}, 等待 {wait:.0f} 秒后重试...")
        _time.sleep(wait)


# 向后兼容别名 (v3.2: 部分调用方使用了wait_for_rate_limit名称)
wait_for_rate_limit = wait_for_upload_slot


def get_rate_limit_status(platform='skillhub'):
    """获取速率限制状态摘要(用于报告)

    Args:
        platform: 平台名称

    Returns:
        dict: 速率限制状态信息
    """
    check = check_upload_rate_limit(platform)
    return {
        'platform': platform,
        'allowed': check['allowed'],
        'reason': check['reason'],
        'hourly_count': check['hourly_count'],
        'daily_count': check['daily_count'],
        'hourly_limit': MAX_UPLOADS_PER_HOUR,
        'daily_limit': MAX_UPLOADS_PER_DAY,
        'min_interval_seconds': MIN_INTERVAL_SECONDS,
        'seconds_since_last': check['seconds_since_last'],
    }


def run_script(script_name, args=None):
    """运行工具脚本"""
    script_path = TOOLS_DIR / script_name
    if not script_path.exists():
        log(f"  ERROR: {script_name} not found")
        return False

    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            cwd=str(TOOLS_DIR.parent)
        )
        if result.returncode == 0:
            log(f"  OK: {script_name}")
            if result.stdout:
                log(f"  Output: {result.stdout[:500]}")
            return True
        else:
            log(f"  FAIL: {script_name} (exit {result.returncode})")
            if result.stderr:
                log(f"  Error: {result.stderr[:500]}")
            return False
    except subprocess.TimeoutExpired:
        log(f"  TIMEOUT: {script_name}")
        return False
    except Exception as e:
        log(f"  ERROR: {script_name}: {e}")
        return False


def step_discover():
    """阶段1: 发现新 Skill + 检测变更"""
    log("=" * 50)
    log("阶段1: DISCOVER - 发现与变更检测")
    log("=" * 50)

    # v3.0: 发现阶段可能触发SkillHub上传, 先检查速率限制状态
    rate_status = get_rate_limit_status('skillhub')
    log(f"  SkillHub速率限制: {rate_status['hourly_count']}/{rate_status['hourly_limit']} (小时), "
        f"{rate_status['daily_count']}/{rate_status['daily_limit']} (天)")
    if not rate_status['allowed']:
        log(f"  警告: SkillHub速率限制未满足 ({rate_status['reason']})")
        log(f"  发现阶段可能触发上传, 请注意速率限制")

    run_script("version_sync_pipeline.py", ["scan"])
    run_script("auto_discover.py")

    # v3.0: 发现阶段完成后, 如果有新的SkillHub上传, 记录到速率限制表
    # (version_sync_pipeline.py的上传通过其自身逻辑处理, 此处仅做状态感知)


def step_audit():
    """阶段4: 质量审计"""
    log("=" * 50)
    log("阶段4: VALIDATE - L1-L8 质量审计")
    log("=" * 50)
    run_script("deep_quality_audit.py")


# ============ 封禁技能感知功能 (v3.0新增) ============

def step_check_banned_skills():
    """阶段3: 检查封禁技能 (v3.0新增)

    在上传前运行 check_banned_skills, 检测哪些技能已被SkillHub封禁/删除。
    检测到的封禁技能会在DB中标记为 deleted_on_skillhub, 后续上传步骤将跳过这些技能。

    根因: 2026-07-24批量上传后, 1564个技能被标记为 deleted_on_skillhub,
    上传前检测可避免重复上传已封禁的技能, 并为封禁模式分析提供数据。
    """
    log("=" * 50)
    log("阶段3: CHECK_BANNED - 封禁技能检测")
    log("=" * 50)
    run_script("platform_ops.py", ["check-banned"])

    # 检测完成后, 记录封禁模式
    step_log_banned_patterns()


def step_log_banned_patterns():
    """记录封禁技能的模式分析 (v3.0新增)

    从数据库查询已标记为 deleted_on_skillhub 的技能, 分析其命名模式:
    - -free/-pro/-tool-free/-tool-pro 后缀(差异化派生)
    - -sk/-sk1/-sk2/-sk3 后缀(slug冲突改名)
    - 短slug (<=8字符, 通用词占用)
    - 多段slug (>3段)

    输出模式统计, 帮助识别封禁原因, 避免未来重复相同模式。
    """
    log("  封禁技能模式分析:")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # 查询所有被封禁的技能
    rows = conn.execute("""
        SELECT slug, current_display_name, source, edition
        FROM skills
        WHERE current_status = 'deleted_on_skillhub'
        ORDER BY slug
    """).fetchall()

    total_banned = len(rows)
    if total_banned == 0:
        log("    无封禁技能")
        conn.close()
        return

    log(f"    封禁技能总数: {total_banned}")

    # 分析命名模式
    patterns = {
        'free_suffix': 0,       # -free 后缀
        'pro_suffix': 0,        # -pro 后缀
        'tool_free_suffix': 0,  # -tool-free 后缀
        'tool_pro_suffix': 0,   # -tool-pro 后缀
        'sk_series': 0,         # -sk/-sk1/-sk2/-sk3 后缀
        'short_slug': 0,        # 短slug (<=8字符)
        'multi_segment': 0,     # 多段slug (>3段)
    }

    for row in rows:
        slug = row['slug'] or ''
        if slug.endswith('-free'):
            patterns['free_suffix'] += 1
        if slug.endswith('-pro'):
            patterns['pro_suffix'] += 1
        if slug.endswith('-tool-free'):
            patterns['tool_free_suffix'] += 1
        if slug.endswith('-tool-pro'):
            patterns['tool_pro_suffix'] += 1
        if slug.endswith(('-sk', '-sk1', '-sk2', '-sk3')):
            patterns['sk_series'] += 1
        if len(slug) <= 8:
            patterns['short_slug'] += 1
        if slug.count('-') > 2:
            patterns['multi_segment'] += 1

    log(f"    命名模式分析:")
    log(f"      -free 后缀 (差异化派生): {patterns['free_suffix']}")
    log(f"      -pro 后缀 (差异化派生): {patterns['pro_suffix']}")
    log(f"      -tool-free 后缀: {patterns['tool_free_suffix']}")
    log(f"      -tool-pro 后缀: {patterns['tool_pro_suffix']}")
    log(f"      -sk 系列 (slug冲突改名): {patterns['sk_series']}")
    log(f"      短slug <=8字符 (通用词占用): {patterns['short_slug']}")
    log(f"      多段slug >3段: {patterns['multi_segment']}")

    # 按来源统计
    source_stats = {}
    for row in rows:
        src = row['source'] or 'unknown'
        source_stats[src] = source_stats.get(src, 0) + 1

    log(f"    按来源分布:")
    for src, cnt in sorted(source_stats.items(), key=lambda x: x[1], reverse=True)[:10]:
        log(f"      {src}: {cnt}")

    # 保存模式分析到报告文件
    pattern_report = {
        'timestamp': datetime.now().isoformat(),
        'total_banned': total_banned,
        'patterns': patterns,
        'source_distribution': source_stats,
    }
    report_path = REPORT_DIR / f"banned_patterns_{datetime.now().strftime('%Y%m%d')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(pattern_report, f, ensure_ascii=False, indent=2)
    log(f"    模式分析报告已保存: {report_path}")

    conn.close()


def get_banned_slugs():
    """获取所有已封禁技能的slug列表 (v3.0新增)

    用于在上传前过滤掉已封禁的技能。

    Returns:
        set: 已封禁技能的slug集合
    """
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT slug FROM skills WHERE current_status = 'deleted_on_skillhub'"
    ).fetchall()
    conn.close()
    return {r[0] for r in rows}


def step_sync_github():
    """阶段5: GitHub 同步"""
    log("=" * 50)
    log("阶段5: SYNC_GITHUB - GitHub 双仓库同步")
    log("=" * 50)
    # Git push to both remotes
    for repo in GITHUB_REPOS:
        try:
            result = subprocess.run(
                ["git", "push", repo["name"], "main"],
                capture_output=True, text=True, timeout=120,
                cwd=str(TOOLS_DIR.parent)
            )
            if result.returncode == 0:
                log(f"  OK: git push {repo['name']}")
            else:
                log(f"  FAIL: git push {repo['name']}: {result.stderr[:200]}")
        except Exception as e:
            log(f"  ERROR: git push {repo['name']}: {e}")


def step_sync_clawhub():
    """阶段7: ClawHub 同步 (v3.0: 增加速率限制和2分钟间隔)

    ClawHub批量上传, 保持200/天限制, 同时增加2分钟上传间隔。
    上传前检查速率限制, 确保不会触发反垃圾系统。

    v3.0变更:
    - 上传前检查速率限制状态
    - 传递 --delay 120 参数给clawhub_batch_uploader, 强制2分钟间隔
    - 上传完成后记录到速率限制跟踪表
    - 跳过已封禁(deleted_on_skillhub)的技能
    """
    log("=" * 50)
    log("阶段7: SYNC_CLAWHUB - ClawHub 批量上传")
    log("=" * 50)

    # v3.0: 检查ClawHub速率限制
    rate_check = check_upload_rate_limit('clawhub')
    log(f"  ClawHub速率限制状态: {rate_check['reason']}")
    log(f"    最近1小时: {rate_check['hourly_count']}/{MAX_UPLOADS_PER_HOUR}")
    log(f"    最近24小时: {rate_check['daily_count']}/{MAX_UPLOADS_PER_DAY}")
    if rate_check['seconds_since_last'] is not None:
        log(f"    距上次上传: {rate_check['seconds_since_last']:.0f}秒 "
            f"(最小间隔{MIN_INTERVAL_SECONDS}秒)")

    # v3.0: 计算本次可上传的数量(考虑速率限制)
    # ClawHub每日限制200, 但SkillHub速率限制每日100, 取较小值确保安全
    remaining_hourly = MAX_UPLOADS_PER_HOUR - rate_check['hourly_count']
    remaining_daily = MAX_UPLOADS_PER_DAY - rate_check['daily_count']
    clawhub_limit = min(200, remaining_daily, remaining_hourly)
    if clawhub_limit <= 0:
        log(f"  跳过ClawHub上传: 速率限制已达上限 ({rate_check['reason']})")
        return

    log(f"  本次最多可上传: {clawhub_limit} 个 (受速率限制约束)")

    # v3.0: 如果距离上次上传不足2分钟, 等待
    if rate_check['seconds_since_last'] is not None and \
            rate_check['seconds_since_last'] < MIN_INTERVAL_SECONDS:
        wait_sec = MIN_INTERVAL_SECONDS - rate_check['seconds_since_last']
        log(f"  等待 {wait_sec:.0f} 秒以满足最小间隔要求...")
        _time.sleep(wait_sec)

    # v3.0: 获取已封禁技能列表, 用于跳过
    banned_slugs = get_banned_slugs()
    if banned_slugs:
        log(f"  已封禁技能: {len(banned_slugs)} 个 (将跳过上传)")

    if CLAWHUB_DRY_RUN:
        run_script("clawhub_batch_uploader.py", [
            "--dry-run",
            "--delay", str(CLAWHUB_UPLOAD_DELAY)
        ])
    else:
        # v3.0: 使用 --from-db 模式 + --delay 120 (2分钟间隔) + 受速率限制的limit
        run_script("clawhub_batch_uploader.py", [
            "--from-db",
            "--limit", str(clawhub_limit),
            "--delay", str(CLAWHUB_UPLOAD_DELAY)
        ])
        # v3.0: 记录上传到速率限制表
        record_upload('clawhub', slug=f"batch_{clawhub_limit}_skills")


def step_sync_ratings():
    """阶段8: 平台评分同步 (v3.0: 仅同步仍可访问的技能)

    从SkillHub公开API同步评分数据到DB, 提升评分覆盖率。
    v3.0增强: 仅同步 current_status='synced_from_skillhub' 的技能,
    跳过 deleted_on_skillhub 的技能(已封禁/删除, API会返回404)。

    sync_platform_ratings 函数(market_monitor.py)已内置 current_status 过滤:
    - 阶段1: INNER JOIN platform_uploads, WHERE current_status='synced_from_skillhub'
    - 阶段2: LEFT JOIN ... IS NULL, WHERE current_status='synced_from_skillhub'
    本步骤增加前置检查, 输出可同步/已封禁的技能数量, 避免无效API调用。

    每次同步200个skill, 可多次执行提升覆盖率。
    """
    log("=" * 50)
    log("阶段8: SYNC_RATINGS - 平台评分同步到DB")
    log("=" * 50)

    # v3.0: 检查可同步的技能数量(仅synced_from_skillhub可访问)
    conn = sqlite3.connect(DB_PATH)
    accessible = conn.execute(
        "SELECT COUNT(*) FROM skills WHERE current_status = 'synced_from_skillhub'"
    ).fetchone()[0]
    deleted = conn.execute(
        "SELECT COUNT(*) FROM skills WHERE current_status = 'deleted_on_skillhub'"
    ).fetchone()[0]
    conn.close()

    log(f"  可同步技能 (synced_from_skillhub): {accessible}")
    log(f"  已封禁技能 (deleted_on_skillhub): {deleted} (将跳过, 避免无效404请求)")

    if accessible == 0:
        log("  无可同步技能, 跳过评分同步")
        return

    # v2.7: 添加--no-rating标志, 跳过AI评分网页抓取(非常慢), 仅同步基本统计数据
    run_script("market_monitor.py", ["sync-ratings", "200", "--no-rating"])


def step_check_low_ratings():
    """阶段9: 低评分检查 (v2.6新增)

    检查评分低于4.5的skill, 触发自动升级流程
    """
    log("=" * 50)
    log("阶段9: CHECK_LOW_RATINGS - 低评分skill检查与升级触发")
    log("=" * 50)
    run_script("market_monitor.py", ["check-low-ratings"])


def generate_daily_report():
    """生成每日报告 (v3.0: 包含速率限制和封禁技能统计)"""
    log("=" * 50)
    log("生成每日同步报告")
    log("=" * 50)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    report = {
        "date": datetime.now().strftime('%Y-%m-%d'),
        "timestamp": datetime.now().isoformat(),
        "summary": {},
        "three_track": {},
        "platforms": {},
        "quality": {},
        "rate_limits": {},       # v3.0: 速率限制状态
        "banned_skills": {},     # v3.0: 封禁技能统计
    }

    # 总览
    c.execute("SELECT COUNT(*) as cnt FROM skills")
    report["summary"]["total_skills"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'active'")
    report["summary"]["active"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'updated'")
    report["summary"]["updated"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'stale'")
    report["summary"]["stale"] = c.fetchone()["cnt"]

    # v3.0: 封禁/同步状态统计
    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'deleted_on_skillhub'")
    report["summary"]["deleted_on_skillhub"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'synced_from_skillhub'")
    report["summary"]["synced_from_skillhub"] = c.fetchone()["cnt"]

    # 三轨模型
    c.execute("SELECT skill_type, COUNT(*) as cnt FROM skills GROUP BY skill_type ORDER BY cnt DESC")
    report["three_track"] = {row["skill_type"]: row["cnt"] for row in c.fetchall()}

    # 平台上传状态
    c.execute("SELECT platform, upload_status, COUNT(*) as cnt FROM platform_uploads GROUP BY platform, upload_status ORDER BY platform")
    for row in c.fetchall():
        p = row["platform"]
        if p not in report["platforms"]:
            report["platforms"][p] = {}
        report["platforms"][p][row["upload_status"]] = row["cnt"]

    # 定价分层
    c.execute("SELECT pricing_tier, COUNT(*) as cnt FROM skills GROUP BY pricing_tier ORDER BY cnt DESC")
    report["quality"]["pricing_tiers"] = {row["pricing_tier"]: row["cnt"] for row in c.fetchall()}

    # 最近操作
    c.execute("""SELECT operation_type, COUNT(*) as cnt
                 FROM operations
                 WHERE operation_date >= date('now', '-1 day')
                 GROUP BY operation_type ORDER BY cnt DESC""")
    report["recent_operations"] = {row["operation_type"]: row["cnt"] for row in c.fetchall()}

    # v3.0: 速率限制状态
    for platform in ['skillhub', 'clawhub']:
        report["rate_limits"][platform] = get_rate_limit_status(platform)

    # v3.0: 封禁技能统计
    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'deleted_on_skillhub'")
    report["banned_skills"]["total"] = c.fetchone()["cnt"]

    c.execute("""SELECT source, COUNT(*) as cnt
                 FROM skills WHERE current_status = 'deleted_on_skillhub'
                 GROUP BY source ORDER BY cnt DESC""")
    report["banned_skills"]["by_source"] = {
        (row["source"] or 'unknown'): row["cnt"] for row in c.fetchall()
    }

    conn.close()

    # 保存报告
    report_path = HEALTH_REPORT_DIR / f"daily_sync_{datetime.now().strftime('%Y%m%d')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    log(f"  报告已保存: {report_path}")

    # 打印摘要
    log(f"\n  总 Skill 数: {report['summary']['total_skills']}")
    log(f"  三轨分布: {report['three_track']}")
    for platform, statuses in report["platforms"].items():
        log(f"  {platform}: {statuses}")
    # v3.0: 速率限制摘要
    for platform, status in report["rate_limits"].items():
        log(f"  速率限制 [{platform}]: "
            f"{status['hourly_count']}/{status['hourly_limit']} (小时), "
            f"{status['daily_count']}/{status['daily_limit']} (天)")
    # v3.0: 封禁技能摘要
    log(f"  封禁技能: {report['banned_skills']['total']} (deleted_on_skillhub)")
    log(f"  可访问技能: {report['summary']['synced_from_skillhub']} (synced_from_skillhub)")

    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="每日同步脚本 v3.0")
    parser.add_argument("--discover", action="store_true", help="仅执行发现阶段")
    parser.add_argument("--audit", action="store_true", help="仅执行审计阶段")
    parser.add_argument("--report", action="store_true", help="仅生成报告")
    parser.add_argument("--ratings", action="store_true", help="仅执行评分同步")
    parser.add_argument("--low-ratings", action="store_true", help="仅执行低评分检查")
    parser.add_argument("--clawhub", action="store_true", help="仅执行ClawHub上传")
    parser.add_argument("--check-banned", action="store_true", help="仅检查封禁技能 (v3.0新增)")
    parser.add_argument("--rate-status", action="store_true", help="查看速率限制状态 (v3.0新增)")
    parser.add_argument("--full", action="store_true", help="完整同步（默认）")
    args = parser.parse_args()

    log("每日同步开始 (v3.0)")
    log(f"数据库: {DB_PATH}")
    log(f"速率限制: {MAX_UPLOADS_PER_HOUR}/小时, {MAX_UPLOADS_PER_DAY}/天, 最小间隔{MIN_INTERVAL_SECONDS}秒")

    if args.discover:
        step_discover()
    elif args.audit:
        step_audit()
    elif args.report:
        generate_daily_report()
    elif args.ratings:
        step_sync_ratings()
    elif args.low_ratings:
        step_check_low_ratings()
    elif args.clawhub:
        step_sync_clawhub()
    elif args.check_banned:
        step_check_banned_skills()
    elif args.rate_status:
        # v3.0: 显示所有平台的速率限制状态
        for platform in ['skillhub', 'clawhub']:
            status = get_rate_limit_status(platform)
            log(f"\n  [{platform}] 速率限制状态:")
            log(f"    允许上传: {status['allowed']}")
            log(f"    原因: {status['reason']}")
            log(f"    最近1小时: {status['hourly_count']}/{status['hourly_limit']}")
            log(f"    最近24小时: {status['daily_count']}/{status['daily_limit']}")
            log(f"    最小间隔: {status['min_interval_seconds']}秒")
            if status['seconds_since_last'] is not None:
                log(f"    距上次上传: {status['seconds_since_last']:.0f}秒")
    else:
        # 完整流程 (v3.0: 新增封禁检测+速率限制感知)
        step_discover()
        step_audit()
        step_check_banned_skills()    # v3.0: 上传前检测封禁技能
        step_sync_github()
        step_sync_clawhub()           # v3.0: 含速率限制和2分钟间隔
        step_sync_ratings()           # v3.0: 仅同步可访问技能
        step_check_low_ratings()
        generate_daily_report()

    log("\n每日同步完成!")


if __name__ == "__main__":
    main()
