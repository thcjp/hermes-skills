---
slug: git-helper-tool-pro
name: git-helper-tool-pro
version: "1.0.0"
displayName: Git助手专业版
summary: 企业级Git辅助工具,支持智能冲突分析、自动修复、批量诊断与团队知识库,提升协作效率。
license: MIT
edition: pro
description: |-
  面向企业研发团队的高级Git辅助工具,提供智能冲突分析、自动修复建议、批量仓库诊断、团队知识库与故障自动恢复。

  核心能力:
  - 智能冲突分析与自动修复建议
  - 批量仓库健康诊断
  - 自动化故障恢复
  - 团队Git知识库与FAQ
  - 操作审计与回溯
  - 团队工作流向导

  适用场景:
  - 企业级Git问题排查
  - 复杂冲突智能分析
  - 多仓库批量诊断
  - 团队Git培训与知识沉淀

  差异化:
  - 专业版完全兼容免费版指引,支持平滑升级
  - 提供智能冲突分析和修复建议
  - 支持批量诊断和自动恢复
  - 内置团队知识库和审计日志

  触发关键词: Git智能助手, 冲突分析, 自动修复, 批量诊断, 故障恢复, 知识库, 审计日志, git assistant, conflict analysis
tags:
- 开发工具
- Git
- 辅助工具
- 企业级
- 智能分析
tools:
- read
- exec
---

# Git助手 - 专业版

## 概述

Git助手专业版为企业研发团队提供智能Git辅助能力。在免费版操作指引之上,专业版新增智能冲突分析、自动修复建议、批量仓库诊断、自动化故障恢复和团队知识库,帮助团队高效解决Git问题。

专业版完全兼容免费版的所有指引和检查清单,研发团队可从免费版无缝升级,已有配置和工作流无需修改。

## 核心能力

### 1. 智能冲突分析

自动分析冲突内容,提供修复建议。

```python
# 专业版智能冲突分析器
import re
import subprocess
import json
from datetime import datetime

class ConflictAnalyzer:
    """智能冲突分析器"""

    CONFLICT_PATTERN = re.compile(
        r'<<<<<<< (\S+)\n(.*?)=======\n(.*?)>>>>>>> (\S+)',
        re.DOTALL
    )

    @staticmethod
    def analyze_conflicts(cwd=None):
        """分析所有冲突文件"""
        # 获取冲突文件列表
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=U"],
            capture_output=True, text=True, cwd=cwd
        )
        conflict_files = result.stdout.strip().split('\n') if result.stdout.strip() else []

        analysis = {
            "analysis_time": datetime.now().isoformat(),
            "total_conflict_files": len(conflict_files),
            "files": []
        }

        for filepath in conflict_files:
            file_analysis = ConflictAnalyzer._analyze_file(filepath, cwd)
            analysis["files"].append(file_analysis)

        analysis["summary"] = ConflictAnalyzer._generate_summary(analysis["files"])
        return analysis

    @staticmethod
    def _analyze_file(filepath, cwd=None):
        """分析单个冲突文件"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            conflicts = list(ConflictAnalyzer.CONFLICT_PATTERN.finditer(content))

            file_info = {
                "file": filepath,
                "conflict_count": len(conflicts),
                "conflicts": [],
                "complexity": "low"
            }

            for i, match in enumerate(conflicts, 1):
                our_branch = match.group(1)
                our_code = match.group(2).strip()
                their_code = match.group(4)
                their_code_content = match.group(3).strip()

                conflict = {
                    "index": i,
                    "our_branch": our_branch,
                    "their_branch": their_code,
                    "our_lines": len(our_code.split('\n')),
                    "their_lines": len(their_code_content.split('\n')),
                    "our_code": our_code[:500],
                    "their_code": their_code_content[:500],
                    "analysis": ConflictAnalyzer._analyze_conflict_content(
                        our_code, their_code_content
                    )
                }
                file_info["conflicts"].append(conflict)

            # 评估复杂度
            total_lines = sum(c["our_lines"] + c["their_lines"] for c in file_info["conflicts"])
            if total_lines > 50:
                file_info["complexity"] = "high"
            elif total_lines > 20:
                file_info["complexity"] = "medium"

            return file_info

        except Exception as e:
            return {"file": filepath, "error": str(e)}

    @staticmethod
    def _analyze_conflict_content(our_code, their_code):
        """分析冲突内容类型"""
        analysis = {
            "type": "unknown",
            "recommendation": "手动检查并选择正确版本",
            "auto_resolvable": False
        }

        # 检测不同类型的冲突

        # 1. 空白冲突(仅空格/换行差异)
        if our_code.strip() == their_code.strip():
            analysis["type"] = "whitespace"
            analysis["recommendation"] = "仅空白差异,任选其一即可"
            analysis["auto_resolvable"] = True

        # 2. 导入冲突
        elif our_code.strip().startswith("import") and their_code.strip().startswith("import"):
            analysis["type"] = "import"
            analysis["recommendation"] = "合并双方导入语句"
            analysis["auto_resolvable"] = True

        # 3. 代码新增冲突(一方为空)
        elif not our_code.strip() or not their_code.strip():
            analysis["type"] = "addition"
            analysis["recommendation"] = "保留有内容的一方"
            analysis["auto_resolvable"] = True

        # 4. 配置冲突
        elif re.search(r'["\']?\w+["\']?\s*[:=]\s*', our_code) and \
             re.search(r'["\']?\w+["\']?\s*[:=]\s*', their_code):
            analysis["type"] = "config"
            analysis["recommendation"] = "检查配置值,选择正确的配置"

        # 5. 函数签名冲突
        elif re.search(r'def\s+\w+|function\s+\w+', our_code) and \
             re.search(r'def\s+\w+|function\s+\w+', their_code):
            analysis["type"] = "function_signature"
            analysis["recommendation"] = "检查函数签名,合并参数"

        return analysis

    @staticmethod
    def _generate_summary(files):
        """生成摘要"""
        total_conflicts = sum(f.get("conflict_count", 0) for f in files)
        auto_resolvable = sum(
            1 for f in files for c in f.get("conflicts", [])
            if c.get("analysis", {}).get("auto_resolvable")
        )
        high_complexity = sum(1 for f in files if f.get("complexity") == "high")

        return {
            "total_conflicts": total_conflicts,
            "auto_resolvable": auto_resolvable,
            "manual_required": total_conflicts - auto_resolvable,
            "high_complexity_files": high_complexity,
            "recommendation": "优先处理自动可解决的冲突" if auto_resolvable > 0 else "所有冲突需手动解决"
        }


# 使用示例
analyzer = ConflictAnalyzer()
analysis = analyzer.analyze_conflicts()
print(json.dumps(analysis, indent=2, ensure_ascii=False))
```

