---
slug: "java-dev-manual"
name: "java-dev-manual"
version: "1.0.0"
displayName: "Java开发手册专业版"
summary: "企业级 Java 开发规约方案，含自定义规则、团队规范模板与 CI 集成。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业级 Java 开发团队的开发规约治理工具，提供团队级规范定制能力。核心能力:
  - 7 大维度规约的团队级自定义配置
  - 规约合规性自动检查与报告生成
  - 新项目脚手架与规范模板集成
  - 架构分层规范与依赖管理约束
  - 设计模式与设计原则的代码示例库
  - CI/CD 规约检查集成与质量门禁

  适用场景:
  - 企业级 Java 项目的规范落地与执行
  - 团队级编码规范的定制与统一
  - 新项目架构搭建与规范初始化
  - 代码合规性审计与持续改进

  差异化: 专业版兼容免费版所有规约内容...
tags:
  - 开发工具
  - Java
  - 开发规范
  - 企业协作
  - 架构设计
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Java开发手册专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| 专业版新增 | 不支持 | 支持 |
| 规约查询 | 不支持 | 支持 |
| 团队级自定义规则 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
| --- | --- | --- |
| 规约查询 | 7 维度速查 | 团队级自定义规则 |
| 合规检查 | 手动对照 | 自动化检查脚本 |
| 项目初始化 | - | 规范脚手架生成 |
| 架构约束 | 分层建议 | 依赖方向自动校验 |
| 设计模式 | 规范建议 | 完整示例代码库 |
| CI 集成 | - | 规约门禁 + 报告 |
| 规约审计 | - | 全项目合规性报告 |
| 规则管理 | 固定规则 | 版本化规则配置 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项。

**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 规约查询

针对规约,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供规约查询相关的配置参数、输入数据和处理选项。

**输出**: 返回规约查询的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`规约查询`的配置文档进行参数调优
### 合规检查

针对合规,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供合规检查相关的配置参数、输入数据和处理选项。

**输出**: 返回合规检查的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`合规检查`的配置文档进行参数调优
#
## 适用场景

### 场景一：团队级规范定制
团队需要根据项目特点定制编码规范。

> 详细代码示例已移至 `references/detail.md`

### 场景二：新项目脚手架生成
新项目需要快速搭建符合规范的工程结构。

> 详细代码示例已移至 `references/detail.md`

### 场景三：规约合规性审计
团队需要对整个项目进行规约合规性审计。

