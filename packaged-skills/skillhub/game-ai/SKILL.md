---

slug: "game-ai"
name: "game-ai"
version: 1.0.1
displayName: "Game AI Systems"
summary: "游戏AI开发指南,行为树/状态机/寻路/决策全覆盖。Game AI development guide covering behavior trees, state machines, pa"
license: "Proprietary"
description: |-，可自动提升工作效率
  Game AI development guide covering behavior trees, state machines, pathfinding,
  and decision-maki。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Lifestyle
  - 工具
  - 效率
  - 自动化
  - 创意
  - 图像
  - 开发
  - 代码
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"

---

# Game AI Systems

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

- 行为树（Behavior Tree）设计与实现：选择节点、序列节点、装饰器、并行节点
- 有限状态机（FSM）构建：状态定义、转换条件、状态层级、状态机可视化
- 寻路算法实现：A* 算法、Dijkstra、BFS/DFS、导航网格（NavMesh）、流场寻路
- 决策系统：效用AI（Utility AI）、GOAP（目标导向行动规划）、黑板系统
- 群体行为模拟：Boids 集群算法、Flocking 行为、编队移动、避障
- 游戏AI架构模式：感知系统、记忆系统、 Steering Behaviors、AI 调度器
- 多语言实现支持：C++/C#/Python/JavaScript，适配 Unity/Unreal/Godot/自研引擎

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| NPC 行为设计 | 角色描述与行为需求 | 行为树/状态机代码 |
| 寻路系统 | 地图数据与起止点 | 最优路径与可视化 |
| 敌人 AI | 敌人类型与难度设定 | AI 决策逻辑代码 |
| 群体模拟 | 群体规模与行为规则 | Boids/Flocking 实现 |
| AI 架构 | 游戏类型与性能需求 | 完整 AI 系统设计方案 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 流程详解：敌人 AI 设计

**步骤 1：选择 AI 架构**

| AI 架构 | 适用场景 | 复杂度 | 典型应用 |
|:---------|:---------|:-------|:---------|
| 有限状态机 (FSM) | 简单 NPC、固定行为模式 | 低 | 守卫巡逻、BOSS 阶段切换 |
| 行为树 (BT) | 复杂 NPC、可扩展行为 | 中 | RPG 角色动作、 RTS 单位 |
| 效用 AI (Utility) | 需要动态权衡的决策 | 中 | 文明系列 AI、模拟人生 |
| GOAP | 开放世界、目标驱动 | 高 | 辐射系列 NPC、杀戮空间 |
| 神经网络/强化学习 | 自适应学习型 AI | 极高 | AlphaGo、自动驾驶 NPC |

**步骤 2：设计行为树**

## 行为树（Behavior Tree）

### 节点类型

```javascript
// 节点状态
const NodeStatus = {
  SUCCESS: 'success',
  FAILURE: 'failure',
  RUNNING: 'running'
};

// 基础节点
class BTNode {
  tick(blackboard) {
    return NodeStatus.FAILURE;
  }
}

// 选择节点（Selector）：依次执行子节点，遇到 SUCCESS 停止
class Selector extends BTNode {
  constructor(children) {
    super();
    this.children = children;
  }
  tick(bb) {
    for (const child of this.children) {
      const status = child.tick(bb);
      if (status !== NodeStatus.FAILURE) {
        return status;  // SUCCESS 或 RUNNING
      }
    }
    return NodeStatus.FAILURE;
  }
}

// 序列节点（Sequence）：依次执行子节点，遇到 FAILURE 停止
class Sequence extends BTNode {
  constructor(children) {
    super();
    this.children = children;
  }
  tick(bb) {
    for (const child of this.children) {
      const status = child.tick(bb);
      if (status !== NodeStatus.SUCCESS) {
        return status;  // FAILURE 或 RUNNING
      }
    }
    return NodeStatus.SUCCESS;
  }
}

// 条件节点
class Condition extends BTNode {
  constructor(checkFn) {
    super();
    this.checkFn = checkFn;
  }
  tick(bb) {
    return this.checkFn(bb) ? NodeStatus.SUCCESS : NodeStatus.FAILURE;
  }
}

// 动作节点
class Action extends BTNode {
  constructor(actionFn) {
    super();
    this.actionFn = actionFn;
  }
  tick(bb) {
    return this.actionFn(bb);
  }
}
```