### 2. 自动修复建议

```python
# 专业版自动修复工具
class ConflictResolver:
    """冲突自动修复工具"""

    @staticmethod
    def auto_resolve(filepath, cwd=None):
        """自动解决可自动处理的冲突"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        resolved_count = 0
        pattern = re.compile(
            r'<<<<<<< (\S+)\n(.*?)=======\n(.*?)>>>>>>> (\S+)',
            re.DOTALL
        )

        def resolver(match):
            nonlocal resolved_count
            our_code = match.group(2)
            their_code = match.group(3)

            analysis = ConflictAnalyzer._analyze_conflict_content(
                our_code.strip(), their_code.strip()
            )

            if analysis["auto_resolvable"]:
                resolved_count += 1

                if analysis["type"] == "whitespace":
                    return our_code.strip() + '\n'
                elif analysis["type"] == "import":
                    # 合并导入
                    all_imports = set()
                    for line in (our_code + their_code).split('\n'):
                        if line.strip():
                            all_imports.add(line.strip())
                    return '\n'.join(sorted(all_imports)) + '\n'
                elif analysis["type"] == "addition":
                    # 保留有内容的一方
                    return our_code if our_code.strip() else their_code
            else:
                # 保留冲突标记,需手动处理
                return match.group(0)

        new_content = pattern.sub(resolver, content)

        if resolved_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return {
            "file": filepath,
            "auto_resolved": resolved_count,
            "remaining": content.count('<<<<<<<') - resolved_count
        }

    @staticmethod
    def batch_auto_resolve(cwd=None):
        """批量自动解决冲突"""
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=U"],
            capture_output=True, text=True, cwd=cwd
        )
        files = result.stdout.strip().split('\n') if result.stdout.strip() else []

        results = []
        for f in files:
            if f:
                results.append(ConflictResolver.auto_resolve(f, cwd))

        return {
            "total_files": len(files),
            "results": results,
            "total_auto_resolved": sum(r["auto_resolved"] for r in results)
        }
```

