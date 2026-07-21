# 详细参考 - game-ai-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (csharp)

```csharp
using System.Collections.Generic;

// GOAP 行动定义
public class GoapAction
{
    public string Name { get; set; }
    public Dictionary<string, object> Preconditions { get; set; }
    public Dictionary<string, object> Effects { get; set; }
    public float Cost { get; set; }
    public bool Running { get; set; }

    public bool CheckPreconditions(Dictionary<string, object> state)
    {
        foreach (var pre in Preconditions)
        {
            if (!state.ContainsKey(pre.Key)) return false;
            if (!state[pre.Key].Equals(pre.Value)) return false;
        }
        return true;
    }

    public Dictionary<string, object> ApplyEffects(Dictionary<string, object> state)
    {
        var newState = new Dictionary<string, object>(state);
        foreach (var effect in Effects)
        {
            newState[effect.Key] = effect.Value;
        }
        return newState;
    }
}

// GOAP 规划器
public class GoapPlanner
{
    public List<GoapAction> Plan(
        Dictionary<string, object> worldState,
        Dictionary<string, object> goal,
        List<GoapAction> availableActions)
    {
        // A* 搜索行动序列
        var openSet = new PriorityQueue<GoapNode>();
        var startNode = new GoapNode { State = worldState, Actions = new List<GoapAction>(), Cost = 0 };

        openSet.Enqueue(startNode, 0);

        while (openSet.Count > 0)
        {
            var current = openSet.Dequeue();

            if (GoalReached(current.State, goal))
                return current.Actions;

            foreach (var action in availableActions)
            {
                if (action.CheckPreconditions(current.State))
                {
                    var newState = action.ApplyEffects(current.State);
                    var newNode = new GoapNode
                    {
                        State = newState,
                        Actions = new List<GoapAction>(current.Actions) { action },
                        Cost = current.Cost + action.Cost,
                    };
                    openSet.Enqueue(newNode, newNode.Cost);
                }
            }
        }
        return null;
    }

    private bool GoalReached(Dictionary<string, object> state, Dictionary<string, object> goal)
    {
        foreach (var g in goal)
        {
            if (!state.ContainsKey(g.Key) || !state[g.Key].Equals(g.Value))
                return false;
        }
        return true;
    }
}

// 使用示例
var planner = new GoapPlanner();
var worldState = new Dictionary<string, object>
{
    ["enemy_visible"] = true,
    ["has_ammo"] = true,
    ["health"] = 80,
    ["player_distance"] = 150,
};

var goal = new Dictionary<string, object> { ["player_dead"] = true };

var plan = planner.Plan(worldState, goal, availableActions);
// 输出: [ApproachPlayer, AimWeapon, FireWeapon, ReloadIfEmpty, Repeat]
```

## 代码示例 (python)

```python
import os
import requests
import numpy as np

API_BASE = "https://api.game-ai-pro.local/v1"
ADMIN_KEY = os.environ["GAME_AI_ADMIN_KEY"]

class RLTrainingManager:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}

    def create_training_env(self, game_scene, agent_config):
        """创建强化学习训练环境"""
        payload = {
            "scene": game_scene,
            "agent": agent_config,
            "algorithm": "PPO",
            "hyperparameters": {
                "learning_rate": 0.0003,
                "batch_size": 64,
                "gamma": 0.99,
                "epochs": 10,
            },
            "reward_function": """
                reward = 0
                if agent_killed_player: reward += 100
                if agent_died: reward -= 50
                if agent_took_damage: reward -= 5
                if agent_maintained_optimal_range: reward += 1
            """,
        }
        resp = requests.post(
            f"{API_BASE}/rl/training",
            headers=self.headers,
            json=payload,
            timeout=120,
        )
        return resp.json()

    def train_agent(self, env_id, episodes=10000):
        """启动训练任务"""
        payload = {"env_id": env_id, "episodes": episodes, "async": True}
        resp = requests.post(
            f"{API_BASE}/rl/train",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()["job_id"]

    def export_model(self, job_id, format="onnx"):
        """导出训练好的模型"""
        resp = requests.get(
            f"{API_BASE}/rl/jobs/{job_id}/export",
            headers=self.headers,
            params={"format": format},
            timeout=60,
        )
        return resp.json()

trainer = RLTrainingManager(ADMIN_KEY)
env = trainer.create_training_env(
    game_scene="boss_arena",
    agent_config={"type": "boss", "actions": ["attack", "defend", "summon", "heal"]},
)
job_id = trainer.train_agent(env["id"], episodes=50000)
```

## 代码示例 (csharp)

```csharp
// 团队 AI 协调器
public class TeamAICoordinator : Node
{
    private List<AIController> _members = new();
    private TeamStrategy _currentStrategy;

    public void AssignRoles(TeamStrategy strategy)
    {
        _currentStrategy = strategy;
        var roles = strategy.GetRoleAssignments(_members.Count);

        for (int i = 0; i < _members.Count; i++)
        {
            _members[i].AssignRole(roles[i]);
        }
    }

    public void UpdateTeamCoordination()
    {
        switch (_currentStrategy.Type)
        {
            case StrategyType.FlankAttack:
                ExecuteFlankAttack();
                break;
            case StrategyType.SuppressingFire:
                ExecuteSuppressingFire();
                break;
            case StrategyType.Retreat:
                ExecuteCoordinatedRetreat();
                break;
        }
    }

    private void ExecuteFlankAttack()
    {
        // 分两组: 一组正面吸引火力,一组侧翼包抄
        var attackers = _members.Take(_members.Count / 2);
        var flankers = _members.Skip(_members.Count / 2);

        foreach (var a in attackers)
            a.SetBehavior(BehaviorType.SuppressingFire);

        foreach (var f in flankers)
            f.SetBehavior(BehaviorType.Flank, target: GetPlayerFlankPosition());
    }
}
```

