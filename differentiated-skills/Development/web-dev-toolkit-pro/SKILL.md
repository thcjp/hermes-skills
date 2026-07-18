---
slug: web-dev-toolkit-pro
name: web-dev-toolkit-pro
version: "1.0.0"
displayName: Web开发工具集(专业版)
summary: 面向团队的企业级Web开发平台,含性能工程、SEO深度、WCAG审查、企业部署与监控。
license: MIT
edition: pro
description: |-
  Web开发工具集专业版为团队与企业提供端到端Web开发工程能力,涵盖性能工程化、SEO深度优化、WCAG AA可访问性审查、企业级部署与监控告警。

  核心能力:
  - 性能工程化(Lighthouse CI/性能预算/监控)
  - SEO深度优化(结构化数据/站点地图/国际化)
  - WCAG AA可访问性审查与改造
  - 企业级部署(多环境/蓝绿/灰度)
  - 监控告警(RUM/Sentry/告警规则)
  - 多框架工程化(Next.js/Remix/Astro)

  适用场景:
  - 中大型团队Web产品性能与SEO优化
  - 企业产品WCAG AA合规改造
  - 多环境部署与灰度发布
  - 生产监控与告警体系搭建

  差异化:专业版兼容免费版的所有建议与代码片段,扩展企业级性能、SEO、可访问性、部署与监控能力,适合规模化团队与生产级产品。

  触发关键词: web, 性能优化, lighthouse, seo, wcag, 可访问性, 企业部署, 监控, rum, sentry, 性能预算
tags:
- Web开发
- 性能优化
- 企业开发
- 可访问性
- SEO
- 监控告警
- CI/CD
tools:
- read
- exec
---

# Web 开发工具集(专业版)

## 概述

`web-dev-toolkit-pro` 是面向团队与企业的端到端 Web 开发工程平台。它在免费版基础 Web 开发辅助之上,扩展了性能工程化、SEO 深度优化、WCAG AA 可访问性审查、企业级部署与监控告警能力,帮助团队构建高性能、可访问、可监控的生产级 Web 产品。

本版本完全兼容免费版输出的所有建议与代码片段,可平滑升级。所有指令通过 Markdown 驱动 Agent,配套脚本用于性能测试、可访问性审查与 CI 集成。

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
| --- | --- | --- |
| 基础 Web 开发 | 免费版全部 HTML/CSS、JS、框架、部署能力 | 完全兼容 |
| 性能工程化 | Lighthouse CI、性能预算、RUM 监控 | Pro 新增 |
| SEO 深度优化 | 结构化数据、站点地图、国际化 hreflang | Pro 新增 |
| WCAG AA 审查 | 自动化审查与改造,达到合规 | Pro 新增 |
| 企业级部署 | 多环境、蓝绿、灰度、CDN 配置 | Pro 新增 |
| 监控告警 | RUM、Sentry、告警规则、SLO | Pro 新增 |
| 多框架工程化 | Next.js / Remix / Astro 深度配置 | Pro 新增 |

## 使用场景

### 场景 1:性能工程化(性能预算 + Lighthouse CI)

为团队建立性能预算,并在 CI 中自动执行 Lighthouse 审查。

```jsonc
// .lighthouserc.json — Lighthouse CI 配置
{
  "ci": {
    "collect": {
      "url": [
        "http://localhost:3000/",
        "http://localhost:3000/dashboard",
        "http://localhost:3000/profile"
      ],
      "numberOfRuns": 3,
      "startServerCommand": "npm run start",
      "settings": {
        "preset": "desktop"
      }
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.9 }],
        "categories:accessibility": ["error", { "minScore": 0.95 }],
        "categories:seo": ["error", { "minScore": 0.95 }],
        "categories:best-practices": ["warn", { "minScore": 0.9 }],
        "first-contentful-paint": ["error", { "maxNumericValue": 1800 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["error", { "maxNumericValue": 200 }]
      }
    },
    "upload": {
      "target": "lhci",
      "serverBaseUrl": "https://lhci.your-org.com"
    }
  }
}
```

```yaml
# .github/workflows/lighthouse.yml — CI 集成
name: Lighthouse CI
on:
  pull_request:
    branches: [main]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      - name: Lighthouse CI
        run: npx @lhci/cli autorun
```

### 场景 2:WCAG AA 可访问性审查

生成审查脚本,对页面进行 WCAG AA 合规检查并输出报告。

