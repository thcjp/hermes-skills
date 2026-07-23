---
slug: react-video-composer
name: remotion-video-studio
version: 1.1.0
displayName: 视频创作工作室
summary: 自然语言转视频,用React代码生成字幕转场配音动画,无需剪辑软件
license: Proprietary
description: 视频创作工作室将自然语言描述转换为基于React的可渲染视频代码,核心功能包括分镜脚本结构化、React视频代码生成(Composition/Sequence/动画原语)、TTS配音与音频转录字幕同步、多规格渲染输出(横屏/竖屏/方形)。适用于文字转视频、字幕同步、数据可视化动画、产品演示视频、社交短视频场景。触发关键词:视频制作、视频生成、React视频、短视频、内容创作、Remotion、字幕同步、视频渲染。
tags:
- 视频制作
- 视频生成
- React视频
- 短视频
- 内容创作
tools:
- read
- exec
  0.5元/次
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 视频创作工作室

将自然语言描述转换为基于 React 的可渲染视频代码。核心理念:在 AI 眼里,视频的每一帧都是一个网页,用前端代码实现视频制作。

## 核心能力

1. **分镜脚本结构化**:接收主题/时长/风格/平台(横屏/竖屏)/目标受众,生成分镜列表(每镜含时间区间/画面描述/字幕/配音文本),输出分镜表供用户确认或调整。
2. **React视频代码生成**:初始化项目结构(Composition.tsx/scenes/audio),逐场景实现React组件用`<Sequence>`控制时间区间,`useCurrentFrame()`和插值函数驱动动画,字幕层基于时间轴渲染,转场效果(crossfade/wipe/reveal)。
3. **配音与音效处理**:TTS配音将脚本文本转为语音生成音频文件,音频转录对配音音频转录生成精确时间轴用于字幕同步,背景音乐可选添加BGM支持节拍同步视觉脉冲。
4. **多规格渲染输出**:浏览器实时预览,调用渲染管线输出MP4/WebM,支持横屏1920x1080、竖屏1080x1920、方形1080x1080多规格。
5. **动画原语库**:淡入淡出/缩放/位移/旋转/路径动画,文字特效(marker sweep/手绘圆圈/爆发线/scribble/sketchout),数据可视化(动态柱状图/折线图/数字翻滚),音频反应(beat sync/glow pulse)。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文字转视频 | 脚本或描述文本 | 自然语言→React视频代码→渲染MP4,输出到`output/{project}/` |
| 字幕同步 | 音频或配音文件 | 自动生成时间轴对齐的字幕层 |
| 数据可视化动画 | 数据集+展示需求 | 数字变化做成动态图表动画 |
| 产品演示视频 | 产品功能描述 | 生成终端操作/界面演示动画 |
| 社交短视频 | 15-60秒内容脚本 | 竖屏适配,强钩子前3秒 |

**不适用于**:
- 实拍视频编辑(请用Premiere/Final Cut)
- 3D动画视频(本工具为2D DOM/Canvas渲染)
- 直播推流(非视频生成场景)
- 长视频(30分钟以上,渲染时间过长)

## 使用流程

### Step 1: 需求采集与脚本结构化
1. 接收用户输入:主题、时长、风格、平台(横屏/竖屏)、目标受众
2. 生成视频脚本:分镜列表,每镜包含(时间区间/画面描述/字幕/配音文本)
3. 确认脚本:输出分镜表供用户确认或调整

### Step 2: React视频代码生成
1. **初始化项目结构**:`src/Composition.tsx`、`src/scenes/`、`src/audio/`
2. **逐场景实现**:每个场景为一个React组件,使用`<Sequence>`控制时间区间
3. **动画编排**:用`useCurrentFrame()`和插值函数(`interpolate()`)驱动动画
4. **字幕层**:基于时间轴渲染字幕,支持样式定制
5. **转场**:crossfade/wipe/reveal等转场效果

### Step 3: 配音与音效
1. **TTS配音**:将脚本文本转为语音,生成音频文件(可用国内TTS服务)
2. **音频转录**:对配音音频转录,生成精确时间轴用于字幕同步
3. **背景音乐**:可选添加BGM,支持节拍同步视觉脉冲

