---
slug: "game"
name: "game"
version: 2.0.1
displayName: "Game"
summary: "AI Agent即时游戏设计引擎,一句话概念即得可玩游戏。The instant game design engine for AI agents。Describe any game con"
license: "MIT"
description: |-
  The instant game design engine for AI agents。Describe any game concept
  in one sentence and get a。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Lifestyle
  - 工具
  - 效率
  - 自动化
  - 生活
  - 健康
  - 创意
  - 图像
  - 开发
  - canvas
  - ctx
  - 游戏
  - playing
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Game

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

- 一句话概念即得可玩游戏：输入游戏概念描述，输出完整可运行的游戏代码
- 支持 2D/3D 游戏类型：平台跳跃、射击、解谜、竞速、塔防、Roguelike、卡牌
- 游戏系统自动生成：物理引擎、碰撞检测、得分系统、关卡设计、敌人 AI
- 多种渲染技术栈：HTML5 Canvas、Phaser.js、Three.js、p5.js、纯 CSS/DOM
- 游戏循环架构：状态管理（菜单/游戏中/暂停/结束）、帧率控制、资源加载
- 音效与视觉效果：粒子系统、屏幕震动、缓动动画、程序化音效
- 触屏与键盘双输入支持，响应式适配桌面和移动设备

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 快速原型 | 一句话游戏概念 | 可运行的游戏 HTML 文件 |
| 玩法验证 | 游戏机制描述 | 包含核心循环的原型代码 |
| 游戏开发 | 详细设计文档 | 完整游戏项目代码 |
| 游戏素材 | 主题与风格 | 程序化生成的精灵图与音效 |
| 关卡设计 | 游戏类型与难度 | 自动生成的关卡数据 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 流程详解：从概念到可玩游戏

**步骤 1：描述游戏概念**

一句话描述需要包含以下要素：

| 要素 | 示例 | 作用 |
|:-----|:-----|:-----|
| 核心玩法 | "平台跳跃收集金币" | 决定游戏类型和机制 |
| 视觉风格 | "像素风" / "霓虹科技" | 决定美术风格 |
| 操作方式 | "方向键移动+空格跳跃" | 决定输入控制 |
| 目标规则 | "60秒内收集尽量多金币" | 决定胜负条件 |

**完整示例**：
> "做一个像素风格的平台跳跃游戏，玩家用方向键移动、空格跳跃，需要在60秒内收集尽可能多的金币，同时躲避移动的敌人，有3条命"

**步骤 2：选择技术栈**

| 技术栈 | 适用类型 | 优点 | 缺点 |
|:-------|:---------|:-----|:-----|
| HTML5 Canvas | 2D 游戏 | 轻量、兼容性好、无依赖 | 需手写渲染逻辑 |
| Phaser.js | 2D 游戏 | 功能完整、物理引擎、场景管理 | 需加载库文件 |
| Three.js | 3D 游戏 | WebGL 3D 渲染、光照 | 学习成本高 |
| p5.js | 创意编程 | 简洁 API、艺术风格 | 性能有限 |
| 纯 CSS/DOM | 简单游戏 | 无依赖、易理解 | 性能差、不适合复杂场景 |

**步骤 3：游戏架构设计**

## 游戏架构模式

### 游戏循环（Game Loop）

所有游戏的核心都是游戏循环，负责更新状态和渲染画面：

```javascript
class Game {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.state = 'menu';  // menu / playing / paused / gameover
    this.lastTime = 0;
    this.entities = [];
    this.score = 0;
    this.lives = 3;
  }

  start() {
    requestAnimationFrame((time) => this.loop(time));
  }

  loop(currentTime) {
    const deltaTime = (currentTime - this.lastTime) / 1000;
    this.lastTime = currentTime;

    if (this.state === 'playing') {
      this.update(deltaTime);   // 更新游戏逻辑
    }
    this.render();              // 渲染画面

    requestAnimationFrame((time) => this.loop(time));
  }

  update(dt) {
    // 更新所有实体
    this.entities.forEach(e => e.update(dt));
    // 碰撞检测
    this.checkCollisions();
    // 检查游戏状态
    this.checkGameState();
  }

  render() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.entities.forEach(e => e.render(this.ctx));
    this.renderUI();
  }
}
```

