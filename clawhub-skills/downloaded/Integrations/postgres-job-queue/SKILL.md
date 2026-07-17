---
slug: postgres-job-queue
name: postgres-job-queue
version: "1.0.0"
displayName: Postgres Job Queue
summary: PostgreSQL-based job queue with priority scheduling, batch claiming, and
  progress tracking. Use w...
license: MIT
description: |-
  PostgreSQL-based job queue with priority scheduling, batch claiming,
  and progress tracking. Use w...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: based, priority, postgresql, job, queue, postgres
tags:
- Integrations
tools:
- read
- exec
---

# Postgres Job Queue

Production-ready job queue using PostgreSQL with priority scheduling, batch claiming, and progress tracking.

---

## When to Use

* Need job queue but want to avoid Redis/RabbitMQ dependencies
* Jobs need priority-based scheduling
* Long-running jobs need progress visibility
* Jobs should survive service restarts

---

## Schema Design

```sql
CREATE TABLE jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_type VARCHAR(50) NOT NULL,
    priority INT NOT NULL DEFAULT 100,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    data JSONB NOT NULL DEFAULT '{}',

    -- Progress tracking
    progress INT DEFAULT 0,
    current_stage VARCHAR(100),
    events_count INT DEFAULT 0,

    -- Worker tracking
    worker_id VARCHAR(100),
    claimed_at TIMESTAMPTZ,

    -- Timing
    created_at TIMESTAMPTZ DEFAULT NOW(),
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,

    -- Retry handling
    attempts INT DEFAULT 0,
    max_attempts INT DEFAULT 3,
    last_error TEXT,

    CONSTRAINT valid_status CHECK (
        status IN ('pending', 'claimed', 'running', 'completed', 'failed', 'cancelled')
    )
);

-- Critical: Partial index for fast claiming
CREATE INDEX idx_jobs_claimable ON jobs (priority DESC, created_at ASC)
    WHERE status = 'pending';
CREATE INDEX idx_jobs_worker ON jobs (worker_id)
    WHERE status IN ('claimed', 'running');
```

---

## Batch Claiming with SKIP LOCKED

```sql
CREATE OR REPLACE FUNCTION claim_job_batch(
    p_worker_id VARCHAR(100),
    p_job_types VARCHAR(50)[],
    p_batch_size INT DEFAULT 10
) RETURNS SETOF jobs AS $$
BEGIN
    RETURN QUERY
    WITH claimable AS (
        SELECT id
        FROM jobs
        WHERE status = 'pending'
          AND job_type = ANY(p_job_types)
          AND attempts < max_attempts
        ORDER BY priority DESC, created_at ASC
        LIMIT p_batch_size
        FOR UPDATE SKIP LOCKED  -- Critical: skip locked rows
    ),
    claimed AS (
        UPDATE jobs
        SET status = 'claimed',
            worker_id = p_worker_id,
            claimed_at = NOW(),
            attempts = attempts + 1
        WHERE id IN (SELECT id FROM claimable)
        RETURNING *
    )
    SELECT * FROM claimed;
END;
$$ LANGUAGE plpgsql;
```

---

## Go Implementation

```go
const (
    PriorityExplicit   = 150  // User-requested
    PriorityDiscovered = 100  // System-discovered
    PriorityBackfill   = 30   // Background backfills
)

type JobQueue struct {
    db       *pgx.Pool
    workerID string
}

func (q *JobQueue) Claim(ctx context.Context, types []string, batchSize int) ([]Job, error) {
    rows, err := q.db.Query(ctx,
        "SELECT * FROM claim_job_batch($1, $2, $3)",
        q.workerID, types, batchSize,
    )
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    var jobs []Job
    for rows.Next() {
        var job Job
        if err := rows.Scan(&job); err != nil {
            return nil, err
        }
        jobs = append(jobs, job)
    }
    return jobs, nil
}

func (q *JobQueue) Complete(ctx context.Context, jobID uuid.UUID) error {
    _, err := q.db.Exec(ctx, `
        UPDATE jobs
        SET status = 'completed',
            progress = 100,
            completed_at = NOW()
        WHERE id = $1`,
        jobID,
    )
    return err
}

func (q *JobQueue) Fail(ctx context.Context, jobID uuid.UUID, errMsg string) error {
    _, err := q.db.Exec(ctx, `
        UPDATE jobs
        SET status = CASE
                WHEN attempts >= max_attempts THEN 'failed'
                ELSE 'pending'
            END,
            last_error = $2,
            worker_id = NULL,
            claimed_at = NULL
        WHERE id = $1`,
        jobID, errMsg,
    )
    return err
}
```

---

## Stale Job Recovery

```go
func (q *JobQueue) RecoverStaleJobs(ctx context.Context, timeout time.Duration) (int, error) {
    result, err := q.db.Exec(ctx, `
        UPDATE jobs
        SET status = 'pending',
            worker_id = NULL,
            claimed_at = NULL
        WHERE status IN ('claimed', 'running')
          AND claimed_at < NOW() - $1::interval
          AND attempts < max_attempts`,
        timeout.String(),
    )
    if err != nil {
        return 0, err
    }
    return int(result.RowsAffected()), nil
}
```

---

## Decision Tree

| Scenario | Approach |
| --- | --- |
| Need guaranteed delivery | PostgreSQL queue |
| Need sub-ms latency | Use Redis instead |
| < 1000 jobs/sec | PostgreSQL is fine |
| > 10000 jobs/sec | Add Redis layer |
| Need strict ordering | Single worker per type |

---

## Related Skills

* **Related:** service-layer-architecture — Service patterns for job handlers
* **Related:** realtime/dual-stream-architecture — Event publishing from jobs

---

## NEVER Do

* **NEVER use SELECT then UPDATE** — Race condition. Use SKIP LOCKED.
* **NEVER claim without SKIP LOCKED** — Workers will deadlock.
* **NEVER store large payloads** — Store references only.
* **NEVER forget partial index** — Claiming is slow without it.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
