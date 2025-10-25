# 🏦 多资产类型RWA智能咨询系统
## Multi-Asset RWA Intelligent Consultation System

> 基于AutoGen + RAG + 多Agent架构的专业RWA代币化咨询平台

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📋 系统简介

这是一个**投行级RWA代币化智能咨询系统**，支持5大核心资产类型的专业分析。系统自动识别资产类型，调用对应的专家Agent，结合RAG知识库和实时网络搜索，生成包含详细流程图的投资备忘录。

### 🎯 核心功能

- ✅ **5种资产类型支持**: 太阳能、数据中心、仓储物流、风电、充电桩
- ✅ **智能资产识别**: 自动识别查询涉及的资产类型
- ✅ **专家Agent路由**: 11个专业Agent协同工作
- ✅ **RAG知识增强**: 2,700+行行业基准数据库
- ✅ **流程图可视化**: ASCII图表（结构图、瀑布图、甘特图）
- ✅ **投行级输出**: 2,000-3,500字专业投资备忘录

---

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆或下载项目
cd D:\test\AutoGen_RWA

# 创建虚拟环境（如果还没有）
python -m venv venv

# 激活虚拟环境
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API密钥

创建 `openai_api_key.txt` 文件，写入你的OpenAI API密钥：

```
sk-your-openai-api-key-here
```

### 3. 构建RAG知识库索引

```bash
# 设置API密钥环境变量
$env:OPENAI_API_KEY = Get-Content openai_api_key.txt

# 构建FAISS向量索引
python rag/build_index.py
```

### 4. 开始使用

#### 方式一：Windows快捷启动（推荐）
```bash
# 自动设置UTF-8编码
.\run_rwa.bat --query "50MW solar farm in Hong Kong" --quick
```

#### 方式二：直接运行
```bash
# 单次查询
python run_rwa_consultant.py --query "10MW data center tokenization" --quick

# 多Agent辩论模式（更深入）
python run_rwa_consultant.py --query "Your question" --debate

# 交互模式
python run_rwa_consultant.py
```

---

## 💡 使用示例

### 资产类型查询示例

```bash
# 1. 太阳能光伏项目
python run_rwa_consultant.py --query "50MW solar farm in Hong Kong, complete RWA tokenization design with flowcharts" --quick

# 2. 数据中心项目
python run_rwa_consultant.py --query "10MW Tier III data center in Tseung Kwan O, IRR and structure analysis" --quick

# 3. 仓储物流项目
python run_rwa_consultant.py --query "200,000 sq ft warehouse in Kwai Chung, REIT-like token structure" --quick

# 4. 风电项目
python run_rwa_consultant.py --query "100MW onshore wind farm, financial modeling and risk assessment" --quick

# 5. 充电桩基础设施
python run_rwa_consultant.py --query "30-stall DC fast charging network, utilization modeling" --quick
```

### 跨资产对比查询

```bash
# 对比不同资产类型
python run_rwa_consultant.py --query "Compare solar vs data center RWA returns and risks" --debate

# 混合项目分析
python run_rwa_consultant.py --query "Solar + wind hybrid renewable energy project structure" --debate
```

### 监管合规查询

```bash
# SFC许可要求
python run_rwa_consultant.py --query "Hong Kong SFC licensing requirements for infrastructure tokens" --quick

# 文档清单
python run_rwa_consultant.py --query "Complete document checklist for 50MW solar RWA offering" --quick
```

---

## 📊 支持的资产类型

| 资产类型 | 识别关键词 | 专家Agent | 典型IRR | 核心优势 |
|---------|-----------|-----------|---------|---------|
| **太阳能光伏** | solar, photovoltaic, pv | SolarRWASpecialist | 10-12% | 25年稳定现金流，政策支持 |
| **数据中心** | data center, datacenter, colocation | DataCenterRWASpecialist | 10-14% | 高EBITDA (45-55%)，AI基础设施 |
| **仓储物流** | warehouse, logistics, storage | WarehouseRWASpecialist | 8-11% | 最稳定NOI (75-85%)，电商驱动 |
| **风电项目** | wind, wind power, wind farm | WindRWASpecialist | 9-13% | 容量因子高 (25-35%) |
| **充电桩** | ev charging, electric vehicle | EVChargingRWASpecialist | 12-16% | 政策强支持，高增长 |

