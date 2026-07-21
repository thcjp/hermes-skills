# 详细参考 - whatsapp-msg-manager-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import json
import subprocess
import time

class WhatsAppBatchSender:
    """WhatsApp批量消息发送器"""

    def __init__(self, phone_number_id: str, rate_limit: float = 0.5):
        self.phone_number_id = phone_number_id
        self.rate_limit = rate_limit  # 每条消息间隔(秒)
        self.results = {"success": [], "failed": []}

    def send_batch(self, recipients: list, message_template: str):
        """批量发送消息

        Args:
            recipients: 收件人列表 [{"phone": "+86...", "vars": {"name": "张三"}}]
            message_template: 消息模板,使用 {name} 等占位符
        """
        total = len(recipients)
        for i, recipient in enumerate(recipients, 1):
            phone = recipient["phone"]
            message = message_template.format(**recipient.get("vars", {}))

            params = json.dumps({
                "phone_number_id": self.phone_number_id,
                "recipient_phone": phone,
                "message": message
            })

            try:
                result = subprocess.run(
                    ["connector_call_tool",
                     "--tool", "whatsapp_send_message",
                     "--params", params],
                    capture_output=True, text=True, timeout=30
                )

                if result.returncode == 0:
                    self.results["success"].append({"phone": phone, "index": i})
                    print(f"[{i}/{total}] 发送成功: {phone}")
                else:
                    self.results["failed"].append({
                        "phone": phone, "index": i,
                        "error": result.stderr
                    })
                    print(f"[{i}/{total}] 发送失败: {phone} - {result.stderr}")

            except Exception as e:
                self.results["failed"].append({
                    "phone": phone, "index": i, "error": str(e)
                })
                print(f"[{i}/{total}] 异常: {phone} - {e}")

            time.sleep(self.rate_limit)

        self._print_summary(total)
        return self.results

    def _print_summary(self, total: int):
        """打印批量发送摘要"""
        success_count = len(self.results["success"])
        failed_count = len(self.results["failed"])
        print(f"\n{'='*50}")
        print(f"批量发送完成: 共 {total} 条")
        print(f"  成功: {success_count} ({success_count/total*100:.1f}%)")
        print(f"  失败: {failed_count} ({failed_count/total*100:.1f}%)")
        print(f"{'='*50}")

if __name__ == "__main__":
    sender = WhatsAppBatchSender(phone_number_id="1029384756", rate_limit=0.5)

    recipients = [
        {"phone": "+8613800138000", "vars": {"name": "张三", "order": "001"}},
        {"phone": "+8613900139000", "vars": {"name": "李四", "order": "002"}},
        {"phone": "+8613700137000", "vars": {"name": "王五", "order": "003"}},
    ]

    template = "您好 {name},您的订单 #{order} 已确认,请留意后续通知。"

    sender.send_batch(recipients, template)
```

## 代码示例 (bash)

```bash
connector_call_tool --tool "whatsapp_create_message_template" --params '{
  "name": "order_shipped_notification",
  "language": "zh_CN",
  "category": "UTILITY",
  "components": [
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "订单发货通知"
    },
    {
      "type": "BODY",
      "text": "您好 {{1}},您的订单 {{2}} 已发货,物流单号:{{3}},预计 {{4}} 送达。"
    },
    {
      "type": "FOOTER",
      "text": "回复 STOP 取消订阅"
    }
  ]
}'

connector_call_tool --tool "whatsapp_send_template_message" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "template_name": "order_shipped_notification",
  "language_code": "zh_CN",
  "components": [
    {
      "type": "body",
      "parameters": [
        {"type": "text", "text": "李四"},
        {"type": "text", "text": "#20260718-001"},
        {"type": "text", "text": "SF1234567890"},
        {"type": "text", "text": "2-3个工作日"}
      ]
    }
  ]
}'

