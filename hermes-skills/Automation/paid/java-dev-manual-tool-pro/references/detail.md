# 详细参考 - java-dev-manual-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
#!/bin/bash
PROJECT_NAME=$1
GROUP_ID=${2:-com.company}
VERSION=${3:-1.0.0}

echo "=== 初始化 Java 项目: $PROJECT_NAME ==="

mkdir -p "$PROJECT_NAME"/src/main/java/${GROUP_ID//.//}/"$PROJECT_NAME"
mkdir -p "$PROJECT_NAME"/src/main/resources
mkdir -p "$PROJECT_NAME"/src/test/java/${GROUP_ID//.//}/"$PROJECT_NAME"

BASE_PKG="${GROUP_ID}.${PROJECT_NAME}"
PKG_PATH="${GROUP_ID//.//}/$PROJECT_NAME"

LAYERS=("controller" "service" "service/impl" "repository" "entity" "dto" "vo" "config" "exception" "common" "util")
for layer in "${LAYERS[@]}"; do
  mkdir -p "$PROJECT_NAME"/src/main/java/$PKG_PATH/$layer
done

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

## 代码示例 (yaml)

```yaml
version: "2.0"
team: "后端开发组"
updated: "2026-07-18"

extends: "default"

rules:
  coding:
    naming:
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
  exception:
    require_error_code: true              # 异常必须包含错误码
    require_user_friendly_msg: true       # 异常信息必须用户友好
    error_code_format: "ERR_{MODULE}_{SEQ}"  # 错误码格式
    log_require_trace_id: true            # 日志必须包含 traceId
  database:
    require_soft_delete: true             # 必须软删除
    soft_delete_field: "is_deleted"       # 软删除字段名
    require_audit_field: true             # 必须审计字段
    audit_fields: ["create_by", "update_by", "create_time", "update_time"]
    forbid_physical_delete: true          # 禁止物理删除
    max_result_size: 1000                 # 单次查询最大结果数
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
excludes:
  - "**/test/**"
  - "**/generated/**"
  - "**/migration/**"
  - "**/dto/**"
```

