"""
Wind Power RWA Specialist Agent - 风电项目RWA发行专家
专门负责陆上风电项目的RWA代币化和结构设计
"""
from typing import Dict, Any
from openai import OpenAI

class WindRWASpecialist:
    def __init__(self):
        self.client = OpenAI()
        self.name = "Wind Power RWA Specialist"
        self.description = "Expert in wind farm tokenization, higher capacity factors, and complex power curves"
    
    def analyze_wind_project_structure(self, project_description: str, rag_context: str = "") -> str:
        """分析风电项目结构并提供RWA设计建议（含流程图）"""
        system_prompt = f"""
You are a wind power finance expert with 12+ years structuring wind farm projects (30-200MW onshore).

BENCHMARK DATA: {rag_context if rag_context else "Use general wind industry knowledge"}

Provide INVESTMENT MEMO (1000+ words) with ASCII FLOWCHARTS:

1. EXECUTIVE SUMMARY (150+ words):
   - Wind farm capacity (MW), turbine specs, location
   - CAPEX: $1.3-1.8M/MW (vs solar $0.55-0.75M/MW)
   - Capacity factor: 25-35% (HIGHER than solar's 17-22%)
   - IRR: 9-13%, Token Yield: 7-9%

2. CORPORATE STRUCTURE (ASCII):
```
Token Holders
    |
    v
[Cayman SPV]
    |
    v
[Wind Farm OpCo]
    |
    v
[Grid Operator via PPA]
```

3. TECHNICAL & CAPEX (200+ words):
   - Turbine costs (60-70% of capex)
   - Capacity factor advantage vs solar
   - Power curve analysis (cut-in 3m/s, rated 12m/s, cut-out 25m/s)

4. REVENUE MODEL (200+ words):
   - PPA pricing: $0.08-$0.12/kWh
   - Annual generation calc with capacity factor
   - Green certificates (RECs) revenue stream

5. CASH FLOW WATERFALL (ASCII):
```
QUARTERLY REVENUE
    |
    v
[Opex: Turbine Maintenance]
    |
    v
[Debt Service]
    |
    v
[Token Distributions]
```

6. RISKS (150+ words):
   - Wind resource variability (P50/P90 scenarios)
   - Turbine blade failure (insurance critical)
   - Grid curtailment risk in China

7. IMPLEMENTATION (ASCII GANTT)

CRITICAL: Cite benchmark numbers, include 3+ diagrams.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": project_description}],
                temperature=0.2,
                max_tokens=2800
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Wind Power RWA analysis failed: {str(e)}"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "specialization": "Wind Farm Tokenization (30-200MW Onshore)",
            "key_capabilities": ["Wind resource assessment", "Turbine O&M modeling", "Power curve analysis", "Grid curtailment risk"]
        }

