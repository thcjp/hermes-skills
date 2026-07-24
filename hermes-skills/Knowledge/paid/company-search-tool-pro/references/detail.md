# 详细参考 - company-search-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import json
from concurrent.futures import ThreadPoolExecutor

class DueDiligenceReport:
    """企业尽调报告生成器（专业版）"""

    def __init__(self):
        self.searcher = CompanySearcher()
        self.dimensions = [
            ("基本信息", "biz_basic_info"),
            ("股东信息", "biz_shareholders"),
            ("主要人员", "biz_key_personnel"),
            ("对外投资", "biz_investments"),
            ("工商变更", "biz_changes"),
            ("被执行人", "biz_executed_person"),
            ("失信被执行", "biz_dishonest"),
            ("限制高消费", "biz_restricted_high_consumption"),
            ("经营异常", "biz_business_anomaly"),
            ("严重违法", "biz_serious_violation"),
            ("行政处罚", "biz_administrative_penalty"),
        ]

    def generate_report(self, company_name, dimensions=None):
        """生成企业尽调报告"""
        entid = self._get_entid(company_name)
        if not entid:
            return {"error": f"未找到企业：{company_name}"}

        target_dims = dimensions or self.dimensions
        results = {}

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {
                executor.submit(self._query_dimension, name, tool, entid): name
                for name, tool in target_dims
            }
            for future in futures:
                name = futures[future]
                try:
                    results[name] = future.result()
                except Exception as e:
                    results[name] = {"error": str(e)}

        return self._format_report(company_name, results)

    def _get_entid(self, company_name):
        """获取entid"""
        result = self.searcher.fuzzy_search(company_name)
        if isinstance(result, dict) and "data" in result:
            companies = result["data"]
            if companies:
                return companies[0].get("entid")
        return None

    def _query_dimension(self, name, tool, entid):
        """查询单个维度"""
        return self.searcher.call_tool(tool, {"entid": entid})

    def _format_report(self, company_name, results):
        """格式化报告"""
        lines = []
        lines.append("=" * 60)
        lines.append(f"  企业尽调报告：{company_name}")
        lines.append("=" * 60)
        lines.append("")

        basic = results.get("基本信息", {})
        if isinstance(basic, dict):
            data = basic.get("data", {})
            lines.append("【基本信息】")
            lines.append(f"  企业名称：{data.get('name', '未知')}")
            lines.append(f"  法定代表人：{data.get('legal_person', '未知')}")
            lines.append(f"  注册资本：{data.get('registered_capital', '未知')}")
            lines.append(f"  成立日期：{data.get('establish_date', '未知')}")
            lines.append(f"  统一社会信用代码：{data.get('credit_code', '未知')}")
            lines.append("")

        risk_items = ["被执行人", "失信被执行", "限制高消费",
                     "经营异常", "严重违法", "行政处罚"]
        lines.append("【风险评估】")
        risk_count = 0
        for item in risk_items:
            data = results.get(item, {})
            if isinstance(data, dict) and data.get("data"):
                risk_count += len(data["data"])
                lines.append(f"  {item}：{len(data['data'])}条记录")
        if risk_count == 0:
            lines.append("  未发现风险记录")
        else:
            lines.append(f"  共发现 {risk_count} 条风险记录")
        lines.append("")

        lines.append("【股东与投资】")
        shareholders = results.get("股东信息", {})
        if isinstance(shareholders, dict) and shareholders.get("data"):
            lines.append(f"  股东数量：{len(shareholders['data'])}")
        investments = results.get("对外投资", {})
        if isinstance(investments, dict) and investments.get("data"):
            lines.append(f"  对外投资：{len(investments['data'])}家")
        lines.append("")

        lines.append("=" * 60)
        return "\n".join(lines)

dd = DueDiligenceReport()
report = dd.generate_report("腾讯")
print(report)
```

## 代码示例 (python)

```python
class RiskScreener:
    """风险筛查器（专业版）"""

    RISK_DIMENSIONS = {
        "被执行人": "biz_executed_person",
        "失信被执行": "biz_dishonest",
        "限制高消费": "biz_restricted_high_consumption",
        "经营异常": "biz_business_anomaly",
        "严重违法": "biz_serious_violation",
        "行政处罚": "biz_administrative_penalty",
    }

    RISK_SEVERITY = {
        "被执行人": "高",
        "失信被执行": "高",
        "限制高消费": "高",
        "经营异常": "中",
        "严重违法": "高",
        "行政处罚": "中",
    }

    def __init__(self):
        self.searcher = CompanySearcher()

    def screen(self, company_name):
        """风险筛查"""
        entid = self._get_entid(company_name)
        if not entid:
            return {"error": "未找到企业"}

        risk_report = {
            "company": company_name,
            "total_risks": 0,
            "high_risk": 0,
            "medium_risk": 0,
            "details": {}
        }

        for risk_name, tool in self.RISK_DIMENSIONS.items():
            result = self.searcher.call_tool(tool, {"entid": entid})
            if isinstance(result, dict) and result.get("data"):
                records = result["data"]
                risk_report["details"][risk_name] = {
                    "count": len(records),
                    "severity": self.RISK_SEVERITY[risk_name],
                    "records": records[:5]  # 仅保留前5条
                }
                risk_report["total_risks"] += len(records)
                if self.RISK_SEVERITY[risk_name] == "高":
                    risk_report["high_risk"] += len(records)
                else:
                    risk_report["medium_risk"] += len(records)

        return risk_report

    def generate_risk_alert(self, risk_report):
        """生成风险告警"""
        if risk_report["total_risks"] == 0:
            return f"企业 {risk_report['company']} 风险筛查通过，未发现风险记录"

        alert = f"风险告警：企业 {risk_report['company']} 发现 {risk_report['total_risks']} 条风险记录\n"
        alert += f"高风险：{risk_report['high_risk']}条\n"
        alert += f"中风险：{risk_report['medium_risk']}条\n"
        alert += "\n详情：\n"
        for risk, detail in risk_report["details"].items():
            alert += f"  [{detail['severity']}风险] {risk}：{detail['count']}条\n"
        return alert

    def _get_entid(self, company_name):
        result = self.searcher.fuzzy_search(company_name)
        if isinstance(result, dict) and "data" in result:
            companies = result["data"]
            if companies:
                return companies[0].get("entid")
        return None

