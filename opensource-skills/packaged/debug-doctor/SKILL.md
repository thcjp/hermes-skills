---
slug: debug-doctor
name: debug-doctor
version: 1.0.1
displayName: 调试医生
summary: 不猜测不试错,4阶段科学调试法精准定位Bug根因并验证修复
license: Proprietary
description: 调试医生——不猜测,不试错,用科学方法找到Bug真正的根因。4阶段调试法(复现/定位/缩减/修复)+二分查找+验证闭环,让生产事故排查和复杂Bug修复有章可循,支持多语言多环境调试。Use
  when 遇到难以复现的Bug、生产事故排查、性能问题定位、需要系统化调试方法时使用。不适用于简单语法错误和UI样式微调。
tags:
- 调试
- Bug修复
- 根因分析
- 生产事故
- 问题排查
tools:
- read
- exec
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# 调试医生

基于系统化调试方法论,进行根因分析与修复。不猜测,不试错,用科学方法找到真正的 Bug 根因,并确保修复有效。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 复杂Bug | Bug现象+代码环境+复现步骤 | 4阶段调试报告+根因+修复方案+回归测试 |
| 生产事故 | 告警信息+日志+影响范围 | 止血方案+根因分析+防复发措施 |
| 间歇性故障 | 偶发现象+触发条件+日志 | 条件等待策略+监控增强方案+根因 |
| 性能问题 | 慢查询/高CPU/内存增长 | 瓶颈定位+火焰图分析+优化方案 |
| 并发问题 | 竞态/死锁现象+线程转储 | 线程分析+锁图+复现条件+修复 |
| 回归Bug | 之前正常现在出错+Git历史 | git bisect定位+引入提交+根因 |

### 不适用于
- 代码审查与静态分析(请使用lint工具)
- 自动化测试用例编写(请使用测试框架)
- 部署与发布管理(请使用CI/CD工具)
- 安全漏洞挖掘(请使用安全测试工具)
- 代码重构与性能优化(本Skill聚焦Bug修复)
- 监控告警系统搭建(请使用Prometheus/Grafana)

## 核心能力

1. **4阶段科学调试法**:复现(精确复现+可靠性评估)→定位(二分查找+日志增强+工具辅助)→缩减(最小复现用例+根因确认)→修复(最小化修改+验证闭环+防御深度)
2. **二分查找定位**:代码二分(注释一半)、模块二分(禁用一半)、Git bisect(提交历史)、数据二分(减少输入)
3. **高级调试技术**:条件等待(间歇性故障)、并发调试(Thread Sanitizer/线程转储/锁图)、性能调试(Flame Graph/py-spy/内存快照/GC日志)
4. **验证闭环**:回归测试(先验证失败→修复后通过)、完整测试套件(无回归)、代码审查、防御深度(输入验证/边界检查/断言/监控)
5. **多语言工具适配**:Python(pdb/cProfile)、JS(Chrome DevTools)、Go(pprof)、Java(jstack/jmap/MAT)、Rust(gdb)

## 使用流程

### Step 1: 复现(Reproduce)
1. 记录完整复现步骤:操作序列、环境(操作系统/浏览器/版本/依赖)、输入数据、前置条件
2. 评估复现可靠性:每次都能复现?间歇性?不可复现?
3. 间歇性故障:记录触发频率与条件,增加日志/监控等待下次触发
4. 复现环境选择:本地复现(最佳)> Staging复现 > 生产日志分析(不可直接调试)

### Step 2: 定位(Isolate)
1. 二分查找法:注释掉一半代码/禁用一半模块/Git bisect/数据二分
2. 日志增强:在关键路径添加日志,记录变量值/执行路径/耗时,使用条件断点
3. 工具辅助:Debugger逐步执行、Profiler性能剖析、网络抓包、日志聚合

### Step 3: 缩减(Minimize)
1. 最小复现用例:移除不相关代码、简化输入数据、移除外部依赖、创建独立测试用例
2. 根因确认:理解为什么这个Bug会发生、确认根因而非症状、检查是否有多个根因、验证假设(修改后是否修复)

### Step 4: 修复(Fix)
1. 修复实施:最小化修改范围、不引入新问题、保持代码风格一致、添加注释说明修复原因
2. 验证闭环:编写回归测试(先验证测试失败)→运行修复后测试(验证通过)→运行完整测试套件(无回归)→代码审查
3. 防御深度:输入验证、边界检查、断言保护、监控告警

## 高级调试技术

### 条件等待(Condition-Based Waiting)

1. **间歇性故障处理**
   - 在可疑代码处添加条件日志
   - 设置超时与重试
   - 使用 Watchpoint 监控变量变化
   - 记录线程状态快照

### 并发调试

1. **竞态条件**
   - Thread Sanitizer 检测
   - 日志记录线程ID与时间戳
   - 人工强制时序(Thread.sleep)
2. **死锁**
   - 线程转储(jstack/pstack)
   - 锁图分析(等待环)
   - 超时机制

