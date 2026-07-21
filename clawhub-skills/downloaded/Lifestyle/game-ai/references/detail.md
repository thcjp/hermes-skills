# 详细参考 - game-ai

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (csharp)

```csharp
public enum NodeStatus
{
    Running,
    Success,
    Failure
}

public abstract class BTNode
{
    public abstract NodeStatus Execute();
}

public class Sequence : BTNode
{
    private readonly List<BTNode> _children = new();
    private int _currentChild = 0;

    public Sequence(params BTNode[] children)
    {
        _children.AddRange(children);
    }

    public override NodeStatus Execute()
    {
        while (_currentChild < _children.Count)
        {
            var status = _children[_currentChild].Execute();

            if (status == NodeStatus.Running)
                return NodeStatus.Running;

            if (status == NodeStatus.Failure)
            {
                _currentChild = 0;
                return NodeStatus.Failure;
            }

            _currentChild++;
        }

        _currentChild = 0;
        return NodeStatus.Success;
    }
}

public class Selector : BTNode
{
    private readonly List<BTNode> _children = new();
    private int _currentChild = 0;

    public Selector(params BTNode[] children)
    {
        _children.AddRange(children);
    }

    public override NodeStatus Execute()
    {
        while (_currentChild < _children.Count)
        {
            var status = _children[_currentChild].Execute();

            if (status == NodeStatus.Running)
                return NodeStatus.Running;

            if (status == NodeStatus.Success)
            {
                _currentChild = 0;
                return NodeStatus.Success;
            }

            _currentChild++;
        }

        _currentChild = 0;
        return NodeStatus.Failure;
    }
}

// 使用示例
public class EnemyAI : Node
{
    private BTNode _behaviorTree;

    public override void _Ready()
    {
        _behaviorTree = new Selector(
            // 优先攻击
            new Sequence(
                new Condition(IsPlayerInRange),
                new Condition(HasAmmo),
                new Action(Attack)
            ),
            // 追逐玩家
            new Sequence(
                new Condition(CanSeePlayer),
                new Action(ChasePlayer)
            ),
            // 巡逻
            new Action(Patrol)
        );
    }

    public override void _Process(double delta)
    {
        _behaviorTree.Execute();
    }
}
```

## 代码示例 (csharp)

```csharp
public enum EnemyState
{
    Idle,
    Patrol,
    Chase,
    Attack,
    Flee
}

public class EnemyFSM : Node
{
    private EnemyState _currentState;
    private Dictionary<EnemyState, IState> _states;

    public override void _Ready()
    {
        _states = new Dictionary<EnemyState, IState>
        {
            [EnemyState.Idle] = new IdleState(this),
            [EnemyState.Patrol] = new PatrolState(this),
            [EnemyState.Chase] = new ChaseState(this),
            [EnemyState.Attack] = new AttackState(this),
            [EnemyState.Flee] = new FleeState(this)
        };

        ChangeState(EnemyState.Idle);
    }

    public void ChangeState(EnemyState newState)
    {
        _states[_currentState]?.Exit();
        _currentState = newState;
        _states[_currentState]?.Enter();
    }

    public override void _Process(double delta)
    {
        _states[_currentState]?.Update(delta);
    }
}

public interface IState
{
    void Enter();
    void Update(double delta);
    void Exit();
}

public class ChaseState : IState
{
    private readonly EnemyFSM _fsm;
    private readonly CharacterBody2D _owner;
    private NavigationAgent2D _navAgent;

    public ChaseState(EnemyFSM fsm)
    {
        _fsm = fsm;
        _owner = fsm.GetParent<CharacterBody2D>();
        _navAgent = _owner.GetNode<NavigationAgent2D>("NavigationAgent2D");
    }

    public void Enter()
    {
        // 开始追逐动画
        _owner.GetNode<AnimationPlayer>("AnimationPlayer").Play("run");
    }

    public void Update(double delta)
    {
        var player = GetTree().GetFirstNodeInGroup("player") as Node2D;
        if (player == null) return;

        // 更新目标位置
        _navAgent.TargetPosition = player.GlobalPosition;

        // 移动向玩家
        var direction = _owner.ToLocal(_navAgent.GetNextPathPosition()).Normalized();
        _owner.Velocity = direction * _owner.Speed;
        _owner.MoveAndSlide();

        // 检查距离
        float distance = _owner.GlobalPosition.DistanceTo(player.GlobalPosition);
        if (distance < 50)
        {
            _fsm.ChangeState(EnemyState.Attack);
        }
        else if (distance > 500)
        {
            _fsm.ChangeState(EnemyState.Patrol);
        }
    }

    public void Exit()
    {
        _owner.Velocity = Vector2.Zero;
    }
}
```