screener = RiskScreener()
risk_report = screener.screen("某公司")
print(screener.generate_risk_alert(risk_report))
```

## 代码示例 (python)

```python
import concurrent.futures
import threading

class BatchCompanySearcher:
    """批量企业查询器（专业版）"""

    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.lock = threading.Lock()
        self.results = {}
        self.stats = {"success": 0, "failed": 0, "total": 0}

    def search_batch(self, company_names, dimension="基本信息"):
        """批量查询多家企业"""
        print(f"启动批量查询，共 {len(company_names)} 家企业，并发数 {self.max_workers}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._search_single, name, dimension): name
                for name in company_names
            }
            for future in concurrent.futures.as_completed(futures):
                name = futures[future]
                try:
                    result = future.result()
                    with self.lock:
                        self.results[name] = result
                        self.stats["total"] += 1
                        if result.get("success"):
                            self.stats["success"] += 1
                        else:
                            self.stats["failed"] += 1
                except Exception as e:
                    with self.lock:
                        self.results[name] = {"error": str(e)}
                        self.stats["failed"] += 1

        self._print_summary()
        return self.results

    def _search_single(self, company_name, dimension):
        """查询单个企业"""
        query = CompanyInfoQuery()
        try:
            if dimension == "基本信息":
                result = query.get_basic_info(company_name)
            elif dimension == "股东信息":
                result = query.get_shareholders(company_name)
            elif dimension == "对外投资":
                result = query.get_investments(company_name)
            else:
                result = query.get_basic_info(company_name)

            return {"success": True, "data": result}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _print_summary(self):
        print("\n=== 批量查询摘要 ===")
        print(f"总数：{self.stats['total']}")
        print(f"成功：{self.stats['success']}")
        print(f"失败：{self.stats['failed']}")

    def export_results(self, filename="batch_results.json"):
        """导出结果"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"结果已导出：{filename}")

batch = BatchCompanySearcher(max_workers=5)
companies = ["腾讯", "阿里巴巴", "字节跳动", "百度", "京东"]
results = batch.search_batch(companies, "基本信息")
batch.export_results()
```

## 代码示例 (python)

```python
class RelationshipAnalyzer:
    """关联关系分析器（专业版）"""

    def __init__(self):
        self.searcher = CompanySearcher()
        self.visited = set()

    def find_shareholder_companies(self, company_name, depth=2):
        """查找股东关联企业"""
        if depth <= 0 or company_name in self.visited:
            return {}
        self.visited.add(company_name)

        entid = self._get_entid(company_name)
        if not entid:
            return {}

        result = self.searcher.call_tool("biz_shareholders", {"entid": entid})
        if not isinstance(result, dict) or not result.get("data"):
            return {}

        relationships = {"company": company_name, "shareholders": []}
        for sh in result["data"][:5]:  # 限制深度避免爆炸
            sh_name = sh.get("name", "")
            if sh_name and sh_name not in self.visited:
                if self._is_company(sh_name):
                    sub = self.find_shareholder_companies(sh_name, depth - 1)
                    relationships["shareholders"].append(sub)
                else:
                    relationships["shareholders"].append({"name": sh_name})

        return relationships

    def find_investment_network(self, company_name, depth=2):
        """查找投资关联网络"""
        if depth <= 0 or company_name in self.visited:
            return {}
        self.visited.add(company_name)

        entid = self._get_entid(company_name)
        if not entid:
            return {}

        result = self.searcher.call_tool("biz_investments", {"entid": entid})
        if not isinstance(result, dict) or not result.get("data"):
            return {}

        network = {"company": company_name, "investments": []}
        for inv in result["data"][:5]:
            inv_name = inv.get("name", "")
            if inv_name and inv_name not in self.visited:
                sub = self.find_investment_network(inv_name, depth - 1)
                network["investments"].append(sub)
        return network

    def _get_entid(self, company_name):
        result = self.searcher.fuzzy_search(company_name)
        if isinstance(result, dict) and "data" in result:
            companies = result["data"]
            if companies:
                return companies[0].get("entid")
        return None

    def _is_company(self, name):
        """判断是否为企业（简化）"""
        return "公司" in name or "集团" in name or "有限" in name

analyzer = RelationshipAnalyzer()
network = analyzer.find_investment_network("腾讯", depth=2)
print(json.dumps(network, ensure_ascii=False, indent=2))
```