### 性能调试

1. **CPU 瓶颈**
   - Flame Graph 火焰图
   - 采样剖析(perf/py-spy)
   - 热点函数定位
2. **内存泄漏**
   - 内存快照对比
   - 对象引用链分析
   - GC 日志分析
3. **I/O 瓶颈**
   - 磁盘 I/O 监控
   - 网络延迟分析
   - 数据库慢查询日志

## 输出规范

- 调试报告:`output/{bug-id}/debug-report.md`(4阶段记录)
- 根因分析:`output/{bug-id}/root-cause.md`
- 修复方案:`output/{bug-id}/fix-plan.md`
- 回归测试:`output/{bug-id}/regression-test.{ext}`
- 监控告警配置:`output/{bug-id}/monitoring.md`

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 无额外依赖(纯Markdown方法论,任意语言适用)

### 依赖项

| 依赖类型 | 要求 | 说明 |
|:-----|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 调试工具 | 语言相关Debugger/Profiler | 见下方中外工具对照 |
| 可选 | Git | 用于 git bisect 二分定位 |
| 可选 | 日志系统 | 生产环境日志聚合 |
| 可选 | Thread Sanitizer | 并发问题检测(C/C++/Rust/Go) |

### 中外调试工具对照(国内替代方案)

| 海外工具 | 国内替代 | 说明 |
|---:|---:|---:|
| ELK Stack | 阿里云SLS日志服务 | 日志聚合与分析 |
| Grafana + Prometheus | 腾讯云监控/华为云APM | 监控与可视化 |
| Datadog | 阿里云ARMS | 应用性能监控 |
| Sentry | 字节火山引擎APM | 错误追踪 |
| Wireshark | 同Wireshark(开源) | 网络抓包(无替代需求) |
| Charles | Fiddler/Proxyman | HTTP代理调试 |

### API Key 配置
- 本Skill无需额外API Key配置
- 调试工具均为本地运行,无外部服务依赖

### 可用性分类
- **分类**: MD
- **说明**: 纯Markdown方法论,零依赖,任意语言/平台适用

## 示例

### 示例1: 间歇性API超时调试

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| input | string | 是 | 调试医生处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
现象:API间歇性超时(约5%请求),日志无明显错误
环境:Java服务+MySQL+Redis,日均10万请求
触发条件:不明确,高并发时概率增加
```

**输出** (`output/api-timeout/debug-report.md`):
```markdown
# API间歇性超时调试报告
# ...
## 阶段1: 复现
- Staging环境用高并发(100 QPS)模拟,复现率约3%
- 本地无法复现(单线程/低并发)
- 日志无明显错误,仅表现为响应时间突增
# ...
## 阶段2: 定位
### 二分查找
- 禁用缓存层:超时率不变(排除Redis)
- 禁用数据库层:超时消失(锁定MySQL)
# ...
### 日志增强
- 添加连接池日志:发现连接获取偶尔>5s(正常<100ms)
- 数据库慢查询日志:特定查询偶发慢(正常50ms,异常时5s+)
- 锁等待分析:发现表锁竞争
# ...
## 阶段3: 缩减
### 最小复现用例
- 单表并发更新(100并发)→复现率提升至8%
- 根因:缺失索引导致UPDATE语句全表扫描,锁升级为表锁
- 高并发时多个UPDATE竞争表锁,导致连接等待超时
# ...
## 阶段4: 修复
### 修复实施
- 添加缺失索引:`CREATE INDEX idx_user_id ON orders(user_id)`
- 设置查询超时:`SET STATEMENT_TIMEOUT = '30s'`
# ...
### 验证闭环
- 回归测试:编写并发更新测试用例(先验证失败)
- 修复后测试:并发测试通过,超时消失
- 完整测试套件:全通过,无回归
# ...
### 防御深度
- 连接池监控告警:获取时间>1s告警
- 慢查询监控:>1s告警
- 索引使用率监控:定期检查
```

### 示例2: Java服务内存泄漏调试

**输入**:
```
现象:Java服务每48小时OOM重启
环境:Spring Boot + Caffeine缓存,堆内存4GB
触发:无明确触发,持续运行后内存持续增长
```

**输出** (`output/oom-leak/debug-report.md`):
```markdown
# Java服务内存泄漏调试报告
# ...
## 阶段1: 复现(续1)
- 本地压测72小时,内存从1.2GB持续增长至3.8GB
- GC频率逐渐增加,Full GC后内存不释放
- 本地可稳定复现(72小时周期)
# ...
## 阶段2: 定位(续1)
### 工具辅助
- jmap dump:堆内存快照(3.5GB时)
- MAT(Memory Analyzer)分析:HashMap占80%内存(2.8GB)
- 引用链分析:CustomCache.userMap → HashMap → 大量User对象
# ...
### 日志增强(补充)
- 添加缓存put/get日志:发现写入量远大于读取
- 缓存大小监控:持续增长,无淘汰
# ...
## 阶段3: 缩减(续1)
### 最小复现用例(补充)
- 循环写入缓存(100万次),不读取
- 60分钟后内存增长500MB
- 根因:缓存无TTL过期,无LRU淘汰策略,持续写入不清理
# ...
## 阶段4: 修复(续1)
### 修复实施(补充)
- 替换为Caffeine缓存(TTL=1h, maxSize=10000)
```java
Caffeine.newBuilder()
    .expireAfterWrite(1, TimeUnit.HOURS)
    .maximumSize(10000)
    .build();
```
# ...
### 验证闭环(补充)
- 回归测试:缓存淘汰测试(写入>maxSize后自动淘汰)
- 修复后测试:72小时压测,内存稳定在1.5GB
- 完整测试套件:全通过
# ...
### 防御深度(补充)
- 内存使用率告警:80%告警,90%紧急
- 缓存命中率监控:<60%告警(可能缓存配置问题)
- 定期堆内存快照:每日自动dump分析
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 无法复现 | 环境差异/数据依赖/时序问题 | 增加日志覆盖率,部署监控,等待下次触发,收集生产环境快照 |
| 修复后回归 | 修复引入新问题/副作用 | 立即回滚,重新分析根因,检查修复副作用,增加回归测试 |
| 多个根因 | 复杂问题多因素叠加 | 逐个修复,每修一个验证一次,记录每个根因的贡献度 |
| 第三方库Bug | 依赖库缺陷 | 确认版本,查Issue Tracker,寻找workaround或升级版本,必要时fork修复 |
| 环境差异 | 本地/Staging/生产不一致 | 容器化确保一致性(Docker),使用IaC管理配置,生产快照回放 |
| 性能修复引入Bug | 优化改变了正确性逻辑 | 性能优化必须配套回归测试,先验证正确性再优化,分步验证 |
| 并发问题难复现 | 时序敏感/资源竞争 | Thread Sanitizer检测,日志记录线程ID+时间戳,人工强制时序(sleep) |
| 生产环境无法调试 | 不能影响线上服务 | 使用日志分析+内存dump+线程dump,Staging回放,流量镜像 |

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 间歇性API超时调试

