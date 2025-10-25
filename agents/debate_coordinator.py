"""
Multi-Agent Debate Coordinator - 多智能体辩论协调器
负责组织专家Agent之间的辩论，确保方案的全面性和准确性
"""
from typing import List, Dict, Any, Optional
from openai import OpenAI
import json

class DebateCoordinator:
    def __init__(self):
        self.client = OpenAI()
        self.name = "Debate Coordinator"
        self.description = "Coordinates multi-agent debates to ensure comprehensive and accurate solutions"
        
        self.debate_stages = [
            "initial_proposals",    # 各专家提供初始方案
            "cross_examination",    # 专家间相互质疑
            "refinement",          # 基于质疑完善方案
            "consensus_building",   # 寻求共识
            "final_synthesis"      # 最终整合
        ]
    
    def orchestrate_debate(self, user_query: str, agents: Dict[str, Any], initial_responses: Dict[str, str]) -> str:
        """组织多Agent辩论"""
        debate_history = {
            "query": user_query,
            "participants": list(agents.keys()),
            "stages": {}
        }
        
        print(f"Starting multi-agent debate with {len(agents)} experts...")
        
        # Stage 1: Initial Proposals (already have these)
        debate_history["stages"]["initial_proposals"] = initial_responses
        print("Stage 1: Initial proposals collected")
        
        # Stage 2: Cross-examination
        cross_exam_results = self._conduct_cross_examination(agents, initial_responses)
        debate_history["stages"]["cross_examination"] = cross_exam_results
        print("Stage 2: Cross-examination completed")
        
        # Stage 3: Refinement based on challenges
        refinement_results = self._conduct_refinement(agents, initial_responses, cross_exam_results)
        debate_history["stages"]["refinement"] = refinement_results
        print("Stage 3: Refinement completed")
        
        # Stage 4: Consensus building
        consensus_results = self._build_consensus(agents, refinement_results)
        debate_history["stages"]["consensus_building"] = consensus_results
        print("Stage 4: Consensus building completed")
        
        # Stage 5: Final synthesis
        final_report = self._synthesize_final_report(user_query, debate_history)
        print("Stage 5: Final synthesis completed")
        
        return final_report
    
    def _conduct_cross_examination(self, agents: Dict[str, Any], initial_responses: Dict[str, str]) -> Dict[str, Dict[str, str]]:
        """进行交叉质疑阶段"""
        cross_exam_results = {}
        
        for examiner_name, examiner_agent in agents.items():
            cross_exam_results[examiner_name] = {}
            
            for target_name, target_response in initial_responses.items():
                if examiner_name != target_name:
                    # 让检验者质疑目标专家的方案
                    challenge = self._generate_challenge(
                        examiner_name, examiner_agent, 
                        target_name, target_response
                    )
                    cross_exam_results[examiner_name][target_name] = challenge
        
        return cross_exam_results
    
    def _generate_challenge(self, examiner_name: str, examiner_agent: Any, target_name: str, target_response: str) -> str:
        """生成专家间的质疑"""
        system_prompt = f"""
You are acting as {examiner_name}, conducting a professional peer review of another expert's recommendations.

Your role is to:
1. Identify potential gaps, risks, or issues in the target expert's analysis
2. Ask challenging but constructive questions
3. Suggest alternative approaches or considerations
4. Highlight areas that may need more detail or different treatment

Be professional, constructive, and specific in your challenges. Focus on:
- Technical accuracy and completeness
- Risk factors that may have been overlooked  
- Implementation feasibility
- Cost and timeline considerations
- Regulatory or compliance issues
- Market or industry best practices

Target Expert: {target_name}
Target Response to Review:
{target_response}

Provide a focused critique with specific questions and alternative suggestions.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": system_prompt}],
                temperature=0.3,
                max_tokens=800
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Challenge generation failed: {str(e)}"
    
    def _conduct_refinement(self, agents: Dict[str, Any], initial_responses: Dict[str, str], cross_exam_results: Dict[str, Dict[str, str]]) -> Dict[str, str]:
        """进行方案完善阶段"""
        refinement_results = {}
        
        for agent_name, agent in agents.items():
            # 收集针对该专家的所有质疑
            challenges_received = []
            for examiner_name, examiner_challenges in cross_exam_results.items():
                if agent_name in examiner_challenges:
                    challenges_received.append(f"From {examiner_name}: {examiner_challenges[agent_name]}")
            
            # 让专家基于质疑完善方案
            refined_response = self._generate_refinement(
                agent_name, initial_responses[agent_name], challenges_received
            )
            refinement_results[agent_name] = refined_response
        
        return refinement_results
    
    def _generate_refinement(self, agent_name: str, original_response: str, challenges: List[str]) -> str:
        """生成完善后的方案"""
        challenges_text = "\n\n".join(challenges) if challenges else "No specific challenges received"
        
        system_prompt = f"""