---

## 🏗️ 系统架构

```
用户查询
    |
    v
┌─────────────────────────┐
│  Asset Type Classifier  │ ← 智能识别资产类型
└─────────────────────────┘
    |
    v
┌─────────────────────────┐
│     RAG Expert Agent    │ ← 检索2,700+行知识库
└─────────────────────────┘
    |
    v
┌─────────────────────────┐
│ Asset-Specific Agents   │ ← 5个专业Agent
│  • Solar                │
│  • Data Center          │
│  • Warehouse            │
│  • Wind                 │
│  • EV Charging          │
└─────────────────────────┘
    |
    v
┌─────────────────────────┐
│ Cross-Functional Agents │ ← 法律、金融、Web搜索
│  • Legal Compliance     │
│  • Financial Structure  │
│  • Web Researcher       │
└─────────────────────────┘
    |
    v
┌─────────────────────────┐
│  Coordinator Agent      │ ← 综合所有专家意见
└─────────────────────────┘
    |
    v
📄 投资备忘录（2,000-3,500字 + 流程图）
```

---

## 📚 知识库内容

每个资产类型都有完整的8模块知识库：

1. **Asset Performance Benchmarks** - 性能基准参数（CAPEX, OPEX, 收入模型）
2. **Financial Model** - 财务模型（IRR, 现金流预测, 敏感性分析）
3. **SPV & Contract Stack** - 公司结构与合同框架
4. **Token Tranche Map** - 代币分层设计与分配瀑布
5. **Regulatory Path** - 香港SFC监管路径（时间线、成本）
6. **Comparable Deals** - 真实案例分析（Equinix, ESR, SUNeVision等）
7. **Risk & Mitigation** - 风险矩阵与缓解策略
8. **Investment Narrative** - 投资叙事与定位声明

**总计**: 6个文档，2,752行专业内容

---

## 🎨 输出示例

系统输出包含多种ASCII流程图：

### 公司结构图示例
```
Token Holders (Professional Investors)
         |
         | Investment ($XXM)
         v
   [Cayman SPV - Issuer]
    (Token Distribution Vehicle)
         |
         | 100% ownership
         v
   [HK Licensed Entity]
   (SFC Type 1 + Type 9)
         |
         | Asset Management
         v
   [Project OpCo]
    (Asset Owner & Operator)
         |
         v
   [Revenue Generation]
```

### 现金流瀑布图示例
```
QUARTERLY REVENUE ($X.XM)
    |
    v
[Priority 1: OPEX] → $XXk
    |
    v
[Priority 2: Debt Service] → $XXk
    |
    v
[Priority 3: Reserves] → $XXk
    |
    v
[Priority 4: Token Distributions] → $XXk
    (Yield: X.X% annualized)
```

### SFC许可时间线示例
```
MONTH 1-6: PRE-APPLICATION
├─ Corporate Setup
├─ Hire ROs (Responsible Officers)
├─ Compliance Manual (100+ pages)
└─ KYC/AML System Setup
    |
    v
MONTH 7: APPLICATION SUBMISSION
├─ Form 1, 4, 5 Submission
├─ 24+ Supporting Documents
└─ Fee: HKD $37,160
    |
    v
MONTH 8-15: SFC REVIEW
├─ Query Rounds (2-3)
├─ On-Site Inspection
└─ Background Checks
    |
    v
MONTH 16-18: LICENSE GRANT
```

---