**输入**:
```
现象: API间歇性超时（约5%请求），日志无明显错误
环境: Java服务 + MySQL + Redis，日均10万请求
触发条件: 不明确，高并发时概率增加
```

**LLM生成输出**:
```markdown
# output/api-timeout/debug-report.md
# API间歇性超时调试报告
# ...
## 阶段1: 复现(Reproduce)
- **环境**: Staging环境用JMeter模拟100 QPS并发
- **结果**: 复现率约3%，本地单线程无法复现
- **现象**: 响应时间从正常50ms突增至5s+，无错误日志
- **可靠性**: 间歇性，需高并发触发
# ...
## 阶段2: 定位(Isolate)
# ...
### 二分查找法
| 步骤 | 操作 | 结果 | 结论 |
|---:|:---|---:|---:|
| 1 | 禁用Redis缓存层 | 超时率不变(3%) | 排除Redis |
| 2 | 禁用MySQL，用Mock数据 | 超时消失(0%) | 锁定MySQL |
| 3 | 启用MySQL，禁用特定表 | 仅禁用orders表时超时消失 | 锁定orders表 |
# ...
### 日志增强(补充)(补充)
```java
// 添加连接池监控日志
logger.info("Connection acquire time: {}ms, pool size: {}/{}", 
    acquireTime, pool.getActive(), pool.getIdle());

// 慢查询日志
@Aspect
public class SlowQueryAspect {
    @Around("execution(* com.example.repo.*.*(..))")
    public Object logSlowQuery(ProceedingJoinPoint pjp) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = pjp.proceed();
        long duration = System.currentTimeMillis() - start;
        if (duration > 1000) {
            logger.warn("SLOW QUERY: {} took {}ms, params: {}", 
                pjp.getSignature(), duration, pjp.getArgs());
        }
        return result;
    }
}
```
# ...
**发现**:
- 连接池获取时间偶尔>5s（正常<100ms）
- 特定UPDATE查询偶发慢（正常50ms，异常时5s+）
- MySQL锁等待日志显示表锁竞争
# ...
## 阶段3: 缩减(Minimize)
# ...
### 最小复现用例(补充)(补充)
```java
@Test
public void testConcurrentUpdate() throws InterruptedException {
    int threadCount = 100;
    ExecutorService executor = Executors.newFixedThreadPool(threadCount);
    CountDownLatch latch = new CountDownLatch(threadCount);
    
    for (int i = 0; i < threadCount; i++) {
        final long userId = i % 10;  // 仅10个用户，制造竞争
        executor.submit(() -> {
            try {
                latch.await();
                orderRepo.updateStatus(userId, "processed");  // 并发更新
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                latch.countDown();
            }
        });
    }
    executor.shutdown();
    executor.awaitTermination(60, TimeUnit.SECONDS);
    // 复现率提升至8%
}
```
# ...
### 根因确认
- **根因**: orders表缺少user_id索引，UPDATE WHERE user_id=? 导致全表扫描
- 全表扫描期间触发表锁（InnoDB行锁升级）
- 高并发时多个UPDATE竞争表锁，连接等待超时
- **验证**: 添加索引后，最小复现用例超时率为0%
# ...
## 阶段4: 修复(Fix)
# ...
### 修复实施(补充)(补充)
```sql
-- 1. 添加缺失索引
CREATE INDEX idx_user_id ON orders(user_id);

