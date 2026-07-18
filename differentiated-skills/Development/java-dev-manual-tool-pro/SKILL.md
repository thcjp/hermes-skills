---
slug: java-dev-manual-tool-pro
name: java-dev-manual-tool-pro
version: "1.0.0"
displayName: Java开发手册专业版
summary: 企业级 Java 开发规约方案，含自定义规则、团队规范模板与 CI 集成。
license: MIT
edition: pro
description: |-
  面向企业级 Java 开发团队的开发规约治理工具，提供团队级规范定制能力。

  核心能力:
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

  差异化: 专业版兼容免费版所有规约内容，额外提供团队级规则定制、自动合规检查、项目脚手架、CI 集成，支持企业级规范治理。

  触发关键词: java企业规范, 团队规约, 合规检查, 项目脚手架, 架构分层, 设计模式库, ci规范集成, 规约审计, 质量门禁
tags:
- 开发工具
- Java
- 开发规范
- 企业协作
- 架构设计
tools:
- read
- exec
---

# Java 开发手册（专业版）

## 概述

本工具面向企业级 Java 开发团队，提供开发规约的完整治理方案。在免费版 7 大维度规约速查能力之上，专业版新增团队级规则定制、规约合规性自动检查、新项目脚手架集成、架构分层约束、设计模式示例库、CI/CD 规约门禁等能力。通过可配置的规则引擎与自动化检查脚本，帮助团队建立统一、可执行、可追踪的编码规范体系。

**版本兼容性说明**：专业版完全兼容免费版（`java-dev-manual-tool-free`）的所有规约内容与速查表，可无缝升级。

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

## 使用场景

### 场景一：团队级规范定制

团队需要根据项目特点定制编码规范。

```yaml
# .java-conventions.yml - 团队级规范配置
version: "2.0"
team: "后端开发组"
updated: "2026-07-18"

# 继承基础规约
extends: "default"

# 规约覆盖
rules:
  # 编程规约
  coding:
    naming:
      # 团队特有的类名后缀要求
      required_suffixes:
        controller: "Controller"
        service: "Service" 
        service_impl: "ServiceImpl"
        repository: "Repository"
        mapper: "Mapper"
        dto: "DTO"
        vo: "VO"
        bo: "BO"
        entity: "Entity"
        config: "Config"
        exception: "Exception"
      # 禁止的命名
      forbidden_names: ["Data", "Info", "Object", "Helper"]
      
    format:
      max_line_length: 120
      max_method_length: 50
      max_class_length: 500
      max_parameters: 5
      
    oop:
      require_builder_pattern: true    # 多参数对象用 Builder
      require_final_field: true        # 不可变字段加 final
      forbid_public_field: true        # 禁止 public 字段
      
    concurrent:
      require_named_thread_factory: true  # 线程必须命名
      require_thread_pool_monitor: true   # 线程池需要监控
      max_thread_pool_size: 200           # 最大线程数
      
    collection:
      require_initial_capacity: true      # 集合必须指定初始容量
      forbid_null_value: true             # Map 禁止 null 值

  # 异常日志规约
  exception:
    require_error_code: true              # 异常必须包含错误码
    require_user_friendly_msg: true       # 异常信息必须用户友好
    error_code_format: "ERR_{MODULE}_{SEQ}"  # 错误码格式
    log_require_trace_id: true            # 日志必须包含 traceId
    
  # 数据库规约
  database:
    require_soft_delete: true             # 必须软删除
    soft_delete_field: "is_deleted"       # 软删除字段名
    require_audit_field: true             # 必须审计字段
    audit_fields: ["create_by", "update_by", "create_time", "update_time"]
    forbid_physical_delete: true          # 禁止物理删除
    max_result_size: 1000                 # 单次查询最大结果数

  # 工程结构规约
  architecture:
    layer_dependencies:                   # 分层依赖方向
      controller: ["service"]
      service: ["repository", "domain"]
      repository: ["entity"]
      domain: []
    forbidden_dependencies:               # 禁止的依赖方向
      - "controller -> repository"
      - "repository -> service"
    require_api_version: true             # API 必须版本化

# 排除规则
excludes:
  - "**/test/**"
  - "**/generated/**"
  - "**/migration/**"
  - "**/dto/**"
```

### 场景二：新项目脚手架生成

新项目需要快速搭建符合规范的工程结构。