```bash
#!/bin/bash
PROJECT_DIR=$1
REPORT_FILE="convention-audit-$(date +%Y%m%d).md"

echo "# Java 规约合规性审计报告" > "$REPORT_FILE"
echo "**审计日期**: $(date)" >> "$REPORT_FILE"
echo "**审计范围**: $PROJECT_DIR" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

JAVA_FILES=$(find "$PROJECT_DIR" -name "*.java" -not -path "*/test/*")
FILE_COUNT=$(echo "$JAVA_FILES" | wc -l)

echo "## 审计概览" >> "$REPORT_FILE"
echo "| 指标 | 数值 |" >> "$REPORT_FILE"
echo "| --- | --- |" >> "$REPORT_FILE"
echo "| Java 文件数 | $FILE_COUNT |" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 1. 命名规范审计" >> "$REPORT_FILE"
echo "### 类名后缀合规性" >> "$REPORT_FILE"
echo "| 规则 | 合规数 | 违规数 | 合规率 |" >> "$REPORT_FILE"
echo "| --- | --- | --- | --- |" >> "$REPORT_FILE"

CONTROLLER_OK=$(find "$PROJECT_DIR" -name "*Controller.java" | wc -l)
CONTROLLER_BAD=$(find "$PROJECT_DIR" -path "*/controller/*" -name "*.java" ! -name "*Controller.java" | wc -l)
echo "| Controller 后缀 | $CONTROLLER_OK | $CONTROLLER_BAD | $(echo "scale=0; $CONTROLLER_OK * 100 / ($CONTROLLER_OK + $CONTROLLER_BAD + 1)" | bc)% |" >> "$REPORT_FILE"

echo "### 拼音命名检查" >> "$REPORT_FILE"
PINYIN_ISSUES=$(grep -rn "yonghu\|dingdan\|zhifu\|shangpin\|gongsi" "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 拼音命名违规: $PINYIN_ISSUES 处" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 2. 异常处理审计" >> "$REPORT_FILE"
EMPTY_CATCH=$(grep -rn "catch.*Exception.*\{" "$PROJECT_DIR" --include="*.java" -A 1 | grep -c "^.*--$" || echo 0)
echo "- 空 catch 块: $EMPTY_CATCH 处" >> "$REPORT_FILE"

SYSTEM_OUT=$(grep -rn "System\.out\.\|System\.err\." "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 使用 System.out: $SYSTEM_OUT 处" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 3. 安全审计" >> "$REPORT_FILE"
SQL_CONCAT=$(grep -rn "String sql.*+.*\"" "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- SQL 拼接: $SQL_CONCAT 处" >> "$REPORT_FILE"

HARDCODED_PWD=$(grep -rin "password.*=.*\"\|secret.*=.*\"" "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 硬编码密码: $HARDCODED_PWD 处" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 4. 并发审计" >> "$REPORT_FILE"
EXECUTORS_USE=$(grep -rn "Executors\." "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 使用 Executors: $EXECUTORS_USE 处" >> "$REPORT_FILE"

THREADLOCAL_NO_REMOVE=$(grep -rn "ThreadLocal" "$PROJECT_DIR" --include="*.java" -l | while read f; do
  SET_COUNT=$(grep -c "\.set(" "$f")
  REMOVE_COUNT=$(grep -c "\.remove(" "$f")
  if [ "$SET_COUNT" -gt "$REMOVE_COUNT" ]; then echo "$f"; fi
done | wc -l)
echo "- ThreadLocal 未清理: $THREADLOCAL_NO_REMOVE 处" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 5. 架构分层审计" >> "$REPORT_FILE"
BAD_DEP=$(grep -rn "import.*repository\." "$PROJECT_DIR"/src/main/java/*/controller/ 2>/dev/null | wc -l)
echo "- Controller 直接依赖 Repository: $BAD_DEP 处" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 审计完成"
echo "报告: $REPORT_FILE"
```

## 使用流程

### 架构分层规范
```
src/main/java/com/company/project/
├── controller/          # 控制层：接收请求，参数校验
│   └── UserController.java
├── service/             # 服务层：业务逻辑
│   ├── UserService.java       # 接口
│   └── impl/
│       └── UserServiceImpl.java  # 实现
├── repository/          # 数据访问层：数据库操作
│   └── UserRepository.java
├── entity/              # 实体层：数据库映射
│   └── UserEntity.java
├── domain/              # 领域层：领域模型
│   └── User.java
├── dto/                 # 数据传输对象
│   ├── UserCreateDTO.java
│   └── UserQueryDTO.java
├── vo/                  # 视图对象
│   └── UserVO.java
├── config/              # 配置类
│   └── WebConfig.java
├── exception/           # 异常处理
│   ├── BusinessException.java
│   └── GlobalExceptionHandler.java
├── common/              # 公共组件
│   ├── Result.java
│   └── PageResult.java
└── util/                # 工具类
    └── DateUtils.java
```

**分层依赖规则**：

| 层 | 允许依赖 | 禁止依赖 |
| --- | --- | --- |
| Controller | Service | Repository, Entity |
| Service | Repository, Domain | Controller |
| Repository | Entity | Service, Controller |
| Domain | 无 | 所有其他层 |

