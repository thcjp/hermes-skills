---
slug: "github-dev-standard"
name: "github-dev-standard"
version: 1.0.1
displayName: "项目开发标准专业版"
summary: "企业级项目开发标准方案，含自动化验收、CI 集成、团队协作与质量度量。。面向企业研发团队的项目开发标准化专业工具，提供自动化验收与团队协作治理方案。核心能力: - 自动化验收清单（CI/CD"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业研发团队的项目开发标准化专业工具，提供自动化验收与团队协作治理方案。核心能力:
  - 自动化验收清单（CI/CD 集成）
  - 团队级开发规范与合并请求模板
  - 缺陷修复返工率与代码质量度量
  - 多文件同步修改与跨语言项目支持
  - 代码审查自动化与风险点识别

  适用场景:
  - 企业级项目的标准化开发流程落地
  - 团队协作中的合并请求质量管控
  - 跨语言、跨模块的大型变更管理
  - 研发质量度量与持续改进

  差异化: 专业版兼容免费版所有流程与清单...
tags:
  - 开发工具
  - 开发规范
  - 代码质量
  - 企业协作
  - CI/CD
  - 版本控制
  - Git
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# 项目开发标准专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
|:-----|:-----|:-----|
| 开发流程 | 9 步手动流程 | 自动化流程编排与追踪 |
| 编码纪律 | 8 条纪律指引 | 自动 diff 分析与违规检测 |
| 验证机制 | 4 层手动验证 | CI/CD 自动化验收 |
| 验收清单 | 15 项手动检查 | 自动化清单脚本 + 度量报表 |
| 合并请求 | - | 标准化模板与审查流程 |
| 质量度量 | - | 返工率、改动量、缺陷率统计 |
| 多文件管理 | 手动搜索引用 | 自动化依赖分析与同步检查 |
| 代码审查 | - | 风险点自动识别与建议 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 开发流程

针对开发流程,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供开发流程相关的配置参数、输入数据和处理选项.
**输出**: 返回开发流程的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`开发流程`的配置文档进行参数调优
### 编码纪律

针对编码纪律,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供编码纪律相关的配置参数、输入数据和处理选项.
**输出**: 返回编码纪律的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`编码纪律`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业级合并请求质量管控

团队成员提交合并请求时，需要自动化的质量检查流程.
```text
用户：团队合并请求质量参差不齐，帮我建立标准化审查流程
# ...
助手：配置合并请求模板 + 自动化验收
# ...
1. 合并请求模板（.github/pull_request_template.md）
   ## 变更说明
   - [ ] 一句话描述本次变更目标
   - [ ] 列出修改的文件和原因
   - [ ] 标注是否有 BREAKING CHANGE
# ...
   ## 验收清单
   - [ ] A1. 目标能用一句话说清
   - [ ] A2. 不修改的范围已明确
   - [ ] B1. 基于正确版本修改
   - [ ] B2. 未重写整个文件
   - [ ] C1. 语法检查通过
   - [ ] C2. 导入检查通过
   - [ ] C3. 样例验证通过
   - [ ] C4. 回归测试通过
   - [ ] D1. diff 大小与任务匹配
   - [ ] D4. 风险点已标注
# ...
   ## 验证命令
   ```bash
   npm run lint && npm test && npm run test:e2e
   ```
# ...
2. 自动化验收脚本
   （请参考skill目录中的脚本文件）
# ...
3. CI 集成（自动运行验收脚本）
   参考 .github/workflows/quality-check.yml
```

### 场景二：缺陷修复返工率度量