```bash
#!/bin/bash
# scripts/init-java-project.sh - 初始化规范项目结构

PROJECT_NAME=$1
GROUP_ID=${2:-com.company}
VERSION=${3:-1.0.0}

echo "=== 初始化 Java 项目: $PROJECT_NAME ==="

# 创建标准目录结构
mkdir -p "$PROJECT_NAME"/src/main/java/${GROUP_ID//.//}/"$PROJECT_NAME"
mkdir -p "$PROJECT_NAME"/src/main/resources
mkdir -p "$PROJECT_NAME"/src/test/java/${GROUP_ID//.//}/"$PROJECT_NAME"

BASE_PKG="${GROUP_ID}.${PROJECT_NAME}"
PKG_PATH="${GROUP_ID//.//}/$PROJECT_NAME"

# 创建分层目录
LAYERS=("controller" "service" "service/impl" "repository" "entity" "dto" "vo" "config" "exception" "common" "util")
for layer in "${LAYERS[@]}"; do
  mkdir -p "$PROJECT_NAME"/src/main/java/$PKG_PATH/$layer
done

# 生成 pom.xml
cat > "$PROJECT_NAME/pom.xml" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>${GROUP_ID}</groupId>
    <artifactId>${PROJECT_NAME}</artifactId>
    <version>${VERSION}</version>
    <packaging>jar</packaging>
    
    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <!-- Spring Boot Starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.2.0</version>
        </dependency>
        <!-- 参数校验 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
            <version>3.2.0</version>
        </dependency>
        <!-- 日志 -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>2.0.9</version>
        </dependency>
        <!-- Lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.30</version>
            <scope>provided</scope>
        </dependency>
        <!-- 测试 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.2.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
EOF

# 生成全局异常处理
cat > "$PROJECT_NAME/src/main/java/$PKG_PATH/exception/GlobalExceptionHandler.java" << 'EOF'
package PKG_PLACEHOLDER.exception;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    @ExceptionHandler(BusinessException.class)
    public Result handleBusiness(BusinessException e) {
        logger.warn("业务异常: code={}, msg={}", e.getCode(), e.getMessage());
        return Result.fail(e.getCode(), e.getMessage());
    }
    
    @ExceptionHandler(Exception.class)
    public Result handleSystem(Exception e) {
        logger.error("系统异常", e);
        return Result.fail("SYSTEM_ERROR", "系统繁忙，请稍后重试");
    }
}
EOF
sed -i "s/PKG_PLACEHOLDER/${BASE_PKG}/g" \
  "$PROJECT_NAME/src/main/java/$PKG_PATH/exception/GlobalExceptionHandler.java"

# 生成统一返回类
cat > "$PROJECT_NAME/src/main/java/$PKG_PATH/common/Result.java" << 'EOF'
package PKG_PLACEHOLDER.common;

import lombok.Data;

@Data
public class Result<T> {
    private String code;
    private String message;
    private T data;
    
    public static <T> Result<T> success(T data) {
        Result<T> r = new Result<>();
        r.setCode("SUCCESS");
        r.setMessage("操作成功");
        r.setData(data);
        return r;
    }
    
    public static <T> Result<T> fail(String code, String message) {
        Result<T> r = new Result<>();
        r.setCode(code);
        r.setMessage(message);
        return r;
    }
}
EOF
sed -i "s/PKG_PLACEHOLDER/${BASE_PKG}/g" \
  "$PROJECT_NAME/src/main/java/$PKG_PATH/common/Result.java"

echo "项目结构已创建: $PROJECT_NAME"
echo "基础包名: $BASE_PKG"
```

### 场景三：规约合规性审计

团队需要对整个项目进行规约合规性审计。