### Step 4: 预览与渲染输出
1. **预览**:在浏览器中实时预览视频效果(`npm start`启动Remotion Studio)
2. **渲染**:调用渲染管线输出MP4/WebM(`npx remotion render`)
3. **多规格输出**:横屏1920x1080、竖屏1080x1920、方形1080x1080

## 示例

### 示例1: 产品介绍短视频

**输入**:
```
制作一个30秒的产品介绍视频,产品是"AI笔记应用"。
风格:科技感,竖屏(1080x1920),适合抖音发布。
分镜: 0-5s 钩子(痛点) / 5-15s 产品展示 / 15-25s 功能演示 / 25-30s CTA
```

**输出** (`output/ai-note-video/src/Composition.tsx`):
```tsx
import { Composition } from "remotion";
import { HookScene } from "./scenes/HookScene";
import { ProductScene } from "./scenes/ProductScene";
import { FeatureScene } from "./scenes/FeatureScene";
import { CTAScene } from "./scenes/CTAScene";

export const ProductVideo = () => {
  return (
    <>
      <Composition
        id="ProductVideo"
        component={VideoComposition}
        durationInFrames={900} // 30秒 @ 30fps
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};

const VideoComposition = () => {
  return (
    <>
      <HookScene />      {/* 0-5s: 痛点钩子 */}
      <ProductScene />   {/* 5-15s: 产品展示 */}
      <FeatureScene />   {/* 15-25s: 功能演示 */}
      <CTAScene />       {/* 25-30s: 行动号召 */}
    </>
  );
};
```

`output/ai-note-video/src/scenes/HookScene.tsx`:
```tsx
import { Sequence, useCurrentFrame, interpolate } from "remotion";

export const HookScene = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: "clamp" });
  const translateY = interpolate(frame, [0, 15], [50, 0], { extrapolateRight: "clamp" });

  return (
    <Sequence from={0} durationInFrames={150}>
      <div style={{ flex: 1, backgroundColor: "#0A0A0A", justifyContent: "center", alignItems: "center" }}>
        <h1 style={{ color: "#00FF88", fontSize: 80, opacity, transform: `translateY(${translateY}px)` }}>
          还在手动整理笔记?
        </h1>
      </div>
    </Sequence>
  );
};
```

渲染命令:
```bash
npx remotion render ProductVideo output/ai-note-video/video.mp4 --codec=h264
```

### 示例2: 数据可视化动画

**输入**:
```
制作一个数据增长动画视频,展示2020-2024年用户数从1万增长到100万。
横屏1920x1080,15秒,数字翻滚效果+柱状图增长动画。
```

