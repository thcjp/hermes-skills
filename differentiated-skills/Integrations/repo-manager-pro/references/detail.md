# 详细参考 - repo-manager-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
{
  "edition": "pro",
  "integration": {
    "github": {
      "connected": true,
      "scope": ["repo", "workflow", "read:org"]
    }
  },
  "batch": {
    "default_parallel": 3,
    "max_parallel": 10,
    "rate_limit_qps": 10,
    "checkpoint_enabled": true,
    "dry_run_by_default": true
  },
  "search": {
    "index_enabled": true,
    "cache_ttl": 300,
    "fuzzy_match": true
  },
  "custom_integrations": [
    {
      "name": "my-ci-tool",
      "endpoint": "https://mcp.my-company.com/ci",
      "auth_token_env": "MCP_TOKEN"
    }
  ],
  "team": {
    "name": "dev-team",
    "members": ["alice", "bob", "carol"],
    "shared_repos": ["owner/repo1", "owner/repo2"]
  },
  "release": {
    "auto_changelog": true,
    "artifact_pattern": "dist/*.zip",
    "notify_on_publish": true
  }
}
```

## 代码示例 (bash)

```bash
repo-manager call --tool "github_list_releases" --params '{
  "owner": "owner",
  "repo": "repo-name"
}'

repo-manager call --tool "github_get_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "release_id": 123
}'

repo-manager call --tool "github_create_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "tag_name": "v1.2.0",
  "name": "v1.2.0 - 性能优化版本",
  "body": "## 新增\n- 功能A\n## 修复\n- Bug #123\n## 优化\n- 性能提升30%",
  "draft": false,
  "prerelease": false
}' --confirm

repo-manager call --tool "github_update_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "release_id": 123,
  "body": "更新发布说明"
}' --confirm

repo-manager call --tool "github_delete_a_release" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "release_id": 123
}' --confirm --force
```

## 代码示例 (bash)

```bash
repo-manager call --tool "github_list_repository_workflows" --params '{
  "owner": "owner",
  "repo": "repo-name"
}'

repo-manager call --tool "github_list_workflow_runs" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "status": "in_progress"
}'

repo-manager call --tool "github_get_a_workflow_run" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "run_id": 123456
}'

repo-manager call --tool "github_cancel_workflow_run" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "run_id": 123456
}' --confirm

repo-manager call --tool "github_rerun_workflow_failed_jobs" --params '{
  "owner": "owner",
  "repo": "repo-name",
  "run_id": 123456
}' --confirm
```