### 敌人 AI 行为树示例

```
Root (Selector)
├── Sequence [生存优先]
│   ├── Condition: 血量 < 30%
│   ├── Condition: 背包有药水
│   └── Action: 使用药水
├── Sequence [战斗]
│   ├── Condition: 看到敌人
│   ├── Selector [攻击策略]
│   │   ├── Sequence [近战]
│   │   │   ├── Condition: 距离 < 2米
│   │   │   └── Action: 近战攻击
│   │   └── Sequence [远程]
│   │       ├── Condition: 有弹药
│   │       └── Action: 远程射击
│   └── Action: 追击敌人
├── Sequence [巡逻]
│   ├── Condition: 无敌人
│   └── Action: 沿巡逻路线移动
└── Action: 待机
```

### 装饰器节点

```javascript
// 反转装饰器：SUCCESS <-> FAILURE
class Inverter extends BTNode {
  constructor(child) { super(); this.child = child; }
  tick(bb) {
    const status = this.child.tick(bb);
    if (status === NodeStatus.SUCCESS) return NodeStatus.FAILURE;
    if (status === NodeStatus.FAILURE) return NodeStatus.SUCCESS;
    return status;
  }
}

// 重复装饰器：重复执行子节点直到 FAILURE
class Repeater extends BTNode {
  constructor(child, maxTimes = Infinity) {
    super(); this.child = child; this.maxTimes = maxTimes;
  }
  tick(bb) {
    let count = 0;
    while (count < this.maxTimes) {
      const status = this.child.tick(bb);
      if (status !== NodeStatus.SUCCESS) return status;
      count++;
    }
    return NodeStatus.SUCCESS;
  }
}

// 超时装饰器：限制子节点执行时间
class TimeLimit extends BTNode {
  constructor(child, maxTime) {
    super(); this.child = child; this.maxTime = maxTime;
  }
  tick(bb) {
    if (!bb.startTime) bb.startTime = Date.now();
    if (Date.now() - bb.startTime > this.maxTime) {
      bb.startTime = null;
      return NodeStatus.FAILURE;
    }
    const status = this.child.tick(bb);
    if (status !== NodeStatus.RUNNING) bb.startTime = null;
    return status;
  }
}
```

## 有限状态机（FSM）

### 基础实现

```javascript
class StateMachine {
  constructor(owner) {
    this.owner = owner;
    this.currentState = null;
    this.states = new Map();
    this.transitions = [];
  }

  addState(name, state) {
    this.states.set(name, state);
  }

  addTransition(from, to, condition) {
    this.transitions.push({ from, to, condition });
  }

  changeState(newState) {
    if (this.currentState) {
      this.currentState.exit(this.owner);
    }
    this.currentState = this.states.get(newState);
    if (this.currentState) {
      this.currentState.enter(this.owner);
    }
  }

  update(dt) {
    // 检查状态转换
    for (const t of this.transitions) {
      if (t.from === this.getCurrentStateName() && t.condition(this.owner)) {
        this.changeState(t.to);
        return;
      }
    }
    // 执行当前状态逻辑
    if (this.currentState) {
      this.currentState.update(this.owner, dt);
    }
  }
}

// 状态定义
class PatrolState {
  enter(enemy) { enemy.speed = 50; enemy.setAnim('walk'); }
  update(enemy, dt) {
    enemy.moveAlongPath(dt);
    if (enemy.canSeePlayer()) {
      // 触发转换到 ChaseState
    }
  }
  exit(enemy) {}
}

class ChaseState {
  enter(enemy) { enemy.speed = 120; enemy.setAnim('run'); }
  update(enemy, dt) {
    enemy.moveTo(enemy.target.position, dt);
    if (enemy.distanceToTarget() < enemy.attackRange) {
      // 触发转换到 AttackState
    }
    if (!enemy.canSeePlayer()) {
      // 触发转换回 PatrolState
    }
  }
  exit(enemy) {}
}
```