## 🛠️ 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| **LLM** | OpenAI GPT-4 | 结构化输出、专业分析 |
| **向量数据库** | FAISS | Facebook AI Similarity Search |
| **Embeddings** | text-embedding-ada-002 | 文档向量化 |
| **文档处理** | LangChain | 文档分割、加载、检索 |
| **Web搜索** | DuckDuckGo Search | 实时信息获取 |
| **Agent框架** | 自定义多Agent系统 | 协调器+专家Agent |

---

## 📁 项目结构

```
AutoGen_RWA/
├── README.md                           # 本文件
├── MULTI_ASSET_RWA_SYSTEM.md          # 完整系统文档
├── PROJECT_SUMMARY.md                  # 项目总结
├── QUICK_START.md                      # 快速入门指南
│
├── main.py                             # 核心系统入口
├── run_rwa_consultant.py               # CLI命令行接口
├── run_rwa.bat                         # Windows快捷启动脚本
├── requirements.txt                    # Python依赖包
│
├── data/docs/                          # RAG知识库
│   ├── solar_rwa_benchmarks.txt        # 太阳能基准数据 (300行)
│   ├── datacenter_rwa_benchmarks.txt   # 数据中心基准 (641行)
│   ├── warehouse_logistics_rwa_benchmarks.txt  # 仓储物流 (614行)
│   ├── wind_power_rwa_benchmarks.txt   # 风电项目 (216行)
│   ├── ev_charging_rwa_benchmarks.txt  # 充电桩 (485行)
│   └── hk_sfc_rwa_licensing_guide.txt  # SFC监管指南 (496行)
│
├── rag/                                # RAG检索系统
│   ├── build_index.py                  # 构建FAISS索引
│   ├── query_index.py                  # 查询接口
│   └── faiss_index/                    # 向量数据库文件
│
├── agents/                             # 专家Agent
│   ├── asset_type_classifier.py        # 资产类型分类器
│   ├── solar_rwa_specialist.py         # 太阳能专家
│   ├── datacenter_rwa_specialist.py    # 数据中心专家
│   ├── warehouse_rwa_specialist.py     # 仓储物流专家
│   ├── wind_rwa_specialist.py          # 风电专家
│   ├── ev_charging_rwa_specialist.py   # 充电桩专家
│   ├── legal_compliance_specialist.py  # 法律合规专家
│   ├── financial_structuring_specialist.py  # 金融结构专家
│   ├── coordinator_agent.py            # 协调器Agent
│   ├── rag_expert_agent.py             # RAG检索专家
│   ├── web_researcher_agent.py         # Web搜索研究员
│   ├── rwa_advisor_agent.py            # RWA总顾问
│   └── debate_coordinator.py           # 辩论协调器
│
└── tools/                              # 工具模块
    ├── mcp_market.py                   # 市场数据工具
    ├── mcp_chain.py                    # 链上数据工具
    └── mcp_search.py                   # Web搜索工具
```

---

## ⚙️ 配置说明

### requirements.txt
```
pyautogen>=0.2.30
langchain-community>=0.3.1
langchain-text-splitters>=0.3.0
langchain-openai>=0.2.0
faiss-cpu>=1.8.0
openai>=1.40.0
pypdf>=4.2.0
requests>=2.32.0
python-dotenv>=1.0.1
ddgs>=0.1.0
googlesearch-python>=1.2.3
```

### 环境变量
- `OPENAI_API_KEY`: OpenAI API密钥（必需）
- `PYTHONIOENCODING`: UTF-8（Windows自动设置）

---

## 🎯 使用场景

### 1. 投资尽职调查
为投资团队快速生成RWA项目的初步分析报告

### 2. 项目可行性研究
评估不同资产类型的RWA代币化可行性

### 3. 监管咨询
了解香港SFC许可要求和合规路径

### 4. 结构设计
获取代币分层、现金流瀑布、SPV结构建议

### 5. 市场对标
对比同类型已发行RWA项目（案例研究）

