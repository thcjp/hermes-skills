---
slug: viral-prophet
name: viral-prophet
version: "1.0.0"
displayName: "爆款预言机"
summary: "发布前预判爆款概率,7维评分+盲预测+T+3d复盘闭环"
license: MIT
description: |-
  爆款预言机——内容还没发,先告诉你能不能爆。7维度LLM加权评分+盲预测机制,在正式发布前给出爆款概率预测,发布3天后T+3d复盘对比预测与实际数据,定期自进化评分标准,越用越准。

  核心能力:
  - 7维内容评分:情感共鸣/钩子强度/社会议题/金句密度/叙事性/受众广度/实用价值
  - 盲预测机制:仅喂稿件不读对话历史,确保预测客观
  - T+3d复盘闭环:预测vs实际数据对比,计算偏差率
  - Rubric自进化:基于历史复盘数据自动调整评分权重
  - 多平台独立rubric:抖音/小红书/B站各维护一套评分标准

  适用场景:
  - 内容矩阵操盘手:发布前筛选高潜力稿件,集中资源推爆款
  - MCN机构主编:量化评估达人内容质量,数据驱动指导
  - 独立创作者:发之前先打分,避免无效发布浪费流量
  - 副业达人:评估选题价值,把时间花在爆款概率高的内容上

  输入要求:待评估的内容文本(稿件/文案/脚本均可)

  差异化:不是事后诸葛亮的阅读量统计,而是发布前的预测+发布后的复盘闭环,盲预测杜绝主观偏见,rubric自进化让评分标准持续校准。

  触发关键词:内容评分、爆款预测、发布前评估、质量校准、复盘、rubric进化、爆款概率、盲预测
homepage: "https://skillhub.cn"
tags: [内容创作, 数据分析, 爆款预测, 营销, 内容运营]
tools: [read, exec]
---

# 爆款预言机

通过"评分-预测-复盘-进化"闭环,持续提升内容质量评估准确度。在内容发布前进行7维度LLM评分和盲预测,发布3天后进行T+3d复盘对比预测与实际数据,定期基于历史复盘数据进化评分标准(rubric)。按平台独立维护rubric,适配不同平台的内容特征。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 内容评分 | 发布前或发布后 | 7维度LLM评分,输出综合分+改进建议 |
| 盲预测 | 评分后发布前 | 仅喂稿件+rubric,不读对话历史,预测互动表现 |
| T+3d复盘 | 发布3天后 | 预测vs实际数据对比,计算偏差 |
| Rubric进化 | 定期批量执行 | 基于历史复盘数据更新评分标准 |

**核心价值**: 通过"评分-预测-复盘-进化"闭环,持续提升内容质量评估准确度。按平台独立维护rubric,适配不同平台的内容特征。

**盲预测设计**: 盲预测不读取对话历史,仅基于稿件和rubric备注预测互动表现,确保预测客观性。脚本内部构造独立Prompt,不传入任何对话上下文或历史消息。

## 工作流

### 1. 内容评分(score)

**输入**: content(文本), platform(平台), rubric_version(版本,可选)

**处理**: 调用LLM对7个维度各打0-10分,计算综合分

**7维度定义**:

| 维度 | 代码 | 说明 | 权重 |
|:-----|:-----|:-----|:-----|
| ER | 情感共鸣 | 内容引发读者情感反应的能力 | 1.5 |
| HP | 钩子强度 | 前3秒/首段抓注意力的能力 | 1.5 |
| SR | 社会议题 | 内容与社会热点/普遍议题的关联度 | 1.5 |
| QL | 金句密度 | 可传播金句/核心观点的密度 | 1.0 |
| NA | 叙事性 | 故事性/叙事流畅度 | 1.0 |
| AB | 受众广度 | 内容覆盖的受众范围 | 1.0 |
| PV | 实用价值 | 读者可获得的实用信息/技巧 | 1.0 |

**综合分公式**: `composite = (ER*1.5 + HP*1.5 + SR*1.5 + QL + NA + AB + PV) / 8.5 * 2.0`

### 2. 盲预测(predict)

**输入**: content(文本), rubric_notes(评分标准备注)

**处理**: 直接调用LLM(不读对话历史),仅基于稿件+rubric_notes预测互动表现

**硬约束**: 脚本内部构造独立Prompt,不传入任何对话上下文或历史消息,确保预测客观性

### 3. T+3d复盘(review)

**输入**: prediction(预测数据), actual_stats(实际数据), platform(平台)

**处理**: 对比预测vs实际,计算准确率和偏差,生成rubric更新建议。review记录保存platform和deviation供evolve使用

### 4. Rubric进化(evolve)