## 寻路算法

### A* 算法实现

```javascript
class AStar {
  constructor(grid) {
    this.grid = grid;  // 2D 数组: 0=可通行, 1=障碍
    this.rows = grid.length;
    this.cols = grid[0].length;
  }

  findPath(start, end) {
    const openSet = [start];
    const closedSet = new Set();
    const gScore = new Map();
    const fScore = new Map();
    const cameFrom = new Map();

    const key = (n) => `${n.x},${n.y}`;
    gScore.set(key(start), 0);
    fScore.set(key(start), this.heuristic(start, end));

    while (openSet.length > 0) {
      // 取 fScore 最小的节点
      openSet.sort((a, b) =>
        (fScore.get(key(a)) || Infinity) - (fScore.get(key(b)) || Infinity)
      );
      const current = openSet.shift();

      if (current.x === end.x && current.y === end.y) {
        return this.reconstructPath(cameFrom, current);
      }

      closedSet.add(key(current));

      for (const neighbor of this.getNeighbors(current)) {
        if (closedSet.has(key(neighbor))) continue;
        if (this.grid[neighbor.y][neighbor.x] === 1) continue;

        const tentativeG = (gScore.get(key(current)) || 0) +
          this.distance(current, neighbor);

        if (!openSet.some(n => n.x === neighbor.x && n.y === neighbor.y)) {
          openSet.push(neighbor);
        } else if (tentativeG >= (gScore.get(key(neighbor)) || Infinity)) {
          continue;
        }

        cameFrom.set(key(neighbor), current);
        gScore.set(key(neighbor), tentativeG);
        fScore.set(key(neighbor), tentativeG + this.heuristic(neighbor, end));
      }
    }
    return null;  // 无路径
  }

  heuristic(a, b) {
    // 曼哈顿距离（4 方向移动）
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    // 对角线移动使用切比雪夫距离:
    // return Math.max(Math.abs(a.x - b.x), Math.abs(a.y - b.y));
  }

  getNeighbors(node) {
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];  // 4方向
    // 8方向: [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    return dirs
      .map(([dx, dy]) => ({ x: node.x + dx, y: node.y + dy }))
      .filter(n => n.x >= 0 && n.x < this.cols && n.y >= 0 && n.y < this.rows);
  }

  reconstructPath(cameFrom, current) {
    const path = [current];
    while (cameFrom.has(`${current.x},${current.y}`)) {
      current = cameFrom.get(`${current.x},${current.y}`);
      path.unshift(current);
    }
    return path;
  }
}
```

### 寻路算法对比

| 算法 | 保证最优 | 启发式 | 适用场景 | 性能 |
|:-----|:---------|:-------|:---------|:-----|
| A* | 是 | 是 | 通用寻路（推荐首选） | 快 |
| Dijkstra | 是 | 否 | 无启发信息的均匀图 | 慢 |
| BFS | 是 | 否 | 无权图最短路径 | 中 |
| DFS | 否 | 否 | 迷宫生成、连通性检查 | 快 |
| JPS (Jump Point Search) | 是 | 是 | 均匀网格快速寻路 | 极快 |
| NavMesh | 是 | 是 | 3D 游戏、复杂地形 | 快 |

## 群体行为（Boids）

