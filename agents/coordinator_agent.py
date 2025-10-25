"""
协调器Agent - 负责任务分解、Agent调度和结果整合
"""
from typing import List, Dict, Any
import json
from openai import OpenAI

class CoordinatorAgent:
    def __init__(self):
        self.client = OpenAI()
        self.available_agents = {
            "rag_expert": "RAG专家 - 查询香港RWA监管文档、法规指引",
            "web_researcher": "联网研究员 - 查询最新政策、市场数据、新闻动态", 
            "rwa_advisor": "RWA顾问 - 提供专业的RWA发行建议和方案"
        }
    
    def analyze_query(self, user_query: str) -> Dict[str, Any]:
        """分析用户查询，决定需要调用哪些Agent"""
        system_prompt = f"""
You are an intelligent coordinator responsible for analyzing user's RWA-related questions and creating query plans.

Available expert agents:
{json.dumps(self.available_agents, ensure_ascii=False, indent=2)}

Please analyze the user's question and return a JSON execution plan:
{{
    "query_type": "question type",
    "complexity": "simple/medium/complex", 
    "required_agents": ["list of required agents"],
    "search_tasks": [
        {{
            "agent": "agent_name",
            "task": "specific task description",
            "priority": 1-3
        }}
    ],
    "reasoning": "reason for choosing these agents"
}}

User question: {user_query}
"""
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_prompt}],
            temperature=0.3
        )
        
        try:
            return json.loads(response.choices[0].message.content)
        except:
            return {
                "query_type": "general",
                "complexity": "medium",
                "required_agents": ["rag_expert", "rwa_advisor"],
                "search_tasks": [
                    {"agent": "rag_expert", "task": user_query, "priority": 1},
                    {"agent": "rwa_advisor", "task": user_query, "priority": 2}
                ],
                "reasoning": "Default to calling RAG expert and RWA advisor"
            }
    
    def synthesize_answer(self, user_query: str, agent_results: Dict[str, str]) -> str:
        """整合各Agent的结果，生成最终答案（投行备忘录格式）"""
        # 智能精简：保留ASCII图表和关键数字，压缩其他内容
        condensed_results = {}
        for agent, result in agent_results.items():
            # 如果结果包含ASCII图表（```标记），优先保留图表部分
            if '```' in result and len(result) > 2500:
                # 提取所有ASCII图表
                parts = result.split('```')
                diagrams = []
                text_parts = []
                for i, part in enumerate(parts):
                    if i % 2 == 1:  # 这是图表内容
                        diagrams.append(f"```{part}```")
                    else:
                        # 压缩文字部分
                        if len(part) > 400:
                            text_parts.append(part[:400] + "...")
                        else:
                            text_parts.append(part)
                
                # 重组：保留所有图表 + 压缩的文字
                condensed = "\n".join(diagrams) + "\n" + "\n".join(text_parts[:3])  # 只保留前3段文字
                condensed_results[agent] = condensed
            elif len(result) > 2000:
                # 没有图表但内容很长，保留前2000字符
                condensed_results[agent] = result[:2000] + f"\n...[{len(result)} chars total]"
            else:
                condensed_results[agent] = result
        
        system_prompt = """
You are a senior RWA investment banker synthesizing expert opinions into an INVESTMENT MEMORANDUM (Goldman Sachs/JP Morgan style).

OUTPUT FORMAT - STRUCTURED INVESTMENT MEMO (2500+ words minimum):

**CRITICAL INSTRUCTIONS FOR FLOWCHARTS AND DIAGRAMS:**

1. **DIRECTLY COPY AND DISPLAY** all ASCII flowcharts, diagrams, and tables provided by expert agents
2. **DO NOT SUMMARIZE OR REMOVE** any ```...``` code blocks containing diagrams
3. **ADD YOUR OWN** additional flowcharts if experts didn't provide them
4. **PRESERVE FORMATTING** of all ASCII art exactly as provided

When you see diagrams in expert responses like:
```
[Expert's ASCII diagram]
```
YOU MUST include them in your final output!

STRUCTURE:

1. EXECUTIVE SUMMARY (200+ words):
   - Include a HIGH-LEVEL PROJECT STRUCTURE DIAGRAM showing:
```
[Project Overview Flowchart]
Token Holders → SPV → Project → Revenue → Distributions
```
   - Direct answer to the user's question with specific details
   - Key findings from all expert consultations
   - Critical success factors and main recommendations

2. DETAILED ANALYSIS (500+ words):
   **MUST INCLUDE: Corporate Structure Diagram from Legal Expert**
   **MUST INCLUDE: Cash Flow Waterfall Diagram from Financial Expert**
   **MUST INCLUDE: Technical Architecture from Solar Specialist**
   
   Copy and display ALL diagrams provided by experts, then explain:
   - In-depth analysis of each aspect
   - Specific data points, metrics, and benchmarks (cite from benchmark database)
   - Real-world examples and case studies
   - Market context and industry trends

3. OPERATIONAL RECOMMENDATIONS (400+ words):
   - Step-by-step implementation guidance
   - Specific actions with timelines
   - Resource requirements (budget, personnel, technology)
   - Success metrics and KPIs
   - Best practices and lessons learned

4. COMPREHENSIVE DOCUMENT CHECKLIST (200+ words):
   - Detailed list of all required documents
   - Purpose and content requirements for each document
   - Templates and format recommendations
   - Submission procedures and authorities

5. DETAILED TIMELINE PLANNING (300+ words):
   **MUST INCLUDE: SFC Licensing Timeline Flowchart from Legal Expert**
   **MUST INCLUDE: 24-Month Implementation Gantt Chart from Solar Specialist**
   
   Copy and display ALL timeline diagrams, then explain:
   - Phase-by-phase breakdown with specific dates
   - Dependencies and critical path analysis
   - Milestone checkpoints and deliverables
   - Buffer time for delays and approvals
   - Parallel vs sequential activities

6. RISK ASSESSMENT & MITIGATION (300+ words):
   - Comprehensive risk analysis (regulatory, market, operational, technical, financial)
   - Likelihood and impact assessment for each risk
   - Specific mitigation strategies with contingency plans
   - Early warning indicators and monitoring mechanisms
   - Risk ownership and responsibility allocation

7. FINANCIAL CONSIDERATIONS (200+ words if applicable):
   - Cost estimates (ranges and breakdown)
   - Revenue projections and ROI analysis
   - Funding structure recommendations
   - Tax implications and optimization strategies

8. REGULATORY COMPLIANCE DETAILS (200+ words):
   - Specific regulations and legal requirements
   - Compliance procedures and deadlines
   - Regulatory authority contacts and resources
   - Ongoing compliance obligations

9. CASE STUDIES & EXAMPLES (100+ words):
   - Similar successful projects (with numbers and outcomes)
   - Lessons learned from failures
   - Industry benchmarks and comparisons

10. RESOURCES & NEXT STEPS (100+ words):
    - Recommended service providers (lawyers, auditors, consultants)
    - Useful websites and official resources
    - Immediate action items
    - Long-term strategic considerations

Use SPECIFIC numbers, dates, amounts, percentages, and concrete examples throughout.
Cite web search results when available with URLs.
Make the response practical, actionable, and immediately useful.

**FINAL REMINDER ON DIAGRAMS:**
- Count the number of ```...``` blocks in expert responses
- Your output MUST contain AT LEAST the same number of diagram blocks
- COPY each diagram EXACTLY as provided (don't paraphrase ASCII art!)
- Add section headers before each diagram like "### Corporate Structure" or "### Cash Flow Waterfall"
"""
        
        context = f"User Question: {user_query}\n\nExpert Research Results (Condensed):\n"
        for agent, result in condensed_results.items():
            context += f"\n[{agent}]:\n{result}\n"
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context}
            ],
            temperature=0.3,
            max_tokens=3000  # 设置为3000以平衡详细度和token限制
        )
        
        return response.choices[0].message.content