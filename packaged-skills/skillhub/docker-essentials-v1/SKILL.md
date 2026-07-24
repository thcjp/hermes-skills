---
slug: "docker-essentials-v1"
name: "docker-essentials-v1"
version: 1.0.1
displayName: "Docker V1迁移专业版"
summary: "企业级V1迁移工具,支持自动兼容性扫描、批量迁移、配置转换与回滚保障。。面向企业运维团队的Docker V1到V2迁移专业工具,提供自动兼容性扫描、批量配置转换、渐进式迁移与回滚保障。核心能"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业运维团队的Docker V1到V2迁移专业工具,提供自动兼容性扫描、批量配置转换、渐进式迁移与回滚保障。核心能力:
  - V1到V2自动兼容性深度扫描
  - 批量Compose配置转换
  - Dockerfile现代化重构
  - 渐进式迁移与回滚保障
  - 迁移影响评估与报告
  - CI/CD流水线适配

  适用场景:
  - 企业级Docker版本升级
  - 大规模容器环境迁移
  - 遗留系统现代化改造
  - 合规性版本升级

  差异化:
  - 专业版完全兼容免费版V1命令,支持平滑升级
  - 提供自动化迁移工具...
tags:
  - 开发工具
  - Docker
  - 遗留系统
  - 企业级
  - 迁移工具
  - 容器
  - DevOps
  - self
  - echo
  - docker
  - file
  - dockerfile
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# Docker V1迁移专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Docker V1迁移专业版支持自动兼容性扫描 | 不支持 | 支持 |
| Docker V1迁移专业版配置转换 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |

## 核心能力

### 1. V1到V2兼容性深度扫描
自动扫描项目中的所有Docker配置,识别迁移风险点.
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供V1到V2兼容性深度扫描所需的指令和必要参数.
**处理**: 解析V1到V2兼容性深度扫描的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回V1到V2兼容性深度扫描的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`Dockerfile现代化重构`的配置文档进行参数调优
### 2. 批量配置转换
自动将V1 Compose文件和Dockerfile转换为V2格式.
**输入**: 用户提供批量配置转换所需的指令和必要参数.
**输出**: 返回批量配置转换的处理结果,包含执行状态码、结果数据和执行日志.
### 3. Dockerfile现代化重构
```python
class DockerfileModernizer:
    """Dockerfile现代化重构器"""
# ...
    def __init__(self, dockerfile_path):
        self.path = dockerfile_path
        self.original = []
        self.modernized = []
        self.changes = []
# ...
    def modernize(self):
        """执行现代化重构"""
        self._read()
        self._apply_best_practices()
        self._suggest_multistage()
        self._write()
        return self.changes
# ...
    def _read(self):
        """读取Dockerfile"""
        with open(self.path, 'r', encoding='utf-8') as f:
            self.source_lines = f.readlines()
# ...
    def _apply_best_practices(self):
        """应用优秀实践"""
        for line in self.source_lines:
            stripped = line.strip()
# ...
            if stripped.startswith('MAINTAINER '):
                author = stripped.split(' ', 1)[1]
                self.modernized.append(f'LABEL maintainer="{author}"\n')
                self.changes.append("MAINTAINER -> LABEL maintainer")
                continue
# ...
            if 'apt-get install' in stripped and '&&' not in stripped:
                self.modernized.append(line)
                self.changes.append("建议合并apt-get install指令")
                continue
# ...
            self.modernized.append(line)
# ...
    def _suggest_multistage(self):
        """建议多阶段构建"""
        has_build = any('RUN npm run build' in l or 'RUN go build' in l
                       or 'RUN make' in l for l in self.original)
        has_no_multistage = not any(' AS ' in l for l in self.original)
# ...
        if has_build and has_no_multistage:
            self.changes.append("建议使用多阶段构建减小镜像体积")
# ...
    def _write(self):
        """写回文件"""
        with open(self.path, 'w', encoding='utf-8') as f:
            f.writelines(self.modernized)
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `dockerfile现代化重构` 选项
- 处理流程: 接收输入 -> 执行Dockerfile现代化重构 -> 返回结果
- 输入: 用户提供Dockerfile现代化重构所需的参数和指令
- 输出: 返回Dockerfile现代化重构的处理结果,包含执行状态码、结果数据和执行日志

**输入**: 用户提供渐进式迁移与回滚所需的指令和必要参数.
**处理**: 解析渐进式迁移与回滚的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回渐进式迁移与回滚的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:企业级V1到V2迁移
对企业级Docker环境进行全面迁移.
```bash
#!/bin/bash
echo "=== 企业级Docker V1到V2迁移 ==="
# ...
echo "阶段1: 兼容性扫描..."
python3 compatibility_scanner.py ./ > migration-assessment.json
echo "评估报告: migration-assessment.json"
# ...
echo -e "\n阶段2: 创建备份..."
tar -czf "docker-v1-backup-$(date +%Y%m%d).tar.gz" \
    docker-compose*.yml Dockerfile* .env* scripts/