定期批量执行,基于近期所有复盘数据:
1. 聚合近期所有review记录
2. 分析哪些维度预测偏差最大
3. 更新对应平台的rubric评分标准
4. 写入 `rubrics/{platform}.json`

**处理**: 聚合近N天review数据 -> 按平台分组 -> 计算各维度偏差比率 -> 偏差超阈值(1.5)的维度调整权重(步长0.1,范围0.5-2.5) -> 原子写入rubric.json

**偏差映射**: views偏差 -> HP/SR权重调整, engagement偏差 -> ER/QL权重调整

### 5. 按平台独立迭代

每个平台独立维护rubric文件:
```
rubrics/
  ├── douyin.json       # 抖音评分标准
  ├── xiaohongshu.json  # 小红书评分标准
  ├── bilibili.json     # B站评分标准
  └── ...
predictions/
  └── {prediction_id}.json  # 预测记录
reviews/
  └── {prediction_id}.json  # 复盘记录
```

## 输入格式

```json
{
  "mode": "score|predict|review|evolve",
  "content": "内容文本",
  "platform": "douyin",
  "rubric_version": "v1",
  "rubric_notes": "评分标准备注",
  "prediction": {"predicted_views": 500, "predicted_engagement": 0.05},
  "actual": {"views": 520, "likes": 30, "comments": 5},
  "days": 7
}
```

## 输出格式

### 评分输出
```json
{
  "success": true,
  "data": {
    "scores": {"ER": 8, "HP": 7, "SR": 6, "QL": 7, "NA": 8, "AB": 7, "PV": 9},
    "composite": 7.41,
    "threshold_pass": true,
    "suggestions": ["增强社会议题关联度", "增加金句密度"]
  },
  "error": null,
  "code": null
}
```

### 预测输出
```json
{
  "success": true,
  "data": {
    "prediction": {"expected_views": "500-800", "expected_engagement": "3-5%"},
    "confidence": 0.75,
    "reasoning": "钩子强度中等,情感共鸣较高,预计互动率3-5%"
  },
  "error": null,
  "code": null
}
```

### 复盘输出
```json
{
  "success": true,
  "data": {
    "accuracy": 0.85,
    "deviation": {"views": 4.0, "engagement": 1.2},
    "rubric_update_suggestions": ["ER权重应从1.5调整为1.3"]
  },
  "error": null,
  "code": null
}
```

### 进化输出
```json
{
  "success": true,
  "data": {
    "platform": "douyin",
    "updated_dimensions": ["HP", "SR"],
    "changes": [{"dimension": "HP", "old_weight": 1.5, "new_weight": 1.4}],
    "rubric_file": "rubrics/douyin.json"
  },
  "error": null,
  "code": null
}
```

## 异常处理

| 异常 | 处理 | code |
|:-----|:-----|:-----|
| LLM API Key未配置 | 返回error提示 | ENV_MISSING |
| LLM调用超时(>30s) | 返回error+降级建议 | LLM_TIMEOUT |
| LLM返回非JSON | 尝试解析失败后返回error | LLM_PARSE_FAILED |
| 空内容输入 | 返回error | EMPTY_CONTENT |
| 无效平台名 | 返回error | INVALID_PLATFORM |
| rubric文件不存在 | 使用默认rubric+v1 | (降级,非错误) |

## 定期执行配置

建议每周执行一次批量复盘和rubric进化,避免高频Token消耗:
1. 采集上周所有平台发布内容数据
2. 对每条内容执行T+3d复盘
3. 聚合分析预测偏差
4. 更新各平台rubric评分标准

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| JSON文件存储 | 文件系统 | 必需 | exec工具创建rubrics/predictions/reviews/目录 |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 7维内容评分和盲预测
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
盲预测由Agent内置LLM独立完成,不读取对话历史。rubric文件按平台独立维护。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 评分示例
```bash
python calibrate_score.py \
  --content "在职场中,最可怕的不是能力不足,而是不知道自己不足。今天分享3个自我提升的方法..." \
  --platform zhihu
```

### 盲预测示例
```bash
python calibrate_predict.py \
  --content "在职场中,最可怕的不是能力不足..." \
  --rubric-notes "zhihu平台偏向深度内容和实用价值"
```

### 复盾示例
```bash
python calibrate_review.py \
  --prediction '{"predicted_views":"500-800","predicted_engagement":"3-5%"}' \
  --actual '{"views":620,"likes":45,"comments":8}' \
  --platform zhihu
```

### 进化示例
```bash
python calibrate_evolve.py --days 7
```

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.0.0 | 2026-07-17 | 初版创建,支持score/predict/review/evolve四种模式,7维内容评分+盲预测+T+3d复盘+rubric进化,按平台独立迭代 |