## 代码示例 (csharp)

```csharp
public class Boid : Node2D
{
    private Vector2 _velocity;
    private List<Boid> _neighbors = new();

    public override void _Process(double delta)
    {
        // 更新邻居列表
        UpdateNeighbors();

        // 计算三个力
        var separation = CalculateSeparation();
        var alignment = CalculateAlignment();
        var cohesion = CalculateCohesion();

        // 合并力
        var acceleration = separation * 1.5f + alignment * 1.0f + cohesion * 1.0f;

        // 更新速度和位置
        _velocity += acceleration * (float)delta;
        _velocity = _velocity.LimitLength(MaxSpeed);

        Position += _velocity * (float)delta;
    }

    private Vector2 CalculateSeparation()
    {
        var steer = Vector2.Zero;
        int count = 0;

        foreach (var neighbor in _neighbors)
        {
            float distance = Position.DistanceTo(neighbor.Position);
            if (distance > 0 && distance < SeparationRadius)
            {
                var diff = Position - neighbor.Position;
                diff = diff.Normalized() / distance;
                steer += diff;
                count++;
            }
        }

        if (count > 0)
            steer /= count;

        return steer;
    }

    private Vector2 CalculateAlignment()
    {
        var avgVelocity = Vector2.Zero;
        int count = 0;

        foreach (var neighbor in _neighbors)
        {
            if (Position.DistanceTo(neighbor.Position) < AlignmentRadius)
            {
                avgVelocity += neighbor._velocity;
                count++;
            }
        }

        if (count > 0)
        {
            avgVelocity /= count;
            avgVelocity = avgVelocity.Normalized() * MaxSpeed;
            return avgVelocity - _velocity;
        }

        return Vector2.Zero;
    }

    private Vector2 CalculateCohesion()
    {
        var center = Vector2.Zero;
        int count = 0;

        foreach (var neighbor in _neighbors)
        {
            if (Position.DistanceTo(neighbor.Position) < CohesionRadius)
            {
                center += neighbor.Position;
                count++;
            }
        }

        if (count > 0)
        {
            center /= count;
            return (center - Position).Normalized() * MaxSpeed - _velocity;
        }

        return Vector2.Zero;
    }
}
```

## 代码示例 (csharp)

```csharp
public class UtilityAI
{
    private readonly List<UtilityAction> _actions = new();

    public void AddAction(UtilityAction action)
    {
        _actions.Add(action);
    }

    public UtilityAction ChooseBestAction()
    {
        float bestScore = float.MinValue;
        UtilityAction bestAction = null;

        foreach (var action in _actions)
        {
            float score = action.CalculateScore();

            // 添加随机性
            score += GD.Randf() * 0.1f;

            if (score > bestScore)
            {
                bestScore = score;
                bestAction = action;
            }
        }

        return bestAction;
    }
}

public abstract class UtilityAction
{
    public abstract float CalculateScore();
    public abstract void Execute();
}

public class AttackAction : UtilityAction
{
    private readonly Enemy _enemy;

    public AttackAction(Enemy enemy)
    {
        _enemy = enemy;
    }

    public override float CalculateScore()
    {
        float score = 0f;

        // 玩家距离近，分数高
        float distance = _enemy.DistanceToPlayer();
        score += Mathf.Clamp(1.0f - distance / 200.0f, 0, 1) * 0.5f;

        // 有弹药，分数高
        score += _enemy.HasAmmo ? 0.3f : 0.0f;

        // 生命值高，更倾向于攻击
        score += _enemy.HealthPercent * 0.2f;

        return score;
    }

    public override void Execute()
    {
        _enemy.Attack();
    }
}
```