# ...
echo -e "\n阶段3: 批量配置转换..."
bash batch-convert.sh
# ...
echo -e "\n阶段4: 验证配置..."
for f in docker-compose*.yml; do
    echo "验证: $f"
    docker compose -f "$f" config -q && echo "[OK]" || echo "[FAIL]"
done
# ...
echo -e "\n阶段5: 渐进式服务迁移..."
SERVICES=$(docker-compose config --services 2>/dev/null)
for svc in $SERVICES; do
    migrate_service "$svc"
done
# ...
echo -e "\n阶段6: 最终验证..."
docker compose ps
echo "迁移完成"
```

### 场景二:CI/CD流水线迁移
迁移CI/CD配置中的Docker命令.
```bash
#!/bin/bash
echo "=== CI/CD配置迁移 ==="
# ...
CI_FILES=$(find . -name ".gitlab-ci.yml" -o -name "Jenkinsfile" -o -path "./.github/workflows/*.yml")
# ...
for file in $CI_FILES; do
    echo "迁移: $file"
    cp "$file" "${file}.v1-backup"
# ...
    sed -i 's/docker-compose /docker compose /g' "$file"
# ...
    sed -i 's/docker-compose -f/docker compose -f/g' "$file"
# ...
    echo "  -> 已更新"
done
# ...
echo -e "\n验证配置语法..."
for file in $CI_FILES; do
    if [[ "$file" == *.yml ]]; then
        python3 -c "import yaml; yaml.safe_load(open('$file'))" && echo "[OK] $file" || echo "[FAIL] $file"
    fi
done
```

### 场景三:迁移影响评估
评估迁移对生产环境的影响.
```python
class MigrationImpactAssessor:
    """迁移影响评估器"""
# ...
    def __init__(self, project_root):
        self.root = project_root
        self.impact = {
            "high": [],
            "medium": [],
            "low": []
        }
# ...
    def assess(self):
        """评估迁移影响"""
        self._assess_compose_changes()
        self._assess_dockerfile_changes()
        self._assess_script_changes()
        self._assess_ci_changes()
        return self._generate_report()
# ...
    def _assess_compose_changes(self):
        """评估Compose变更影响"""
        pass
# ...
    def _generate_report(self):
        """生成影响评估报告"""
        total = sum(len(v) for v in self.impact.values())
        return {
            "total_items": total,
            "high_impact": len(self.impact["high"]),
            "medium_impact": len(self.impact["medium"]),
            "low_impact": len(self.impact["low"]),
            "recommendation": self._get_recommendation(),
            "details": self.impact
        }
# ...
    def _get_recommendation(self):
        """获取迁移建议"""
        if len(self.impact["high"]) > 0:
            return "建议在非生产环境充分测试后再迁移"
        elif len(self.impact["medium"]) > 5:
            return "建议分阶段迁移,每阶段验证后继续"
        else:
            return "可以安全迁移,建议保留回滚点"
```

## 使用流程

### 步骤一:运行兼容性扫描
```
请扫描当前项目的Docker配置,评估V1到V2迁移的兼容性.
```

### 步骤二:查看评估报告
报告包含:
1. 兼容性问题列表
2. 自动修复建议
3. 迁移就绪度评估
4. 预估工作量

### 步骤三:执行迁移
```
请根据评估报告执行V1到V2迁移,创建回滚点并逐步迁移.
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | docker-essentials-v1处理的内容输入 |,  |
| content | string | 否 | docker-essentials-v1处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "v1 相关配置参数",
    result: "v1 相关配置参数",
    result: "v1 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Linux / macOS / Windows
- **运行时**:Docker Engine(V1和V2均支持)
- **工具**:Python 3.8+ / Bash

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Docker Engine | 运行时 | 必需 | docker.com 下载 |
| docker-compose V1 | 工具 | 迁移前 | pip install docker-compose |
| docker compose V2 | 工具 | 迁移后 | Docker Compose插件 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| jq | 工具 | 推荐 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 如需访问私有镜像仓库,需配置认证

### 可用性分类
- **分类**:MD+EXEC+PRO(专业版支持自动扫描、批量转换和回滚保障)
- **说明**:企业级迁移工具,支持V1到V2全流程迁移
- **适用规模**:中小型到大型项目
- **兼容性**:完全兼容免费版V1命令,同时支持V2环境

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1:专业版如何兼容免费版?
专业版完全兼容免费版的所有V1命令。专业版同时支持V1和V2命令,在迁移过程中可双环境运行.
### Q2:迁移过程中服务会中断吗?
采用渐进式迁移策略,逐个服务迁移,每次迁移一个服务时该服务会短暂中断,其他服务不受影响.
### Q3:迁移失败如何回滚?
```bash
rollback_service web
```

### Q4:迁移需要多长时间?
| 项目规模 | 文件数 | 预估时间 | 复杂度 |
|:------|------:|:------|:------|
| 小型 | <10 | 1-2小时 | 低 |
| 中型 | 10-50 | 半天-1天 | 中 |
| 大型 | 50-200 | 2-5天 | 高 |
| 超大型 | >200 | 1-2周 | 极高 |

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

