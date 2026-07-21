---
slug: kujiale-design
name: kujiale-design
version: "1.0.0"
displayName: 酷家乐设计-专业版
summary: 企业级室内设计工具,支持多方案对比、批量渲染、自定义风格与团队协作,适配商业设计生产。
license: Proprietary
edition: pro
description: |-
  酷家乐设计专业版,面向企业团队与专业室内设计师的高级智能设计工具。核心能力:
  - 多方案并行对比,支持同户型多风格快速生成
  - 批量渲染高清效果图与全景图
  - 自定义硬装风格库与软装搭配
  - 团队协作与方案版本管理
  - 优先渲染队列与企业级技术支持

  适用场景:
  - 装修公司多方案快速比稿
  - 房地产样板房批量设计
  - 设计团队方案资产管理
  - 家居品牌风格化展示

  差异化:专业版在免费版基础上扩展多方案对比、批量渲染、自定义风格与团队协作,兼容免费版所有流程,适合商业级室内设计生产流水线
tags:
- Creative
- 室内设计
- 企业版
- 商业内容
tools:
  - - read
- exec
---
# 酷家乐设计-专业版

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-------|:-------|:-------|:-----|
| 户型搜索/上传 | 是 | 是 | 两种方式均支持 |
| 硬装风格选择 | 基础库 | 完整库+自定义 | 支持自定义风格 |
| 智能布局 | 是 | 是 | 自动家具布局 |
| 渲染画质 | 标准 | 高清/超清 | 印刷级输出 |
| 多方案对比 | 否 | 是 | 同户型多风格 |
| 批量渲染 | 否 | 是 | 多房间并发 |
| 全景图 | 是 | 是 | 360度全景 |
| 团队协作 | 否 | 是 | 方案共享与权限 |
| 版本管理 | 否 | 是 | 方案历史版本 |
| 技术支持 | 社区 | 专属 | 工单响应 |

## 适用场景

### 场景一:装修公司多方案比稿

装修公司需为同一户型提供 3 种风格方案供客户比稿,使用多方案并行生成。

```bash
# 多方案并行生成(同一户型,不同风格)
python3 scripts/multi_design.py \
  --planId <planId> \
  --styles "现代简约,北欧风,新中式" \
  --parallel 3 \
  --output ./proposals/

# 每个方案独立布局与渲染
# 方案1: 现代简约
node ./scripts/createDesign.js --token=<token> --planId=<planId>
node ./scripts/triggerLayout.js --token=<token> --designId=<designId1> --styleId=<styleId1> --autoDesign=true
node ./scripts/trigger-render.js --obsDesignId=<designId1> --xToken=<token> --quality=hd

# 方案2: 北欧风(并行)
node ./scripts/createDesign.js --token=<token> --planId=<planId>
node ./scripts/triggerLayout.js --token=<token> --designId=<designId2> --styleId=<styleId2> --autoDesign=true
node ./scripts/trigger-render.js --obsDesignId=<designId2> --xToken=<token> --quality=hd

# 生成对比报告
python3 scripts/compare_proposals.py \
  --proposals ./proposals/ \
  --output comparison_report.md
```

### 场景二:房地产样板房批量设计

房地产开发商需为样板房的多个房间批量生成高清渲染图。

```bash
# 批量渲染多个房间
python3 scripts/batch_render.py \
  --designId <designId> \
  --rooms "客餐厅,主卧,次卧,书房,厨房" \
  --quality 4k \
  --parallel 5 \
  --output ./renders/

# 批量生成全景图
python3 scripts/batch_panorama.py \
  --designId <designId> \
  --rooms "客餐厅,主卧,次卧" \
  --output ./panoramas/
```

### 场景三:团队协作设计方案

设计团队需协同完成一个大型项目,使用团队协作与版本管理。

```bash
# 创建团队项目
python3 scripts/team_project.py create \
  --name "万科未来城样板房" \
  --team "design-team-a"

# 提交方案版本
python3 scripts/design_commit.py \
  --project "万科未来城样板房" \
  --designId <designId> \
  --message "v1.0 现代简约方案" \
  --reviewer alice

# 团队成员拉取与审核
python3 scripts/design_pull.py --project "万科未来城样板房"
python3 scripts/design_review.py --pr 42 --action approve --comment "风格统一,通过"
```

## 使用流程

### 优秀步:配置企业 token

```json
// .kjlconfig.json
{
  "access_token": "your_pro_token",
  "edition": "pro",
  "team_id": "your_team_id"
}
```

### 第二步:版本校验

```bash
node ./scripts/versionCheck.js --token=${token} --version=1.0.0
```

### 第三步:启动多方案设计

```bash
# 多方案并行生成
python3 scripts/multi_design.py \
  --planId <planId> \
  --styles "现代简约,北欧风,新中式" \
  --parallel 3
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 16+ + Python 3.9+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 酷家乐 Pro API | 外部 API | 必需 | 企业服务渠道申请 |
| Node.js 16+ | 运行时 | 必需 | 官方安装 |
| Python 3.9+ | 运行时 | 必需 | 官方安装 |
| axios | HTTP 库 | 必需 | npm install axios |
| Git | 版本控制 | 必需 | 系统自带 |

### API Key 配置
- **配置文件**: `.kjlconfig.json`(项目根目录)
- **字段名**: `access_token`(企业版 token)
- **附加字段**: `edition=pro`、`team_id`
- **获取方式**: 通过企业服务渠道申请,享有高优先级渲染队列
- **安全建议**: 配置文件加入 `.gitignore`,token 使用密钥管理服务存储

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持多方案对比、批量渲染、团队协作等企业级室内设计场景

## 案例展示

专业版完整配置:

```json
// .kjlconfig.json
{
  "access_token": "your_pro_token",
  "edition": "pro",
  "team_id": "your_team_id",
  "default_render_quality": "4k",
  "default_parallel": 5,
  "custom_styles_repo": "git@team:styles-repo"
}
```

```bash
# 高级参数
--quality standard|hd|4k        # 渲染画质
--parallel <n>                  # 并发数(1-10)
--multi-style <style1,style2>   # 多方案风格
--batch-rooms <room1,room2>     # 批量渲染房间
--team-project <name>           # 团队项目名
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有流程与脚本,迁移时仅需更换 token 并设置 `edition=pro`。

### Q2:多方案并发生成会冲突吗?
A:不会。每个方案独立创建 designId,互不影响。并发数受 API 限制(最高 10)。

### Q3:4K 渲染时间多久?
A:4K 渲染约需 5-10 分钟/房间,批量渲染时建议并发 3-5 个,避免超时。

### Q4:自定义风格如何导入?
A:在酷家乐平台创建自定义风格后,获取 styleId,在脚本中传入即可。支持团队风格库共享。

### Q5:团队协作支持多少人?
A:License 绑定团队席位,支持 5-50 人团队(视授权规模)。支持角色权限管理。

### Q6:能否集成到 CRM 系统?
A:可以。通过 API 可集成到装修公司 CRM 系统,实现客户→户型→方案→渲染的自动化流程。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
