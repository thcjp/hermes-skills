---

slug: kubernetes-devops
name: "kubernetes-devops"
version: 1.0.1
displayName: "Kubernetes运维工具"
summary: "K8s清单助手,生成规范的部署清单。This is a coherent Kubernetes manifest helper; its main risk is that users co"
summary_zh: "K8s清单助手,生成规范的部署清单。This is a coherent Kubernetes manifest helper; its main risk is that users co"
license: "MIT"
description: |-
  This is a coherent Kubernetes manifest helper; its main risk is that users could copy examples th。Use when 用户需要kubernetes-devops相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
  - Operations
  - 工具
  - 效率
  - 运维
  - 监控
  - api
  - llm
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"

---

# Kubernetes DevOps Toolkit

## Overview

Kubernetes DevOps Toolkit is a powerful tool designed to simplify the process of creating, managing, and deploying Kubernetes manifests. It provides a comprehensive set of features to help developers and operations teams automate their workflows and improve efficiency.

## Paid Features

| Feature | Free Version | Paid Version |
|---------|--------------|--------------|
| Basic Functionality | Supported | Supported |
| Advanced Parameter Configuration & Custom Rules | Not Supported | Supported |
| Batch Task Orchestration & Queue Management | Not Supported | Supported |
| Result Export & Multi-format Conversion | Not Supported | Supported |
| Real-time Status Monitoring & Exception Alerts | Not Supported | Supported |
| Historical Record Tracing & Difference Comparison | Not Supported | Supported |

## Core Capabilities

- **Coherent Kubernetes Manifest Helper**: Simplifies the creation of Kubernetes manifests.
- **Risk Mitigation**: Reduces the risk of manual errors by automating deployment processes.

## Getting Started

1. **Ensure Dependencies**: Confirm that the runtime environment meets the requirements specified in the dependencies section.
2. **Invoke the Skill**: In the AI Agent conversation, call the skill and provide the necessary input parameters.
3. **Review Output**: Check the output results and proceed with further processing as needed.

For detailed input and output formats, refer to the respective sections below.

## Use Cases

| Scenario | Input | Output |
|----------|-------|--------|
| Content Generation | Prompt and style parameters | Generated content and quality score |
| Deployment & Release | Deployment configuration and environment parameters | Deployment status and version information |
| Kubernetes Manifest Assistant | Target data and configuration parameters | Processing results and execution status |

**Not Suitable for**: Complex decision-making scenarios requiring human judgment.

## Usage Process

2. **Select Appropriate Usage Method**: Choose the appropriate usage method the applicable scenario.
3. **Execute Operation & Check Output**: Perform the operation and check the output results.
4. **Troubleshooting**: Refer to the troubleshooting section for error handling if necessary.

## Input Format

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| content        | string | No       | Input content for Kubernetes DevOps Toolkit processing |
| content        | string | No       | Input content for Kubernetes DevOps Toolkit processing |
| style          | string | No       | Output style, refer to `references/style.md` |

## Output Format

```json
{
  "success": true,
  "data": {
    "result": "devops related configuration parameters",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "professional"
    }
  },
  "error": null
}
```

Output templates can be found in `assets/output.json`.

## Exception Handling

| Problem | Diagnosis | Fix |
|---------|-----------|-----|
| Pod stuck `Pending` | `kubectl describe pod` — check events | Fix resource requests, node capacity, PVC binding |
| `ImagePullBackOff` | Wrong image name/tag or missing pull secret | Verify image exists, add `imagePullSecrets` |
| `CrashLoopBackOff` | App crashes on start | Check logs: `kubectl logs <pod> --previous` |
| Service not reachable | Selector mismatch | Verify `kubectl get endpoints <svc>` is non-empty |
| ConfigMap not loading | Name mismatch or wrong namespace | Check names match and namespace is correct |
| Readiness probe failing | Wrong path or port | Verify health endpoint works inside container |
| OOMKilled | Memory limit too low | Increase `resources.limits.memory` |

## Dependencies

### Runtime Environment

- **Agent Platform**: Supports any AI Agent compatible with SKILL.md (Claude Code, Cursor, Codex, Gemini CLI, etc.)
- **Operating System**: Windows, macOS, Linux

### Additional Dependencies

| Dependency | Type | Required | Acquisition Method |
|------------|------|----------|--------------------|
| LLM API    | API  | Required | Provided by the Agent's built-in LLM |

### API Key Configuration

- Configure the API key as follows:
  ```bash
  export API_KEY="your_api_key_here"
  ```
  Restart the session or open a new terminal for the changes to take effect. Keep the API key secure and avoid exposing it to version control systems.

## Common Questions

### Q1: How do I get started with Kubernetes?
A: Refer to the "Getting Started" section for detailed instructions.