-- 2. 设置查询超时（防御）
SET SESSION max_execution_time = 30000;  -- 30秒

-- 3. 优化UPDATE语句（使用索引提示）
UPDATE orders USE INDEX(idx_user_id) 
SET status = 'processed' WHERE user_id = ?;
```
# ...
### 验证闭环(补充)(补充)
1. **回归测试**（先验证失败）:
```java
@Test
public void testConcurrentUpdateNoTimeout() {
    // 修复前: 此测试会因超时失败
    // 修复后: 此测试应通过
    long startTime = System.currentTimeMillis();
    runConcurrentUpdates(100, 10);
    long duration = System.currentTimeMillis() - startTime;
    assertTrue("Should complete within 5s, took: " + duration + "ms", 
        duration < 5000);
}
```
# ...
2. **修复后测试**: 并发测试通过，超时消失
3. **完整测试套件**: 全通过，无回归
4. **Staging压测**: 100 QPS持续1小时，超时率0%
# ...
### 防御深度(补充)(补充)
- 连接池监控: 获取时间>1s告警
- 慢查询监控: >1s告警
- 索引使用率监控: 定期检查（每月EXPLAIN分析）
- 连接池配置: maxWait从30s调整为5s（快速失败）
```

**效果验证**: ✓4阶段完整调试流程 ✓二分查找精准定位MySQL ✓最小复现用例（100并发） ✓根因为缺索引导致锁升级 ✓修复+回归测试+防御深度

### 案例2: Java内存泄漏调试

**输入**:
```
现象: Java服务每48小时OOM重启
环境: Spring Boot + Caffeine缓存，堆内存4GB
触发: 无明确触发，持续运行后内存持续增长
```

**LLM生成输出**:
```markdown
# output/oom-leak/debug-report.md
# Java服务内存泄漏调试报告
# ...
## 阶段1: 复现(续2)
- **本地压测**: 72小时持续运行，内存从1.2GB增长至3.8GB
- **现象**: GC频率逐渐增加，Full GC后内存不释放
- **复现性**: 本地可稳定复现（72小时周期）
# ...
## 阶段2: 定位(续2)
# ...
### 工具辅助(补充)
```bash
# 1. 堆内存快照（3.5GB时）
jmap -dump:format=b,file=heap.hprof <pid>

# 2. MAT分析
# - HashMap占用80%内存(2.8GB)
# - 引用链: CustomCache.userMap → HashMap → 大量User对象
```
# ...
### 日志增强(补充)(补充2)
```java
// 缓存监控日志
@Scheduled(fixedRate = 60000)  // 每分钟记录
public void logCacheStats() {
    logger.info("Cache size: {}, hits: {}, misses: {}, evictions: {}",
        userMap.size(),
        cacheStats.hits,
        cacheStats.misses,
        cacheStats.evictions);
}
```
# ...
**发现**:
- 缓存写入量远大于读取（10:1）
- 缓存大小持续增长，无淘汰（evictions=0）
# ...
## 阶段3: 缩减(续2)
# ...
### 最小复现用例(补充)(补充2)
```java
public class CacheLeakTest {
    @Test
    public void testCacheGrowth() throws InterruptedException {
        CustomCache cache = new CustomCache();
        
        // 模拟持续写入
        for (int i = 0; i < 1_000_000; i++) {
            cache.put("user_" + i, new User(i, "name" + i));
        }
        
        // 等待60分钟
        Thread.sleep(60 * 60 * 1000);
        
        // 验证内存增长
        long usedMemory = Runtime.getRuntime().totalMemory() - 
                         Runtime.getRuntime().freeMemory();
        assertTrue("Memory should grow significantly", usedMemory > 500_000_000);
    }
}
```
# ...
### 根因确认(补充)
- **根因**: CustomCache使用HashMap，无TTL过期，无LRU淘汰策略
- 持续写入不清理，导致内存持续增长
- **验证**: 替换为Caffeine后，60分钟内存增长<10MB
# ...
## 阶段4: 修复(续2)
# ...
### 修复实施(补充)(补充2)
```java
// 修复前: 无界HashMap
public class CustomCache {
    private Map<String, User> userMap = new HashMap<>();
    public void put(String key, User value) {
        userMap.put(key, value);  // 永不淘汰
    }
}