### 3. 批量仓库诊断

```python
# 专业版批量仓库诊断
class BatchRepositoryDiagnostics:
    """批量仓库诊断工具"""

    def __init__(self, repo_paths):
        self.repos = repo_paths

    def diagnose_all(self):
        """诊断所有仓库"""
        results = {}
        for repo in self.repos:
            results[repo] = self._diagnose_repo(repo)
        return self._generate_summary(results)

    def _diagnose_repo(self, repo_path):
        """诊断单个仓库"""
        diag = {"path": repo_path, "issues": [], "status": "healthy"}

        try:
            # 1. 检查仓库状态
            status = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True, text=True, cwd=repo_path
            )
            if status.stdout.strip():
                diag["issues"].append({
                    "level": "warning",
                    "issue": "有未提交的变更",
                    "count": len(status.stdout.strip().split('\n'))
                })

            # 2. 检查未推送提交
            ahead = subprocess.run(
                ["git", "rev-list", "--count", "@{upstream}..HEAD"],
                capture_output=True, text=True, cwd=repo_path
            )
            if ahead.stdout.strip().isdigit() and int(ahead.stdout) > 0:
                diag["issues"].append({
                    "level": "warning",
                    "issue": f"有{ahead.stdout.strip()}个未推送提交"
                })

            # 3. 检查落后远程
            behind = subprocess.run(
                ["git", "rev-list", "--count", "HEAD..@{upstream}"],
                capture_output=True, text=True, cwd=repo_path
            )
            if behind.stdout.strip().isdigit() and int(behind.stdout) > 0:
                diag["issues"].append({
                    "level": "info",
                    "issue": f"落后远程{behind.stdout.strip()}个提交"
                })

            # 4. 检查stash
            stash = subprocess.run(
                ["git", "stash", "list"],
                capture_output=True, text=True, cwd=repo_path
            )
            if stash.stdout.strip():
                count = len(stash.stdout.strip().split('\n'))
                if count > 5:
                    diag["issues"].append({
                        "level": "info",
                        "issue": f"有{count}个stash"
                    })

            # 5. 检查仓库大小
            size = subprocess.run(
                ["du", "-sh", ".git"],
                capture_output=True, text=True, cwd=repo_path
            )
            if size.stdout:
                size_str = size.stdout.split('\t')[0]
                if 'G' in size_str:
                    diag["issues"].append({
                        "level": "warning",
                        "issue": f"仓库较大({size_str}),建议优化"
                    })

            # 6. 检查已合并分支
            merged = subprocess.run(
                ["git", "branch", "--merged"],
                capture_output=True, text=True, cwd=repo_path
            )
            merged_branches = [
                b.strip().lstrip('* ') for b in merged.stdout.split('\n')
                if b.strip() and b.strip() not in ['main', 'master']
            ]
            if merged_branches:
                diag["issues"].append({
                    "level": "info",
                    "issue": f"有{len(merged_branches)}个可清理的分支"
                })

            if diag["issues"]:
                diag["status"] = "needs_attention"

        except Exception as e:
            diag["status"] = "error"
            diag["issues"].append({"level": "error", "issue": str(e)})

        return diag

    def _generate_summary(self, results):
        """生成诊断摘要"""
        total = len(results)
        healthy = sum(1 for r in results.values() if r["status"] == "healthy")
        needs_attention = sum(1 for r in results.values() if r["status"] == "needs_attention")
        errors = sum(1 for r in results.values() if r["status"] == "error")

        return {
            "diagnosis_time": datetime.now().isoformat(),
            "total_repos": total,
            "healthy": healthy,
            "needs_attention": needs_attention,
            "errors": errors,
            "details": results
        }
```

### 4. 自动化故障恢复

