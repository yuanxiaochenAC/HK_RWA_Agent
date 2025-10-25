"""
Solar RWA Specialist Agent - 光伏项目RWA发行专家
专门负责光伏项目的RWA代币化技术细节、项目结构设计和行业最佳实践
"""
from typing import List, Dict, Any
from openai import OpenAI

class SolarRWASpecialist:
    def __init__(self):
        self.client = OpenAI()
        self.name = "Solar RWA Specialist"
        self.description = "Expert in solar project tokenization, structure design, and industry best practices"
        
        # 光伏RWA专业知识库
        self.solar_rwa_knowledge = {
            "project_types": {
                "utility_scale": "Large-scale ground-mounted solar farms (>1MW)",
                "distributed": "Rooftop and small commercial installations (<1MW)",
                "community": "Community solar gardens and shared solar programs"
            },
            "revenue_streams": {
                "ppa_contracts": "Power Purchase Agreements with utilities/corporates",
                "feed_in_tariffs": "Government-guaranteed payment rates",
                "merchant_sales": "Spot market electricity sales",
                "srecs": "Solar Renewable Energy Certificates",
                "capacity_payments": "Grid stability service payments"
            },
            "risk_factors": {
                "technology": "Panel degradation, inverter failure, performance variance",
                "weather": "Irradiation variability, extreme weather events",
                "regulatory": "Policy changes, tariff modifications, grid access",
                "counterparty": "Off-taker credit risk, PPA contract risk",
                "operational": "O&M costs, equipment replacement, insurance"
            }
        }
    
    def analyze_solar_project_structure(self, project_description: str, rag_context: str = "") -> str:
        """分析光伏项目结构并提供RWA设计建议（强制使用RAG数据库中的基准参数）"""
        system_prompt = f"""
You are a senior solar project finance and RWA tokenization expert with 15+ years of experience in structuring renewable energy investments.

Your expertise includes:
- Solar project development and financing structures (500+ MW portfolio experience)
- RWA tokenization for renewable energy assets ($100M+ in tokenized projects)
- Hong Kong and international regulatory frameworks (SFC licensing, securities law)
- Risk assessment and mitigation strategies
- Due diligence requirements for solar investments

Solar RWA Knowledge Base:
{self._format_knowledge_base()}

CRITICAL: You MUST reference the following INDUSTRY BENCHMARK DATA from our proprietary database in your analysis.
Use these SPECIFIC NUMBERS and REAL CASE STUDIES in your response:

{rag_context if rag_context else "Note: RAG database context not provided. Use general industry knowledge but flag this limitation."}

IMPORTANT: Provide an INVESTMENT-GRADE MEMORANDUM style analysis (1000-1200 words minimum) with:

1. EXECUTIVE SUMMARY (150+ words):
   - Project overview with specific capacity (MW), location, technology type
   - Total project cost with SPECIFIC CAPEX breakdown (cite $/W from benchmark data)
   - Financing structure with debt-to-equity ratio
   - Expected returns: Project IRR, Equity IRR, Token Holder Yield (use benchmark ranges)
   - Key investment highlights (3-5 bullet points with numbers)

2. TECHNICAL SPECIFICATIONS & CAPEX (250+ words):
   - Detailed CAPEX breakdown with SPECIFIC NUMBERS from benchmark data:
     * Total Capex (cite typical $0.55-$0.75/W range, recommend specific value)
     * Component costs (panels, inverters, mounting, BOS) with percentages
     * EPC and development costs
     * Contingency budget
   - Performance parameters with SPECIFIC NUMBERS:
     * Capacity Factor (cite typical 17-22%, recommend based on location)
     * Performance Ratio (PR: 82-88%)
     * Annual Degradation Rate (0.4-0.6%)
   - Energy generation projections (MWh/year with calculation methodology)
   - MANDATORY ASCII DIAGRAM: Project component layout showing solar panels, inverters, grid connection

3. LEGAL & OWNERSHIP STRUCTURE (200+ words):
   - MANDATORY DETAILED ASCII STRUCTURE DIAGRAM:
```
Token Holders (Professional Investors)
         |
         | Investment ($10M equity)
         v
   [Cayman SPV - Issuer]
    (Token Distribution Vehicle)
         |
         | 100% ownership
         v
   [HK Licensed Entity]
   (Type 1 + Type 9 SFC License)
         |
         | Asset Management
         v
   [Project OpCo - Hong Kong]
    (Solar Farm Owner & Operator)
         |
         | PPA Revenue Flow
         v
   [Utility Offtaker]
   (Government or Private Entity)
```
   - Asset ownership framework (land lease vs ownership, equipment title)
   - Governance structure (Board composition, investor voting rights)
   - Jurisdictional analysis (why Cayman + Hong Kong structure optimizes tax + regulation)

4. TOKENIZATION ARCHITECTURE (250+ words):
   - Token structure design with SPECIFIC NUMBERS:
     * Total token issuance (number of tokens, price per token)
     * Minimum investment (e.g., $10,000-$100,000)
     * Token type (revenue-sharing vs equity-like)
   - Token valuation methodology:
     * NAV calculation formula (with example calculation)
     * Revaluation frequency (quarterly/semi-annual)
   - MANDATORY CASH FLOW WATERFALL ASCII DIAGRAM:
```
QUARTERLY REVENUE ($2.7M example)
         |
         v
    [Step 1: O&M Costs]
     Deduct: $162,500
         |
         v
    [Step 2: Debt Service]
     Deduct: $450,000 (principal + interest)
         |
         v
    [Step 3: Reserve Accounts]
     Deduct: $100,000 (DSRA + Maintenance)
         |
         v
    [Step 4: Token Distributions]
     Distribute: $1,987,500
     (Yield: 8.1% annualized)
         |
         v
    [Professional Investor Accounts]
```
   - Distribution schedule (quarterly, projected yield 6-9% citing benchmark)
   - REFERENCE CASE STUDY: Cite similar project (e.g., SUNSEAP Singapore)

5. REVENUE MODEL & FINANCIAL PROJECTIONS (300+ words):
   - PPA structure with SPECIFIC NUMBERS:
     * PPA rate ($/kWh, cite typical $0.08-$0.15 range, recommend specific)
     * PPA tenor (years)
     * Escalation clause (%, e.g., 2%/year)
     * Offtaker identity and credit rating
   - 10-year revenue projection TABLE (Year, Generation MWh, Price $/kWh, Revenue $M)
   - OPEX breakdown with SPECIFIC NUMBERS (cite $10-$17/kW/year benchmark):
     * Fixed O&M (60-70% of OPEX)
     * Variable O&M (20-25%)
     * Insurance (8-12%)
     * Asset management (3-5%)
   - Financial returns analysis:
     * Project Unlevered IRR: X.X% (calculate based on all-equity)
     * Project Levered IRR: Y.Y% (calculate with 60-70% debt)
     * Equity IRR: Z.Z% (after debt service)
     * Token Holder Yield: A.A% (annual distribution rate)
     * Payback period: N years
     * DSCR: 1.3x-1.5x (cite benchmark minimum 1.25x)

6. DEBT FINANCING STRUCTURE (200+ words):
   - Senior debt terms with SPECIFIC NUMBERS:
     * Loan amount (% of project cost, typically 60-70%)
     * Interest rate (cite benchmark 4.5-6.5%, recommend specific)
     * Tenor (15-20 years to match PPA)
     * Amortization schedule (level payment vs sculpted)
   - Debt covenants:
     * Minimum DSCR requirement (typically 1.25x)
     * Reserve account requirements (6-12 months debt service)
     * Major maintenance reserve (cite $ amount)
   - Lender requirements (sponsor equity, completion guarantee, etc.)

7. RISK MITIGATION FRAMEWORK (250+ words):
   - Comprehensive risk matrix TABLE (Risk, Likelihood, Impact, Mitigation)
   - Insurance requirements with SPECIFIC COVERAGE AMOUNTS:
     * Property insurance: $XX million
     * Business interruption: $XX million/year
     * Liability insurance: $XX million
   - Performance guarantees:
     * Panel warranty (25 years, 80% capacity at year 25)
     * Inverter warranty (12-15 years)
     * EPC performance guarantee (liquidated damages for shortfall)
   - Weather risk mitigation (production variance analysis, P50/P90 scenarios)
   - Counterparty credit risk mitigation (letter of credit, escrow)

8. HONG KONG SFC LICENSING ROADMAP (200+ words):
   - Required licenses with SPECIFIC COSTS (cite from benchmark data):
     * Type 1 + Type 9 licenses (HKD $10M capital requirement)
     * Application fees: HKD $37,160 total
     * Annual compliance costs: $150k-$250k
   - MANDATORY LICENSING TIMELINE FLOWCHART:
```
MONTH 1-6: PRE-APPLICATION
├─ Corporate Setup (HK Limited Company)
├─ Hire 2 Responsible Officers (ROs)
├─ Draft Compliance Manual (100+ pages)
├─ Implement KYC/AML System
└─ Secure Office Space
    |
    v
MONTH 7: APPLICATION SUBMISSION
├─ Submit Form 1 (Corporate License)
├─ Submit Form 4 (RO Approvals) x2
├─ Attach 24+ Documents
└─ Pay HKD $37,160 Fee
    |
    v
MONTH 8-15: SFC REVIEW
├─ Query Round 1 (20-40 questions)
├─ Applicant Response (21 days)
├─ Query Round 2 (refinements)
├─ On-Site Inspection
└─ Background Checks on ROs
    |
    v
MONTH 16-18: LICENSE GRANT
├─ Conditional Approval
├─ Final Modifications
├─ License Certificate Issued
└─ Commence Token Operations
```
   - Professional Investor requirements (portfolio >HKD $8M or income >HKD $1M)
   - Document checklist (reference full list in regulatory guide)
   - REAL CASE: BC Technology (OSL) licensing timeline - 18 months

9. COMPARABLE PROJECTS & CASE STUDIES (200+ words):
   - CASE STUDY 1: SUNSEAP Singapore
     * Capacity: 5-100MW aggregate
     * Token yield: 7-8% annualized
     * Investment minimum: SGD $10,000
     * Key success factor: Government renewable energy policy support
   - CASE STUDY 2: Brookfield Renewable YieldCo
     * Scale: 21+ GW global portfolio
     * Distribution: 5-9% annual with inflation escalation
     * Investor type: Institutional + retail (publicly traded)
     * Lesson: Diversification reduces risk, attracts lower-cost capital
   - CASE STUDY 3: Enerparc Germany ABS
     * Project size: 30-80MW individual SPVs
     * Structure: Asset-backed notes
     * Interest rate: 3.5-5.0% (Euro)
     * Lesson: Investment-grade PPA critical for credit rating
   - Market pricing trends and investor appetite analysis

10. NEXT STEPS & IMPLEMENTATION ROADMAP (150+ words):
    - MANDATORY COMPREHENSIVE IMPLEMENTATION GANTT CHART:
```
TIMELINE: 24-MONTH PROJECT ROADMAP

MONTH 1-3: PREPARATION PHASE
├─ Week 1-2:   Technical Feasibility Study
├─ Week 3-4:   Engage Legal Counsel (Mayer Brown / Simmons & Simmons)
├─ Week 5-8:   Financial Model Development
├─ Week 9-12:  SPV Structure Design
└─ Deliverable: Investment Teaser (20-page document)

MONTH 4-9: LICENSING & STRUCTURING
├─ Month 4:    Incorporate HK Entity + Cayman SPV
├─ Month 5-6:  Hire ROs & Build Compliance Team
├─ Month 7:    Submit SFC License Application
├─ Month 8-9:  Respond to SFC Queries + Debt Financing
└─ Deliverable: Full Offering Memorandum (100+ pages)

MONTH 10-18: REGULATORY APPROVAL & PREPARATION
├─ Month 10-15: SFC Review & On-Site Inspection
├─ Month 16:    License Grant
├─ Month 17:    Smart Contract Development & Audit
├─ Month 18:    Investor Roadshow (Target: 50 PIs)
└─ Deliverable: Token Ready for Issuance

MONTH 19-24: TOKEN LAUNCH & OPERATIONS
├─ Month 19:    Token Issuance (Target: $10M raise)
├─ Month 20:    Project Construction Completion
├─ Month 21:    Grid Connection & Commissioning
├─ Month 22:    First Revenue Generation
├─ Month 23:    First Distribution to Token Holders
└─ Month 24:    Secondary Market Launch (OSL / HashKey)
```
    - Critical path dependencies and risk mitigation
    - Resource allocation ($4-6M total budget for setup + operations)
    - Key decision points and go/no-go milestones

CRITICAL: Use SPECIFIC NUMBERS from the benchmark database throughout (CAPEX $/W, OPEX $/kW/year, capacity factor %, IRR ranges, license costs, case study yields).
Reference REAL PROJECTS by name (SUNSEAP, Brookfield, Enerparc).
Provide ASCII DIAGRAMS for structure visualization.
Make every recommendation backed by quantitative data.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": project_description}
                ],
                temperature=0.2,
                max_tokens=3500  # 增加以支持投行级详细输出
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Solar RWA analysis failed: {str(e)}"
    
    def generate_technical_document_checklist(self, project_type: str) -> List[Dict[str, Any]]:
        """生成技术文档清单"""
        base_documents = [
            {
                "category": "Technical Documentation",
                "priority": "Critical",
                "documents": [
                    "Detailed Engineering Design Package",
                    "Solar Resource Assessment Report (minimum 2 years of data)",
                    "Energy Yield Projection (P50/P90 scenarios)",
                    "Grid Impact Study and Interconnection Agreement",
                    "Equipment Specifications and Warranties",
                    "Performance Ratio and Degradation Analysis",
                    "Construction and Commissioning Timeline",
                    "Operations & Maintenance Manual"
                ]
            },
            {
                "category": "Financial Modeling",
                "priority": "Critical", 
                "documents": [
                    "20-year Cash Flow Model with Sensitivity Analysis",
                    "LCOE (Levelized Cost of Energy) Calculation",
                    "IRR and NPV Analysis for Different Scenarios",
                    "Debt Service Coverage Ratio Projections", 
                    "Insurance Cost Analysis and Coverage Details",
                    "Tax Analysis including Depreciation Benefits",
                    "Exit Strategy and Residual Value Assessment"
                ]
            },
            {
                "category": "Risk Assessment",
                "priority": "High",
                "documents": [
                    "Comprehensive Risk Register and Mitigation Matrix",
                    "Weather and Irradiation Risk Analysis",
                    "Technology Risk Assessment (equipment failure rates)",
                    "Counterparty Credit Analysis (off-taker assessment)",
                    "Regulatory Risk Assessment (policy change scenarios)",
                    "Force Majeure and Insurance Coverage Analysis",
                    "Operational Risk Framework"
                ]
            }
        ]
        
        return base_documents
    
    def _format_knowledge_base(self) -> str:
        """格式化知识库用于prompt"""
        formatted = "SOLAR RWA KNOWLEDGE BASE:\n\n"
        
        for category, items in self.solar_rwa_knowledge.items():
            formatted += f"{category.upper().replace('_', ' ')}:\n"
            for key, value in items.items():
                formatted += f"- {key}: {value}\n"
            formatted += "\n"
            
        return formatted
    
    def provide_industry_benchmarks(self) -> Dict[str, Any]:
        """提供行业基准数据"""
        return {
            "typical_capacity_factors": {
                "hong_kong": "12-15%",
                "southern_china": "13-16%",
                "global_average": "15-25%"
            },
            "capex_benchmarks": {
                "utility_scale": "$0.8-1.2 per Watt",
                "rooftop_commercial": "$1.2-1.8 per Watt",
                "floating_solar": "$1.0-1.4 per Watt"
            },
            "opex_benchmarks": {
                "fixed_om": "$15-25 per kW per year",
                "insurance": "$2-4 per kW per year",
                "land_lease": "$200-500 per acre per year"
            },
            "ppa_pricing": {
                "hong_kong_fit": "HK$3-4 per kWh",
                "corporate_ppa": "HK$0.8-1.2 per kWh",
                "merchant_pricing": "Variable based on grid prices"
            }
        }
    
    def get_capabilities(self) -> List[str]:
        """返回该Agent的能力描述"""
        return [
            "Solar project technical structure analysis",
            "RWA tokenization strategy design",
            "Financial modeling and cash flow analysis", 
            "Risk assessment and mitigation planning",
            "Industry benchmark data provision",
            "Technical due diligence guidance",
            "Operations & maintenance framework design",
            "Performance monitoring system recommendations"
        ]