```bash
#!/bin/bash
# scripts/java-convention-audit.sh - 规约合规性审计

PROJECT_DIR=$1
REPORT_FILE="convention-audit-$(date +%Y%m%d).md"

echo "# Java 规约合规性审计报告" > "$REPORT_FILE"
echo "**审计日期**: $(date)" >> "$REPORT_FILE"
echo "**审计范围**: $PROJECT_DIR" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 统计文件数
JAVA_FILES=$(find "$PROJECT_DIR" -name "*.java" -not -path "*/test/*")
FILE_COUNT=$(echo "$JAVA_FILES" | wc -l)

echo "## 审计概览" >> "$REPORT_FILE"
echo "| 指标 | 数值 |" >> "$REPORT_FILE"
echo "| --- | --- |" >> "$REPORT_FILE"
echo "| Java 文件数 | $FILE_COUNT |" >> "$REPORT_FILE"

# 1. 命名规范审计
echo "" >> "$REPORT_FILE"
echo "## 1. 命名规范审计" >> "$REPORT_FILE"

# 检查类名后缀
echo "### 类名后缀合规性" >> "$REPORT_FILE"
echo "| 规则 | 合规数 | 违规数 | 合规率 |" >> "$REPORT_FILE"
echo "| --- | --- | --- | --- |" >> "$REPORT_FILE"

CONTROLLER_OK=$(find "$PROJECT_DIR" -name "*Controller.java" | wc -l)
CONTROLLER_BAD=$(find "$PROJECT_DIR" -path "*/controller/*" -name "*.java" ! -name "*Controller.java" | wc -l)
echo "| Controller 后缀 | $CONTROLLER_OK | $CONTROLLER_BAD | $(echo "scale=0; $CONTROLLER_OK * 100 / ($CONTROLLER_OK + $CONTROLLER_BAD + 1)" | bc)% |" >> "$REPORT_FILE"

# 检查拼音命名
echo "### 拼音命名检查" >> "$REPORT_FILE"
PINYIN_ISSUES=$(grep -rn "yonghu\|dingdan\|zhifu\|shangpin\|gongsi" "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 拼音命名违规: $PINYIN_ISSUES 处" >> "$REPORT_FILE"

# 2. 异常处理审计
echo "" >> "$REPORT_FILE"
echo "## 2. 异常处理审计" >> "$REPORT_FILE"
EMPTY_CATCH=$(grep -rn "catch.*Exception.*\{" "$PROJECT_DIR" --include="*.java" -A 1 | grep -c "^.*--$" || echo 0)
echo "- 空 catch 块: $EMPTY_CATCH 处" >> "$REPORT_FILE"

SYSTEM_OUT=$(grep -rn "System\.out\.\|System\.err\." "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 使用 System.out: $SYSTEM_OUT 处" >> "$REPORT_FILE"

# 3. 安全审计
echo "" >> "$REPORT_FILE"
echo "## 3. 安全审计" >> "$REPORT_FILE"
SQL_CONCAT=$(grep -rn "String sql.*+.*\"" "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- SQL 拼接: $SQL_CONCAT 处" >> "$REPORT_FILE"

HARDCODED_PWD=$(grep -rin "password.*=.*\"\|secret.*=.*\"" "$PROJECT_DIR" --include="*.java" | wc -l)
echo "- 硬编码密码: $HARDCODED_PWD 处" >> "$REPORT_FILE"

# 4. 并发审计
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

# 5. 架构审计
echo "" >> "$REPORT_FILE"
echo "## 5. 架构分层审计" >> "$REPORT_FILE"
# 检查 Controller 直接访问 Repository
BAD_DEP=$(grep -rn "import.*repository\." "$PROJECT_DIR"/src/main/java/*/controller/ 2>/dev/null | wc -l)
echo "- Controller 直接依赖 Repository: $BAD_DEP 处" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "## 审计完成"
echo "报告: $REPORT_FILE"
```

## 快速开始

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

### 设计模式示例库

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

## 配置示例

### CI/CD 规约门禁

```yaml
# .github/workflows/convention-check.yml
name: Java 规约检查
on: [pull_request]

jobs:
  convention:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: 执行规约审计
        run: ./scripts/java-convention-audit.sh src/
        
      - name: 检查 Critical 违规
        run: |
          CRITICAL=$(grep -c "硬编码密码\|SQL 拼接\|使用 Executors" convention-audit-*.md)
          if [ "$CRITICAL" -gt 3 ]; then
            echo "::error::Critical 违规超过 3 处，阻止合并"
            exit 1
          fi
```

## 最佳实践

1. **规范先于开发**：新项目必须先生成规范脚手架再编码

2. **规则版本管理**：规范配置纳入 Git，变更需评审

3. **定期合规审计**：每迭代执行全项目审计

4. **分层严格约束**：Controller 禁止直接访问 Repository

5. **异常统一处理**：全局异常处理器 + 业务异常类

6. **设计模式沉淀**：将团队常用的设计模式形成示例库

7. **CI 强制门禁**：Critical 违规超过阈值阻止合并

8. **规范培训**：新成员入职必须学习团队规范

## 常见问题

### Q1：如何推动团队执行规范？

```text
1. CI 强制门禁：Critical 违规阻止合并
2. 定期审计报告：公布各模块合规率
3. 脚手架集成：新项目开箱即合规
4. 培训与文档：提供示例和最佳实践
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
    // 通用错误 1xxxx
    SUCCESS("00000", "成功"),
    PARAM_ERROR("10001", "参数错误"),
    SYSTEM_ERROR("10002", "系统繁忙"),
    
    // 用户模块 2xxxx
    USER_NOT_FOUND("20001", "用户不存在"),
    USER_DISABLED("20002", "用户已被禁用"),
    
    // 订单模块 3xxxx
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
# 合规率 = (1 - 违规文件数 / 总文件数) × 100%
TOTAL=$(find src/ -name "*.java" | wc -l)
VIOLATIONS=$(grep -rl "System\.out\|Executors\.\|yonghu" src/ --include="*.java" | wc -l)
COMPLIANCE=$(echo "scale=1; (1 - $VIOLATIONS / $TOTAL) * 100" | bc)
echo "合规率: $COMPLIANCE%"
```

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **JDK 版本**: 建议 11 及以上
- **构建工具**: Maven 3.6+ 或 Gradle 7+
- **CI/CD 平台**: GitHub Actions / GitLab CI / Jenkins 等

### 第三方依赖

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