团队需要量化缺陷修复的质量，跟踪返工率指标.
```bash
# 质量度量脚本
cat > （请参考skill目录中的脚本文件） << 'EOF'
#!/bin/bash
# ...
# 统计指定时间范围内的缺陷修复数据
START_DATE=$1
END_DATE=$2
# ...
echo "=== 缺陷修复质量报告 ==="
echo "时间范围: $START_DATE 至 $END_DATE"
echo ""
# ...
# 统计缺陷修复提交数
FIX_COMMITS=$(git log --since="$START_DATE" --until="$END_DATE" \
  --oneline --grep="fix(" | wc -l)
# ...
# 统计返工提交数（同一文件多次修复）
REWORK_FILES=$(git log --since="$START_DATE" --until="$END_DATE" \
  --name-only --grep="fix(" | sort | uniq -d | wc -l)
# ...
# 统计平均改动量
AVG_DIFF=$(git log --since="$START_DATE" --until="$END_DATE" \
  --grep="fix(" --shortstat | grep "changed" | \
  awk '{print $4}' | awk '{sum+=$1; count++} END {if(count>0) print sum/count; else print 0}')
# ...
echo "缺陷修复提交数: $FIX_COMMITS"
echo "返工文件数: $REWORK_FILES"
echo "平均改动行数: $AVG_DIFF"
echo ""
echo "返工率: $(echo "scale=1; $REWORK_FILES * 100 / $FIX_COMMITS" | bc)%"
EOF
chmod +x （请参考skill目录中的脚本文件）
```

### 场景三：多文件同步修改检查

大型变更涉及多个文件，需要确保所有引用点同步更新.
```bash
# 依赖说明
cat > （请参考skill目录中的脚本文件） << 'EOF'
#!/bin/bash
# ...
# 检查数据结构变更是否同步所有引用
echo "=== 多文件同步检查 ==="
# ...
# 1. 查找本次变更的文件
CHANGED_FILES=$(git diff --name-only HEAD~1)
# ...
# 2. 提取变更的类名/函数名
for file in $CHANGED_FILES; do
  if [[ $file == *.py ]]; then
    # 检查被重命名的类
    OLD_NAMES=$(git diff HEAD~1 -- "$file" | grep "^-class\|^-def" | awk '{print $2}')
    for name in $OLD_NAMES; do
      CLEAN_NAME=$(echo $name | sed 's/(.*//')
      REMAINING=$(grep -r "$CLEAN_NAME" src/ --include="*.py" | wc -l)
      if [ "$REMAINING" -gt 0 ]; then
        echo "[警告] $CLEAN_NAME 在以下文件中仍有引用:"
        grep -rl "$CLEAN_NAME" src/ --include="*.py"
      fi
    done
  fi
done
# ...
echo ""
echo "=== diff 改动量统计 ==="
git diff --stat HEAD~1
echo ""
git diff --shortstat HEAD~1
EOF
chmod +x （请参考skill目录中的脚本文件）
```

## 使用流程

### CI/CD 集成配置

```yaml
# .github/workflows/quality-check.yml
name: 质量检查
on:
  pull_request:
    branches: [main, develop]
# ...
jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
# ...
      - name: 语法检查
        run: |
          python3 -m py_compile $(find . -name "*.py" -not -path "./.venv/*")
          node -c $(find . -name "*.js" -not -path "./node_modules/*")
# ...
      - name: 导入检查
        run: |
          python3 -c "from src.main import app"
          node -e "require('./src/index.js')"
# ...
      - name: 单元测试
        run: |
          python3 -m pytest tests/ --cov=src --cov-report=term
          npm test
# ...
      - name: diff 改动量检查
        run: |
          DIFF_LINES=$(git diff origin/main...HEAD --shortstat | grep "changed" | awk '{print $4}')
          echo "改动行数: $DIFF_LINES"
          if [ "$DIFF_LINES" -gt 200 ]; then
            echo "[警告] 改动量超过 200 行，请确认是否合理"
          fi
# ...
      - name: 验收清单检查
        run: |
          （请参考skill目录中的脚本文件）
```

### 自动化验收脚本