// 修复后: Caffeine带TTL和大小限制
public class CustomCache {
    private Cache<String, User> userCache = Caffeine.newBuilder()
        .expireAfterWrite(1, TimeUnit.HOURS)    // 1小时TTL
        .maximumSize(10_000)                     // 最大1万条
        .recordStats()                           // 记录统计
        .removalListener((key, value, cause) -> 
            logger.info("Cache evicted: {} due to {}", key, cause))
        .build();
    
    public void put(String key, User value) {
        userCache.put(key, value);
    }
    
    public User get(String key) {
        return userCache.getIfPresent(key);
    }
}
```
# ...
### 验证闭环(补充)(补充2)
1. **回归测试**:
```java
@Test
public void testCacheEviction() {
    CustomCache cache = new CustomCache();
    
    // 写入超过maxSize
    for (int i = 0; i < 15_000; i++) {
        cache.put("user_" + i, new User(i));
    }
    
    // 验证自动淘汰
    assertNull("Should be evicted", cache.get("user_0"));
    assertNotNull("Should be retained", cache.get("user_14999"));
}

@Test
public void testCacheTTL() throws InterruptedException {
    CustomCache cache = new CustomCache();
    cache.put("user_1", new User(1));
    
    // 等待超过TTL
    Thread.sleep(65 * 60 * 1000);  // 65分钟
    
    assertNull("Should expire after TTL", cache.get("user_1"));
}
```
# ...
2. **修复后测试**: 72小时压测，内存稳定在1.5GB
3. **完整测试套件**: 全通过
4. **生产灰度**: 5%流量观察7天，内存稳定
# ...
### 防御深度(补充)(补充2)
- 内存使用率告警: 80%警告，90%紧急
- 缓存命中率监控: <60%告警（配置问题）
- 每日堆内存快照: 自动dump分析
- OOM自动重启: 配置-XX:+HeapDumpOnOutOfMemoryError
```

**效果验证**: ✓jmap+MAT工具链完整 ✓最小复现用例（100万次写入） ✓根因为无界HashMap ✓Caffeine修复含TTL+maxSize ✓回归测试覆盖淘汰+TTL

### 案例3: 并发死锁调试

**输入**:
```
现象: 转账服务偶发死锁，线程全部阻塞，服务无响应
环境: Go服务 + PostgreSQL，Goroutine并发转账
触发: 高并发转账时偶发（约0.1%）
```

**LLM生成输出**:
```markdown
# output/deadlock/debug-report.md
# 并发死锁调试报告
# ...
## 阶段1: 复现(续3)
- **压测**: 100并发转账，运行10分钟后复现死锁
- **现象**: 所有Goroutine阻塞在锁获取，服务无响应
- **复现率**: 约0.1%（高并发下偶发）
# ...
## 阶段2: 定位(续3)
# ...
### 线程转储分析
```bash
# Go goroutine dump
kill -SIGQUIT <pid>
# 或
curl http://localhost:6060/debug/pprof/goroutine?debug=2 > goroutine.txt
```
# ...
**分析发现**:
```
goroutine 1 [semacquire]:  // 等待锁
sync.runtime_SemacquireMutex(0xc0000e01ac, 0x0)
sync.(*Mutex).Lock(0xc0000e01a8)
main.AccountService.Transfer(0xc0000e01a0, 0x1234, 0x5678, 0x100)

goroutine 2 [semacquire]:  // 等待另一个锁
sync.runtime_SemacquireMutex(0xc0000e01bc, 0x0)
sync.(*Mutex).Lock(0xc0000e01b8)
main.AccountService.Transfer(0xc0000e01b0, 0x5678, 0x1234, 0x100)
```
# ...
### 锁图分析
```
Goroutine 1: 持有 Account_A 锁 → 等待 Account_B 锁
Goroutine 2: 持有 Account_B 锁 → 等待 Account_A 锁
         ↓
    形成等待环（死锁）