### 状态管理

```javascript
const GAME_STATES = {
  MENU: 'menu',
  PLAYING: 'playing',
  PAUSED: 'paused',
  GAME_OVER: 'gameover',
  LEVEL_COMPLETE: 'level_complete'
};

function handleStateTransition(newState) {
  switch(newState) {
    case GAME_STATES.PLAYING:
      gameLoop.start();
      break;
    case GAME_STATES.PAUSED:
      gameLoop.stop();
      break;
    case GAME_STATES.GAME_OVER:
      showGameOverScreen();
      break;
  }
}
```

## 游戏类型与核心机制

### 平台跳跃游戏

核心机制实现要点：

```javascript
// 玩家物理
class Player {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.vx = 0;
    this.vy = 0;
    this.width = 32;
    this.height = 32;
    this.onGround = false;
    this.jumpPower = -450;  // 跳跃力度
    this.moveSpeed = 200;   // 移动速度
    this.gravity = 1200;    // 重力
  }

  update(dt) {
    // 应用重力
    this.vy += this.gravity * dt;

    // 水平移动
    if (input.left) this.vx = -this.moveSpeed;
    else if (input.right) this.vx = this.moveSpeed;
    else this.vx *= 0.8;  // 摩擦减速

    // 跳跃
    if (input.jump && this.onGround) {
      this.vy = this.jumpPower;
      this.onGround = false;
    }

    // 更新位置
    this.x += this.vx * dt;
    this.y += this.vy * dt;

    // 平台碰撞（AABB）
    this.onGround = false;
    platforms.forEach(p => {
      if (this.aabb(p)) {
        if (this.vy > 0 && this.y < p.y) {
          this.y = p.y - this.height;
          this.vy = 0;
          this.onGround = true;
        }
      }
    });
  }
}
```

### 射击游戏

| 机制 | 实现方式 |
|:-----|:---------|
| 子弹管理 | 对象池模式，复用子弹对象避免 GC |
| 敌人生成 | 定时器 + 难度曲线，随时间增加生成频率 |
| 碰撞检测 | 圆形碰撞（距离比较）或 AABB（矩形相交） |
| 射击模式 | 散弹、追踪弹、激光、范围攻击 |

### 解谜游戏

| 类型 | 核心逻辑 |
|:-----|:---------|
| 推箱子 | 网格状态 + 可逆移动 + 死锁检测 |
| 连连看 | 图案匹配 + 路径连通算法 |
| 消除类 | 网格匹配 + 下落填充 + 连锁反应 |
| 数字华容道 | 状态空间搜索 + 可解性判断 |

## 视觉效果系统

### 粒子系统

```javascript
class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 300;
    this.vy = (Math.random() - 0.5) * 300 - 100;
    this.life = 1.0;
    this.color = color;
    this.size = Math.random() * 4 + 2;
  }

  update(dt) {
    this.x += this.vx * dt;
    this.y += this.vy * dt;
    this.vy += 400 * dt;  // 粒子重力
    this.life -= dt * 2;  // 生命衰减
  }

  render(ctx) {
    ctx.globalAlpha = Math.max(0, this.life);
    ctx.fillStyle = this.color;
    ctx.fillRect(this.x, this.y, this.size, this.size);
    ctx.globalAlpha = 1;
  }
}

// 触发爆炸效果
function createExplosion(x, y, count = 20) {
  for (let i = 0; i < count; i++) {
    particles.push(new Particle(x, y, '#ff6b6b'));
  }
}
```

### 屏幕震动

```javascript
let shakeIntensity = 0;
let shakeDuration = 0;

function triggerShake(intensity, duration) {
  shakeIntensity = intensity;
  shakeDuration = duration;
}

// 在渲染前应用偏移
function applyShake() {
  if (shakeDuration > 0) {
    const offsetX = (Math.random() - 0.5) * shakeIntensity;
    const offsetY = (Math.random() - 0.5) * shakeIntensity;
    ctx.save();
    ctx.translate(offsetX, offsetY);
    shakeDuration -= dt;
    shakeIntensity *= 0.9;  // 衰减
  }
}
```