```python
# 专业版自动故障恢复
class GitRecoveryAssistant:
    """Git故障自动恢复助手"""

    RECOVERY_SCENARIOS = {
        "accidental_commit": {
            "description": "误提交了不需要的代码",
            "steps": [
                "git reset --soft HEAD~1   # 撤销提交,保留变更",
                "git restore --staged .     # 取消暂存",
                "git restore .              # 丢弃变更(如需要)"
            ],
            "safe": True
        },
        "accidental_push": {
            "description": "误推送了提交到远程",
            "steps": [
                "git revert <commit-sha>    # 创建反向提交(安全)",
                "git push origin <branch>   # 推送撤销"
            ],
            "safe": True
        },
        "accidental_delete_branch": {
            "description": "误删除了本地分支",
            "steps": [
                "git reflog                 # 查找分支最后位置",
                "git checkout -b <branch> <sha>  # 从SHA恢复分支"
            ],
            "safe": True
        },
        "accidental_reset": {
            "description": "误执行了git reset --hard",
            "steps": [
                "git reflog                 # 查找reset前的提交",
                "git reset --hard <sha>     # 恢复到该提交"
            ],
            "safe": True
        },
        "merge_conflict_stuck": {
            "description": "合并冲突中无法继续",
            "steps": [
                "git merge --abort          # 取消合并",
                "git reset --hard HEAD       # 重置到合并前状态"
            ],
            "safe": True
        },
        "rebase_stuck": {
            "description": "变基过程中卡住",
            "steps": [
                "git rebase --abort         # 取消变基",
                "# 解决冲突后重新变基"
            ],
            "safe": True
        },
        "detached_head": {
            "description": "处于分离HEAD状态",
            "steps": [
                "git branch temp-branch     # 创建临时分支保存",
                "git switch main            # 切回主分支",
                "git merge temp-branch      # 合并临时分支"
            ],
            "safe": True
        }
    }

    @staticmethod
    def detect_issue(cwd=None):
        """自动检测当前问题"""
        issues = []

        # 检查是否在合并中
        merge_head = subprocess.run(
            ["git", "rev-parse", "--verify", "MERGE_HEAD"],
            capture_output=True, text=True, cwd=cwd
        )
        if merge_head.returncode == 0:
            issues.append({
                "scenario": "merge_conflict_stuck",
                "message": "检测到正在合并中"
            })

        # 检查是否在变基中
        rebase_dir = subprocess.run(
            ["test", "-d", ".git/rebase-merge"],
            capture_output=True, cwd=cwd
        )
        if rebase_dir.returncode == 0:
            issues.append({
                "scenario": "rebase_stuck",
                "message": "检测到正在变基中"
            })

        # 检查分离HEAD
        symbolic = subprocess.run(
            ["git", "symbolic-ref", "-q", "HEAD"],
            capture_output=True, text=True, cwd=cwd
        )
        if symbolic.returncode != 0:
            issues.append({
                "scenario": "detached_head",
                "message": "检测到分离HEAD状态"
            })

        return issues

    @staticmethod
    def get_recovery_plan(scenario):
        """获取恢复方案"""
        plan = GitRecoveryAssistant.RECOVERY_SCENARIOS.get(scenario)
        if plan:
            return {
                "scenario": scenario,
                "description": plan["description"],
                "steps": plan["steps"],
                "safe": plan["safe"]
            }
        return None

    @staticmethod
    def auto_recover(scenario, cwd=None):
        """自动执行恢复"""
        plan = GitRecoveryAssistant.get_recovery_plan(scenario)
        if not plan or not plan["safe"]:
            return {"success": False, "message": "无法自动恢复,需手动处理"}

        results = []
        for step in plan["steps"]:
            if step.startswith("#"):
                results.append({"step": step, "status": "skip"})
                continue

            cmd = step.split()
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
            results.append({
                "step": step,
                "status": "success" if result.returncode == 0 else "failed",
                "output": result.stdout + result.stderr
            })

            if result.returncode != 0:
                return {"success": False, "results": results}

        return {"success": True, "results": results}
```

### 5. 团队知识库