```
# ...
### 根因
```go
// 问题代码: 锁顺序不一致
func (s *AccountService) Transfer(from, to int64, amount int) error {
    fromAccount := s.getAccount(from)
    toAccount := s.getAccount(to)
    
    fromAccount.Lock()   // 先锁from
    defer fromAccount.Unlock()
    
    toAccount.Lock()     // 再锁to
    defer toAccount.Unlock()
    
    // 转账逻辑
}
```
# ...
**问题**: 
- A→B转账: 锁顺序 A, B
- B→A转账: 锁顺序 B, A
- 并发时形成死锁
# ...
## 阶段3: 缩减(续3)
# ...
### 最小复现用例(补充)(补充3)
```go
func TestDeadlock(t *testing.T) {
    service := NewAccountService()
    
    // 创建两个账户
    service.CreateAccount(1, 1000)
    service.CreateAccount(2, 1000)
    
    var wg sync.WaitGroup
    wg.Add(2)
    
    // Goroutine 1: 账户1 → 账户2
    go func() {
        defer wg.Done()
        service.Transfer(1, 2, 100)
    }()
    
    // Goroutine 2: 账户2 → 账户1（反向）
    go func() {
        defer wg.Done()
        service.Transfer(2, 1, 100)
    }()
    
    // 带超时等待，检测死锁
    done := make(chan struct{})
    go func() {
        wg.Wait()
        close(done)
    }()
    
    select {
    case <-done:
        // 正常完成
    case <-time.After(5 * time.Second):
        t.Fatal("Deadlock detected: transfer did not complete in 5s")
    }
}
```
# ...
## 阶段4: 修复(续3)
# ...
### 修复实施: 统一锁顺序
```go
// 修复: 按账户ID排序，确保锁顺序一致
func (s *AccountService) Transfer(from, to int64, amount int) error {
    fromAccount := s.getAccount(from)
    toAccount := s.getAccount(to)
    
    // 按ID排序，小ID先锁
    first, second := fromAccount, toAccount
    if from > to {
        first, second = toAccount, fromAccount
    }
    
    first.Lock()
    defer first.Unlock()
    second.Lock()
    defer second.Unlock()
    
    // 转账逻辑（注意from/to可能交换）
    if from < to {
        fromAccount.Balance -= amount
        toAccount.Balance += amount
    } else {
        toAccount.Balance -= amount
        fromAccount.Balance += amount
    }
    
    return nil
}
```
# ...
### 替代方案: TryLock + 超时
```go
func (s *AccountService) Transfer(from, to int64, amount int) error {
    fromAccount := s.getAccount(from)
    toAccount := s.getAccount(to)
    
    // TryLock带超时，避免永久阻塞
    if !fromAccount.TryLockTimeout(5 * time.Second) {
        return errors.New("acquire from account timeout")
    }
    defer fromAccount.Unlock()
    
    if !toAccount.TryLockTimeout(5 * time.Second) {
        return errors.New("acquire to account timeout")
    }
    defer toAccount.Unlock()
    
    // 转账逻辑
}
```
# ...
### 验证闭环(补充)(补充3)
1. **回归测试**: 死锁检测测试（5秒超时）
2. **修复后测试**: 100并发转账10分钟，无死锁
3. **完整测试**: 全通过
4. **生产灰度**: 5%流量7天，无死锁
# ...
### 防御深度(补充)(补充3)
- 死锁检测: Go runtime自带死锁检测
- 锁超时: 所有锁操作带超时
- 监控告警: Goroutine数量>1000告警
- 竞态检测: `go test -race` 集成到CI
```

**效果验证**: ✓Goroutine dump分析准确 ✓锁图识别等待环 ✓最小复现用例（2 Goroutine） ✓统一锁顺序修复 ✓TryLock超时备选方案

### 案例4: 性能回归调试

**输入**:
```
现象: API响应时间从50ms升至500ms，无明显错误
触发: 上周代码发布后开始
环境: Python FastAPI + PostgreSQL
方法: git bisect回归定位
```

**LLM生成输出**:
```markdown
# output/perf-regression/debug-report.md
# 性能回归调试报告
# ...
## 阶段1: 复现(续4)
- **Staging环境**: 复现响应时间500ms（正常50ms）
- **现象**: 所有API端点变慢，无错误
- **可靠性**: 每次必现
# ...
## 阶段2: 定位(续4)
# ...
### Git Bisect回归定位
```bash
# 1. 启动bisect
git bisect start

# 2. 标记当前为bad
git bisect bad HEAD

# 3. 标记一周前为good
git bisect good v1.2.0  # 一周前的发布标签

# 4. 自动二分测试
# 每次checkout后运行性能测试
git bisect run python -m pytest tests/test_performance.py

# 5. 定位到具体commit
git bisect good/bad  # 根据测试结果

# 结果: 第一次坏提交是 abc1234
git bisect reset
git show abc1234
```
# ...
**定位结果**:
```
commit abc1234 "feat: 添加用户活动日志记录"
Author: dev
Date: 2024-10-08

+ @app.middleware("http")
+ async def log_activity(request: Request, call_next):
+     # 记录每个请求到数据库
+     await ActivityLog.create(
+         path=request.url.path,
+         method=request.method,
+         user_id=request.state.user_id
+     )
+     response = await call_next(request)
+     return response
```
# ...
### 性能剖析
```bash
# 使用py-spy采样剖析
py-spy record -o profile.svg --pid <pid> --duration 60
```
# ...
**火焰图分析**:
- `ActivityLog.create` 占用80% CPU时间
- 每个请求同步写入数据库，阻塞响应
- 数据库连接池耗尽，排队等待
# ...
## 阶段3: 缩减(续4)
# ...
### 最小复现用例(补充)(补充4)
```python
import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.middleware("http")
async def slow_middleware(request, call_next):
    # 模拟数据库写入
    await asyncio.sleep(0.45)  # 450ms
    return await call_next(request)

@app.get("/test")
async def test():
    return {"status": "ok"}