## 输入控制

### 键盘输入

```javascript
const input = { left: false, right: false, jump: false };

document.addEventListener('keydown', (e) => {
  switch(e.code) {
    case 'ArrowLeft': case 'KeyA': input.left = true; break;
    case 'ArrowRight': case 'KeyD': input.right = true; break;
    case 'Space': case 'ArrowUp': case 'KeyW':
      input.jump = true;
      e.preventDefault();  // 阻止页面滚动
      break;
  }
});

document.addEventListener('keyup', (e) => {
  switch(e.code) {
    case 'ArrowLeft': case 'KeyA': input.left = false; break;
    case 'ArrowRight': case 'KeyD': input.right = false; break;
    case 'Space': case 'ArrowUp': case 'KeyW': input.jump = false; break;
  }
});
```

### 触屏输入

```javascript
canvas.addEventListener('touchstart', (e) => {
  e.preventDefault();
  const touch = e.touches[0];
  const rect = canvas.getBoundingClientRect();
  const x = touch.clientX - rect.left;

  // 左半屏移动，右半屏跳跃
  if (x < canvas.width / 2) {
    if (x < canvas.width / 4) input.left = true;
    else input.right = true;
  } else {
    input.jump = true;
  }
});
```

## 最佳实践

### 性能优化

| 优化项 | 方法 | 效果 |
|:-------|:-----|:-----|
| 对象池 | 复用子弹/粒子对象 | 减少 GC 停顿 |
| 空间分区 | 网格/四叉树管理碰撞 | 减少碰撞检测次数 |
| 离屏 Canvas | 预渲染静态背景 | 减少每帧绘制量 |
| 帧率控制 | 固定时间步长更新 | 物理稳定性 |
| 资源懒加载 | 按关卡加载资源 | 减少初始加载时间 |

### 游戏设计原则

1. **核心循环清晰**：玩家在 5 秒内理解"做什么 -> 得到什么反馈"
2. **难度曲线**：从简单开始，逐步引入新机制，保持心流状态
3. **即时反馈**：每个操作都有视觉/音效反馈（粒子、震动、音效）
4. **失败友好**：快速重生、进度保存、明确的失败原因
5. **元游戏层**：积分榜、成就、解锁系统增加重玩动力

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| concept | string | 是 | 游戏概念描述，一句话或详细设计文档 |
| game_type | string | 否 | 游戏类型: `platformer`/`shooter`/`puzzle`/`racing`/`tower-defense` |
| tech_stack | string | 否 | 技术栈: `canvas`/`phaser`/`three`/`p5`，默认 `canvas` |
| content | string | 否 | game处理的内容输入，可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "game_type": "platformer",
    "tech_stack": "canvas",
    "title": "金币冒险",
    "description": "像素风平台跳跃游戏，收集金币躲避敌人",
    "code": "<!-- 完整可运行的 HTML 游戏代码 -->",
    "features": ["物理跳跃", "碰撞检测", "敌人AI", "计分系统", "3条命", "60秒计时"],
    "controls": {"move": "方向键/WASD", "jump": "空格/上键"},
    "metadata": {
      "template_used": "game-engine",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Game？
A: 用一句话描述你想要的游戏即可。例如"做一个太空射击游戏，玩家控制飞船消灭陨石，有计分和生命值"。系统会生成一个完整的、可直接在浏览器中运行的单文件 HTML 游戏。你也可以提供更详细的需求（如视觉风格、操作方式、游戏规则），生成的游戏会更加精确。

### Q2: 生成的游戏可以直接运行吗？
A: 是的。生成的游戏是一个自包含的 HTML 文件，包含所有 JavaScript、CSS 和游戏逻辑代码，无需安装任何依赖，直接在浏览器中打开即可运行。游戏支持键盘和触屏操作，自适应桌面和移动设备屏幕。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

