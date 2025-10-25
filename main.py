#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Multi-Agent RWA Consultation System with Debate Mechanism
增强的多Agent RWA咨询系统，包含专家辩论机制
"""
import sys
import os
import io
from typing import Dict, Any, List

# 设置UTF-8编码环境变量，解决Windows GBK编码问题
os.environ['PYTHONIOENCODING'] = 'utf-8'

from agents.coordinator_agent import CoordinatorAgent
from agents.rag_expert_agent import RAGExpertAgent
from agents.web_researcher_agent import WebResearcherAgent
from agents.rwa_advisor_agent import RWAAdvisorAgent

# 新增专业Agent - 按资产类型
from agents.solar_rwa_specialist import SolarRWASpecialist
from agents.datacenter_rwa_specialist import DataCenterRWASpecialist
from agents.warehouse_rwa_specialist import WarehouseRWASpecialist
from agents.wind_rwa_specialist import WindRWASpecialist
from agents.ev_charging_rwa_specialist import EVChargingRWASpecialist
from agents.legal_compliance_specialist import LegalComplianceSpecialist
from agents.financial_structuring_specialist import FinancialStructuringSpecialist

# 辩论协调器
from agents.debate_coordinator import DebateCoordinator

# 资产类型分类器
from agents.asset_type_classifier import AssetTypeClassifier


class EnhancedRWAConsultingSystem:
    def __init__(self):
        """初始化增强的多Agent系统"""
        self.coordinator = CoordinatorAgent()
        self.debate_coordinator = DebateCoordinator()
        self.asset_classifier = AssetTypeClassifier()  # 新增：资产类型分类器
        
        # 基础Agent
        self.basic_agents = {
            "rag_expert": RAGExpertAgent(),
            "web_researcher": WebResearcherAgent(),
            "rwa_advisor": RWAAdvisorAgent()
        }
        
        # 专业Agent - 按资产类型
        self.specialist_agents = {
            "solar_rwa_specialist": SolarRWASpecialist(),
            "datacenter_rwa_specialist": DataCenterRWASpecialist(),
            "warehouse_rwa_specialist": WarehouseRWASpecialist(),
            "wind_rwa_specialist": WindRWASpecialist(),
            "ev_charging_rwa_specialist": EVChargingRWASpecialist(),
            "legal_compliance_specialist": LegalComplianceSpecialist(),
            "financial_structuring_specialist": FinancialStructuringSpecialist()
        }
        
        # 合并所有Agent
        self.all_agents = {**self.basic_agents, **self.specialist_agents}
        
        print("Enhanced RWA Intelligent Consulting System Started")
        print("=== EXPERT PANEL ===")
        print("Basic Experts:")
        for name, agent in self.basic_agents.items():
            print(f"  - {agent.name}")
        print("Specialist Experts:")
        for name, agent in self.specialist_agents.items():
            print(f"  - {agent.name}")
        print("Debate Coordinator: Multi-Agent Consensus Builder")
        print("=" * 80)
    
    def enhanced_consult(self, user_query: str, use_debate: bool = True) -> str:
        """增强的咨询流程，包含专家辩论"""
        try:
            print(f"\nUser Query: {user_query}")
            print(f"Debate Mode: {'Enabled' if use_debate else 'Disabled'}")
            print("\nAnalyzing query requirements...")
            
            # 1. 智能选择相关专家
            selected_agents = self._select_relevant_agents(user_query)
            print(f"Selected Experts: {', '.join([self.all_agents[name].name for name in selected_agents])}")
            
            # 2. 先获取RAG context（用于所有专家Agent）
            print("\n=== PHASE 1: COLLECTING EXPERT OPINIONS ===")
            rag_context = ""
            if "rag_expert" in selected_agents or any(name in selected_agents for name in ["solar_rwa_specialist", "legal_compliance_specialist", "financial_structuring_specialist"]):
                print("Retrieving knowledge base context...")
                rag_context = self.all_agents["rag_expert"].search_documents(user_query)
                print("Knowledge base context retrieved")
            
            initial_responses = {}
            
            for agent_name in selected_agents:
                print(f"Consulting {self.all_agents[agent_name].name}...")
                
                try:
                    if agent_name == "rag_expert":
                        result = rag_context  # 已经获取
                    elif agent_name == "web_researcher":
                        result = self.all_agents[agent_name].research_topic(user_query)
                    elif agent_name == "solar_rwa_specialist":
                        # 传递RAG context给Solar专家
                        result = self.all_agents[agent_name].analyze_solar_project_structure(user_query, rag_context)
                    elif agent_name == "datacenter_rwa_specialist":
                        # 传递RAG context给Data Center专家
                        result = self.all_agents[agent_name].analyze_datacenter_structure(user_query, rag_context)
                    elif agent_name == "warehouse_rwa_specialist":
                        # 传递RAG context给Warehouse专家
                        result = self.all_agents[agent_name].analyze_warehouse_structure(user_query, rag_context)
                    elif agent_name == "wind_rwa_specialist":
                        # 传递RAG context给Wind专家
                        result = self.all_agents[agent_name].analyze_wind_project_structure(user_query, rag_context)
                    elif agent_name == "ev_charging_rwa_specialist":
                        # 传递RAG context给EV Charging专家
                        result = self.all_agents[agent_name].analyze_ev_charging_structure(user_query, rag_context)
                    elif agent_name == "legal_compliance_specialist":
                        result = self.all_agents[agent_name].analyze_regulatory_requirements("Solar RWA", user_query)
                    elif agent_name == "financial_structuring_specialist":
                        result = self.all_agents[agent_name].design_financial_structure(user_query, 10000000, "institutional")
                    else:
                        # For other agents, use general advice method
                        context = "\n".join([f"{k}: {v}" for k, v in initial_responses.items()])
                        result = self.all_agents[agent_name].provide_advice(user_query, context)
                    
                    initial_responses[agent_name] = result
                    print(f"[OK] {self.all_agents[agent_name].name} completed")
                    
                except Exception as e:
                    error_msg = f"{self.all_agents[agent_name].name} consultation failed: {str(e)}"
                    initial_responses[agent_name] = error_msg
                    print(f"[ERROR] {error_msg}")
            
            # 3. 决定是否进行专家辩论
            if use_debate and len(selected_agents) >= 2:
                print(f"\n=== PHASE 2: MULTI-AGENT DEBATE ===")
                selected_agent_objects = {name: self.all_agents[name] for name in selected_agents}
                final_answer = self.debate_coordinator.orchestrate_debate(
                    user_query, selected_agent_objects, initial_responses
                )
            else:
                print(f"\n=== PHASE 2: STANDARD SYNTHESIS ===")
                final_answer = self.coordinator.synthesize_answer(user_query, initial_responses)
            
            return final_answer
            
        except Exception as e:
            return f"Enhanced system processing error: {str(e)}"
    
    def _select_relevant_agents(self, user_query: str) -> List[str]:
        """智能选择相关专家（基于资产类型分类）"""
        selected = []
        
        # 第一步：识别资产类型
        asset_types = self.asset_classifier.classify_asset_types(user_query)
        
        print(f"\n[Asset Classifier] Identified asset types: {asset_types if asset_types else 'General RWA query'}")
        
        # 第二步：根据资产类型选择专家
        # 所有查询都需要RAG（检索知识库）
        selected.append("rag_expert")
        
        # 如果识别到具体资产类型，添加Solar RWA Specialist（目前通用）
        if asset_types:
            for asset_type in asset_types:
                asset_info = self.asset_classifier.get_asset_info(asset_type)
                print(f"  → {asset_info.get('name', asset_type)}")
            
            # 根据资产类型选择对应的专家
            if "solar" in asset_types:
                selected.append("solar_rwa_specialist")
            
            if "datacenter" in asset_types:
                selected.append("datacenter_rwa_specialist")
            
            if "warehouse" in asset_types:
                selected.append("warehouse_rwa_specialist")
            
            if "wind" in asset_types:
                selected.append("wind_rwa_specialist")
            
            if "ev_charging" in asset_types:
                selected.append("ev_charging_rwa_specialist")
        else:
            # 通用RWA查询，使用通用顾问
            selected.append("solar_rwa_specialist")  # 默认专家
        
        # 第三步：基于查询内容添加额外专家
        query_lower = user_query.lower()
        
        if any(keyword in query_lower for keyword in ["legal", "compliance", "regulation", "law", "license", "sfc"]):
            if "legal_compliance_specialist" not in selected:
                selected.append("legal_compliance_specialist")
        
        if any(keyword in query_lower for keyword in ["financial", "structure", "pricing", "investment", "return", "irr", "token"]):
            if "financial_structuring_specialist" not in selected:
                selected.append("financial_structuring_specialist")
        
        if any(keyword in query_lower for keyword in ["document", "file", "requirement"]):
            pass  # RAG已经包含，不重复
        
        if any(keyword in query_lower for keyword in ["market", "price", "current", "latest", "news", "policy"]):
            if "web_researcher" not in selected:
                selected.append("web_researcher")
        
        # RWA总顾问作为辅助（可选）
        if "rwa_advisor" not in selected:
            selected.append("rwa_advisor")
        
        # 确保至少有基础专家
        if not selected:
            selected = ["rag_expert", "rwa_advisor"]
        
        # 对于复杂查询，包含更多专家
        complex_indicators = ["prepare", "need", "requirement", "document", "process", "step"]
        if any(indicator in query_lower for indicator in complex_indicators):
            if "solar" in query_lower or "photovoltaic" in query_lower:
                # 光伏项目的完整专家团队
                selected.extend(["solar_rwa_specialist", "legal_compliance_specialist", "financial_structuring_specialist"])
        
        # 去重并返回
        return list(set(selected))
    
    def quick_consult(self, user_query: str) -> str:
        """快速咨询模式（不使用辩论）"""
        return self.enhanced_consult(user_query, use_debate=False)
    
    def expert_debate_consult(self, user_query: str) -> str:
        """专家辩论咨询模式"""
        return self.enhanced_consult(user_query, use_debate=True)
    
    def interactive_mode(self):
        """交互式问答模式"""
        print("\nEntering Interactive Mode (type 'quit' to exit)")
        print("Commands:")
        print("  - 'quick: [question]' for quick consultation")
        print("  - 'debate: [question]' for expert debate consultation")
        print("  - '[question]' for default enhanced consultation")
        print("-" * 80)
        
        while True:
            try:
                user_input = input("\nEnter your RWA question: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nThank you for using Enhanced RWA Consulting System!")
                    break
                
                if not user_input:
                    continue
                
                # 解析命令
                if user_input.startswith('quick:'):
                    query = user_input[6:].strip()
                    answer = self.quick_consult(query)
                elif user_input.startswith('debate:'):
                    query = user_input[7:].strip()
                    answer = self.expert_debate_consult(query)
                else:
                    answer = self.enhanced_consult(user_input)
                
                print(f"\n" + "="*80)
                print("CONSULTATION RESULT:")
                print("="*80)
                print(answer)
                print("="*80)
                
            except KeyboardInterrupt:
                print("\n\nThank you for using Enhanced RWA Consulting System!")
                break
            except Exception as e:
                print(f"\nProcessing error: {str(e)}")


def main():
    """主程序入口"""
    system = EnhancedRWAConsultingSystem()
    
    if len(sys.argv) > 1:
        # 命令行模式
        if sys.argv[1] == "quick":
            query = " ".join(sys.argv[2:])
            result = system.quick_consult(query)
        elif sys.argv[1] == "debate":
            query = " ".join(sys.argv[2:])
            result = system.expert_debate_consult(query)
        else:
            query = " ".join(sys.argv[1:])
            result = system.enhanced_consult(query)
            
        print(f"\nConsultation Result:")
        print("="*80)
        print(result)
    else:
        # 交互模式
        system.interactive_mode()


if __name__ == "__main__":
    main()
