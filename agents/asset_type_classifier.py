"""
Asset Type Classifier - 资产类型智能识别器
自动识别用户查询涉及的RWA资产类型，支持跨资产类型分析
"""
from typing import List, Dict, Any
from openai import OpenAI

class AssetTypeClassifier:
    def __init__(self):
        self.client = OpenAI()
        self.name = "Asset Type Classifier"
        
        # 支持的资产类型及其关键词
        self.asset_types = {
            "solar": {
                "name": "Solar Photovoltaic Projects",
                "keywords": ["solar", "photovoltaic", "pv", "太阳能", "光伏"],
                "description": "Solar farm projects, rooftop solar, ground-mounted PV installations"
            },
            "datacenter": {
                "name": "Data Center & Edge Infrastructure",
                "keywords": ["data center", "datacenter", "dc", "edge computing", "colocation", "数据中心", "机房"],
                "description": "Tier III/IV data centers, edge computing nodes, colocation facilities"
            },
            "warehouse": {
                "name": "Warehouse & Logistics Parks",
                "keywords": ["warehouse", "logistics", "storage", "distribution", "仓储", "物流", "仓库"],
                "description": "Modern warehouses, logistics parks, cold storage, e-commerce fulfillment centers"
            },
            "wind": {
                "name": "Wind Power Projects",
                "keywords": ["wind", "wind power", "wind farm", "wind turbine", "风电", "风力"],
                "description": "Onshore wind farms (30-200MW), wind turbine installations"
            },
            "ev_charging": {
                "name": "EV Charging Infrastructure",
                "keywords": ["ev charging", "electric vehicle", "charging station", "charger", "充电桩", "电动汽车", "充电站"],
                "description": "DC fast charging stations, AC charging networks, battery swap stations"
            }
        }
    
    def classify_asset_types(self, user_query: str) -> List[str]:
        """
        智能识别用户查询涉及的资产类型
        Returns: List of asset type codes (e.g., ["solar", "datacenter"])
        """
        # 第一步：基于关键词快速匹配
        keyword_matches = self._keyword_matching(user_query)
        
        # 第二步：如果关键词匹配不明确，使用LLM进行语义分析
        if len(keyword_matches) == 0:
            llm_classification = self._llm_classification(user_query)
            return llm_classification
        elif len(keyword_matches) == 1:
            return keyword_matches
        else:
            # 多个匹配，使用LLM排序优先级
            return self._llm_prioritization(user_query, keyword_matches)
    
    def _keyword_matching(self, query: str) -> List[str]:
        """基于关键词的快速匹配"""
        query_lower = query.lower()
        matches = []
        
        for asset_code, asset_info in self.asset_types.items():
            for keyword in asset_info["keywords"]:
                if keyword.lower() in query_lower:
                    matches.append(asset_code)
                    break  # 找到一个关键词即可
        
        return matches
    
    def _llm_classification(self, query: str) -> List[str]:
        """使用LLM进行语义分类（当关键词匹配失败时）"""
        asset_descriptions = "\n".join([
            f"{code}: {info['name']} - {info['description']}"
            for code, info in self.asset_types.items()
        ])
        
        prompt = f"""
You are an RWA asset classifier. Analyze the user's question and identify which asset type(s) it relates to.

Available Asset Types:
{asset_descriptions}

User Query: "{query}"

Return ONLY the asset type codes (comma-separated) that are relevant, or "general" if it's a general RWA question not specific to any asset type.

Examples:
- "50MW solar farm tokenization" → solar
- "data center in Hong Kong" → datacenter
- "warehouse and logistics REIT" → warehouse
- "wind and solar hybrid project" → wind,solar
- "what is RWA?" → general
- "EV charging network investment" → ev_charging

Your answer (codes only, comma-separated):
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=50
            )
            
            result = response.choices[0].message.content.strip().lower()
            
            # 解析结果
            if result == "general":
                return []  # 通用问题，不限定资产类型
            else:
                # 返回识别到的资产类型
                codes = [code.strip() for code in result.split(",")]
                # 验证代码有效性
                valid_codes = [code for code in codes if code in self.asset_types]
                return valid_codes if valid_codes else []
                
        except Exception as e:
            print(f"[Asset Classifier] LLM classification failed: {str(e)}, falling back to keyword matching")
            return []
    
    def _llm_prioritization(self, query: str, matched_types: List[str]) -> List[str]:
        """当多个资产类型匹配时，使用LLM排序优先级"""
        matched_descriptions = "\n".join([
            f"{code}: {self.asset_types[code]['name']}"
            for code in matched_types
        ])
        
        prompt = f"""
Multiple asset types matched for this query. Rank them by relevance (most relevant first).

Query: "{query}"

Matched Asset Types:
{matched_descriptions}

Return the codes in order of relevance (comma-separated, most relevant first).
If the query is equally relevant to multiple types, list all of them.

Your ranking (codes only):
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=50
            )
            
            result = response.choices[0].message.content.strip().lower()
            codes = [code.strip() for code in result.split(",")]
            # 只返回有效的代码
            return [code for code in codes if code in matched_types]
            
        except Exception as e:
            print(f"[Asset Classifier] LLM prioritization failed: {str(e)}, returning all matches")
            return matched_types
    
    def get_asset_info(self, asset_code: str) -> Dict[str, Any]:
        """获取资产类型的详细信息"""
        return self.asset_types.get(asset_code, {})
    
    def get_all_asset_types(self) -> Dict[str, Dict[str, Any]]:
        """获取所有支持的资产类型"""
        return self.asset_types