connector_call_tool --tool "whatsapp_delete_message_template" --params '{
  "template_name": "old_promo_template"
}'
```

## 代码示例 (bash)

```bash
connector_call_tool --tool "whatsapp_send_interactive_buttons" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "header": "订单确认",
  "body": "您的订单 #20260718-001 总计 299.00 元,请确认是否继续。",
  "buttons": [
    {"id": "confirm", "title": "确认下单"},
    {"id": "modify", "title": "修改订单"},
    {"id": "cancel", "title": "取消订单"}
  ]
}'

connector_call_tool --tool "whatsapp_send_interactive_list" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "header": "选择配送时间",
  "body": "请选择您方便的配送时间段:",
  "button_text": "查看时间段",
  "sections": [
    {
      "title": "工作日",
      "rows": [
        {"id": "wd-am", "title": "周一至周五 上午", "description": "9:00-12:00"},
        {"id": "wd-pm", "title": "周一至周五 下午", "description": "14:00-18:00"}
      ]
    },
    {
      "title": "周末",
      "rows": [
        {"id": "we-am", "title": "周六 上午", "description": "9:00-12:00"},
        {"id": "we-pm", "title": "周六 下午", "description": "14:00-18:00"}
      ]
    }
  ]
}'
```

## 代码示例 (yaml)

```yaml
whatsapp:
  accounts:
    - id: "1029384756"
      name: "客服主号"
      role: "customer_service"
      default: true
    - id: "1029384757"
      name: "营销号"
      role: "marketing"

  batch:
    rate_limit_seconds: 0.5        # 每条消息间隔
    max_batch_size: 1000           # 单批次最大数量
    retry_failed: true             # 自动重试失败消息
    retry_max_attempts: 3          # 最大重试次数
  templates:
    auto_check_status: true        # 发送前自动检查模板审批状态
    cache_duration_minutes: 30     # 模板状态缓存时长
  media:
    cache_media_id: true           # 缓存media_id避免重复上传
    cache_max_size_mb: 500         # 媒体缓存上限
    allowed_types:
      - "image/jpeg"
      - "image/png"
      - "video/mp4"
      - "application/pdf"

  security:
    confirm_before_send: true
    log_all_operations: true       # 记录所有操作日志
    audit_log_path: "./logs/whatsapp-audit.log"
```

## 代码示例 (bash)

```bash
connector_call_tool --tool "whatsapp_send_interactive_buttons" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "header": "订单确认",
  "body": "订单 #20260718-001\n商品:无线蓝牙耳机 x1\n金额:299.00 元\n\n请确认您的订单:",
  "buttons": [
    {"id": "confirm", "title": "确认订单"},
    {"id": "cancel", "title": "取消订单"}
  ]
}'

connector_call_tool --tool "whatsapp_send_media" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "media_url": "https://example.com/shipping-label.png",
  "caption": "订单已发货!物流单号:SF1234567890"
}'

connector_call_tool --tool "whatsapp_send_template_message" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "template_name": "delivery_confirmation",
  "language_code": "zh_CN",
  "components": [
    {"type": "body", "parameters": [{"type": "text", "text": "张三"}]}
  ]
}'
```

## 代码示例 (python)

```python
class TemplateManager:
    """消息模板管理器"""

    CATEGORY_UTILITY = "UTILITY"
    CATEGORY_MARKETING = "MARKETING"

    NAMING_PATTERN = "{domain}_{action}_{lang}"

    @staticmethod
    def generate_template_name(domain: str, action: str, lang: str = "zh"):
        """生成规范的模板名称"""
        return TemplateManager.NAMING_PATTERN.format(
            domain=domain, action=action, lang=lang
        )

    @staticmethod
    def validate_template_body(text: str) -> dict:
        """校验模板内容"""
        issues = []
        import re
        placeholders = re.findall(r'\{\{(\d+)\}\}', text)
        if len(placeholders) > 10:
            issues.append("变量占位符超过10个上限")
        if len(text) > 1024:
            issues.append("模板正文超过1024字符上限")
        return {"valid": len(issues) == 0, "issues": issues}
```