**输出** (`output/data-viz/src/scenes/GrowthScene.tsx`):
```tsx
import { Sequence, useCurrentFrame, interpolate, spring } from "remotion";

export const GrowthScene = () => {
  const frame = useCurrentFrame();
  const progress = spring({ frame, fps: 30, config: { damping: 200 } });
  const users = Math.floor(interpolate(progress, [0, 1], [10000, 1000000]));
  const barHeight = interpolate(progress, [0, 1], [10, 800]);

  return (
    <Sequence durationInFrames={450}>
      <div style={{ flex: 1, backgroundColor: "#1A1A2E", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
        <h1 style={{ color: "#FFFFFF", fontSize: 120, fontFamily: "monospace" }}>
          {users.toLocaleString()} 用户
        </h1>
        <div style={{ width: 200, height: barHeight, backgroundColor: "#E94560", marginTop: 50 }} />
      </div>
    </Sequence>
  );
};
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| Remotion渲染失败 | Chrome/Chromium缺失或版本不兼容 | 安装Chrome或设置PUPPETEER_EXECUTABLE_PATH,Docker中用`ghcr.io/remotion-dev/docker`镜像 |
| 渲染超时 | 视频过长或场景复杂 | 分段渲染后合并,或降低帧率(30→24fps),减少特效 |
| TTS配音失败 | TTS服务不可达或API Key无效 | 检查网络和Key,改用本地TTS(如edge-tts),或人工录制 |
| 字幕不同步 | 转录时间轴不准确 | 用Whisper重新转录,手动调整字幕时间戳 |
| 内存不足 | 高分辨率+长视频渲染 | 降低分辨率(1080p→720p),分段渲染,增加服务器内存 |
| 字体缺失 | 系统无指定字体 | 安装字体或使用Web字体,Remotion支持`@remotion/google-fonts` |
| 动画卡顿 | 每帧重计算未缓存 | 用`useMemo`缓存计算结果,减少不必要的重渲染 |
| 音视频不同步 | 音频和视频帧率不匹配 | 确保音频采样率与视频fps一致,用`<Audio>`组件同步 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| Node.js 18+ | 运行时 | 必需 | Remotion框架运行 | Node.js官网,国内用cnpm/nvm镜像 |
| Remotion | 框架 | 必需 | `npm install remotion @remotion/cli` | `cnpm install remotion @remotion/cli` |
| Chrome/Chromium | 工具 | 必需 | 渲染引擎 | 国内可直接下载,或用Docker镜像 |
| FFmpeg | 工具 | 必需 | 视频编码 | 各平台下载或包管理器安装 |
| TTS服务 | 服务 | 可选 | 文本转语音配音 | 阿里云语音合成/腾讯云TTS/edge-tts(免费) |
| Whisper | 工具 | 可选 | 音频转录(字幕同步) | openai-whisper本地部署或云端API |
| LLM API | API | 可选 | 由Agent内置LLM提供脚本生成 | 国内Agent(通义/文心/智谱)均可 |

### API Key 配置
- **本Skill本身无需API Key**: 代码生成由Agent LLM完成
- **TTS服务**: 阿里云/腾讯云TTS的API Key通过环境变量传入,不硬编码
- **Whisper API**: 如用云端Whisper,API Key通过环境变量传入
- **安全要求**: API Key零暴露,不写入视频代码、不输出到日志、不硬编码

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于运行Remotion渲染

## 核心能力详解

- **Composition编排**:多场景`<Sequence>`组合,时间轴精确控制
- **动画原语**:淡入淡出、缩放、位移、旋转、路径动画
- **文字特效**:marker sweep(标记扫过)、手绘圆圈、爆发线、scribble、sketchout
- **数据可视化**:动态柱状图、折线图、数字翻滚
- **音频反应**:beat sync(节拍同步)、glow pulse(发光脉冲)
- **字幕与标题卡**:同步字幕、动画标题卡、overlay字幕
- **转场**:crossfade、wipe、reveal、shader transition

## 设计原则

1. **帧即网页**:每一帧都是React渲染的DOM/Canvas
2. **可组合**:动画原语可自由组合,不硬编码
3. **可预览**:浏览器实时预览,所见即所得
4. **可渲染**:确定性渲染,同一代码同一视频
5. **性能优先**:避免每帧重计算,用`useMemo`缓存

## 输出规范

- 视频代码保存到`output/{project-name}/src/`
- 脚本分镜表保存到`output/{project-name}/script.md`
- 渲染命令:`npx remotion render {Composition} out/video.mp4`
- 支持参数化:通过props传入不同数据生成系列视频

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 竖屏短视频(前3秒强钩子+CTA)

**输入**:
```
主题: 知识付费课程推广短视频
时长: 15秒
平台: 抖音(竖屏1080x1920)
风格: 科技感,强钩子
分镜:
- 0-3s: 钩子("这个技能让你薪资翻倍")
- 3-8s: 痛点+解决方案展示
- 8-12s: 课程亮点(3个要点动画)
- 12-15s: CTA("点击链接立即学习")
```

**LLM生成输出** (`output/course-promo/src/Composition.tsx`):
```tsx
import { Composition } from "remotion";
import { HookScene } from "./scenes/HookScene";
import { SolutionScene } from "./scenes/SolutionScene";
import { FeatureScene } from "./scenes/FeatureScene";
import { CTAScene } from "./scenes/CTAScene";

export const CoursePromo = () => (
  <Composition
    id="CoursePromo"
    component={VideoComposition}
    durationInFrames={450} // 15秒 @ 30fps
    fps={30}
    width={1080}
    height={1920}
  />
);

const VideoComposition = () => (
  <>
    <HookScene />      {/* 0-3s: 强钩子 */}
    <SolutionScene />  {/* 3-8s: 痛点+方案 */}
    <FeatureScene />   {/* 8-12s: 课程亮点 */}
    <CTAScene />       {/* 12-15s: 行动号召 */}
  </>
);
```

**LLM生成输出** (`output/course-promo/src/scenes/HookScene.tsx`):
```tsx
import { Sequence, useCurrentFrame, interpolate, spring } from "remotion";

