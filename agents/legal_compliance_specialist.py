"""
Legal & Compliance Specialist Agent - 法律合规专家
专门负责香港金融法规、RWA合规要求和法律文件准备
"""
from typing import List, Dict, Any
from openai import OpenAI

class LegalComplianceSpecialist:
    def __init__(self):
        self.client = OpenAI()
        self.name = "Legal & Compliance Specialist"
        self.description = "Expert in Hong Kong financial regulations, RWA compliance, and legal documentation"
        
        # 香港金融法规知识库
        self.hk_regulations = {
            "primary_laws": {
                "securities_futures_ordinance": "SFO - Main securities law in Hong Kong",
                "companies_ordinance": "CO - Corporate governance and structure requirements",
                "anti_money_laundering_ordinance": "AMLO - AML/CFT compliance requirements",
                "personal_data_privacy_ordinance": "PDPO - Data protection requirements"
            },
            "regulatory_bodies": {
                "sfc": "Securities and Futures Commission - Primary securities regulator",
                "hkma": "Hong Kong Monetary Authority - Banking and monetary policy",
                "cr": "Companies Registry - Corporate registration and compliance",
                "fiu": "Financial Intelligence Unit - AML/CFT enforcement"
            },
            "licensing_requirements": {
                "type_1": "Dealing in securities",
                "type_4": "Advising on securities", 
                "type_6": "Advising on corporate finance",
                "type_9": "Asset management"
            }
        }
    
    def analyze_regulatory_requirements(self, project_type: str, structure_details: str) -> str:
        """分析监管要求"""
        system_prompt = f"""
You are a senior Hong Kong financial services lawyer and compliance expert with 20+ years of experience in securities regulation, fintech, digital assets, and cross-border structuring.

Your credentials include:
- Licensed Hong Kong solicitor with SFC regulatory experience
- Advised on 50+ token offerings and digital asset structures
- Deep expertise in Securities and Futures Ordinance (SFO)
- Former SFC consultant on fintech regulation
- Specialized in RWA and stablecoin regulatory frameworks

Hong Kong Regulatory Framework:
{self._format_regulatory_framework()}

IMPORTANT: Provide an EXTREMELY COMPREHENSIVE legal analysis (900-1200 words minimum) with:

1. REGULATORY CLASSIFICATION & ANALYSIS (250+ words):
   - Detailed securities analysis under SFO Section 2 and Schedule 1
   - Howey Test application and analysis (investment of money, common enterprise, profits from others' efforts)
   - Whether tokens are "securities", "collective investment schemes", or "structured products"
   - Specific SFC licensing requirements with detailed breakdown:
     * Type 1 (Dealing in securities) - when required, application process, capital requirements (HKD 3-5 million)
     * Type 4 (Advising on securities) - advisory role requirements
     * Type 6 (Advising on corporate finance) - for structuring and IPO-like activities
     * Type 9 (Asset management) - if managing investor funds
   - Professional Investor (PI) vs Retail distribution analysis
   - Exemptions available (Private placement to <50 investors, PI-only offerings)
   - SPECIFIC CITATIONS: SFO Cap. 571, Securities and Futures (Professional Investor) Rules
   - RECENT UPDATES: 2024-2025 SFC guidance on virtual assets and tokenization

2. HONG KONG CORPORATE STRUCTURE (200+ words):
   - Recommended SPV structure (Limited Company vs Guarantee Company)
   - Minimum capital requirements (typically HKD 1 for limited company)
   - Director requirements (minimum 1, Hong Kong resident director advantages)
   - Company Secretary obligations (must be Hong Kong resident or licensed trust company)
   - Registered office requirements
   - Share capital structure and classes of shares
   - Governance framework (board composition, quorum requirements, voting rights)
   - Trustee/Custodian arrangements:
     * Licensed Trust Company requirements under Trustee Ordinance (Cap. 29)
     * Custodian licensing under SFO
     * Asset segregation and client money rules
   - Cross-border considerations:
     * Double taxation treaties (Hong Kong has 40+ DTAs)
     * BEPS compliance and substance requirements
     * Offshore holding company structures (Cayman, BVI considerations)
   - SPECIFIC COSTS: Company registration (HKD 1,720), annual filing fees, audit requirements

3. STABLECOIN REGULATORY REGIME (200+ words if applicable):
   - Anti-Money Laundering and Counter-Terrorist Financing (Amendment) Ordinance 2024
   - HKMA licensing requirements for stablecoin issuers (effective August 1, 2025)
   - Reserve requirements (100% backing in high-quality liquid assets)
   - Redemption rights and mechanisms (redemption at par value on demand)
   - Capital adequacy requirements
   - Audit and attestation obligations (monthly reserve reports)
   - Segregation of reserve assets
   - Application process and timeline (6-12 months for HKMA review)
   - Transitional provisions for existing issuers
   - SPECIFIC REGULATIONS: Guideline on Supervision of Licensed Stablecoin Issuers

4. AML/CFT COMPLIANCE FRAMEWORK (200+ words):
   - Customer Due Diligence (CDD) requirements under AMLO
   - Enhanced Due Diligence (EDD) for high-risk customers
   - Beneficial ownership identification (25% threshold)
   - PEP screening requirements
   - Ongoing monitoring obligations
   - Suspicious Transaction Reporting (STR) to JFIU
   - Record keeping requirements (6 years for CDD, 7 years for transactions)
   - Staff training requirements (annual AML training mandatory)
   - AML Compliance Officer appointment
   - Risk assessment framework (institutional vs retail risk profiles)
   - Sanctions screening (OFAC, UN, HK lists)
   - SPECIFIC FORMS: STR form, Large Cash Transaction Report (>HKD 120,000)
   - PENALTIES: Maximum fine HKD 1 million + 2 years imprisonment for non-compliance

5. DOCUMENTATION PACKAGE (150+ words):
   MANDATORY DOCUMENTATION FLOWCHART:
```
DOCUMENTATION HIERARCHY

TIER 1: CONSTITUTIONAL (Foundation)
├─ Memorandum & Articles (Cayman/HK)
├─ Board Resolutions (Initial + Ongoing)
├─ Shareholder Agreements
└─ Director Service Agreements
    |
    v
TIER 2: REGULATORY (SFC Submission)
├─ Form 1: Corporate License Application
├─ Form 4: RO Applications (x2)
├─ Form 5: Asset Management Supplement
├─ Business Plan (3-year projections)
├─ Compliance Manual (100+ pages)
├─ AML/CFT Policies
└─ IT Security & BCP Policies
    |
    v
TIER 3: OFFERING DOCUMENTS (Investor-Facing)
├─ Information Memorandum (80-150 pages)
├─ Term Sheet (Token Economics)
├─ Risk Disclosure (SFC Format)
├─ Subscription Agreement
└─ PI Verification Forms
    |
    v
TIER 4: SERVICE PROVIDER (Operational)
├─ Custodian Agreement (token custody)
├─ Legal Counsel Engagement
├─ Auditor Appointment (Big 4)
├─ Fund Administrator Agreement
└─ Smart Contract Developer NDA
    |
    v
TIER 5: TECHNICAL (Blockchain)
├─ Smart Contract Code Repository
├─ Security Audit Report (OpenZeppelin/CertiK)
├─ Blockchain Infrastructure SLA
└─ Disaster Recovery Plan
```
   Detailed content requirements for each document tier
   
   E. Compliance Policies:
      - AML/CFT Policy Manual (50-100 pages typical)
      - KYC Procedures
      - Conflicts of Interest Policy
      - Market Conduct Rules
      - Cybersecurity and Data Protection Policy (PDPO compliance)
      - Business Continuity Plan

6. REGULATORY TIMELINE & PROCESS (150+ words):
   - Company incorporation: 1-2 weeks
   - SFC license application review: 6-12 months
   - HKMA stablecoin license (if applicable): 6-12 months
   - Parallel processing strategies
   - Pre-application consultation opportunities (SFC Fintech Contact Point)
   - Common reasons for delays: incomplete documentation, inadequate capital, unqualified ROs
   - Fast-track possibilities for established firms
   - Conditional approval and post-approval obligations
   - Annual compliance calendar (audit filing, business plan updates, RO renewals)

7. ONGOING COMPLIANCE OBLIGATIONS (100+ words):
   - Annual audit and financial reporting (within 4 months of year-end)
   - Monthly management accounts (for SFC licensed entities)
   - Notification obligations (material changes within 7 days)
   - Complaint handling and reporting
   - Annual compliance review by external auditor
   - RO continuing professional training (CPT) requirements
   - Client asset segregation and reconciliation (daily for client securities)
   - COSTS: Annual SFC license fee (HKD 11,700-69,100 depending on type)

8. ENFORCEMENT & RISK FACTORS (100+ words):
   - SFC enforcement statistics (2024: 15 disciplinary actions, average fine HKD 2-10 million)
   - Common violations: unlicensed activities, inadequate AML controls, client money breaches
   - Criminal vs regulatory sanctions
   - Personal liability of directors and officers
   - Mitigation strategies: robust compliance framework, regular external reviews, proactive SFC engagement
   - Insurance requirements: Professional Indemnity (PI) insurance minimum HKD 1 million
   - Early warning indicators: customer complaints, internal control failures

9. TAX CONSIDERATIONS (80+ words):
   - Hong Kong profits tax (16.5% for corporations, 8.25% on first HKD 2 million)
   - Stamp duty on share transfers (0.2% typically)
   - Withholding tax treatment (no WHT on dividends, interest)
   - Tax advantages: territorial tax system (offshore income not taxed)
   - Transfer pricing documentation requirements
   - Inland Revenue Department (IRD) filing obligations

10. PRACTICAL RECOMMENDATIONS (100+ words):
    - Engage Big 4 accounting firm for audit and tax
    - Retain top-tier Hong Kong law firm (typical cost: HKD 3,000-5,000/hour)
    - Budget for regulatory compliance: HKD 2-5 million first year, HKD 500k-1M annually
    - Timeline: minimum 12-18 months from planning to launch
    - Key success factors: experienced ROs, adequate capital, robust systems
    - Red flags to avoid: unlicensed marketing, retail distribution without license

Provide SPECIFIC section references, form numbers, deadlines, costs, and penalties throughout.
Include recent case studies and SFC enforcement actions where relevant.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Project: {project_type}\nStructure: {structure_details}"}
                ],
                temperature=0.1,
                max_tokens=2800  # 优化token使用，保持法律分析详细度
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Legal analysis failed: {str(e)}"
    
    def generate_legal_document_checklist(self) -> List[Dict[str, Any]]:
        """生成法律文件清单"""
        return [
            {
                "category": "Corporate Formation Documents",
                "priority": "Critical",
                "timeline": "Week 1-2",
                "documents": [
                    "Articles of Association for SPV",
                    "Memorandum of Association", 
                    "Board Resolutions for Token Issuance",
                    "Shareholder Agreements",
                    "Director and Officer Appointment Letters",
                    "Corporate Secretary Appointment",
                    "Registered Office Service Agreement"
                ],
                "responsible_party": "Hong Kong corporate lawyer",
                "estimated_cost": "HK$50,000 - 80,000"
            },
            {
                "category": "Securities Law Compliance",
                "priority": "Critical", 
                "timeline": "Week 2-4",
                "documents": [
                    "Legal Opinion on Securities Classification",
                    "Private Placement Memorandum",
                    "Subscription Agreement Template",
                    "Professional Investor Certification Forms",
                    "Risk Disclosure Statements",
                    "Cooling-off Period Notices",
                    "SFC Licensing Applications (if required)"
                ],
                "responsible_party": "Securities lawyer",
                "estimated_cost": "HK$150,000 - 300,000"
            },
            {
                "category": "Service Provider Agreements",
                "priority": "High",
                "timeline": "Week 3-5", 
                "documents": [
                    "Custodian/Trustee Agreement",
                    "Asset Manager Agreement",
                    "Auditor Engagement Letter",
                    "Legal Counsel Retainer Agreement",
                    "Compliance Consultant Agreement",
                    "Technology Provider Agreement",
                    "Insurance Broker Agreement"
                ],
                "responsible_party": "Commercial lawyer",
                "estimated_cost": "HK$80,000 - 120,000"
            },
            {
                "category": "Compliance Policies",
                "priority": "High",
                "timeline": "Week 4-6",
                "documents": [
                    "Anti-Money Laundering (AML) Policy",
                    "Know Your Customer (KYC) Procedures",
                    "Data Protection and Privacy Policy",
                    "Conflicts of Interest Policy",
                    "Whistleblowing Policy",
                    "Record Keeping Policy",
                    "Incident Response Procedures"
                ],
                "responsible_party": "Compliance consultant",
                "estimated_cost": "HK$60,000 - 100,000"
            }
        ]
    
    def assess_cross_border_implications(self, investor_jurisdictions: List[str]) -> Dict[str, Any]:
        """评估跨境法律影响"""
        return {
            "withholding_tax": {
                "hong_kong": "No withholding tax on dividends to non-residents",
                "mainland_china": "10% withholding tax on dividends",
                "singapore": "Tax treaty may reduce rates",
                "usa": "30% unless treaty protection applies"
            },
            "regulatory_notifications": {
                "fatca_crs": "Required for US and other CRS jurisdictions",
                "beneficial_ownership": "Ultimate beneficial owner disclosure required",
                "foreign_investment": "May trigger foreign investment rules in some jurisdictions"
            },
            "documentation_requirements": {
                "tax_certificates": "Tax residency certificates for treaty benefits",
                "regulatory_approvals": "Some jurisdictions require pre-approval for investments",
                "ongoing_reporting": "Annual or periodic reporting to home regulators"
            }
        }
    
    def _format_regulatory_framework(self) -> str:
        """格式化监管框架信息"""
        formatted = "HONG KONG REGULATORY FRAMEWORK:\n\n"
        
        for category, items in self.hk_regulations.items():
            formatted += f"{category.upper().replace('_', ' ')}:\n"
            for key, value in items.items():
                formatted += f"- {key}: {value}\n"
            formatted += "\n"
            
        return formatted
    
    def get_regulatory_timeline(self) -> Dict[str, str]:
        """获取监管时间线"""
        return {
            "company_incorporation": "3-5 business days",
            "bank_account_opening": "2-4 weeks",
            "sfc_licensing": "4-6 months (if required)",
            "tax_registration": "1-2 weeks",
            "compliance_setup": "4-6 weeks",
            "document_preparation": "6-8 weeks",
            "legal_review": "2-3 weeks",
            "regulatory_clearance": "Varies by complexity"
        }
    
    def get_capabilities(self) -> List[str]:
        """返回该Agent的能力描述"""
        return [
            "Hong Kong securities law analysis",
            "Regulatory classification assessment",
            "Corporate structure recommendations",
            "Legal documentation preparation",
            "Compliance framework design",
            "Cross-border regulatory analysis",
            "Risk assessment and mitigation",
            "Regulatory timeline planning"
        ]
