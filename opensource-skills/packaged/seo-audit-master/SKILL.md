---
slug: seo-audit-master
name: seo-audit-master
version: "1.0.0"
displayName: "SEO审计大师"
summary: "全站SEO体检:技术内容架构链接四维度审计,输出可执行优化清单"
license: MIT
description: |-
  SEO审计大师——对网站执行全面SEO审计,技术SEO+内容SEO+架构验证+链接分析四维度覆盖。输出可执行的优化清单,让搜索引擎排名提升有据可循。

  核心能力:
  - 技术SEO审计:可抓取性/索引/速度/移动适配
  - 内容SEO审计:关键词/标题/meta/内容质量评估
  - 架构验证:结构化数据/内部链接/面包屑
  - 链接分析:外链质量/反链数量/锚文本分布
  - 可执行清单:按优先级排序的优化建议
  - 竞品对比:SEO差距分析与追赶策略

  适用场景:
  - 独立创业者新站优化:上线前奠定SEO基础
  - SaaS创业者排名下降诊断:搜索流量下降原因分析
  - 副业达人全站审计:定期SEO健康检查保持排名
  - 一人公司网站迁移:改版/迁移后SEO完整性检查

  差异化:不是泛泛的SEO建议工具,而是四维度结构化审计的SEO专家,输出按优先级排序的可执行优化清单,让没有SEO经验的创业者也能系统化提升搜索排名。

  触发关键词:SEO审计、SEO诊断、技术SEO、内容SEO、SEO优化、网站审计、搜索引擎优化、索引、可抓取性、结构化数据
tags: [SEO优化, 网站审计, 搜索引擎优化, 技术SEO, 流量增长]
tools: [read, exec]
---

# SEO审计大师

对网站执行全面 SEO 审计。从技术到内容,从架构到链接,输出可执行的优化清单。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 全站审计 | 上线前/定期体检 | 全面 SEO 健康检查 |
| 排名下降 | 搜索流量下降 | 诊断排名下降原因 |
| 新站优化 | 新站上线 | 奠定 SEO 基础 |
| 竞品对比 | 对标竞品 | SEO 差距分析 |
| 迁移检查 | 网站改版/迁移 | 迁移后 SEO 完整性检查 |

## 工作流

### 1. 技术 SEO 审计

1. **可抓取性**:
   - robots.txt 检查
   - 爬虫访问权限
   - noindex/nofollow 标签审查
   - 网站地图(sitemap.xml)完整性
2. **索引状态**:
   - Google Search Console 索引覆盖
   - 已索引页面数 vs 总页面数
   - 重复页面/规范化(canonical)问题
3. **页面速度**:
   - Core Web Vitals(LCP/CLS/INP)
   - TTFB/FCP
   - 移动端速度
4. **移动适配**:
   - 响应式设计检查
   - 移动友好性测试
   - 视口配置
5. **HTTPS 安全**:SSL 证书/混合内容检查

### 2. 内容 SEO 审计

1. **关键词分析**:
   - 目标关键词排名
   - 关键词覆盖缺口
   - 关键词 cannibalization(自相竞争)
   - 长尾关键词机会
2. **标题与描述**:
   - title 标签(长度/关键词/独特性)
   - meta description(长度/吸引力)
   - H1-H6 层级结构
3. **内容质量**:
   - 内容深度与长度
   - 关键词密度(1-2%)
   - 语义相关词(LSI)
   - 内容新鲜度/更新频率
   - 重复内容检测
4. **图片优化**:
   - alt 文本
   - 文件大小/格式(WebP)
   - 文件名规范

### 3. 架构验证

1. **结构化数据**:
   - JSON-LD schema 检查
   - 富媒体搜索结果资格
   - 结构化数据错误
2. **内部链接**:
   - 内部链接结构
   - 锚文本分布
   - 孤立页面(无内链)
   - 点击深度(重要页 ≤3 次点击)
3. **URL 结构**:
   - URL 规范化
   - URL 长度/可读性
   - URL 层级结构
   - 重定向链(301/302)
4. **面包屑导航**:实施与结构化数据

### 4. 链接分析

1. **外链概况**:
   - 反链总数/域名数
   - 反链质量(域名权重)
   - 锚文本分布
   - 有毒链接识别
2. **内链权重**:PageRank 流向分析
3. **出站链接**:外部链接质量与数量

### 5. 优化清单与报告

1. **问题优先级**:
   - 关键(Critical):严重影响排名
   - 重要(Important):影响排名
   - 建议(Suggested):锦上添花
2. **可执行清单**:每个问题附具体修复步骤
3. **预期收益**:修复后的预期影响
4. **实施难度**:每项修复的难度评估

## 审计检查清单(核心)

- [ ] robots.txt 配置正确
- [ ] sitemap.xml 完整且提交
- [ ] 所有重要页面已索引
- [ ] canonical 标签正确
- [ ] Core Web Vitals 全部达标
- [ ] 移动友好
- [ ] HTTPS 无混合内容
- [ ] title/meta description 完整
- [ ] H1 唯一且含关键词
- [ ] 结构化数据无错误
- [ ] 内部链接结构合理
- [ ] 无孤立页面
- [ ] 无重复内容
- [ ] 图片有 alt 文本

## 输出规范

- 审计报告:`output/{site-domain}/seo-audit.md`
- 问题清单:`output/{site-domain}/issues.md`(按优先级排序)
- 优化建议:`output/{site-domain}/recommendations.md`
- 关键词分析:`output/{site-domain}/keywords.md`
- 技术检查:`output/{site-domain}/technical.md`

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 可选 | 由Agent内置LLM提供SEO分析 |
| 联网搜索 | 工具 | 可选 | WebSearch/WebFetch检查排名 |

### API Key 配置
- 本Skill无需额外API Key配置

### 纯Markdown使用说明
本Skill为SEO审计方法论指导。排名检查需要联网搜索能力。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用