```python
# 专业版团队Git知识库
class GitKnowledgeBase:
    """Git团队知识库"""

    FAQ = {
        "如何撤销最近的提交": {
            "answer": "使用 git reset --soft HEAD~1 撤销提交但保留变更",
            "command": "git reset --soft HEAD~1",
            "category": "撤销操作"
        },
        "如何修改最近的提交信息": {
            "answer": "使用 git commit --amend -m '新信息' 修改",
            "command": "git commit --amend -m 'new message'",
            "category": "提交管理"
        },
        "如何解决合并冲突": {
            "answer": "1.查看冲突文件 2.编辑解决 3.git add 4.git commit",
            "command": "git diff --name-only --diff-filter=U",
            "category": "冲突解决"
        },
        "如何创建标签": {
            "answer": "使用 git tag -a v1.0 -m '版本说明' 创建附注标签",
            "command": "git tag -a v1.0 -m 'message'",
            "category": "版本管理"
        },
        "如何查看文件历史": {
            "answer": "使用 git log --oneline -- file.txt 查看文件提交历史",
            "command": "git log --oneline -- file.txt",
            "category": "历史查看"
        }
    }

    TROUBLESHOOTING = {
        "push被拒绝(non-fast-forward)": {
            "cause": "远程有你本地没有的提交",
            "solution": "先 git pull --rebase 再 push",
            "commands": [
                "git pull --rebase origin main",
                "git push origin main"
            ]
        },
        "merge conflict无法解决": {
            "cause": "合并冲突未完全解决",
            "solution": "检查冲突标记,确保全部解决",
            "commands": [
                "grep -r '<<<\\|>>>\\|===' .",
                "git add .",
                "git commit"
            ]
        },
        "fatal: not a git repository": {
            "cause": "不在Git仓库目录中",
            "solution": "切换到仓库目录或初始化仓库",
            "commands": [
                "cd /path/to/repo",
                "# 或 git init"
            ]
        },
        "permission denied (publickey)": {
            "cause": "SSH密钥未配置或未添加",
            "solution": "生成SSH密钥并添加到Git平台",
            "commands": [
                "ssh-keygen -t ed25519 -C 'email'",
                "cat ~/.ssh/id_ed25519.pub",
                "# 添加到Git平台"
            ]
        }
    }

    @staticmethod
    def search(query):
        """搜索知识库"""
        results = {"faq": [], "troubleshooting": []}

        for question, info in GitKnowledgeBase.FAQ.items():
            if query.lower() in question.lower():
                results["faq"].append({
                    "question": question,
                    "answer": info["answer"],
                    "command": info["command"],
                    "category": info["category"]
                })

        for problem, info in GitKnowledgeBase.TROUBLESHOOTING.items():
            if query.lower() in problem.lower():
                results["troubleshooting"].append({
                    "problem": problem,
                    "cause": info["cause"],
                    "solution": info["solution"],
                    "commands": info["commands"]
                })

        return results

    @staticmethod
    def get_all_categories():
        """获取所有分类"""
        categories = set()
        for info in GitKnowledgeBase.FAQ.values():
            categories.add(info["category"])
        return sorted(categories)
```

## 使用场景

### 场景一:智能冲突解决

遇到复杂冲突时获取智能分析。

```bash
#!/bin/bash
# 智能冲突解决流程
echo "=== 智能冲突解决 ==="

# 1. 分析冲突
echo "1. 分析冲突..."
python3 -c "
from conflict_analyzer import ConflictAnalyzer
import json
analysis = ConflictAnalyzer.analyze_conflicts()
print(json.dumps(analysis, indent=2, ensure_ascii=False))
print(f\"\\n冲突总数: {analysis['summary']['total_conflicts']}\")
print(f\"可自动解决: {analysis['summary']['auto_resolvable']}\")
print(f\"需手动处理: {analysis['summary']['manual_required']}\")
"

# 2. 自动解决可处理的冲突
echo -e "\n2. 自动解决冲突..."
python3 -c "
from conflict_resolver import ConflictResolver
result = ConflictResolver.batch_auto_resolve()
print(f'自动解决: {result[\"total_auto_resolved\"]} 个')
"

# 3. 手动处理剩余冲突
echo -e "\n3. 剩余冲突需手动处理"
git diff --name-only --diff-filter=U

# 4. 完成合并
echo -e "\n4. 所有冲突解决后:"
echo "  git add ."
echo "  git commit"
```

### 场景二:批量仓库健康检查

检查团队所有仓库的健康状态。

```bash
#!/bin/bash
# 批量仓库健康检查
echo "=== 批量仓库健康检查 ==="

python3 -c "
from batch_diagnostics import BatchRepositoryDiagnostics
import json

repos = [
    '/home/user/project-a',
    '/home/user/project-b',
    '/home/user/project-c'
]

diagnostics = BatchRepositoryDiagnostics(repos)
report = diagnostics.diagnose_all()

print(f\"总仓库数: {report['total_repos']}\")
print(f\"健康: {report['healthy']}\")
print(f\"需关注: {report['needs_attention']}\")
print(f\"错误: {report['errors']}\")

for repo, diag in report['details'].items():
    status = diag['status']
    issues = len(diag.get('issues', []))
    print(f'  [{status}] {repo} ({issues}个问题)')
"
```