```javascript
class Boid {
  constructor(x, y) {
    this.position = { x, y };
    this.velocity = { x: Math.random()-0.5, y: Math.random()-0.5 };
    this.acceleration = { x: 0, y: 0 };
    this.maxSpeed = 4;
    this.maxForce = 0.2;
    this.perception = 50;
  }

  flock(boids) {
    const alignment = this.align(boids);
    const cohesion = this.cohere(boids);
    const separation = this.separate(boids);

    // 权重调整
    alignment.x *= 1.0;  alignment.y *= 1.0;
    cohesion.x *= 1.0;   cohesion.y *= 1.0;
    separation.x *= 1.5; separation.y *= 1.5;

    this.acceleration.x = alignment.x + cohesion.x + separation.x;
    this.acceleration.y = alignment.y + cohesion.y + separation.y;
  }

  align(boids) {
    // 对齐：朝向邻居的平均速度方向
    let avgVel = { x: 0, y: 0 };
    let count = 0;
    for (const other of boids) {
      const dist = this.distance(other);
      if (other !== this && dist < this.perception) {
        avgVel.x += other.velocity.x;
        avgVel.y += other.velocity.y;
        count++;
      }
    }
    if (count > 0) {
      avgVel.x /= count; avgVel.y /= count;
      return this.steer(avgVel);
    }
    return { x: 0, y: 0 };
  }

  // cohere() 和 separate() 类似，分别计算聚集和分离力
  // cohere: 朝向邻居的中心位置
  // separate: 远离过近的邻居
}
```

## 最佳实践

### AI 性能优化

| 优化策略 | 方法 | 效果 |
|:---------|:-----|:-----|
| AI 分帧调度 | 将 AI 计算分散到多帧，避免单帧卡顿 | 平滑帧率 |
| LOD AI | 远处 NPC 使用简化 AI，近处使用完整 AI | 减少 CPU 开销 |
| 寻路缓存 | 缓存路径结果，避免重复计算 | 降低寻路开销 |
| 空间分区 | 使用四叉树/网格加速邻居查询 | 加速群体行为 |
| 行为树频率控制 | 非关键 NPC 降低 tick 频率 | 减少 AI 更新次数 |

### AI 设计原则

1. **有趣 > 智能**：AI 的目标是创造有趣的游戏体验，而非追求最优策略
2. **可预测性**：玩家应能学习 AI 的行为模式并制定对策
3. **公平性**：AI 不应拥有玩家没有的信息（如穿墙视野）
4. **个性差异**：不同类型敌人应有明显不同的行为风格
5. **调试友好**：可视化 AI 状态、感知范围、寻路路径

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| action | string | 是 | 操作类型: `behavior-tree`/`fsm`/`pathfinding`/`flocking`/`architecture` |
| game_type | string | 否 | 游戏类型: `rpg`/`fps`/`rts`/`platformer`/`stealth` |
| language | string | 否 | 实现语言: `cpp`/`csharp`/`python`/`javascript` |
| content | string | 否 | game-ai处理的内容输入，可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "ai_type": "behavior-tree",
    "language": "javascript",
    "code": "class Selector extends BTNode { ... }",
    "tree_structure": "Root(Selector) -> Sequence[Combat] -> ...",
    "description": "敌人 AI 行为树，包含巡逻、追击、攻击、逃跑行为",
    "features": ["行为树节点", "感知系统", "状态转换", "黑板系统"],
    "metadata": {
      "template_used": "game-ai-builder",
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

### Q1: 如何开始使用Game AI Systems？
A: 描述你的 AI 需求即可。例如"为 RPG 游戏设计一个敌人 AI，需要巡逻、追击玩家、近战攻击和低血量逃跑行为"。系统会根据需求选择合适的 AI 架构（行为树/状态机/效用AI），生成完整的代码实现。你也可以指定游戏类型（RPG/FPS/RTS）和实现语言（C++/C#/JavaScript）。

### Q2: 行为树和状态机如何选择？
A: 状态机（FSM）适合行为模式固定、状态较少的简单 NPC（如守卫的"巡逻-警戒-攻击"三态循环），优点是实现简单、调试直观。行为树（BT）适合需要复杂决策、行为可扩展的 NPC（如 RPG 中需要考虑血量、距离、弹药、队友状态等多种条件的角色），优点是模块化、可复用、易于扩展新行为。一般建议：简单敌人用 FSM，BOSS 和重要 NPC 用 BT。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