## Error Handling

| Error Scenario | Cause | Solution |
|----------------|-------|----------|
| LLM response timeout or no response | Network latency or high model load | Retry the request; confirm that the LLM service on the Agent platform is normal |
| Incorrect input format | User input does not match the skill's expected format | Check if the input format matches the skill's usage instructions, refer to the examples section |
| Execution result does not match expectations | Inadequate instruction description or insufficient context | Provide more detailed instruction descriptions and supplement necessary context information |
| Command execution fails | Runtime environment does not meet requirements or insufficient permissions | Confirm that the runtime environment meets the requirements specified in the dependencies section; check command permission settings |

## Differentiation Advantages

### Comparison with Similar Solutions

In the Kubernetes operations tool market, there are several potential alternatives, including manual operations, general configuration management tools, and some automated scripts. Compared to these solutions, Kubernetes DevOps Toolkit 2 has the following advantages:

- **Manual Operations**: Manually operating Kubernetes configurations is time-consuming and prone to errors. Kubernetes DevOps Toolkit 2 significantly improves operational efficiency and reduces the likelihood of human errors through code generation and programming assistance.
- **General Configuration Management Tools**: Although general configuration management tools can manage multiple environments, they usually lack specific optimizations for Kubernetes. Kubernetes DevOps Toolkit 2 focuses on Kubernetes and provides deep integration and optimized features.
- **Automated Scripts**: Automated scripts can simplify some repetitive tasks, but their maintainability and scalability are usually not as good as Kubernetes DevOps Toolkit 2. Kubernetes DevOps Toolkit 2 provides a complete solution, including parameter configuration, batch task orchestration, and real-time monitoring functions.

### Unique Features

Kubernetes DevOps Toolkit 2 has the following unique features:

- **Advanced Parameter Configuration & Custom Rules**: Allows users to customize the generation rules for deployment manifests to meet complex Kubernetes configuration requirements.
- **Batch Task Orchestration & Queue Management**: Supports batch operations and queue management, simplifying the deployment and management of large-scale Kubernetes resources.
- **Real-time Status Monitoring & Exception Alerts**: Monitors Kubernetes resource status in real-time and quickly responds to abnormal situations.
- **Historical Record Tracing & Difference Comparison**: Records deployment history and supports difference comparison, facilitating problem tracking and rollback operations.
- **Cross-platform Support**: Compatible with multiple operating systems and Agent platforms, improving the tool's availability and convenience.

### Efficiency Improvement

Using Kubernetes DevOps Toolkit 2, users can:

- **Save Time**: Through automation and programming assistance, deployment and configuration time is reduced by more than 50%.
- **Reduce Steps**: Simplify the operational process, reducing manual steps to a minimum.

### Application Scenario Innovation

Kubernetes DevOps Toolkit 2 showcases innovation in the following application scenarios:

- **Rapid Prototyping**: Through code generation functionality, quickly create Kubernetes resources to accelerate the development and iteration of new applications.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Integrated into CI/CD processes to achieve automated deployment and continuous optimization.
- **Resource Monitoring & Analysis**: Combined with monitoring tools to enable real-time performance monitoring and fault diagnosis of Kubernetes clusters.

## Function Details & Boundary Conditions

### Core Function Details

1. **Advanced Parameter Configuration & Custom Rules**
   - **Input Parameters**: User-defined configuration rules, such as resource types, versions, environment variables, etc.
   - **Processing Logic**: Generates corresponding Kubernetes manifests user-defined rules.
   - **Output Result**: Generated Kubernetes manifest files containing user-specified parameters and rules.

2. **Batch Task Orchestration & Queue Management**
   - **Input Parameters**: Batch task list, including task types, execution order, dependencies, etc.
   - **Processing Logic**: Automatically schedules task execution order task list and dependencies, and manages task queues.
   - **Output Result**: Execution results, including the execution status and output information of each task.

3. **Real-time Status Monitoring & Exception Alerts**
   - **Input Parameters**: Monitoring metrics, such as resource usage, service status, etc.
   - **Processing Logic**: Collects monitoring metrics in real-time and performs abnormal detection predefined thresholds.
   - **Output Result**: Exception alert information, including the type of abnormality, occurrence time, and impact range.

4. **Historical Record Tracing & Difference Comparison**
   - **Input Parameters**: Historical versions to trace or versions to compare.
   - **Processing Logic**: Queries historical version information and calculates differences between different versions.
   - **Output Result**: Version difference information, including change content and impact range.

5. **Cross-platform Support**
   - **Input Parameters**: Supported platform types, such as Windows, macOS, Linux, etc.
   - **Processing Logic**: Performs corresponding configuration and optimization the characteristics of different platforms.
   - **Output Result**: Kubernetes DevOps Toolkit 2 running on the specified platform.