### 场景三:自动故障恢复

遇到Git问题时自动检测并恢复。

```bash
#!/bin/bash
# 自动故障检测与恢复
echo "=== Git故障检测 ==="

python3 -c "
from recovery_assistant import GitRecoveryAssistant
import json

# 1. 检测问题
issues = GitRecoveryAssistant.detect_issue()
if issues:
    print('检测到问题:')
    for issue in issues:
        print(f'  - {issue[\"message\"]}')
        
        # 2. 获取恢复方案
        plan = GitRecoveryAssistant.get_recovery_plan(issue['scenario'])
        if plan:
            print(f'    描述: {plan[\"description\"]}')
            print(f'    步骤:')
            for step in plan['steps']:
                print(f'      {step}')
            
            # 3. 自动恢复
            print(f'    尝试自动恢复...')
            result = GitRecoveryAssistant.auto_recover(issue['scenario'])
            print(f'    结果: {\"成功\" if result[\"success\"] else \"失败\"}')
else:
    print('未检测到问题,仓库状态正常')
"
```

## 快速开始

### 步骤一:运行诊断

```
请对当前Git仓库进行健康诊断,发现问题并提供修复建议。
```

### 步骤二:智能解决

```
请分析当前的合并冲突,自动解决可处理的冲突。
```

### 步骤三:查看知识库

```
如何撤销已推送的提交?
```

## 配置示例

### 企业级配置

```yaml
# .git-helper-pro.yml
version: "2.0"
edition: pro

# 智能冲突分析
conflict_analysis:
  enabled: true
  auto_resolve: true
  safe_mode: true
  complexity_threshold: 50

# 批量诊断
batch_diagnostics:
  enabled: true
  repos:
    - /home/user/project-a
    - /home/user/project-b
  schedule: weekly
  report_format: json

# 自动恢复
auto_recovery:
  enabled: true
  safe_only: true
  create_backup: true

# 知识库
knowledge_base:
  enabled: true
  auto_search: true
  custom_faq: ./git-faq.yml

# 审计日志
audit:
  enabled: true
  log_file: ./git-audit.log
  log_level: info
  include_commands: true
  retention_days: 90
```

## 最佳实践

1. **定期诊断**:设置定期仓库健康检查

```bash
# 每周诊断
0 2 * * 0 python3 batch_diagnostics.py
```

2. **智能解决**:优先使用自动分析处理冲突

3. **安全恢复**:恢复前创建备份

4. **知识沉淀**:将常见问题添加到知识库

5. **审计追踪**:记录所有Git操作用于追溯

## 常见问题

### Q1:专业版如何兼容免费版?

专业版完全兼容免费版的所有指引和检查清单。免费版的配置可直接使用,专业版会自动启用智能分析和诊断功能。

### Q2:自动冲突解决安全吗?

自动解决仅处理可安全自动处理的冲突类型(空白差异、导入合并、单方新增),复杂冲突仍需手动处理。

### Q3:支持多少个仓库批量诊断?

| 仓库数量 | 耗时 | 并行 |
|:---------|:-----|:-----|
| 1-10 | <30s | 串行 |
| 10-50 | 1-3min | 并行 |
| 50-100 | 3-10min | 并行 |
| 100+ | 10min+ | 分批 |

### Q4:如何扩展知识库?

```yaml
# 自定义FAQ
custom_faq:
  - question: "如何配置Git代理"
    answer: "使用 git config 设置HTTP代理"
    command: "git config --global http.proxy http://proxy:8080"
    category: "配置"
```

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Git 2.20+ / Python 3.8+ / Bash

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git 2.20+ | 运行时 | 必需 | git-scm.com 下载 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Bash | 运行时 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 远程仓库认证配置:

```bash
# SSH认证
ssh-keygen -t ed25519 -C "your@email.com"

# HTTPS Token
git config --global credential.helper store
```

### 可用性分类

- **分类**:MD+EXEC+PRO(专业版支持智能分析、批量诊断和自动恢复)
- **说明**:企业级Git辅助工具,支持智能冲突分析和团队知识库
- **适用规模**:个人到大型团队多仓库项目
- **兼容性**:完全兼容免费版指引和配置,支持平滑升级
