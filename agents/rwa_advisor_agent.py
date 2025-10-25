"""
RWA顾问Agent - 提供专业的RWA发行建议和解决方案
"""
from typing import List, Dict, Any
from openai import OpenAI

class RWAAdvisorAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "RWA专业顾问"
        self.description = "提供RWA发行的专业建议、流程指导和解决方案"
    
    def provide_advice(self, query: str, context_info: str = "") -> str:
        """基于查询和上下文信息提供专业建议"""
        system_prompt = """
你是一位资深的RWA（Real World Assets）专业顾问，具有丰富的香港金融市场经验。

专业领域：
- RWA代币化项目设计
- 香港监管合规指导
- 发行流程规划
- 风险评估和管理
- 法律文件准备
- 市场策略建议

回答要求：
1. 提供具体可执行的建议
2. 按优先级排列建议事项
3. 明确指出潜在风险点
4. 给出时间规划建议
5. 列出具体的文件清单（如适用）
6. 提供后续步骤指导

保持专业、实用、可操作的建议风格。
"""
        
        user_content = f"""
用户咨询：{query}

相关背景信息：
{context_info}

请提供专业的RWA发行建议和指导。
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"专业建议生成失败：{str(e)}"
    
    def create_document_checklist(self, project_type: str) -> List[Dict[str, Any]]:
        """为特定项目类型创建文件清单"""
        checklists = {
            "光伏": [
                {"category": "项目文件", "items": [
                    "光伏项目可行性研究报告",
                    "项目投资协议",
                    "土地使用权证明",
                    "环境影响评估报告",
                    "电力销售协议(PPA)",
                    "项目建设许可证"
                ]},
                {"category": "财务文件", "items": [
                    "项目财务预测报告", 
                    "审计财务报表",
                    "现金流分析报告",
                    "资产评估报告",
                    "保险证明文件"
                ]},
                {"category": "法律文件", "items": [
                    "项目法律意见书",
                    "合规性确认函",
                    "知识产权证明",
                    "监管批准文件"
                ]}
            ],
            "房地产": [
                {"category": "资产文件", "items": [
                    "房产权属证明",
                    "土地使用权证",
                    "建筑物评估报告",
                    "租赁协议",
                    "物业管理协议"
                ]},
                {"category": "财务文件", "items": [
                    "租金收入证明",
                    "运营成本分析",
                    "资产评估报告",
                    "财务审计报告"
                ]}
            ]
        }
        
        return checklists.get(project_type, checklists["光伏"])
    
    def get_risk_assessment(self, project_type: str) -> Dict[str, List[str]]:
        """提供风险评估"""
        risk_categories = {
            "监管风险": [
                "香港监管政策变化风险",
                "合规要求更新风险", 
                "跨境监管协调风险"
            ],
            "市场风险": [
                "代币流动性风险",
                "市场接受度风险",
                "价格波动风险"
            ],
            "技术风险": [
                "智能合约安全风险",
                "区块链技术风险",
                "系统运维风险"
            ],
            "运营风险": [
                "项目执行风险",
                "管理团队风险", 
                "第三方服务风险"
            ]
        }
        return risk_categories
    
    def get_capabilities(self) -> List[str]:
        """返回该Agent的能力描述"""
        return [
            "RWA项目结构设计",
            "合规流程规划指导",
            "风险评估和管理建议",
            "文件准备清单制定",
            "发行时间规划建议",
            "投资者沟通策略",
            "后续管理方案设计"
        ]