```bash
#!/bin/bash
# （请参考skill目录中的脚本文件） - 合并前自动化验收
# ...
set -e
# ...
echo "=== 执行 15 项验收清单 ==="
# ...
# C1. 语法检查
echo "[C1] 语法检查..."
python3 -m py_compile $(find src -name "*.py") && echo "  通过" || exit 1
# ...
# C2. 导入检查
echo "[C2] 导入检查..."
python3 -c "from src.main import app" && echo "  通过" || exit 1
# ...
# C3. 样例验证
echo "[C3] 样例验证..."
python3 -m pytest tests/ -k "smoke" --tb=short && echo "  通过" || exit 1
# ...
# C4. 回归测试
echo "[C4] 回归测试..."
python3 -m pytest tests/ --tb=short && echo "  通过" || exit 1
# ...
# D1. diff 改动量
echo "[D1] diff 改动量检查..."
DIFF_LINES=$(git diff origin/main...HEAD --shortstat | grep -o '[0-9]* insertion' | awk '{print $1}')
echo "  新增行数: $DIFF_LINES"
if [ "$DIFF_LINES" -gt 200 ]; then
  echo "  [警告] 改动量偏大，请审查必要性"
fi
# ...
echo ""
echo "=== 验收完成 ==="
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | github-dev-standard处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **CI/CD 平台**: GitHub Actions / GitLab CI / Jenkins 等

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Python | 运行时 | 可选 | python.org 下载 |
| Node.js | 运行时 | 可选 | nodejs.org 下载 |
| Git | 命令行工具 | 必需 | 系统包管理器安装 |
| GitHub CLI | 命令行工具 | 推荐 | `brew install gh` 或官方安装 |
| jq | JSON 处理 | 可选 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- GitHub CLI 操作需要配置个人访问令牌（`gh auth login`）
- CI/CD 集成需要在平台配置对应的访问令牌

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行开发流程，专业版功能依赖 CI/CD 平台和命令行执行能力

## 案例展示

### 团队合并请求模板

```markdown
<!-- .github/pull_request_template.md -->
# ...
## 常见问题
# ...
### Q1：如何降低缺陷修复返工率？
# ...
```text
1. 严格执行 9 步流程，先写任务卡再编码
2. 控制改动量在 15 行以内
3. 4 层验证全部通过后再提交
4. 合并请求至少一人审查
5. 定期复盘返工原因
```
# ...
### Q2：CI 集成后验证太慢怎么办？
# ...
```yaml
# 并行执行验证任务
jobs:
  syntax-check:
    runs-on: ubuntu-latest
    steps:
      - run: python3 -m py_compile $(find src -name "*.py")

  unit-test:
    runs-on: ubuntu-latest
    steps:
      - run: python3 -m pytest tests/unit/

  integration-test:
    runs-on: ubuntu-latest
    steps:
      - run: python3 -m pytest tests/integration/
```
# ...
### Q3：如何处理跨语言项目的同步检查？
# ...
```bash
# 多语言引用检查脚本
check_references() {
  local old_name=$1
  echo "检查 $old_name 的所有引用..."

  # Python 引用
  grep -r "$old_name" src/ --include="*.py"

  # JavaScript 引用
  grep -r "$old_name" src/ --include="*.js" --include="*.ts"

  # 配置文件引用
  grep -r "$old_name" config/ --include="*.yaml" --include="*.json"

  # 文档引用
  grep -r "$old_name" docs/ --include="*.md"
}
```
# ...
### Q4：团队不遵守流程怎么办？
# ...
```text
1. CI 强制拦截不合规的合并请求
2. 合并请求模板设为必填项
3. 自动化验收脚本设为合并必要条件
4. 定期公布质量度量数据
5. 将流程遵守纳入团队考核
```
# ...
### Q5：如何量化代码审查效果？
# ...
```bash
# 统计审查发现的问题数
REVIEW_COMMENTS=$(gh pr list --state merged --limit 100 \
  --json number,comments | jq '[.[].comments | length] | add')

# 统计审查后修改的提交数
POST_REVIEW_COMMITS=$(git log --merges --grep="review" --oneline | wc -l)

echo "审查评论总数: $REVIEW_COMMENTS"
echo "审查后修改提交数: $POST_REVIEW_COMMITS"
```
# ...
### Q6：如何处理紧急修复的流程豁免？
# ...
```text
1. 紧急修复可走快速通道（hotfix 分支）
2. 豁免部分验证（但保留语法检查）
3. 修复后 24 小时内补全验收清单
4. 紧急修复需值班负责人审批
5. 每月统计紧急修复比例，优化流程
```
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...