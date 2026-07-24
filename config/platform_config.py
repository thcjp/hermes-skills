#!/usr/bin/env python3
"""
平台配置中心
=============
统一管理所有上传平台的配置：SkillHub、ClawHub、GitHub双仓库。
所有脚本从此模块导入平台配置，消除散乱定义。
"""

from project_config import PROJECT_ROOT

# ============ SkillHub 配置 ============

SKILLHUB_CLI_PATH = "skillhub"  # CLI命令名
SKILLHUB_API_URL = "https://api.skillhub.ai"
SKILLHUB_WAF_CHAR_LIMIT = 5800  # WAF请求体字符限制
SKILLHUB_PUBLISH_COMMAND = "skillhub publish"  # 发布命令模板
SKILLHUB_CREDENTIALS_FILE = PROJECT_ROOT / ".credentials" / "skillhub.json"
SKILLHUB_MAX_RETRIES = 3

# SkillHub审核状态
SKILLHUB_STATUSES = {
    'success', 'pending_review', 'published', 'rejected',
    'blocked', 'failed', 'retry_pending'
}

# ============ ClawHub 配置 ============

CLAWHUB_CLI_PATH = "npx clawhub"
CLAWHUB_API_URL = "https://api.clawhub.dev"
CLAWHUB_DAILY_UPLOAD_LIMIT = 200  # 每24小时上传限制
CLAWHUB_RATE_LIMIT_HOURS = 24
CLAWHUB_TOKEN_FILE = PROJECT_ROOT / ".credentials" / "clawhub_token.json"
CLAWHUB_PUBLISH_COMMAND = "npx clawhub publish"
CLAWHUB_PROTECTED_PREFIX = "openclaw-"  # 受保护的命名空间前缀

# ============ GitHub 双仓库配置 ============

# 公开引流仓库（仅免费skill）
GITHUB_PUBLIC_REMOTE = "hermes-skills"
GITHUB_PUBLIC_REPO_URL = "https://github.com/thcjp/hermes-skills"
GITHUB_PUBLIC_VISIBILITY = "public"

# 私有备份仓库（全部skill + 项目代码）
GITHUB_PRIVATE_REMOTE = "origin"
GITHUB_PRIVATE_REPO_URL = "https://github.com/thcjp/-.git"
GITHUB_PRIVATE_VISIBILITY = "private"

# 分支
GITHUB_BRANCH = "main"

# 免费/付费判定规则（与github_repo_strategy.py一致）
FREE_PRICING_VALUES = {"free", "Free", "FREE"}
FREE_PRICING_TIERS = {"L1-入门级", "L2-标准级"}
FREE_LICENSES = {"MIT", "Apache-2.0"}
PAID_PRICING_TIERS = {"L3-专业级", "L4-企业级"}
PAID_LICENSES = {"Proprietary", "Commercial"}

# GitHub Git 远程仓库配置（供推送使用）
GITHUB_REPOS = [
    {
        "name": GITHUB_PUBLIC_REMOTE,
        "url": GITHUB_PUBLIC_REPO_URL,
        "visibility": GITHUB_PUBLIC_VISIBILITY,
        "push_free": True,
        "push_paid": True,  # 付费skill也推送到公开引流仓库（与clawhub付费版一致）
        "paid_strategy": "clawhub_aligned",  # 付费版与clawhub保持一致
    },
    {
        "name": GITHUB_PRIVATE_REMOTE,
        "url": GITHUB_PRIVATE_REPO_URL,
        "visibility": GITHUB_PRIVATE_VISIBILITY,
        "push_free": True,
        "push_paid": True,
    },
]

# GitHub 扫描仓库列表（供 auto_discover.py 和 multi_source_discover.py 发现新 skill 使用）
GITHUB_SCAN_REPOS = [
    {"owner": "anthropics", "repo": "skills", "license": "Apache-2.0"},
    {"owner": "obra", "repo": "superpowers", "license": "MIT"},
    {"owner": "addyosmani", "repo": "agent-skills", "license": "MIT"},
    {"owner": "ComposioHQ", "repo": "awesome-claude-skills", "license": "mixed"},
    {"owner": "VoltAgent", "repo": "awesome-openclaw-skills", "license": "mixed"},
    # 高星 AI Agent / LLM 项目仓库（可能包含可提取的 skill 或 tool）
    {"owner": "humanlayer", "repo": "12-factor-agents", "license": "MIT"},
    {"owner": "langchain-ai", "repo": "langgraph", "license": "MIT"},
    {"owner": "crewAIInc", "repo": "crewAI", "license": "MIT"},
    {"owner": "microsoft", "repo": "autogen", "license": "MIT"},
    {"owner": "openai", "repo": "openai-agents-python", "license": "MIT"},
    {"owner": "ollama", "repo": "ollama", "license": "MIT"},
    {"owner": "vllm-project", "repo": "vllm", "license": "Apache-2.0"},
    {"owner": "huggingface", "repo": "transformers", "license": "Apache-2.0"},
    {"owner": "ggerganov", "repo": "llama.cpp", "license": "MIT"},
    {"owner": "run-llama", "repo": "llama_index", "license": "MIT"},
]


def is_free_skill(pricing: str = "", pricing_tier: str = "", license_val: str = "") -> bool:
    """判断skill是否为免费skill（推送到公开引流仓库）

    Args:
        pricing: frontmatter中的pricing字段值
        pricing_tier: frontmatter中的pricing_tier字段值
        license_val: frontmatter中的license字段值

    Returns:
        True if free skill (可以推送到公开引流仓库)
        False if paid skill (仅推送到私有备份仓库)
    """
    if pricing and pricing.lower() in FREE_PRICING_VALUES:
        return True
    if pricing_tier and pricing_tier in FREE_PRICING_TIERS:
        return True
    if license_val and license_val in FREE_LICENSES:
        return True
    return False


def get_push_strategy(pricing: str = "", pricing_tier: str = "", license_val: str = "") -> dict:
    """获取推送策略

    Returns:
        {
            'is_free': bool,
            'push_to_public': bool,
            'push_to_private': bool,
            'visibility': str,
        }
    """
    free = is_free_skill(pricing, pricing_tier, license_val)
    return {
        'is_free': free,
        'push_to_public': free,
        'push_to_private': True,  # 所有skill都推送到私有备份
        'visibility': 'public' if free else 'private',
    }
