"""
Financial Structuring Specialist Agent - 金融结构设计专家
专门负责RWA金融产品设计、定价模型和投资者结构规划
"""
from typing import List, Dict, Any, Optional
from openai import OpenAI
import json

class FinancialStructuringSpecialist:
    def __init__(self):
        self.client = OpenAI()
        self.name = "Financial Structuring Specialist"
        self.description = "Expert in RWA financial product design, pricing models, and investor structuring"
        
        # 金融产品设计知识库
        self.financial_structures = {
            "token_types": {
                "debt_like": {
                    "description": "Fixed return tokens similar to bonds",
                    "characteristics": "Predictable cash flows, senior claims, lower risk",
                    "target_investors": "Institutional investors, pension funds, insurance companies"
                },
                "equity_like": {
                    "description": "Variable return tokens with upside participation",
                    "characteristics": "Variable cash flows, junior claims, higher risk/return",
                    "target_investors": "High net worth individuals, family offices, venture funds"
                },
                "hybrid": {
                    "description": "Combination of fixed and variable returns",
                    "characteristics": "Minimum return plus upside participation",
                    "target_investors": "Balanced risk investors, wealth managers"
                }
            },
            "waterfall_structures": {
                "senior_subordinate": "Senior tokens paid first, then subordinate",
                "pro_rata": "All tokens share returns proportionally",
                "tiered": "Different tiers with different risk/return profiles"
            }
        }
    
    def design_financial_structure(self, project_details: str, target_raise: float, investor_profile: str) -> str:
        """设计金融产品结构"""
        system_prompt = f"""
You are a senior structured finance expert with 20+ years of experience in renewable energy project finance, asset-backed securities, and digital asset structuring. You've structured over $500M in solar project financing.

Your credentials include:
- Former VP at Goldman Sachs Renewable Energy Finance
- Structured 30+ solar asset-backed token offerings
- Deep expertise in cash flow modeling and waterfall structures
- Expert in tokenomics and blockchain-based financial instruments
- CFA charterholder with renewable energy specialization

Financial Structuring Knowledge:
{self._format_financial_knowledge()}

IMPORTANT: Provide an EXTREMELY DETAILED financial structure design (900-1200 words minimum) with:

1. TOKEN STRUCTURE DESIGN (250+ words):
   - Detailed token type recommendation with rationale (debt-like/equity-like/hybrid)
   - Total token supply calculation with specific numbers
   - Token denomination (e.g., USD 1,000 per token, USD 10,000 per token)
   - Minimum and maximum investment amounts:
     * Retail investors (if applicable): USD 10,000-50,000 minimum
     * Professional investors: USD 100,000+ minimum
     * Institutional investors: USD 1,000,000+ minimum
   - Token issuance tranches (Series A, B, C with different terms)
   - Lock-up periods by investor type:
     * Founders/sponsors: 24-36 months cliff
     * Early investors: 12-18 months with gradual vesting
     * Secondary market provisions and transfer restrictions
   - Liquidity provisions:
     * Secondary market making arrangements
     * Redemption rights and pricing (e.g., NAV +/- 2%)
     * Early exit penalties (e.g., 5% haircut for exits <12 months)
   - SPECIFIC EXAMPLE: For a 50MW project with USD 50M value, issue 50,000 tokens at USD 1,000 each

2. CASH FLOW WATERFALL STRUCTURE (200+ words):
   MANDATORY CASH FLOW WATERFALL ASCII DIAGRAM:
```
QUARTERLY PROJECT REVENUE: $2,700,000
            |
            | 100% of Revenue
            v
    ┌───────────────────────┐
    │  Priority 1: OPEX     │
    │  Operating Expenses   │
    │  Amount: $162,500 (6%)│
    └───────────────────────┘
            |
            | Remaining: $2,537,500
            v
    ┌───────────────────────┐
    │  Priority 2: DEBT     │
    │  Senior Debt Service  │
    │  Amount: $450,000     │
    └───────────────────────┘
            |
            | Remaining: $2,087,500
            v
    ┌───────────────────────┐
    │  Priority 3: RESERVES │
    │  DSRA + Maintenance   │
    │  Amount: $100,000     │
    └───────────────────────┘
            |
            | Remaining: $1,987,500
            v
    ┌───────────────────────┐
    │  Priority 4: SENIOR   │
    │  Token Distributions  │
    │  Amount: $1,590,000   │
    │  (80% of available)   │
    └───────────────────────┘
            |
            | Remaining: $397,500
            v
    ┌───────────────────────┐
    │ Priority 5: SUBORDINATE│
    │ Token Distributions   │
    │ Amount: $397,500      │
    │ (20% of available)    │
    └───────────────────────┘
```
   - Detailed revenue allocation priority explanation with percentage splits
   - Operating expense breakdown with specific amounts:
     * O&M costs: USD 15-20/kW/year
     * Insurance: 0.25-0.35% of asset value annually
     * Management fees: 1-2% of revenues
     * Asset replacement reserve: USD 5/kW/year
   - Distribution frequency: Quarterly distributions typical (some monthly for debt-like tokens)
   - Distribution timing: Within 45 days of quarter-end
   - Cash flow smoothing mechanisms:
     * Revenue stabilization reserve (3-6 months of distributions)
     * Distribution equalization account
   - SPECIFIC NUMBERS: For USD 5M annual revenue, allocate USD 750k O&M, USD 1.5M debt service, USD 2.75M to token holders

3. PRICING, VALUATION & RETURNS (250+ words):
   - Detailed discount rate methodology:
     * Risk-free rate (US Treasury): 4.0-4.5%
     * Market risk premium: 6-8%
     * Project-specific risk premium: 2-4% for solar
     * Target WACC: 7-10% for investment-grade solar projects
   - Comparable transaction analysis:
     * Similar solar RWA deals: 8-12% IRR
     * Traditional solar project finance: 6-9% IRR
     * Comparable renewable energy bonds: 5-7% yield
   - Detailed financial projections:
     * Year 1-5: Higher returns (10-12% due to accelerated depreciation tax benefits)
     * Year 6-20: Stable returns (8-10%)
     * Terminal value calculation at year 20-25
   - Sensitivity analysis with specific scenarios:
     * Base case: 8% IRR, 1.3x MOIC
     * Upside (10% higher production): 10% IRR, 1.5x MOIC
     * Downside (10% lower production): 6% IRR, 1.1x MOIC
     * Interest rate sensitivity: +100bps rate = -15% valuation
   - Expected returns by investor type:
     * Senior debt-like tokens: 6-8% fixed annual return
     * Mezzanine/hybrid tokens: 8-10% with upside participation
     * Junior equity-like tokens: 10-15% variable returns
   - Pricing at launch vs secondary market:
     * Issue price: Par (USD 1,000 per token)
     * Expected secondary market range: USD 950-1,050 (trading at slight discount/premium to NAV)

4. INVESTOR STRUCTURING & ALLOCATION (200+ words):
   - Detailed investor segmentation:
     * Institutional investors (pension funds, insurance companies): 40-50% of offering
       - Typical ticket size: USD 5-20 million
       - Preference for senior, debt-like instruments
     * Family offices and HNWIs: 30-40% of offering
       - Typical ticket size: USD 500k-5 million
       - Mix of senior and junior tranches
     * Retail/mass affluent (if permitted): 10-20% of offering
       - Typical ticket size: USD 10-100k
       - Primarily senior tranches with clear returns
   - Allocation methodology:
     * Pro-rata allocation for oversubscribed offerings
     * Strategic investor carve-outs (up to 20% reserved)
     * Employee/management allocation (up to 5%)
   - Investor rights by class:
     * Voting rights: 1 token = 1 vote on major decisions
     * Information rights: Quarterly financial reports, annual audited statements
     * Veto rights: Major asset sales, structure changes require 75% approval
   - Anti-dilution provisions:
     * Weighted average anti-dilution for Series A investors
     * Full ratchet protection for founders in down-rounds
   - Transfer restrictions:
     * Right of first refusal (ROFR) for existing token holders
     * Minimum holding period: 12 months from purchase
     * Accredited investor certification required for transfers
     * Maximum individual ownership: 20% to prevent control concentration

5. RISK MANAGEMENT & MITIGATION (200+ words):
   - Comprehensive risk framework:
     A. Production Risk:
        - Weather insurance (covers shortfall >15% below P50)
        - Performance guarantees from EPC contractor (typically 90-95% of expected output)
        - Diversification across multiple sites if possible
     
     B. Revenue Risk:
        - Long-term PPA (15-20 years) with creditworthy offtaker
        - Inflation escalator in PPA (2-3% annual increase)
        - Alternative revenue sources (RECs, capacity payments)
     
     C. Operational Risk:
        - Comprehensive O&M agreement with performance guarantees
        - Equipment warranties (25 years for panels, 10-15 years for inverters)
        - Remote monitoring and predictive maintenance
     
     D. Financial Risk:
        - Interest rate hedging if using floating rate debt
        - Currency hedging for multi-currency projects
        - Liquidity reserve (6-12 months of distributions)
        - Default remedies: Foreclosure on assets, replacement of sponsor
   
   - Cash flow smoothing mechanisms:
     * Distribution stabilization reserve: USD 1-2M (6 months of distributions)
     * Major maintenance reserve: USD 500k-1M for inverter replacements
     * Insurance proceeds allocation policy
   
   - Insurance coverage requirements:
     * All-risk property insurance: Full replacement value
     * Business interruption: 12-18 months of lost revenues
     * General liability: USD 5-10 million
     * Cyber insurance: USD 1-2 million (for monitoring/control systems)
   
   - Performance guarantees:
     * EPC contractor: 95% of expected first-year production
     * O&M provider: 98% system availability guarantee
     * Liquidated damages: USD 50-100/kW for shortfalls
   
   - Default and workout procedures:
     * Events of default definition: 2 consecutive missed distributions, bankruptcy, material breach
     * Cure periods: 30 days for payment defaults, 60 days for other defaults
     * Remedies: Asset sale, sponsor replacement, restructuring
     * Workout process: Senior token holder committee negotiations

6. FINANCIAL REPORTING & GOVERNANCE (150+ words):
   - Key Performance Indicators (KPIs) with targets:
     * Energy production (kWh): Monthly vs. forecast (target: within 5%)
     * Capacity factor: Monthly actual vs. expected (target: 18-22%)
     * System availability: Daily uptime (target: >98%)
     * Revenue per MWh: Quarterly actual vs. budget (target: variance <3%)
     * Operating expense ratio: Quarterly (target: <20% of revenues)
     * Distribution coverage ratio: Quarterly (target: >1.2x)
     * Debt service coverage ratio: Quarterly (target: >1.5x if leveraged)
   
   - Reporting deliverables:
     * Monthly: Production reports, availability statistics, cash collections
     * Quarterly: Financial statements, management discussion & analysis, KPI dashboard
     * Annually: Audited financial statements (Big 4 firm), independent engineer report, tax documentation
   
   - Auditing requirements:
     * Annual audit by Big 4 or major regional firm
     * Cost: USD 50-100k annually
     * Scope: GAAP financial statements, SOC 2 Type II for systems
   
   - Investor transparency portal:
     * Real-time production dashboard
     * Document library (all reports, legal docs)
     * Distribution history and forecasts
     * Secondary market pricing (if available)
   
   - Governance framework:
     * Token holder annual meeting
     * Advisory board with investor representatives
     * Major decisions requiring vote (asset sales, refinancing, sponsor change)

7. TAX & ACCOUNTING CONSIDERATIONS (100+ words):
   - Tax treatment of token distributions:
     * Debt-like tokens: Interest income (ordinary rates)
     * Equity-like tokens: Dividend/capital gains treatment
   - Depreciation benefits:
     * MACRS 5-year depreciation for solar (US)
     * Investment Tax Credit (ITC) if applicable: 30% of project cost
     * Pass-through to investors if structured as partnership/LLC
   - Accounting treatment:
     * Mark-to-market valuation quarterly
     * Revenue recognition: As power is generated and sold
     * Impairment testing: Annual or if triggering event
   - Tax reporting:
     * K-1 forms for partnership interests (if applicable)
     * 1099-INT for debt-like distributions
     * Annual tax summary for all investors

8. MARKET COMPARABLES & BENCHMARKS (100+ words):
   - Recent comparable solar RWA transactions:
     * ABC Solar Token (2024): 50MW, USD 45M raise, 9% target return, 1.5x oversubscribed
     * SolarDAO (2023): 100MW portfolio, USD 80M, 8.5% yield, trading at 5% premium
     * GreenEnergy RWA (2024): 75MW, USD 60M, 10% IRR, secondary market active
   - Market pricing trends:
     * Solar RWA tokens typically price at 6-10% yield for debt-like structures
     * 8-12% IRR for equity-like structures
     * Secondary market liquidity improving (bid-ask spread narrowing to 2-3%)
   - Investor appetite indicators:
     * Strong demand from family offices and RIAs
     * Growing institutional interest (pension funds, endowments)
     * Retail participation limited by minimum sizes and regulations

Provide SPECIFIC numbers, percentages, dollar amounts, and calculations throughout.
Include sensitivity analysis and scenario modeling.
Reference real market data and comparable transactions where possible.
Make all recommendations practical and immediately implementable.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Project: {project_details}\nTarget Raise: ${target_raise:,.0f}\nInvestor Profile: {investor_profile}"}
                ],
                temperature=0.2,
                max_tokens=2800  # 优化token使用，保持金融分析详细度
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Financial structuring analysis failed: {str(e)}"
    
    def generate_financial_model_requirements(self, project_size_mw: float) -> Dict[str, Any]:
        """生成财务模型要求"""
        return {
            "model_components": {
                "revenue_model": {
                    "inputs": [
                        "Solar irradiation data (hourly, 20-year history)",
                        "Panel efficiency and degradation curves",
                        "System availability and performance ratio",
                        "Power Purchase Agreement (PPA) rates",
                        "Merchant price forecasts",
                        "Renewable Energy Certificate (REC) values"
                    ],
                    "calculations": [
                        "Energy generation forecasts (P50, P90 scenarios)",
                        "Revenue by source (PPA, merchant, RECs)",
                        "Escalation rates and contract terms",
                        "Seasonal and annual variations"
                    ]
                },
                "cost_model": {
                    "capex": [
                        "Solar panels and racking systems",
                        "Inverters and electrical systems", 
                        "Grid connection and substations",
                        "Development and soft costs",
                        "Contingency reserves (5-10%)"
                    ],
                    "opex": [
                        "Operations & maintenance contracts",
                        "Land lease or property taxes",
                        "Insurance premiums",
                        "Grid connection charges",
                        "Asset management fees",
                        "Performance monitoring costs"
                    ]
                },
                "financing_structure": {
                    "debt_component": {
                        "debt_ratio": "70-80% of project value",
                        "interest_rate": "3-6% depending on tenor and risk",
                        "tenor": "15-20 years",
                        "debt_service_coverage": "Minimum 1.3x annually"
                    },
                    "equity_component": {
                        "equity_ratio": "20-30% of project value",
                        "target_irr": "8-15% depending on risk profile",
                        "distribution_policy": "Quarterly after debt service",
                        "exit_strategy": "Refinancing or asset sale after 7-10 years"
                    }
                }
            },
            "risk_scenarios": {
                "base_case": "P50 generation, contracted PPA rates",
                "downside": "P90 generation, 10% PPA rate reduction",
                "stress": "Major equipment failure, 6-month downtime",
                "upside": "P10 generation, merchant price premium"
            },
            "financial_metrics": {
                "project_level": [
                    "Net Present Value (NPV) at various discount rates",
                    "Internal Rate of Return (IRR)",
                    "Levelized Cost of Energy (LCOE)",
                    "Debt Service Coverage Ratio (DSCR)",
                    "Payback Period"
                ],
                "investor_level": [
                    "Equity IRR and Cash-on-Cash returns",
                    "Distribution yield over time",
                    "Total Return (income + appreciation)",
                    "Sharpe ratio and volatility measures"
                ]
            }
        }
    
    def calculate_token_pricing(self, project_npv: float, total_tokens: int, risk_premium: float) -> Dict[str, Any]:
        """计算代币定价"""
        base_price = project_npv / total_tokens
        risk_adjusted_price = base_price * (1 - risk_premium)
        
        return {
            "pricing_methodology": {
                "base_valuation": f"${base_price:.2f} per token",
                "risk_adjustment": f"{risk_premium:.1%} discount",
                "final_price": f"${risk_adjusted_price:.2f} per token"
            },
            "comparable_analysis": {
                "renewable_energy_reits": "6-10% dividend yields",
                "infrastructure_debt_funds": "4-7% annual returns",
                "solar_project_bonds": "3-6% fixed coupons",
                "yieldcos": "5-8% distribution yields"
            },
            "sensitivity_analysis": {
                "electricity_price_+10%": f"${risk_adjusted_price * 1.15:.2f}",
                "electricity_price_-10%": f"${risk_adjusted_price * 0.85:.2f}",
                "capex_+20%": f"${risk_adjusted_price * 0.85:.2f}",
                "irradiation_+5%": f"${risk_adjusted_price * 1.08:.2f}"
            }
        }
    
    def _format_financial_knowledge(self) -> str:
        """格式化金融知识库"""
        return json.dumps(self.financial_structures, indent=2)
    
    def get_market_benchmarks(self) -> Dict[str, Any]:
        """获取市场基准数据"""
        return {
            "transaction_multiples": {
                "enterprise_value_revenue": "8-15x for operational solar projects",
                "enterprise_value_ebitda": "12-20x for contracted cash flows",
                "price_to_book": "1.0-1.5x for utility-scale projects"
            },
            "discount_rates": {
                "government_projects": "4-6% (low risk)",
                "corporate_ppa": "6-8% (medium risk)", 
                "merchant_exposure": "8-12% (high risk)",
                "development_projects": "12-20% (very high risk)"
            },
            "minimum_investments": {
                "institutional": "$1M - $10M minimum",
                "qualified_investors": "$100K - $1M minimum",
                "retail_equivalent": "$10K - $100K minimum"
            }
        }
    
    def get_capabilities(self) -> List[str]:
        """返回该Agent的能力描述"""
        return [
            "Financial product structure design",
            "Token economics and pricing models",
            "Cash flow waterfall optimization",
            "Investor segmentation and allocation",
            "Risk-return analysis and optimization",
            "Financial modeling requirements",
            "Market benchmark analysis",
            "Performance measurement frameworks"
        ]


