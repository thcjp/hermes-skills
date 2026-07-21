# 详细参考 - cloud-storage-manager-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
team:
  name: DataTeam
  description: 数据团队协作空间

roles:
  admin:
    permissions:
      - provider.config
      - team.manage
      - operation.upload
      - operation.download
      - operation.delete
      - cost.view
      - cost.report

  operator:
    permissions:
      - operation.upload
      - operation.download
      - cost.view

  viewer:
    permissions:
      - operation.list
      - cost.view

members:
  - email: alice@corp.com
    role: admin
  - email: bob@corp.com
    role: operator
  - email: charlie@corp.com
    role: viewer
```

## 代码示例 (yaml)

```yaml
policies:
  - bucket: s3://data-lake/
    rules:
      - name: hot-to-warm
        filter:
          age: ">30d"
          access_freq: "<daily"
        transition: STANDARD_IA
        notify: true

      - name: warm-to-cold
        filter:
          age: ">90d"
          access_freq: "<weekly"
        transition: GLACIER

      - name: cold-to-archive
        filter:
          age: ">365d"
        transition: DEEP_ARCHIVE

      - name: expired-delete
        filter:
          age: ">2555d"  # 7年合规保留期
        action: delete
        require_approval: true
```

## 代码示例 (yaml)

```yaml
pairs:
  - name: drive-onedrive-sync
    left: gdrive://team-a/shared/
    right: onedrive://team-b/shared/
    conflict_strategy: latest-wins
    realtime: true
    debounce: 5s
    exclude:
      - "*.tmp"
      - ".DS_Store"
    notify:
      webhook: https://my.endpoint/sync-event
      on_conflict: true

  - name: s3-r2-backup
    left: s3://primary/
    right: r2://backup/
    conflict_strategy: left-wins
    schedule: "0 */6 * * *"
    delete_distant: false
```

## 代码示例 (yaml)

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: cloud-sync
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: csm-sync
            image: csm/cli:pro-latest
            args: ["sync", "--config", "/etc/csm/sync.yaml"]
            env:
            - name: AWS_ACCESS_KEY_ID
              valueFrom:
                secretKeyRef:
                  name: cloud-secrets
                  key: aws-access-key
```