### 示例
```java
// 策略模式：支付方式选择
public interface PaymentStrategy {
    PayResult pay(PayRequest request);
}

@Component
public class AlipayStrategy implements PaymentStrategy {
    public PayResult pay(PayRequest request) { /* ... */ }
}

@Component
public class WechatPayStrategy implements PaymentStrategy {
    public PayResult pay(PayRequest request) { /* ... */ }
}

@Component
public class PaymentStrategyFactory {
    @Autowired
    private Map<String, PaymentStrategy> strategies;

    public PaymentStrategy get(String type) {
        return strategies.get(type + "Strategy");
    }
}

// 模板方法模式：数据导出
public abstract class DataExporter {
    public final void export() {
        List<Data> data = fetchData();
        String content = transform(data);
        write(content);
    }
    protected abstract List<Data> fetchData();
    protected abstract String transform(List<Data> data);
    protected abstract void write(String content);
}
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | java-dev-manual处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的代码 |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过5000字 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **JDK 版本**: 建议 11 及以上
- **构建工具**: Maven 3.6+ 或 Gradle 7+
- **CI/CD 平台**: GitHub Actions / GitLab CI / Jenkins 等

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| JDK | 编译器/运行时 | 必需 | oracle.com 或 openjdk.net 下载 |
| Maven | 构建工具 | 推荐 | maven.apache.org 下载 |
| SLF4J | 日志框架 | 推荐 | maven 中央仓库 |
| Lombok | 工具库 | 推荐 | maven 中央仓库 |
| Spring Boot | 应用框架 | 可选 | spring.io |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- CI/CD 集成需要在平台配置对应的访问令牌
- 依赖下载需要配置 Maven 仓库镜像

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 提供规约查询与项目脚手架，专业版功能依赖构建工具和 CI/CD 平台

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1：如何推动团队执行规范？
```text
1. CI 强制门禁：Critical 违规阻止合并
2. 定期审计报告：公布各模块合规率
3. 脚手架集成：新项目开箱即合规
4. 培训与文档：提供示例和优秀实践
5. 渐进式推进：先 Critical 后 Major
```

### Q2：如何处理遗留代码不合规？
```text
1. 审计评估：生成完整违规报告
2. 优先级排序：Critical 优先修复
3. 分批改进：每迭代修复一部分
4. 增量控制：新代码必须合规
5. 重构机会：在功能迭代时顺带修复
```

### Q3：如何自定义错误码体系？
```java
public enum ErrorCode {
    // 通用错误 1详情见说明x
    SUCCESS("00000", "成功"),
    PARAM_ERROR("10001", "参数错误"),
    SYSTEM_ERROR("10002", "系统繁忙"),

    // 用户模块 2详情见说明x
    USER_NOT_FOUND("20001", "用户不存在"),
    USER_DISABLED("20002", "用户已被禁用"),

    // 订单模块 3详情见说明x
    ORDER_NOT_FOUND("30001", "订单不存在"),
    ORDER_PAID("30002", "订单已支付");

    private final String code;
    private final String message;

    ErrorCode(String code, String message) {
        this.code = code;
        this.message = message;
    }
}
```

### Q4：如何实现软删除规范？
```java
@MappedSuperclass
public abstract class BaseEntity {
    @CreatedBy
    private String createBy;

    @CreatedDate
    private LocalDateTime createTime;

    @LastModifiedBy
    private String updateBy;

    @LastModifiedDate
    private LocalDateTime updateTime;

    @TableLogic
    private Integer isDeleted;
}

// 使用时继承 BaseEntity
@Entity
@Table(name = "users")
public class UserEntity extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
}
```

### Q5：如何做 API 版本管理？
```java
// URL 路径版本
@RestController
@RequestMapping("/api/v1/users")
public class UserControllerV1 {
    @GetMapping("/{id}")
    public Result getUser(@PathVariable Long id) { }
}

@RestController
@RequestMapping("/api/v2/users")
public class UserControllerV2 {
    @GetMapping("/{id}")
    public Result getUser(@PathVariable Long id) { }
}

// Header 版本
@GetMapping(value = "/users/{id}", headers = "X-API-Version=2")
public Result getUserV2(@PathVariable Long id) { }
```

### Q6：如何统计规范合规率？
```bash
TOTAL=$(find src/ -name "*.java" | wc -l)
VIOLATIONS=$(grep -rl "System\.out\|Executors\.\|yonghu" src/ --include="*.java" | wc -l)
COMPLIANCE=$(echo "scale=1; (1 - $VIOLATIONS / $TOTAL) * 100" | bc)
echo "合规率: $COMPLIANCE%"
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