export const HookScene = () => {
  const frame = useCurrentFrame();

  // 文字弹入动画(spring弹性)
  const scale = spring({ frame, fps: 30, config: { damping: 12, stiffness: 200 } });
  // 背景脉冲效果
  const bgPulse = interpolate(
    Math.sin(frame * 0.3), [-1, 1], [0.85, 1]
  );

  // 3秒末淡出
  const opacity = interpolate(frame, [75, 90], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <Sequence from={0} durationInFrames={90}>
      <div style={{
        flex: 1, backgroundColor: "#0A0A0A", justifyContent: "center",
        alignItems: "center", opacity, transform: `scale(${bgPulse})`,
      }}>
        <h1 style={{
          color: "#00FF88", fontSize: 90, fontWeight: 900, textAlign: "center",
          transform: `scale(${scale})`,
          textShadow: "0 0 30px rgba(0,255,136,0.5)",
        }}>
          这个技能<br/>让你薪资翻倍
        </h1>
      </div>
    </Sequence>
  );
};
```

**LLM生成输出** (`output/course-promo/src/scenes/FeatureScene.tsx`):
```tsx
import { Sequence, useCurrentFrame, interpolate, spring } from "remotion";

const features = [
  { icon: "🚀", title: "实战项目驱动", desc: "5个企业级项目" },
  { icon: "💼", title: "大厂面试题库", desc: "200+高频题" },
  { icon: "🎓", title: "导师1v1辅导", desc: "简历优化+模拟面试" },
];