### 6. 客户演示
生成包含流程图的专业投资备忘录用于客户展示

---

## 📈 性能指标

| 指标 | 数值 |
|------|------|
| 支持资产类型 | 5种（可扩展） |
| 专家Agent数量 | 11个 |
| 知识库规模 | 2,752行 |
| 平均响应时间 | 30-60秒（Quick）/ 2-5分钟（Debate） |
| 输出长度 | 2,000-3,500字 |
| RAG检索准确率 | Top-5 >85% |

---

## 🔧 常见问题 (FAQ)

### Q1: 系统需要联网吗？
A: 是的，需要联网访问OpenAI API和DuckDuckGo搜索。RAG知识库可以离线使用。

### Q2: 支持中文输入吗？
A: 支持中英文混合输入，但输出主要为英文。可以在查询中要求"用中文回答"。

### Q3: 如何添加新的资产类型？
A: 
1. 在 `data/docs/` 添加新的基准数据文件
2. 创建对应的Specialist Agent（参考现有Agent）
3. 在 `asset_type_classifier.py` 添加资产类型定义
4. 在 `main.py` 注册新Agent
5. 重建RAG索引

### Q4: 输出的数字准确吗？
A: 输出基于行业基准数据和真实案例，但仅供参考。实际项目需要专业顾问验证。

### Q5: 可以导出为PDF吗？
A: 当前输出为纯文本。可以复制到Word/Google Docs，然后导出为PDF。

### Q6: Windows终端乱码怎么办？
A: 使用 `.\run_rwa.bat` 启动，会自动设置UTF-8编码。或手动执行：
```powershell
chcp 65001
$env:PYTHONIOENCODING='utf-8'
```

---

## 🚧 未来路线图

### 短期（1-3个月）
- [ ] 添加更多资产类型（工业PPA、碳信用、绿色证书）
- [ ] 支持中文输出模式
- [ ] Web UI界面（Streamlit/Gradio）
- [ ] 导出为PDF/PPT功能

### 中期（3-6个月）
- [ ] 实时区块链数据集成
- [ ] 财务模型Excel自动生成
- [ ] 多语言支持（中文、日文）
- [ ] 智能合约模板生成

### 长期（6-12个月）
- [ ] AI生成SVG流程图
- [ ] 投资者匹配推荐系统
- [ ] 监管政策实时追踪
- [ ] 移动端APP

---

## 📄 许可证

MIT License - 仅供研究和教育用途

---

## ⚠️ 免责声明

- 本系统输出仅供参考，**不构成投资建议**
- 实际RWA项目需要聘请专业法律、财务顾问
- Hong Kong SFC许可申请需要持牌机构协助
- 所有案例和数据来源于公开信息，可能存在时效性
- 用户需自行承担使用本系统的风险

---

## 📞 技术支持

如遇问题，请检查：
1. ✅ Python版本 >= 3.12
2. ✅ 所有依赖已安装 (`pip list`)
3. ✅ OpenAI API密钥有效
4. ✅ RAG索引已构建 (`rag/faiss_index/` 文件夹存在)
5. ✅ 网络连接正常

---

## 🌟 致谢

本系统基于以下开源项目：
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft多Agent框架
- [LangChain](https://github.com/langchain-ai/langchain) - LLM应用开发框架
- [FAISS](https://github.com/facebookresearch/faiss) - Facebook向量搜索引擎
- [OpenAI](https://openai.com/) - GPT-4 API

---

**最后更新**: 2025-10-25  
**版本**: v2.0 (Multi-Asset)  
**作者**: AutoGen RWA Team

✅ **系统已完整部署，可投入使用！**

如需详细文档，请查看：
- 📘 [完整系统文档](MULTI_ASSET_RWA_SYSTEM.md)
- 📗 [快速入门指南](QUICK_START.md)
- 📙 [项目总结](PROJECT_SUMMARY.md)
