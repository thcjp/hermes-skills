---
slug: game-ai
name: game-ai
version: "1.0.0"
displayName: Game AI Systems
summary: Game AI development guide covering behavior trees, state machines, pathfinding,
  and decision-maki...
license: MIT
description: |-
  Game AI development guide covering behavior trees, state machines, pathfinding,
  and decision-maki。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Lifestyle
tools:
  - - read
- exec
# Game AI Systems
## AI 架构选择
### 架构对比
---
```yaml
有限状态机 (FSM):
  优点: 简单、直观、易于调试
  缺点: 状态多时难以维护
  适用: 简单敌人、Boss 阶段

行为树 (BT):
  优点: 模块化、可复用、易扩展
  缺点: 需要框架支持
  适用: 复杂 NPC、战术 AI

效用系统 (Utility AI):
  优点: 灵活、智能决策
  缺点: 参数调节困难
  适用: 模拟人生类、策略游戏

GOAP:
  优点: 目标导向、动态规划
  缺点: 计算成本高
  适用: 智能敌人、复杂行为
```

## 有限状态机 (FSM)
### 基础实现

> 详细代码示例已移至 `references/detail.md`

## 行为树 (Behavior Tree)
### 节点类型
```yaml
复合节点:
  Sequence: 顺序执行（一个失败则失败）
  Selector: 选择执行（一个成功则成功）
  Parallel: 并行执行

装饰节点:
  Inverter: 反转结果
  Repeater: 重复执行
  UntilFail: 直到失败

叶子节点:
  Condition: 条件检查
  Action: 执行动作
```

### 行为树实现

> 详细代码示例已移至 `references/detail.md`

## 寻路算法
### A* 算法
```csharp
public class AStar
{
    private readonly Grid _grid;

    public List<Point> FindPath(Point start, Point end)
    {
        var openSet = new PriorityQueue<Point>();
        var cameFrom = new Dictionary<Point, Point>();
        var gScore = new Dictionary<Point, float>();
        var fScore = new Dictionary<Point, float>();

        openSet.Enqueue(start, 0);
        gScore[start] = 0;
        fScore[start] = Heuristic(start, end);

        while (openSet.Count > 0)
        {
            var current = openSet.Dequeue();

            if (current == end)
                return ReconstructPath(cameFrom, current);

            foreach (var neighbor in _grid.GetNeighbors(current))
            {
                float tentativeGScore = gScore[current] + _grid.GetCost(current, neighbor);

                if (!gScore.ContainsKey(neighbor) || tentativeGScore < gScore[neighbor])
                {
                    cameFrom[neighbor] = current;
                    gScore[neighbor] = tentativeGScore;
                    fScore[neighbor] = gScore[neighbor] + Heuristic(neighbor, end);

                    if (!openSet.Contains(neighbor))
                        openSet.Enqueue(neighbor, fScore[neighbor]);
                }
            }
        }

        return null; // 无路径
    }

    private float Heuristic(Point a, Point b)
    {
        // 曼哈顿距离
        return Math.Abs(a.X - b.X) + Math.Abs(a.Y - b.Y);
    }

    private List<Point> ReconstructPath(Dictionary<Point, Point> cameFrom, Point current)
    {
        var path = new List<Point> { current };

        while (cameFrom.ContainsKey(current))
        {
            current = cameFrom[current];
            path.Insert(0, current);
        }

        return path;
    }
}
```

### Godot NavigationAgent2D
```csharp
public class EnemyNavigation : CharacterBody2D
{
    private NavigationAgent2D _navAgent;
    private Node2D _target;

    public override void _Ready()
    {
        _navAgent = GetNode<NavigationAgent2D>("NavigationAgent2D");

        // 配置
        _navAgent.PathDesiredDistance = 10.0f;
        _navAgent.TargetDesiredDistance = 10.0f;
        _navAgent.Radius = 20.0f;

        // 连接信号
        _navAgent.VelocityComputed += OnVelocityComputed;
    }

    public void SetTarget(Node2D target)
    {
        _target = target;
        UpdatePath();
    }

    private async void UpdatePath()
    {
        if (_target == null) return;

        // 异步计算路径
        _navAgent.TargetPosition = _target.GlobalPosition;
        await ToSignal(_navAgent, NavigationAgent2D.SignalName.PathChanged);
    }

    public override void _PhysicsProcess(double delta)
    {
        if (_navAgent.IsNavigationFinished())
            return;

        var nextPos = _navAgent.GetNextPathPosition();
        var direction = GlobalPosition.DirectionTo(nextPos);
        var velocity = direction * Speed;

        // 避障
        _navAgent.Velocity = velocity;
    }

    private void OnVelocityComputed(Vector2 safeVelocity)
    {
        Velocity = safeVelocity;
        MoveAndSlide();
    }
}
```

## 群体行为
### Boids 算法

> 详细代码示例已移至 `references/detail.md`

## 决策系统
### 效用 AI

> 详细代码示例已移至 `references/detail.md`

## 感知系统
### 视觉感知
```csharp
public class VisionSensor : Node2D
{
    [Export] public float ViewDistance = 300.0f;
    [Export] public float ViewAngle = 90.0f;
    [Export] public LayerMask VisionLayer;

    public Node2D Target { get; private set; }

    public override void _Process(double delta)
    {
        Target = null;

        var players = GetTree().GetNodesInGroup("player");
        foreach (Node2D player in players)
        {
            if (CanSee(player))
            {
                Target = player;
                break;
            }
        }
    }

    private bool CanSee(Node2D target)
    {
        var direction = target.GlobalPosition - GlobalPosition;
        float distance = direction.Length();

        // 检查距离
        if (distance > ViewDistance)
            return false;

        // 检查角度
        float angle = Mathf.RadToDeg(direction.Angle());
        float angleDiff = Mathf.Abs(Mathf.AngleDifference(angle, GlobalRotationDegrees));
        if (angleDiff > ViewAngle / 2)
            return false;

        // 射线检测
        var space = GetWorld2D().DirectSpaceState;
        var query = new PhysicsRayQueryParameters2D
        {
            From = GlobalPosition,
            To = target.GlobalPosition,
            CollisionMask = VisionLayer
        };

        var result = space.IntersectRay(query);
        if (result.Count > 0)
        {
            var collider = result["collider"].As<Node>();
            return collider == target;
        }

        return true;
    }

    // 可视化调试
    public override void _Draw()
    {
        // 绘制视野扇形
        DrawArc(Vector2.Zero, ViewDistance, -ViewAngle / 2, ViewAngle / 2, 32, Colors.Yellow, 1.0f);
    }
}
```

## 参考资源
* **行为树模式**: [references/behavior-trees.md](/api/v1/skills/game-ai/file?path=references%2Fbehavior-trees.md&ownerHandle=thb32133451)
* **寻路算法**: [references/pathfinding.md](/api/v1/skills/game-ai/file?path=references%2Fpathfinding.md&ownerHandle=thb32133451)
* **高级技术**: [references/advanced-ai.md](/api/v1/skills/game-ai/file?path=references%2Fadvanced-ai.md&ownerHandle=thb32133451)

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力
- Game AI development guide covering behavior trees, state machines, pathfinding,
  and decision-maki
- 触发关键词: systems, development, guide, behavior, covering, game

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例
### 示例1：基础用法
```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Game AI Systems？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Game AI Systems有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