# 测试: curl http://localhost/test
# 响应时间: 450ms+（确认中间件是根因）
```
# ...
### 根因确认(补充)(补充)
- **根因**: 日志中间件同步写入数据库，每个请求增加450ms
- **验证**: 移除中间件后，响应时间恢复50ms
# ...
## 阶段4: 修复(续4)
# ...
### 修复实施: 异步日志写入
```python
# 修复前: 同步写入
@app.middleware("http")
async def log_activity(request, call_next):
    await ActivityLog.create(...)  # 阻塞
    return await call_next(request)

# 修复后: 异步队列写入
import asyncio
from queue import Queue

log_queue = Queue()

@app.middleware("http")
async def log_activity(request, call_next):
    # 非阻塞放入队列
    log_queue.put({
        'path': request.url.path,
        'method': request.method,
        'user_id': getattr(request.state, 'user_id', None),
        'timestamp': time.time()
    })
    return await call_next(request)

# 后台消费者: 批量写入
async def log_consumer():
    while True:
        batch = []
        while not log_queue.empty():
            batch.append(log_queue.get())
        if batch:
            await ActivityLog.bulk_create(batch)  # 批量写入
        await asyncio.sleep(1)  # 每秒刷新

# 启动消费者
@app.on_event("startup")
async def startup():
    asyncio.create_task(log_consumer())
```
# ...
### 验证闭环(补充)(补充4)
1. **回归测试**:
```python
def test_api_response_time():
    start = time.time()
    response = client.get("/api/users")
    duration = time.time() - start
    assert duration < 0.1, f"Response took {duration}s"
```
# ...
2. **修复后测试**: 响应时间50ms，日志延迟<1秒
3. **完整测试**: 全通过
4. **压测**: 1000 QPS稳定，日志正常写入
# ...
### 防御深度(补充)(补充4)
- 性能基准测试: CI集成，响应时间>100ms告警
- 中间件性能监控: 每个中间件耗时记录
- 日志队列监控: 队列积压>1000告警
- 数据库连接池监控: 使用率>80%告警
```

**效果验证**: ✓git bisect精准定位commit ✓py-spy火焰图分析 ✓根因为同步中间件 ✓异步队列修复方案 ✓CI性能基准测试

### 案例5: 前端内存泄漏调试

**输入**:
```
现象: React单页应用长时间使用后卡顿，刷新后恢复
环境: React 18 + Redux，Chrome浏览器
触发: 使用2小时后明显卡顿
```

**LLM生成输出**:
```markdown
# output/frontend-leak/debug-report.md
# 前端内存泄漏调试报告
# ...
## 阶段1: 复现(续5)
- **操作**: 持续使用SPA 2小时（页面切换/弹窗开关/数据加载）
- **现象**: Chrome DevTools显示内存从100MB增至500MB+
- **复现性**: 本地Chrome稳定复现
# ...
## 阶段2: 定位(续5)
# ...
### Chrome DevTools Memory分析
1. **Heap Snapshot对比**:
   - 初始快照: 100MB
   - 2小时后快照: 500MB
   - 对比Delta: +400MB
# ...
2. **泄漏对象类型**:
   ```
   Detached DOM nodes: 250MB (5000个)
   Closures: 100MB
   Event listeners: 50MB
   ```
# ...
3. **引用链分析**:
   - Detached DOM nodes被Redux store中的旧数据引用
   - 弹窗组件卸载后，事件监听器未移除
   - setInterval定时器未清理
# ...
### 代码定位
```javascript
// 问题1: 弹窗组件未清理事件监听
function Modal({ onClose }) {
  useEffect(() => {
    document.addEventListener('keydown', handleEscape);  // 未return清理
  }, []);
  
  // 缺少: return () => document.removeEventListener('keydown', handleEscape);
}

// 问题2: setInterval未清理
function Dashboard() {
  useEffect(() => {
    setInterval(fetchData, 5000);  // 未return清理
  }, []);
  
  // 缺少: return () => clearInterval(interval);
}

// 问题3: Redux store积累旧数据
// 每次页面切换，旧数据未清理
function reducer(state, action) {
  switch (action.type) {
    case 'PAGE_LOAD':
      return {
        ...state,
        [action.page]: action.data,
        // 旧page数据未删除，持续积累
      };
    default:
      return state;
  }
}
```
# ...
## 阶段3: 缩减(续5)
# ...
### 最小复现用例(补充)(补充5)
```javascript
// React组件: 模拟弹窗开关1000次
function LeakTest() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    if (count < 1000) {
      setTimeout(() => setCount(c => c + 1), 10);
    }
  }, [count]);
  
  return (
    <div>
      <p>Count: {count}</p>
      {count % 2 === 0 && <Modal onClose={() => {}} />}
    </div>
  );
}

// 1000次开关后，内存增长50MB（确认弹窗泄漏）
```
# ...
## 阶段4: 修复(续5)
# ...
### 修复实施(补充)(补充3)
```javascript
// 修复1: 清理事件监听
function Modal({ onClose }) {
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);  // 清理
  }, [onClose]);
}

