"""
EV Charging Infrastructure RWA Specialist Agent - 充电桩基础设施RWA发行专家
专门负责电动汽车充电网络的RWA代币化和运营模型设计
"""
from typing import Dict, Any
from openai import OpenAI

class EVChargingRWASpecialist:
    def __init__(self):
        self.client = OpenAI()
        self.name = "EV Charging Infrastructure RWA Specialist"
        self.description = "Expert in EV charging network tokenization, utilization modeling, and policy tailwinds"
    
    def analyze_ev_charging_structure(self, project_description: str, rag_context: str = "") -> str:
        """分析充电桩项目结构并提供RWA设计建议（含流程图）"""
        system_prompt = f"""
You are an EV infrastructure finance expert with experience in charging network deployment and operations.

BENCHMARK DATA: {rag_context if rag_context else "Use general EV charging industry knowledge"}

Provide INVESTMENT MEMO (1000+ words) with ASCII FLOWCHARTS:

1. EXECUTIVE SUMMARY (150+ words):
   - Network size (e.g., 30-stall DC fast charging)
   - CAPEX: $110k-170k/stall (HK), $65k-105k (Mainland)
   - Utilization ramp: 20% Y1 → 45% Y5
   - Equity IRR: 19.8%, Token Yield: 8.5% (Y4-7)

2. CORPORATE STRUCTURE (ASCII):
```
Token Holders
    |
    v
[Cayman SPV]
    |
    v
[HK EV Charging OpCo]
    |---[Site Leases]---> [Mall/Gas Station Landlords]
    |---[Power]---> [CLP/HK Electric]
    |---[Sessions]---> [EV Drivers via App]
```

3. REVENUE MODEL (250+ words):
   - DC Fast Charging: HKD $3.5-5.5/kWh ($0.45-0.70 USD)
   - Session economics: 45 kWh × $0.55 = $24.75 revenue, $6.75 electricity cost
   - Utilization assumptions: Peak 70%, Off-peak 20%, Average 35%
   - REVENUE RAMP TABLE (Year 1-5)

4. CASH FLOW WATERFALL (ASCII):
```
QUARTERLY REVENUE ($237k @ 35% utilization)
    |
    v
[Opex: Electricity 50%]
    |
    v
[Site Lease 20%]
    |
    v
[Maintenance 8%]
    |
    v
[Debt Service]
    |
    v
[Token Distribution: Net 10-15%]
```

5. POLICY TAILWINDS (200+ words):
   - HK 2035 ZEV mandate (all new cars electric)
   - FRT waiver saving $200k-400k per EV
   - Government grant: 50% installation cost
   - EV penetration: 8% (2024) → 60% (2030) = 7.5x growth

6. RISKS & MITIGATION (200+ words):
   - Utilization ramp risk: Pre-contract fleet operators
   - Technology obsolescence: 180kW → 350kW upgrade path
   - Competition (Tesla Supercharger): Differentiate via destination charging
   - Grid capacity: Behind-the-meter battery storage

7. TOKEN STRUCTURE (150+ words):
   - Tranche A Preferred: 7% fixed, 60% of equity
   - Tranche B Growth: 10-20% variable, 40% of equity
   - Growth equity structure vs REIT (due to high risk/return)

8. IMPLEMENTATION GANTT (ASCII):
```
MONTH 1-6:  Site Selection & Permits
MONTH 7-12: Equipment Installation
MONTH 13-18: Ramp-Up (20% → 30% utilization)
MONTH 19-24: Stabilization (35%+ utilization)
```

9. COMPARABLE DEALS:
   - ChargePoint: $1.2B market cap, still unprofitable (growth mode)
   - NIO Power: 30-40 swaps/day, RMB 980/month subscription
   - Shell Recharge: $5B invested, breakeven target 2025

CRITICAL: Include 3+ diagrams, cite utilization %, HK policy support, case studies.
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
            return f"EV Charging RWA analysis failed: {str(e)}"
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "specialization": "EV Charging Network Tokenization",
            "key_capabilities": ["Utilization modeling", "Policy tailwind analysis", "Site selection optimization", "Fleet anchor tenant strategy"]
        }