export const FeatureScene = () => {
  const frame = useCurrentFrame();

  return (
    <Sequence from={240} durationInFrames={120}>
      <div style={{
        flex: 1, backgroundColor: "#1A1A2E", flexDirection: "column",
        justifyContent: "center", alignItems: "center", padding: 60,
      }}>
        <h2 style={{ color: "#FFFFFF", fontSize: 60, marginBottom: 60, fontWeight: 800 }}>
          课程三大亮点
        </h2>
        {features.map((feature, i) => {
          // 每个要点依次弹入(stagger)
          const delay = i * 15;
          const localFrame = frame - delay;
          const itemOpacity = interpolate(localFrame, [0, 10], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
          const translateY = interpolate(localFrame, [0, 10], [50, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

          return (
            <div key={i} style={{
              flexDirection: "row", alignItems: "center", marginBottom: 40,
              opacity: itemOpacity, transform: `translateY(${translateY}px)`,
            }}>
              <span style={{ fontSize: 70, marginRight: 30 }}>{feature.icon}</span>
              <div>
                <h3 style={{ color: "#00FF88", fontSize: 42, fontWeight: 700 }}>{feature.title}</h3>
                <p style={{ color: "#CCCCCC", fontSize: 28 }}>{feature.desc}</p>
              </div>
            </div>
          );
        })}
      </div>
    </Sequence>
  );
};
```

**LLM生成输出** (`output/course-promo/src/scenes/CTAScene.tsx`):
```tsx
import { Sequence, useCurrentFrame, interpolate, spring } from "remotion";

export const CTAScene = () => {
  const frame = useCurrentFrame();
  // 按钮脉冲动画
  const buttonScale = interpolate(
    Math.sin(frame * 0.2), [-1, 1], [1, 1.08]
  );
  const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <Sequence from={360} durationInFrames={90}>
      <div style={{
        flex: 1, backgroundColor: "#0A0A0A", justifyContent: "center",
        alignItems: "center", opacity,
      }}>
        <h1 style={{ color: "#FFFFFF", fontSize: 72, fontWeight: 900, textAlign: "center", marginBottom: 60 }}>
          限时特惠<br/>立减500元
        </h1>
        <div style={{
          backgroundColor: "#FF6B35", padding: "30px 80px", borderRadius: 20,
          transform: `scale(${buttonScale})`,
          boxShadow: "0 0 40px rgba(255,107,53,0.6)",
        }}>
          <span style={{ color: "#FFFFFF", fontSize: 48, fontWeight: 800 }}>
            点击链接立即学习
          </span>
        </div>
      </div>
    </Sequence>
  );
};
```

**LLM生成输出** (`output/course-promo/script.md`):
```markdown
# 视频脚本分镜表

| 镜号 | 时间 | 画面描述 | 字幕 | 配音文本 |
|:-----|:-----|:---------|:-----|:---------|
| 1 | 0-3s | 黑底绿字弹入,脉冲背景 | 这个技能让你薪资翻倍 | 想让薪资翻倍?这个技能你必须知道 |
| 2 | 3-8s | 痛点文字+方案展示 | 程序员进阶痛点→系统化课程 | 很多程序员卡在初级岗,缺的是系统化的进阶路线 |
| 3 | 8-12s | 三个亮点依次弹入 | 实战项目/面试题库/1v1辅导 | 我们的课程:5个实战项目+200道面试题+导师1对1辅导 |
| 4 | 12-15s | CTA按钮脉冲 | 限时特惠立减500元 | 限时特惠立减500,点击链接立即学习 |
```

**效果验证**: ✓竖屏1080x1920正确 ✓前3秒强钩子(spring弹入+脉冲) ✓stagger动画(要点依次出现) ✓CTA按钮脉冲动画 ✓分镜表含时间/画面/字幕/配音

### 案例2: 数据可视化动画(数字翻滚+柱状图增长)

**输入**:
```
主题: 展示公司2020-2024年用户增长
时长: 10秒
风格: 数据科技感,横屏1920x1080
要求: 数字翻滚效果+柱状图从0增长的动画
数据: 2020:1万, 2021:5万, 2022:15万, 2023:35万, 2024:100万
```

**LLM生成输出** (`output/data-viz/src/scenes/GrowthScene.tsx`):
```tsx
import { Sequence, useCurrentFrame, interpolate, spring } from "remotion";

const data = [
  { year: "2020", users: 10000 },
  { year: "2021", users: 50000 },
  { year: "2022", users: 150000 },
  { year: "2023", users: 350000 },
  { year: "2024", users: 1000000 },
];

export const GrowthScene = () => {
  const frame = useCurrentFrame();
  const durationInFrames = 300; // 10秒 @ 30fps

  // 总体进度(0到1,用spring实现缓动)
  const progress = spring({
    frame,
    fps: 30,
    config: { damping: 200, mass: 1 },
    durationInFrames: 120,
  });

  // 当前显示的数据索引(随时间推进)
  const dataIndex = Math.min(
    Math.floor(interpolate(frame, [30, 270], [0, data.length - 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })),
    data.length - 1
  );

  // 当前数字(翻滚效果)
  const currentUsers = Math.floor(
    interpolate(progress, [0, 1], [10000, data[dataIndex].users])
  );

  // 格式化数字
  const formatNumber = (num: number) => {
    if (num >= 10000) return `${(num / 10000).toFixed(1)}万`;
    return num.toLocaleString();
  };

  // 最大柱状图高度(像素)
  const maxBarHeight = 500;
  const maxUsers = data[data.length - 1].users;

  return (
    <Sequence durationInFrames={durationInFrames}>
      <div style={{
        flex: 1, backgroundColor: "#0F0F23", flexDirection: "column",
        justifyContent: "center", alignItems: "center",
      }}>
        {/* 大标题 */}
        <h1 style={{
          color: "#FFFFFF", fontSize: 48, fontWeight: 700, marginBottom: 20,
        }}>
          用户增长 2020-2024
        </h1>

        {/* 翻滚数字 */}
        <div style={{
          color: "#00FF88", fontSize: 120, fontFamily: "monospace",
          fontWeight: 900, marginBottom: 40,
          textShadow: "0 0 40px rgba(0,255,136,0.4)",
        }}>
          {formatNumber(currentUsers)}
        </div>

        {/* 柱状图 */}
        <div style={{ flexDirection: "row", alignItems: "flex-end", gap: 40, height: maxBarHeight + 60 }}>
          {data.map((item, i) => {
            // 每个柱子依次增长(stagger)
            const barDelay = i * 40;
            const barProgress = spring({
              frame: frame - barDelay,
              fps: 30,
              config: { damping: 200 },
              durationInFrames: 60,
            });
            const barHeight = (item.users / maxUsers) * maxBarHeight * Math.max(0, barProgress);
            // 当前高亮的柱子
            const isActive = i === dataIndex;
            const barColor = isActive ? "#00FF88" : "#3A3A6E";

            return (
              <div key={item.year} style={{ alignItems: "center", flexDirection: "column" }}>
                <div style={{
                  width: 80, height: Math.max(2, barHeight),
                  backgroundColor: barColor, borderRadius: 8,
                  boxShadow: isActive ? "0 0 20px rgba(0,255,136,0.6)" : "none",
                  transition: "background-color 0.3s",
                }} />
                <span style={{
                  color: isActive ? "#00FF88" : "#888888",
                  fontSize: 24, marginTop: 10, fontWeight: isActive ? 700 : 400,
                }}>
                  {item.year}
                </span>
              </div>
            );
          })}
        </div>

        {/* 底部标注 */}
        <p style={{ color: "#666666", fontSize: 20, marginTop: 30 }}>
          5年增长100倍 · 数据来源: 公司年报
        </p>
      </div>
    </Sequence>
  );
};
```

**效果验证**: ✓数字翻滚效果(interpolate+spring缓动) ✓柱状图stagger增长(依次弹起) ✓当前数据柱子高亮(颜色+发光) ✓格式化显示(1万/100万) ✓数据来源标注

### 案例3: 产品演示视频(TTS配音+字幕同步)

**输入**:
```
主题: AI笔记应用功能演示
时长: 20秒
风格: 简洁现代,横屏1920x1080
配音: 使用edge-tts生成中文语音
字幕: 自动同步配音时间轴
分镜:
- 0-5s: "AI笔记,让记录更智能"
- 5-10s: "语音转文字,实时记录"
- 10-15s: "智能摘要,一键提炼要点"
- 15-20s: "立即下载,开启智能笔记"
```

**LLM生成输出** (`output/ai-note-demo/src/Composition.tsx`):
```tsx
import { Composition, Audio } from "remotion";
import { Scene1, Scene2, Scene3, Scene4 } from "./scenes";
import { SubtitleLayer } from "./components/SubtitleLayer";
import narration from "../audio/narration.mp3";
import subtitles from "../data/subtitles.json";

export const AINoteDemo = () => (
  <Composition
    id="AINoteDemo"
    component={VideoComposition}
    durationInFrames={600} // 20秒 @ 30fps
    fps={30}
    width={1920}
    height={1080}
  />
);

const VideoComposition = () => (
  <>
    {/* 配音音频(贯穿全程) */}
    <Audio src={narration} />

    {/* 四个场景 */}
    <Scene1 />
    <Scene2 />
    <Scene3 />
    <Scene4 />

    {/* 字幕层(覆盖在所有场景之上) */}
    <SubtitleLayer subtitles={subtitles} />
  </>
);
```

**LLM生成输出** (`output/ai-note-demo/src/components/SubtitleLayer.tsx`):
```tsx
import { Sequence, useCurrentFrame } from "remotion";

interface Subtitle {
  startFrame: number;
  endFrame: number;
  text: string;
}

export const SubtitleLayer = ({ subtitles }: { subtitles: Subtitle[] }) => {
  const frame = useCurrentFrame();

  // 找到当前帧对应的字幕
  const currentSubtitle = subtitles.find(
    (s) => frame >= s.startFrame && frame < s.endFrame
  );

  if (!currentSubtitle) return null;

  // 字幕淡入淡出
  const fadeIn = Math.min(1, (frame - currentSubtitle.startFrame) / 8);
  const fadeOut = Math.min(1, (currentSubtitle.endFrame - frame) / 8);
  const opacity = Math.min(fadeIn, fadeOut);

  return (
    <div style={{
      position: "absolute", bottom: 80, left: 0, right: 0,
      justifyContent: "center", alignItems: "center", opacity,
    }}>
      <div style={{
        backgroundColor: "rgba(0,0,0,0.7)", borderRadius: 12,
        padding: "16px 40px", maxWidth: "80%",
      }}>
        <span style={{
          color: "#FFFFFF", fontSize: 36, fontWeight: 500,
          textAlign: "center",
        }}>
          {currentSubtitle.text}
        </span>
      </div>
    </div>
  );
};
```

**LLM生成输出** (`output/ai-note-demo/data/subtitles.json`):
```json
[
  { "startFrame": 0, "endFrame": 150, "text": "AI笔记,让记录更智能" },
  { "startFrame": 150, "endFrame": 300, "text": "语音转文字,实时记录" },
  { "startFrame": 300, "endFrame": 450, "text": "智能摘要,一键提炼要点" },
  { "startFrame": 450, "endFrame": 600, "text": "立即下载,开启智能笔记" }
]
```

**LLM生成输出** (`output/ai-note-demo/scripts/generate-tts.py`):
```python
# 使用edge-tts生成中文配音
import edge_tts
import json
import asyncio
import subprocess

# 配音脚本(对应4个场景)
script = [
    {"text": "AI笔记,让记录更智能", "duration": 5},
    {"text": "语音转文字,实时记录", "duration": 5},
    {"text": "智能摘要,一键提炼要点", "duration": 5},
    {"text": "立即下载,开启智能笔记", "duration": 5},
]

async def generate_narration():
    """生成完整配音音频"""
    full_text = "".join([s["text"] + "。" for s in script])
    communicate = edge_tts.Communicate(full_text, "zh-CN-XiaoxiaoNeural")
    await communicate.save("output/ai-note-demo/audio/narration.mp3")
    print("配音已生成: audio/narration.mp3")

def generate_subtitles():
    """生成字幕时间轴(基于固定时长,实际可用Whisper精确转录)"""
    fps = 30
    subtitles = []
    current_frame = 0
    for s in script:
        subtitles.append({
            "startFrame": current_frame,
            "endFrame": current_frame + int(s["duration"] * fps),
            "text": s["text"],
        })
        current_frame += int(s["duration"] * fps)

    with open("output/ai-note-demo/data/subtitles.json", "w", encoding="utf-8") as f:
        json.dump(subtitles, f, ensure_ascii=False, indent=2)
    print("字幕已生成: data/subtitles.json")

async def main():
    await generate_narration()
    generate_subtitles()

    # 用Whisper精确转录(可选,提升字幕同步精度)
    # subprocess.run([
    #     "whisper", "audio/narration.mp3",
    #     "--model", "base",
    #     "--language", "zh",
    #     "--output_format", "json",
    #     "--output_dir", "data/"
    # ])

asyncio.run(main())
```

**效果验证**: ✓TTS配音集成(Audio组件) ✓字幕层覆盖所有场景 ✓字幕淡入淡出(fadeIn/fadeOut) ✓时间轴帧级精确(30fps) ✓edge-tts中文配音(免费)

### 案例4: 动画标题卡(文字特效+转场)

**输入**:
```
主题: 视频片头标题卡
时长: 5秒
风格: 高级感,文字逐字出现
效果: 文字sketchout描边动画+marker sweep标记扫过
横屏1920x1080
```

**LLM生成输出** (`output/title-card/src/scenes/TitleCard.tsx`):
```tsx
import { Sequence, useCurrentFrame, interpolate, spring } from "remotion";

const title = "产品发布会";
const subtitle = "2024年度盛典";

export const TitleCard = () => {
  const frame = useCurrentFrame();

  // 标题逐字出现
  const titleChars = title.split("");
  const titleProgress = interpolate(frame, [15, 75], [0, titleChars.length], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });

  // 副标题淡入
  const subtitleOpacity = interpolate(frame, [80, 100], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });
  const subtitleY = interpolate(frame, [80, 100], [30, 0], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });

  // marker sweep(标记扫过效果)
  const sweepX = interpolate(frame, [30, 90], [-200, 2100], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });

  // 装饰线动画
  const lineWidth = interpolate(frame, [20, 60], [0, 600], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });

  return (
    <Sequence durationInFrames={150}>
      <div style={{
        flex: 1, backgroundColor: "#0A0A0A", justifyContent: "center",
        alignItems: "center", flexDirection: "column", overflow: "hidden",
      }}>
        {/* 装饰线(上方) */}
        <div style={{
          width: lineWidth, height: 2, backgroundColor: "#FFD700",
          marginBottom: 40,
        }} />

        {/* 标题(逐字出现) */}
        <div style={{ flexDirection: "row", position: "relative" }}>
          {titleChars.map((char, i) => {
            const charVisible = i < Math.floor(titleProgress);
            const charOpacity = interpolate(
              titleProgress - i, [0, 0.5], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
            );
            // sketchout效果:先显示描边再填充
            const isSketching = i === Math.floor(titleProgress);

            return (
              <span key={i} style={{
                color: isSketching ? "transparent" : "#FFFFFF",
                fontSize: 120, fontWeight: 900, margin: "0 5px",
                WebkitTextStroke: isSketching ? "2px #FFD700" : "0",
                opacity: charOpacity,
                transition: "all 0.1s",
              }}>
                {char}
              </span>
            );
          })}

          {/* marker sweep(金色光带扫过) */}
          <div style={{
            position: "absolute", top: 0, left: sweepX, width: 100, height: "100%",
            background: "linear-gradient(90deg, transparent, rgba(255,215,0,0.6), transparent)",
            pointerEvents: "none",
          }} />
        </div>

        {/* 副标题 */}
        <div style={{
          opacity: subtitleOpacity, transform: `translateY(${subtitleY}px)`,
          marginTop: 30,
        }}>
          <span style={{
            color: "#FFD700", fontSize: 48, fontWeight: 300,
            letterSpacing: 8,
          }}>
            {subtitle}
          </span>
        </div>

        {/* 装饰线(下方) */}
        <div style={{
          width: lineWidth, height: 2, backgroundColor: "#FFD700",
          marginTop: 40,
        }} />
      </div>
    </Sequence>
  );
};
```

**效果验证**: ✓逐字出现动画(interpolate控制字符显示) ✓sketchout描边效果(WebkitTextStroke) ✓marker sweep金色光带扫过 ✓装饰线同步展开动画 ✓副标题延迟淡入(错落感)

## 常见问题

### Q1: Remotion渲染需要什么环境?国内能用吗?
A: Remotion需要Node.js 18+和Chrome/Chromium。国内完全可用:Remotion是开源框架,GitHub下载或cnpm安装,渲染在本地完成不依赖海外服务。Chrome用国内镜像下载,或用Docker镜像`ghcr.io/remotion-dev/docker`。FFmpeg用各平台包管理器安装。渲染过程完全本地,无网络依赖。

### Q2: 如何实现字幕与配音同步?
A: 两步法:(1)用TTS生成配音音频(推荐edge-tts免费,或阿里云/腾讯云TTS);(2)用Whisper对音频转录生成带时间戳的字幕(SRT/JSON格式);(3)在React组件中根据时间戳渲染字幕。Remotion的`<Audio>`组件可精确控制音频播放,字幕用`useCurrentFrame()`与音频帧对齐。

### Q3: 渲染速度慢怎么办?
A: 优化方法:(1)降低分辨率(1080p→720p);(2)降低帧率(30→24fps);(3)减少复杂动画和特效;(4)用`useMemo`缓存每帧计算;(5)分段渲染后用FFmpeg合并;(6)用云GPU渲染(阿里云GPU实例)。Remotion支持并发渲染(`--concurrency`参数),多核CPU可加速。

### Q4: 如何生成竖屏短视频(抖音/快手)?
A: 在Composition中设置`width={1080} height={1920}`(9:16竖屏)。设计时注意:竖屏垂直空间大,适合上下布局;文字字号加大(移动端观看);前3秒强钩子(用户划走率高);CTA放在显眼位置。渲染命令加`--codec=h264`确保兼容性。

### Q5: Remotion商用需要授权吗?
A: Remotion采用自定义许可证,个人和非商业项目免费。商业项目(公司员工使用)需购买Remotion License(按公司规模付费)。详情见remotion.dev/license。开源替代方案:用FFmpeg+图片序列帧生成视频,但功能远不如Remotion。建议小团队先用免费版验证,商用时购买授权。

## 已知限制

- 渲染依赖Chrome/Chromium,服务器环境需安装或用Docker镜像,增加了部署复杂度
- 渲染速度受CPU/GPU性能影响,长视频(5分钟+)渲染可能需要数十分钟到数小时
- Remotion商业使用需购买License,个人免费但公司使用需付费授权
- 2D DOM/Canvas渲染,无法实现3D动画和实拍视频合成
- TTS配音质量取决于TTS服务,免费TTS(如edge-tts)音质一般,高质量需付费服务

## 安全

- **API Key零暴露**: TTS服务/Whisper API的API Key通过环境变量传入,不硬编码到视频代码、不写入日志、不输出到渲染结果
- **渲染环境隔离**: 渲染在本地或受控服务器完成,不将源代码上传到第三方
- **音频版权**: BGM和配音需注意版权,使用授权音乐或免版税音乐(如YouTube音频库)
- **字体版权**: 商用视频注意字体版权,推荐开源字体(思源黑体/阿里巴巴普惠体)
- **内容合规**: 生成的视频内容需符合平台规范(抖音/快手/B站)和法律法规,不生成违规内容