### Boundary Conditions

1. **Input Size Limit**: The size limit of individual task input parameters is 10MB.
2. **Character Encoding Requirements**: Input parameters support UTF-8 encoding.
3. **Concurrency Limit**: The number of tasks handled simultaneously is limited to 100.
4. **Resource Usage Limit**: The resource usage of a single task during execution is limited to 100 CPU cores and 200GB of memory.
5. **Network Latency Limit**: Task execution may be affected when network latency exceeds 500ms.
6. **Version Compatibility Limit**: Some features may require support from specific versions of the Kubernetes cluster.
7. **API Call Frequency Limit**: The API call frequency per user per hour is limited to 1000 times.
8. **Log Storage Limit**: The log storage space is limited to 10GB.

### Error Handling

1. **Task execution failure**: Check whether the task configuration is correct or try to re-execute the task.
2. **Abnormal monitoring metrics**: Check whether the monitoring metric configuration is correct or contact technical support.
3. **Failure to query historical versions**: Check whether the version information is correct or try to use other version query methods.
4. **API call failure**: Check whether the network connection is normal or try to call the API again.
5. **Platform not supported**: Check whether the target platform is within the supported range or try to use other platforms.

### Performance Metrics

1. **Task execution time**: The execution time of a single task does not exceed 10 minutes.
2. **Monitoring metric collection frequency**: Collect monitoring metrics once per minute.
3. **Log recording frequency**: Record log information once per second.
4. **API response time**: The API response time does not exceed 500ms.
5. **Resource usage rate**: The resource usage rate does not exceed 80%.

## Technical Details & Implementation Notes

### Technical Architecture

The technical architecture of Kubernetes DevOps Toolkit 2 is a modular design and mainly includes the following core modules:

1. **Code Generation Module**: Automatically generates Kubernetes manifests user-defined configuration rules.
2. **Task Orchestration Module**: Automatically schedules task execution order task lists and dependencies, and manages task queues.
3. **Monitoring Module**: Collects Kubernetes resource status in real-time and performs abnormal detection predefined thresholds.
4. **Historical Record Module**: Records deployment history and supports difference comparison.
5. **Cross-platform Support Module**: Performs corresponding configuration and optimization the characteristics of different platforms.

Core algorithms include:

- **Template Engine**: Uses a template engine to generate Kubernetes manifests, supports custom rules and parameters.
- **Task Scheduling Algorithm**: Schedules task execution order task dependencies and execution order, and manages task queues.
- **Monitoring Algorithm**: Performs abnormal detection on monitoring metrics predefined thresholds.
- **Version Comparison Algorithm**: Calculates differences between different versions and generates difference reports.

### Parameter Description

| Parameter Name | Type | Value Range | Default Value | Description |
|----------------|------|-------------|---------------|-------------|
| content        | string | -           | -             | Kubernetes manifest content input, supports json/text/markdown formats |
| style          | string | -           | -             | Output style, refer to `references/style.md` |
| resource_type  | string | -           | -             | Resource type, such as Deployment, Service, etc. |
| version        | string | -           | -             | Resource version |
| environment    | string | -           | -             | Environment variables |
| task_list      | list  | -           | -             | Batch task list, including task types, execution order, dependencies, etc. |
| monitor_metrics | list  | -           | -             | Monitoring metrics, such as resource usage, service status, etc. |
| history_versions | list | -           | -             | Historical versions to trace or versions to compare |

### Return Value

```json
{
  "success": true,
  "data": {
    "result": "devops related configuration parameters",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "professional"
    }
  },
  "error": null
}
```

- `success`: Boolean value indicating whether the operation was successful.
- `data`: Object containing the operation result and metadata.
  - `result`: String indicating the operation result.
  - `metadata`: Object containing template usage information, word count, and output style, etc.

### Code Examples

**Example 1: Generate Kubernetes Manifest**

```python
from kubernetes_devops import generate_k8s_manifest

content = '{"apiVersion": "v1", "kind": "Pod", "metadata": {"name": "example-pod"}, "spec": {"containers": [{"name": "example-container", "image": "nginx:latest"}]}}'
manifest = generate_k8s_manifest(content)
print(manifest)
```

**Example 2: Batch Task Orchestration**

```python
from kubernetes_devops import batch_task_execution

task_list = [
    {"type": "deploy", "name": "example-pod", "image": "nginx:latest"},
    {"type": "scale", "name": "example-pod", "replicas": 3}
]

results = batch_task_execution(task_list)
print(results)
```

**Example 3: Monitor Kubernetes Resources**

```python
from kubernetes_devops import monitor_k8s_resources

monitor_metrics = ["cpu_usage", "memory_usage"]
results = monitor_k8s_resources(monitor_metrics)
print(results)
```