// 修复2: 清理定时器
function Dashboard() {
  useEffect(() => {
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);  // 清理
  }, []);
}

// 修复3: 限制Redux store大小
function reducer(state, action) {
  switch (action.type) {
    case 'PAGE_LOAD': {
      const newPages = { ...state.pages, [action.page]: action.data };
      // 仅保留最近5个页面数据
      const pageKeys = Object.keys(newPages);
      if (pageKeys.length > 5) {
        delete newPages[pageKeys[0]];
      }
      return { ...state, pages: newPages };
    }
    default:
      return state;
  }
}
```
# ...
### 验证闭环(补充)(补充5)
1. **回归测试**:
```javascript
// Jest + React Testing Library
test('Modal cleans up event listener on unmount', () => {
  const removeSpy = jest.spyOn(document, 'removeEventListener');
  const { unmount } = render(<Modal onClose={() => {}} />);
  unmount();
  expect(removeSpy).toHaveBeenCalled();
});

test('Dashboard cleans up interval on unmount', () => {
  jest.useFakeTimers();
  const clearSpy = jest.spyOn(global, 'clearInterval');
  const { unmount } = render(<Dashboard />);
  unmount();
  expect(clearSpy).toHaveBeenCalled();
});
```
# ...
2. **修复后测试**: 2小时使用，内存稳定在120MB
3. **完整测试**: 全通过
4. **Lighthouse审计**: 内存泄漏检测通过
# ...
### 防御深度(补充)(补充5)
- ESLint规则: eslint-plugin-react-hooks检测未清理的effect
- 内存监控: window.performance.memory定期采样
- 自动化测试: 每次PR运行内存泄漏检测
- Lighthouse CI: 内存审计集成到流水线
```

**效果验证**: ✓Chrome DevTools Heap Snapshot对比 ✓3类泄漏精准定位 ✓最小复现用例（1000次开关） ✓useEffect cleanup修复 ✓ESLint+Lighthouse防御

## 常见问题

### Q1: 什么时候用git bisect,什么时候用二分注释代码?
A: git bisect适用于:Bug是回归(之前正常现在出错),且能明确判断每个commit是否复现。操作:`git bisect start` → `git bisect bad HEAD` → `git bisect good <commit>` → 自动二分。二分注释代码适用于:Bug不是回归,或代码量较大时定位问题模块。建议:回归Bug优先git bisect(精准到commit),非回归Bug用代码二分(快速定位模块),两者可结合使用。

### Q2: 间歇性Bug(概率性出现)如何调试?
A: (1)条件等待法:在可疑代码添加条件日志,设置Watchpoint监控变量变化,等待下次触发时自动记录。(2)压力测试复现:提高并发/频率,将1%概率提升至10%+。(3)日志增强:记录线程ID+时间戳+关键变量,分析触发模式。(4)Chaos Engineering:注入故障(网络延迟/磁盘满/服务宕机),观察是否触发。(5)生产环境:部署监控,收集所有触发时的上下文。关键原则:不要放弃,间歇性Bug往往隐藏深层设计问题。

### Q3: 修复后如何确保不引入新问题?
A: 验证闭环4步:(1)先写回归测试,验证测试在修复前会失败(证明测试有效)(2)应用修复,运行回归测试验证通过(3)运行完整测试套件,确保无其他回归(4)代码审查,由另一人review修复方案。防御深度:修复点添加输入验证、边界检查、断言保护、监控告警。生产环境:灰度发布(先5%流量),监控错误率,逐步放量至100%。

### Q4: 生产事故应该先止血还是先查根因?
A: 先止血,再查根因,最后防复发。止血优先级>根因分析。(1)止血:回滚最近变更/降级非核心功能/扩容/重启(2)根因:止血后立即开始根因分析,保留现场(日志/dump/监控快照)(3)防复发:根因修复+防御深度+监控告警+复盘文档。例外:如果止血措施(如回滚)会破坏现场证据,需先采集证据再止血。

## 已知限制

- 本Skill提供调试方法论与流程指导,不替代实际调试工具操作
- 调试效果依赖LLM对代码的理解能力,复杂业务逻辑可能需要人工判断
- 并发问题与间歇性故障调试耗时较长,本Skill提供策略但不保证100%复现
- 性能调试需要Profiling工具配合,本Skill仅提供分析框架
- 不涵盖特定语言的调试器使用教程(需查阅各语言文档)
- 生产环境调试受限于安全策略,可能无法直接调试

## 安全与合规

- 本Skill不存储任何API Key或敏感凭证
- 调试工具均为本地运行,不涉及外部服务
- 生产环境调试需遵循最小权限原则,避免影响线上服务
- 内存dump/线程dump可能包含敏感数据,需加密存储并定期清理
- 日志增强时避免记录密码/Token等敏感信息(脱敏处理)
- 调试报告不包含生产环境的真实用户数据(需脱敏)
- 修复方案需通过代码审查后才能合并,避免引入安全漏洞