```bash
#!/usr/bin/env bash
# scripts/a11y-audit.sh — WCAG AA 可访问性审查
set -euo pipefail

PAGES=(
  "http://localhost:3000/"
  "http://localhost:3000/dashboard"
  "http://localhost:3000/profile"
)

REPORT_DIR="reports/a11y"
mkdir -p "$REPORT_DIR"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

echo "=== WCAG AA 可访问性审查 ==="
echo ""

for url in "${PAGES[@]}"; do
  echo "[审查] $url"
  npx pa11y "$url" --standard WCAG2AA \
    --reporter json \
    > "$REPORT_DIR/$(echo $url | sed 's/[^a-zA-Z0-9]/-/g')-$TIMESTAMP.json" \
    || true
done

# 汇总
echo ""
echo "=== 汇总 ==="
total_issues=$(jq '[.[].issues | length] | add' $REPORT_DIR/*-$TIMESTAMP.json 2>/dev/null || echo "0")
echo "总问题数: $total_issues"
echo "报告目录: $REPORT_DIR/"
```

### 场景 3:SEO 深度优化(结构化数据 + 国际化)

为多语言站点配置结构化数据与 hreflang。

```html
<!-- 多语言 SEO 头部 -->
<head>
  <!-- 主语言声明 -->
  <html lang="zh-CN">

  <!-- hreflang 多语言声明 -->
  <link rel="alternate" hreflang="zh-CN" href="https://example.com/zh/" />
  <link rel="alternate" hreflang="en-US" href="https://example.com/en/" />
  <link rel="alternate" hreflang="ja-JP" href="https://example.com/ja/" />
  <link rel="alternate" hreflang="x-default" href="https://example.com/" />

  <!-- Open Graph -->
  <meta property="og:title" content="页面标题">
  <meta property="og:description" content="页面描述">
  <meta property="og:image" content="https://example.com/og.png">
  <meta property="og:url" content="https://example.com/zh/">
  <meta property="og:type" content="website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="页面标题">
  <meta name="twitter:image" content="https://example.com/og.png">

  <!-- 结构化数据(JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "公司名",
    "url": "https://example.com",
    "logo": "https://example.com/logo.png",
    "sameAs": [
      "https://twitter.com/yourorg",
      "https://www.linkedin.com/company/yourorg"
    ]
  }
  </script>
</head>
```

### 场景 4:企业级蓝绿部署

```yaml
# .github/workflows/deploy.yml — 蓝绿部署
name: Blue-Green Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: 部署到 Green 环境
        run: |
          npx vercel deploy --prod --token ${{ secrets.VERCEL_TOKEN }} \
            --name ${{ env.PROJECT_NAME }}-green

      - name: 健康检查 Green
        run: |
          for i in {1..10}; do
            STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://green.your-app.com/health)
            if [ "$STATUS" = "200" ]; then
              echo "Green 健康"
              break
            fi
            sleep 10
          done

      - name: 切换流量到 Green
        run: |
          # 更新 CDN/DNS 指向 Green
          npx vercel alias set ${{ env.PROJECT_NAME }}-green your-app.com \
            --token ${{ secrets.VERCEL_TOKEN }}

      - name: 保留 Blue 作为回滚
        run: echo "Blue 环境保留 1 小时用于回滚"
```

## 快速开始

### 第一步:声明团队上下文

在对话中说明团队规模、产品类型与质量目标,例如:

```
我们是 15 人的前端团队,生产环境是 Next.js 部署在 Vercel,
需要性能预算(LCP < 2.5s, CLS < 0.1)、WCAG AA 合规、
SEO 优化(多语言 zh/en/ja),以及生产监控告警体系。
```

### 第二步:获取工程方案

工具会输出 Lighthouse CI 配置、可访问性审查脚本、SEO 结构化数据模板、部署 YAML 与监控告警规则。

### 第三步:落地与监控

```bash
# 应用 Lighthouse CI 配置
cp .lighthouserc.json ./

# 运行可访问性审查
bash scripts/a11y-audit.sh

# 部署到生产
git push origin main  # 触发 CI 部署

# 查看监控仪表盘
# https://sentry.io/your-org
# https://lhci.your-org.com
```

## 配置示例

### 性能预算配置

```jsonc
// budget.json — 性能预算
{
  "resourceSizes": [
    { "resourceType": "script", "budget": 200 },
    { "resourceType": "stylesheet", "budget": 50 },
    { "resourceType": "image", "budget": 300 },
    { "resourceType": "font", "budget": 100 },
    { "resourceType": "total", "budget": 700 }
  ],
  "resourceCounts": [
    { "resourceType": "third-party", "budget": 10 }
  ],
  "timings": [
    { "metric": "largest-contentful-paint", "budget": 2500 },
    { "metric": "cumulative-layout-shift", "budget": 0.1 },
    { "metric": "total-blocking-time", "budget": 200 }
  ]
}
```