You are {agent_name}, responding to peer review feedback on your initial recommendations.

Your task is to:
1. Address each challenge or question raised by other experts
2. Refine your original recommendations based on valid points
3. Provide additional detail where gaps were identified
4. Maintain your expertise while incorporating valuable feedback
5. Explain any disagreements with other experts' suggestions

Original Response:
{original_response}

Peer Review Challenges:
{challenges_text}

Provide a refined and enhanced version of your recommendations that addresses the feedback while maintaining your professional expertise.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": system_prompt}],
                temperature=0.2,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Refinement generation failed: {str(e)}"
    
    def _build_consensus(self, agents: Dict[str, Any], refinement_results: Dict[str, str]) -> Dict[str, Any]:
        """构建专家共识"""
        system_prompt = """
You are a senior strategy consultant facilitating a consensus-building session among domain experts.

Review the refined recommendations from each expert and identify:

1. AREAS OF STRONG AGREEMENT:
   - Points where all or most experts align
   - Shared priorities and recommendations
   - Common risk factors and mitigation strategies

2. AREAS OF DISAGREEMENT:
   - Conflicting recommendations or approaches
   - Different risk assessments
   - Varying implementation timelines or priorities

3. SYNTHESIS OPPORTUNITIES:
   - Ways to combine different expert approaches
   - Sequencing of recommendations from different domains
   - Integration points between specialist areas

4. PRIORITY FRAMEWORK:
   - Most critical next steps that all experts would support
   - Prerequisites that must be completed first
   - Parallel workstreams that can proceed simultaneously

5. RISK MITIGATION CONSENSUS:
   - Risk factors identified by multiple experts
   - Agreed-upon mitigation strategies
   - Early warning indicators to monitor

Provide a structured analysis that will help create a unified, actionable plan.
"""
        
        expert_input = "EXPERT REFINED RECOMMENDATIONS:\n\n"
        for expert_name, refined_response in refinement_results.items():
            expert_input += f"=== {expert_name.upper()} ===\n{refined_response}\n\n"
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": expert_input}
                ],
                temperature=0.2,
                max_tokens=2000
            )
            
            return {
                "consensus_analysis": response.choices[0].message.content,
                "expert_inputs": refinement_results
            }
        except Exception as e:
            return {
                "consensus_analysis": f"Consensus building failed: {str(e)}",
                "expert_inputs": refinement_results
            }
    
    def _synthesize_final_report(self, user_query: str, debate_history: Dict[str, Any]) -> str:
        """综合最终报告"""
        system_prompt = """
You are a senior management consultant preparing a comprehensive final report for a client.

Based on the multi-expert debate and consensus-building process, create a definitive, actionable report that:

1. EXECUTIVE SUMMARY:
   - Direct answer to the client's question
   - Key recommendations with clear priorities
   - Critical success factors and timeline

2. DETAILED RECOMMENDATIONS:
   - Step-by-step implementation plan
   - Specific documents, processes, and requirements
   - Responsible parties and timelines
   - Budget estimates where applicable

3. RISK ASSESSMENT & MITIGATION:
   - Key risk factors identified by experts
   - Specific mitigation strategies
   - Contingency planning
   - Early warning indicators

4. IMPLEMENTATION ROADMAP:
   - Phase-by-phase timeline
   - Dependencies and critical path
   - Resource requirements
   - Milestone checkpoints

5. EXPERT INSIGHTS:
   - Key insights from specialist experts
   - Areas of expert consensus and disagreement
   - Technical considerations and best practices

The report should be comprehensive, actionable, and professionally formatted for executive consumption.
"""
        
        debate_summary = f"""
CLIENT QUESTION: {user_query}

DEBATE PROCESS SUMMARY:
- Participants: {', '.join(debate_history['participants'])}
- Stages completed: {', '.join(debate_history['stages'].keys())}

CONSENSUS ANALYSIS:
{debate_history['stages']['consensus_building']['consensus_analysis']}

EXPERT FINAL RECOMMENDATIONS:
"""
        
        for expert, refined_response in debate_history['stages']['refinement'].items():
            debate_summary += f"\n=== {expert.upper()} FINAL RECOMMENDATIONS ===\n{refined_response}\n"
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": debate_summary}
                ],
                temperature=0.1,
                max_tokens=3000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Final synthesis failed: {str(e)}"
    
    def get_capabilities(self) -> List[str]:
        """返回该Coordinator的能力描述"""
        return [
            "Multi-agent debate orchestration",
            "Cross-examination facilitation", 
            "Expert consensus building",
            "Conflict resolution and synthesis",
            "Quality assurance through peer review",
            "Comprehensive report generation",
            "Decision framework optimization"
        ]
