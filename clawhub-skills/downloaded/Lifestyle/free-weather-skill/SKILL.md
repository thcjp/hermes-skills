---
slug: free-weather-skill
name: free-weather-skill
version: "0.1.0"
displayName: Weather
summary: "免API Key获取实时天气与预报,解决出行前需快速了解天气状况的需求"
license: MIT-0
description: |-
  Get current weather and forecasts (no API key required)。核心能力:

  - 生活工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 个人健康、生活管理、习惯养成

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Lifestyle
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Weather

Welcome to the Weather skill, your go-to solution for quick and easy access to current weather conditions and forecasts without the need for an API key. This skill leverages the power of wttr.in and Open-Meteo APIs to provide you with accurate and comprehensive weather information.

## Quick Overview

- **No API Key Required**: Access weather data without any additional setup.
- **Multiple Formats**: Choose from various formats to suit your needs.
- **Flexible Units**: Convert temperature and wind speed units as desired.
- **Programmable**: Use the skill programmatically for automation and integration.

## Core Features

- **Current Weather**: Get the latest weather conditions for any location.
- **Forecast**: View short-term and long-term weather forecasts.
- **Custom Formats**: Select from different output formats for compact or detailed information.
- **Unit Conversion**: Convert temperature and wind speed units to metric or imperial systems.

## Getting Started

### Prerequisites

- **Agent Platform**: Any AI Agent that supports SKILL.md (e.g., Claude Code, Cursor, Codex, Gemini CLI).
- **Operating System**: Windows, macOS, or Linux.
- **Network Connection**: Stable internet connection to access external APIs.

### Installation

- No installation required. Simply add the skill to your Agent platform.

### Configuration

- No additional configuration is needed. The skill is ready to use out of the box.

## Usage Guide

### Basic Usage

To get the current weather for a location, use the following command:

```bash
curl -s "wttr.in/London?format=3"
```

For a compact format, use:

```bash
curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
```

To view the full forecast, use:

```bash
curl -s "wttr.in/London?T"
```

### Advanced Usage

- **URL Encoding**: Use URL encoding for spaces and special characters.
- **Airport Codes**: Use airport codes instead of city names for more specific data.
- **Units**: Add `?m` for metric units or `?u` for USCS units.
- **Today Only**: Use `?1` for today's weather only or `?0` for current weather only.
- **PNG**: Convert weather data to a PNG image with `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png`.

## Examples

### Example 1: Get Current Weather

```bash
Input: curl -s "wttr.in/New+York?format=3"
Output: New York, 18°C, partly cloudy, 70% humidity, 10 m/s wind
```

### Example 2: Get Forecast

```bash
Input: curl -s "wttr.in/New+York?T"
Output: 3-day forecast for New York
```

## Error Handling

If you encounter any errors while using the skill, refer to the following table for troubleshooting steps:

| Error Scenario | Reason | Solution |
|----------------|--------|----------|
| Configuration Error | Missing or incorrect parameters | Check the usage guide for correct parameters |
| Runtime Error | Incompatible environment | Ensure your environment meets the prerequisites |
| Network Error | Connection timeout or unreachable | Check your network connection and try again |

## Security Considerations

- The skill does not store or collect any personal information.
- All data is retrieved from external APIs and is not stored locally.
- The skill does not make any unauthorized external calls.

## Known Limitations

- **API Key Requirement**: While the skill description mentions no API key is required, some APIs may still require one for access to all features.
- **Data Coverage**: Free APIs may not cover all regions, especially remote areas.
- **Feature Limitations**: Free APIs may not support all advanced features, such as historical weather data or specific meteorological parameters.

## FAQs

### Q1: How do I start using the Weather skill?
A: Read the usage guide to ensure your environment meets the prerequisites and follow the installation instructions.

### Q2: What should I do if I encounter an error?
A: Refer to the error handling section for troubleshooting steps.

### Q3: What are the limitations of the Weather skill?
A: The skill has limitations related to API key requirements, data coverage, and feature support. Refer to the known limitations section for more information.

## Conclusion

The Weather skill is a powerful tool for anyone who needs quick and easy access to weather information. With its comprehensive features and user-friendly interface, it's the perfect solution for personal and professional use.