### 监控告警规则(Sentry + RUM)

```javascript
// sentry.client.config.js — Sentry 前端监控
import * as Sentry from '@sentry/nextjs';

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 0.1,  // 生产环境采样 10%
  replaysSessionSampleRate: 0.01,
  replaysOnErrorSampleRate: 1.0,
  // 性能阈值告警
  beforeSend(event) {
    // LCP > 4s 触发告警
    if (event.extra?.lcp > 4000) {
      Sentry.captureMessage('LCP 超过 4s 阈值', 'warning');
    }
    return event;
  },
  // Web Vitals 监控
  integrations: [
    new Sentry.BrowserTracing({
      tracingOrigins: ['localhost', 'your-app.com'],
    }),
  ],
});
```

## 最佳实践

1. **性能预算可执行化**:在 CI 中用 Lighthouse CI 强制性能预算,违规阻断 PR。
2. **核心 Web 指标监控**:生产环境用 RUM 监控 LCP/CLS/INP,设置 SLO 与告警。
3. **WCAG AA 内建**:组件与页面默认合规,CI 中用 `pa11y` 与 `axe-core` 自动审查。
4. **多语言 SEO 完整**:hreflang、Open Graph、结构化数据(JSON-LD)缺一不可。
5. **蓝绿部署**:新版本先部署到 Green,健康检查通过后切换流量,Blue 保留用于回滚。
6. **错误监控**:Sentry 捕获前端错误与性能问题,采样率生产环境 10%,错误回放 100%。
7. **CDN 边缘缓存**:静态资源 CDN 缓存,HTML 短缓存或 SSR 动态。
8. **多环境配置**:dev/staging/prod 严格隔离,环境变量通过 CI/CD 注入,不进代码仓库。

## 常见问题

### Q1: Lighthouse CI 在 CI 中如何加速?

1) 使用 `numberOfRuns: 3` 减少运行次数;2) 仅对关键页面(URL)审查;3) 缓存 Lighthouse 报告,PR 未变更相关文件时跳过;4) 用 LHCI Server 集中存储与对比。

### Q2: WCAG AA 审查如何持续保证?

CI 中运行 `pa11y` 与 `axe-core`,违规阻断 PR。组件库默认合规,新建页面继承合规性。定期用 `@axe/playwright` 做端到端可访问性测试。

### Q3: 多语言 SEO 的 hreflang 如何验证?

用 Google Search Console 的"国际化定位"报告检测 hreflang 错误。也可用 Aleyda Solis 的 hreflang 检查器在线验证。

### Q4: 蓝绿部署如何处理数据库迁移?

数据库迁移必须向后兼容(新增字段而非修改/删除)。先在 Green 执行迁移(向后兼容),切换流量后再清理旧字段。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有建议与代码片段。个人开发者可继续使用免费版,团队场景启用 Pro 版获得性能工程、SEO 深度、可访问性与企业部署能力。两个版本可在同一仓库并存。

### Q6: 如何度量 Web 产品健康度?

跟踪五个指标:核心 Web 指标达标率(LCP/CLS/INP)、WCAG AA 合规率、SEO 评分、错误率(每千次会话错误数)、SLO 达成率。五者共同反映产品健康度。

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+
- **浏览器**:Chrome(用于 Lighthouse 与 Playwright)
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方安装包 |
| Lighthouse CI | npm 包 | 推荐 | `npm i -D @lhci/cli` |
| pa11y | npm 包 | 推荐 | `npm i -D pa11y` |
| axe-core | npm 包 | 推荐 | `npm i -D axe-core` |
| @sentry/nextjs | npm 包 | 推荐 | `npm i @sentry/nextjs` |
| Playwright | npm 包 | 可选 | `npm i -D @playwright/test` |
| Vercel CLI | CLI | 可选 | `npm i -g vercel` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 核心能力基于 Markdown 指令,无需额外 API Key
- Lighthouse CI Server 需配置 `LHCI_TOKEN`
- Sentry 需配置 `SENTRY_DSN` 与 `SENTRY_AUTH_TOKEN`
- Vercel 部署需配置 `VERCEL_TOKEN`
- 监控告警(Slack/PagerDuty)需配置对应平台的 Webhook URL

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级 Web 工程方案;Lighthouse CI、可访问性脚本、部署与监控配置需在仓库中落地并由 CI 执行
