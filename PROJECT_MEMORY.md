# Project Memory - d:\skills (SkillHub 商业化发布项目)

## 项目目标
在腾讯 SkillHub (https://skillhub.cloud.tencent.com) 发布优质 Skill 获取收益。

## SkillHub 账号凭证
- **API Key**: `skh_7906ab19cefaf3854349fae7b8b97310c5582073b76acf1557731c0f1c612c11`
- **Host**: `https://api.skillhub.cn`
- **账号**: @user_cb75122a (userId=600324)
- **状态**: 已实名,已登录
- **凭证文件**: `d:\skills\.skillhub-credentials\api-key.txt`

## 发布环境(已就绪 2026-07-17)
- **CLI**: skillhub 2026.7.7,路径 ~/.local/bin/skillhub(Git Bash 环境)
- **运行方式**: Git Bash (C:\Program Files\Git\bin\bash.exe),非 WSL
- **便捷脚本**: d:\skills\skillhub.ps1 + d:\skills\run-skillhub.sh
- **用法**: .\skillhub.ps1 publish .\skill文件夹 --dry-run

## 商业化分析成果(2026-07-17)
### 可提取销售清单(20个候选,分3梯队)
**第一梯队 - 直接对标获奖(5个)**:
1. writing-style-distiller(对标铜奖蒸馏写作,改造易)
2. dailyhot(对标闪光奖全网热搜,零依赖改造最易)
3. news-monitor(对标闪光奖新闻雷达,改造中)
4. competitor-analyzer+ecommerce-pricing-strategy(对标闪光奖竞价雷达,改造中)
5. smart-browser(对标银奖浏览器自动化,改造中)

**第二梯队 - 独特能力市场空白(8个)**:
6. content-calibrator(7维评分差异化最强)
7. drama-generator(25步短剧改造难建议拆分)
8. novel-generator(8步小说生成)
9. video-generator(多引擎改造难建议拆分)
10. ai-art-studio(AI画图接单)
11. fortune-teller(8种命理改造易)
12. ebook-generator(电子书)
13. poetry-weaver(古诗词)

**第三梯队 - 通用工具型(7个改造易)**:
14. seo-optimizer / 15. title-generator / 16. market-copywriter
17. hook-generator / 18. content-rewriter
19. geo-content-optimizer / 20. viral-content-analyzer

### 发布路线图
- 阶段一(第1周): 零依赖Skill快速验证 - title-generator/market-copywriter/dailyhot/viral-content-analyzer/fortune-teller
- 阶段二(第2-3周): 核心攻坚 - writing-style-distiller/content-calibrator/竞品定价/news-monitor/smart-browser/novel-generator/ai-art-studio
- 阶段三(第4-6周): 深度+组合 - drama/video拆分 + 工具箱套餐

### 独立性改造通用模式
1. PostgreSQL → SQLite/JSON文件
2. 内部MCP → 独立Python脚本/直接LLM调用
3. Skill间依赖 → 内联或可选
4. 租户体系 → 移除,单用户模式

## 分析报告
- 路径: d:\skills\skillhub-monetization-analysis\skillhub-monetization-analysis.html
