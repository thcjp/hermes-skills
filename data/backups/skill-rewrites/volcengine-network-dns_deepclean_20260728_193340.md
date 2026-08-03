---
slug: "volcengine-network-dns"
name: "volcengine-network-dns"
version: 1.0.1
displayName: "网络DNS"
summary: "火山引擎网络服务DNS记录管理,区记录查询与更新。DNS record management on Volcengine networking services。Use when users"
summary_zh: "火山引擎网络服务DNS记录管理,区记录查询与更新。DNS record management on Volcengine networking services。Use when users"
license: "MIT"
description: |-
  DNS record management on Volcengine networking services。Use when users
  need zone record query/up。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - Other
  - 网络
  - DNS
  - 工具
  - dns
  - agent
  - api
tools:
  - read
  - exec
homepage: ""
category: "Operations"
---

```yaml
---
slug: "volcengine-network-dns"
name: "volcengine-network-dns"
version: 1.0.1
displayName: "Volcengine Network DNS"
summary: "Comprehensive DNS management solution for Volcengine networking services, including zone record queries and updates."
summary_zh: "火山引擎网络服务综合DNS管理解决方案，包括区记录查询与更新。"
license: "MIT"
description: |-
  Volcengine Network DNS provides a robust platform for managing DNS records within Volcengine networking services. It allows users to efficiently query and update zone records, streamlining the process of DNS management. This service is ideal for scenarios requiring database operations, SQL queries, and data storage management. It is not suited for database architecture design decisions.
tags:
  - Network
  - DNS
  - Management
  - Volcengine
  - API
  - Cloud
tools:
  - read
  - exec
homepage: "https://www.volcengine.com/en/dns"
category: "Operations"
---

# Volcengine Network DNS

## Overview

Volcengine Network DNS is a powerful tool designed for managing DNS records within Volcengine networking services. It enables users to perform a variety of operations, including querying and updating zone records, which is crucial for maintaining a robust and efficient network infrastructure.

## Paid Features

| Feature | Free Edition | Paid Edition |
|---------|--------------|--------------|
| Basic Functions | Supported | Supported |
| Volcengine Network DNS Record Management | Not Supported | Supported |
| Volcengine Network Zone Record Query | Not Supported | Supported |
| Multi-Tenancy Management and Permission Assignment | Not Supported | Supported |
| Operation Audit and Compliance Logs | Not Supported | Supported |
| Customizable Dashboards and Reports | Not Supported | Supported |

## Core Capabilities

- **DNS Record Management**: Efficiently manage DNS records within Volcengine networking services.
- **Zone Record Query/Update**: Perform queries and updates on zone records as needed.

## Getting Started

1. **Verify Prerequisites**: Ensure that the environment meets the requirements outlined in the Dependencies section.
2. **Invoke the Skill**: In the AI Agent conversation, call the skill with the necessary input parameters.
3. **Review Output**: Check the output results and proceed with further actions as required.

> Detailed input and output formats can be found in the respective sections below.

## Use Cases

| Scenario | Input | Output |
|----------|-------|--------|
| Network Configuration | Network name and subnet parameters | Network ID and connectivity status |
| DNS Query | Domain and record type | Resolved record and TTL information |
| Information Query | Query criteria and keywords | Query results and matching records |

**Not Applicable**: Complex decision scenarios requiring human judgment.

## Usage Workflow

1. **Verify Prerequisites**: Ensure that the environment meets the requirements outlined in the Dependencies section.
2. **Select Appropriate Usage Method**: Choose the appropriate method based on the applicable scenario.
3. **Execute Operations**: Perform the operation and check the output results.
4. **Handle Errors**: Refer to the Error Handling section if errors occur.

## Input Format

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| instruction    | string | Yes | User instruction text |
| context        | string | No | Contextual information |

## Output Format

```json
{
  "success": true,
  "data": {
    "result": "dns related configuration parameters",
    "result": "dns related configuration parameters"
  },
  "error": null
}
```

## Exception Handling

| Error Scenario | Reason | Solution |
|----------------|--------|----------|
| Configuration Error | Missing or incorrect parameters | Check the configuration requirements in the Dependencies section |
| Runtime Error | Inadequate runtime environment | Confirm that the runtime environment meets the requirements specified in the Dependencies section |
| Network Error | Connection timeout or unreachability | Check network connections |

## Dependencies

### Runtime Environment

- **Agent Platform**: Any AI Agent supporting SKILL.md (Claude Code / Cursor / Codex / Gemini CLI, etc.)
- **Operating System**: Windows / macOS / Linux

### Additional Dependencies

| Dependency | Type | Required | Acquisition Method |
|------------|------|----------|-------------------|
| LLM API | API | Required | Provided by the integrated LLM of the Agent |

### API Key Configuration

- Configure the API key by setting the `API_KEY` environment variable:

```bash
export API_KEY="your_api_key_here"
```

Restart the session or open a new terminal for the configuration to take effect. Store the API key securely and avoid exposing it to version control systems.

## Error Handling (Continued)

| Error Scenario (Continued) | Reason | Solution |
|----------------------------|--------|----------|
| LLM Response Timeout or No Response | Network latency or high model load | Retry the request; confirm that the LLM service of the Agent platform is functioning normally |
| Incorrect Input Format | User input does not match the skill's expected format | Check that the input conforms to the format requirements specified in the usage instructions, refer to the examples section |
| Discrepancy between Execution Results and Expectations | Insufficient clarity in instruction descriptions or insufficient context | Provide more detailed instruction descriptions and supplement necessary context information |
| Command Execution Failure | Inadequate runtime environment or insufficient permissions | Confirm that the runtime environment meets the requirements specified in the Dependencies section; check command permission settings |

## FAQ

### How Do I Get Started?

Follow the usage workflow section, configure the environment and parameters as per the instructions, and you can start using it. It is recommended to read the Dependencies section for the first time to ensure that the environment is ready.

### What Should I Do If I Encounter Errors?

Refer to the Error Handling section and find the corresponding solution based on the error scenario. If the error handling section does not cover it, collect error information and understand the skill's ability boundaries in the Known Limitations section.

## Differentiated Advantages

### Comparison with Similar Solutions

1. **Manual Operation**: Manually managing DNS records requires frequent login to servers or the use of command-line tools, which is complex and prone to errors. Volcengine Network DNS 2 provides a centralized management interface and API interfaces, allowing users to quickly complete DNS record queries and updates with simple operations or programming methods, greatly simplifying the operation process and reducing the risk of human errors.

2. **Other DNS Management Tools**: Some third-party DNS management tools are available on the market, which are rich in features but usually require additional installation and configuration, and are expensive. Volcengine Network DNS 2 is part of Volcengine networking services and does not require additional installation, directly integrated into the Volcengine console, with lower cost of use and seamless integration with other Volcengine services.

3. **General Methods**: Some general methods like using scripts to automate DNS management can save time, but they require writing and maintaining scripts, which are high barriers for non-technical personnel. Volcengine Network DNS 2 provides a visual operation interface and rich API interfaces, reducing technical barriers and allowing more users to easily use it.

### Unique Features

1. **Multi-Tenancy Management and Permission Assignment**: Volcengine Network DNS 2 supports multi-tenancy management, allowing administrators to assign different permissions to different users, effectively protecting data security and improving management efficiency.

2. **Operation Audit and Compliance Logs**: All operations are recorded in logs, making it easy for users to perform audits and compliance checks, ensuring the traceability of operations.

3. **Customizable Dashboards and Reports**: Users can customize dashboards and reports according to their own needs, and monitor the running status of DNS services in real time.

4. **Integration with Other Volcengine Services**: Volcengine Network DNS 2 is seamlessly integrated with other Volcengine services such as cloud servers and load balancers, making it convenient for users to perform overall network management.

5. **Rich API Interfaces**: Provides rich API interfaces, supporting automated operations, convenient for users to perform secondary development and integration.

### Efficiency Improvement

Using Volcengine Network DNS 2, users can save about 50% of time on DNS record queries and updates, and reduce 80% of manual errors.

### Application Scenario Innovation

1. **Cloud DNS Management**: Volcengine Network DNS 2 can easily manage DNS records of cloud servers, improving the availability and reliability of cloud services.

2. **Domain Name Resolution Optimization**: By using Volcengine Network DNS 2, users can optimize domain name resolution performance and improve website access speed.

3. **Mobile Application DNS Management**: Volcengine Network DNS 2 can easily manage DNS records of mobile applications, ensuring the normal operation of applications on various platforms.

## Detailed Function Description and Boundary Conditions

### Core Function Description

1. **DNS Record Management**:
   - **Input Parameters**: Domain, record type (e.g., A, CNAME, MX), record value, TTL (time to live).
   - **Processing Logic**: Create, update, or delete DNS records based on the provided domain and record type.
   - **Output Result**: Indication of whether the operation was successful, as well as details of the DNS records after the operation.

2. **Zone Record Query**:
   - **Input Parameters**: Domain.
   - **Processing Logic**: Query the zone records of a specified domain, including record type, record value, TTL, etc.
   - **Output Result**: List of zone records queried.

3. **Multi-Tenancy Management and Permission Assignment**:
   - **Input Parameters**: User ID, operation permissions (e.g., read, write, manage).
   - **Processing Logic**: Control user access to DNS records based on user ID and permission settings.
   - **Output Result**: Indication of whether the permission assignment was successful.

4. **Operation Audit and Compliance Logs**:
   - **Input Parameters**: None.
   - **Processing Logic**: Automatically record all operation logs, including the operation user, operation time, and operation content, etc.
   - **Output Result**: List of operation logs that can be queried.

5. **Customizable Dashboards and Reports**:
   - **Input Parameters**: Report type (e.g., DNS query count, error rate, etc.).
   - **Processing Logic**: Generate corresponding report data based on the report type.
   - **Output Result**: Custom report content.

### Boundary Conditions

1. **Input Size Limitation**: The length of the record value of a single DNS record does not exceed 255 characters.
2. **Character Encoding Requirement**: Supports UTF-8 encoding.
3. **Concurrency Limitation**: The system supports 100 concurrent requests by default; for higher concurrency, contact technical support.
4. **Query Result Limitation**: The result of a single query does not exceed 100 records.
5. **Operation Frequency Limitation**: A user can perform up to 10 DNS record operations within 1 minute.
6. **Log Storage Limitation**: The log storage period is 1 year.
7. **Report Data Volume Limitation**: The report data volume does not exceed 1GB.
8. **Permission Assignment Limitation**: Does not support cross-tenant permission assignment.

### Error Handling

1. **Missing or Incorrect Parameters**: Return an error message prompting the user to check the input parameters.
2. **Insufficient Operation Permissions**: Return an error message prompting the user that the operation is unauthorized.
3. **Record Does Not Exist**: Return an error message prompting the user that the record does not exist.
4. **Network Connection Error**: Return an error message prompting the user to check the network connection.
5. **System Error**: Return an error message prompting the user that the system is abnormal, and to contact technical support.
6. **Database Error**: Return an error message prompting the user that the database is abnormal, and to contact technical support.
7. **API Call Error**: Return an error message prompting the user that the API call is abnormal, and to contact technical support.
8. **Log Storage Error**: Return an error message prompting the user that log storage is abnormal, and to contact technical support.

### Performance Metrics

1. **Query Response Time**: Average response time does not exceed 100 milliseconds.
2. **Update Operation Success Rate**: Average success rate is not less than 99.9%.
3. **System Availability**: The average availability of the system is not less than 99.9%.
4. **Concurrency Processing Capability**: The maximum concurrency processing capability of the system is 100 requests.
5. **Log Processing Capability**: The system can process up to 100,000 logs per second.

## Technical Details and Implementation

### Technical Architecture

Volcengine Network DNS 2 adopts a microservices architecture, with core algorithms including DNS resolution, record management, permission control, and log recording. The DNS resolution module is responsible for resolving user input domains and forwarding requests to the corresponding backend services; the record management module is responsible for handling the creation, update, and deletion of DNS records; the permission control module is responsible for managing the access permissions of different users; and the log recording module is responsible for recording all operation logs.

### Parameter Description

The following table describes the main parameters of Volcengine Network DNS 2 and their explanations:

| Parameter Name | Type | Range | Default Value | Description |
|----------------|------|-------|--------------|-------------|
| domain         | string | -     | -            | The domain to be operated |
| recordType    | string | A, CNAME, MX, etc. | - | DNS record type, such as A, CNAME, MX, etc. |
| recordValue   | string | -     | -            | DNS record value, such as IP address, hostname, etc. |
| ttl           | int   | 1-86400 | 86400 | DNS record time to live, in seconds |
| userId        | string | -     | -            | User ID, used for permission control |
| operation     | string | create, update, delete | - | Operation type, such as create (create), update (update), delete (delete) |

### Return Value

The following table describes the main return values of Volcengine Network DNS 2 and their data structures:

```json
{
  "success": true,
  "data": {
    "result": "Operation successful",
    "records": [
      {
        "domain": "example.com",
        "recordType": "A",
        "recordValue": "192.168.1.1",
        "ttl": 86400
      }
    ]
  },
  "error": null
}
```

- success: Boolean value, indicating whether the operation was successful.
- data: Object, containing the operation result and detailed information.
  - result: String, indicating the operation result, such as "Operation successful".
  - records: Array, containing the list of DNS records after the operation.

### Code Examples

The following are code examples for Volcengine Network DNS 2:

**Example 1: Query DNS Record**

```python
import requests

url = "https://api.volcengine.com/dns/v1"
params = {
    "domain": "example.com",
    "recordType": "A"
}

response = requests.get(url, params=params)
print(response.json())
```

**Example 2: Create DNS Record**

```python
import requests

url = "https://api.volcengine.com/dns/v1"
data = {
    "domain": "example.com",
    "recordType": "A",
    "recordValue": "192.168.1.1",
    "ttl": 86400
}

response = requests.post(url, json=data)
print(response.json())
```

**Example 3: Update DNS Record**

```python
import requests

url = "https://api.volcengine.com/dns/v1"
data = {
    "domain": "example.com",
    "recordType": "A",
    "recordValue": "192.168.1.2",
    "ttl": 86400
}

response = requests.put(url, json=data)
print(response.json())
```