#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RWA智能咨询系统 - 命令行运行接口
Enhanced Multi-Agent RWA Consultation System - CLI Interface

使用方法 Usage:
# 🔍 单次查询模式 Single Query Mode
python run_rwa_consultant.py --query "I have a solar company project and want to issue RWA in Hong Kong. What documents do I need?"

# 💬 交互式模式 Interactive Mode  
python run_rwa_consultant.py

# 🚀 专家辩论模式 Expert Debate Mode
python run_rwa_consultant.py --query "50MW solar farm RWA tokenization requirements" --debate

# ⚡ 快速咨询模式 Quick Consultation Mode
python run_rwa_consultant.py --query "Hong Kong RWA regulations" --quick
"""

import argparse
import sys
import os
import io
from typing import Optional

# 设置UTF-8编码环境变量，解决Windows GBK编码问题
os.environ['PYTHONIOENCODING'] = 'utf-8'

def setup_environment():
    """设置环境和API密钥"""
    try:
        # 设置编码
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        
        # 设置API密钥
        if os.path.exists('openai_api_key.txt'):
            with open('openai_api_key.txt', 'r') as f:
                os.environ['OPENAI_API_KEY'] = f.read().strip()
            print("API key configured successfully")
        else:
            print("Warning: openai_api_key.txt not found")
            return False
        
        return True
    except Exception as e:
        print(f"Environment setup failed: {e}")
        return False

def print_banner():
    """打印欢迎横幅"""
    banner = """
================================================================================
                      RWA INTELLIGENT CONSULTATION SYSTEM                     
                       Enhanced Multi-Agent Expert System                      
================================================================================
  Expert Panel:                                                           
    - Solar RWA Specialist      - Solar project tokenization expert              
    - Legal Compliance Expert   - Hong Kong regulations specialist                                 
    - Financial Structuring     - Investment structure designer                             
    - RAG Document Expert       - Document retrieval specialist                                 
    - Web Research Agent        - Real-time information researcher                                   
    - Multi-Agent Debate System - Expert consensus builder                                 
================================================================================
"""
    print(banner)

def print_help():
    """打印帮助信息"""
    help_text = """
Usage Examples:

[1] Single Query Mode:
   python run_rwa_consultant.py --query "Your RWA question here"
   
[2] Expert Debate Mode:
   python run_rwa_consultant.py --query "Your question" --debate
   
[3] Quick Mode:
   python run_rwa_consultant.py --query "Your question" --quick
   
[4] Interactive Mode:
   python run_rwa_consultant.py

Sample Queries:
   - "I have a solar project and want to issue RWA tokens in Hong Kong"
   - "What legal documents are required for RWA issuance?"
   - "How to structure a 50MW solar farm tokenization?"
   - "Hong Kong regulatory requirements for digital assets"
   
Tips:
   - Use --debate for complex queries requiring expert discussion
   - Use --quick for simple factual questions
   - Interactive mode allows multiple questions in one session
"""
    print(help_text)

def run_single_query(query: str, mode: str = "enhanced"):
    """运行单次查询"""
    try:
        from main import EnhancedRWAConsultingSystem
        
        print(f"Initializing RWA Consultation System...")
        system = EnhancedRWAConsultingSystem()
        
        print(f"Processing Query: {query}")
        print(f"Mode: {mode.upper()}")
        print("=" * 100)
        
        if mode == "debate":
            result = system.expert_debate_consult(query)
        elif mode == "quick":
            result = system.quick_consult(query)
        else:
            result = system.enhanced_consult(query)
        
        print("\nCONSULTATION RESULT:")
        print("=" * 100)
        print(result)
        print("=" * 100)
        
        return True
        
    except Exception as e:
        print(f"Query processing failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_interactive_mode():
    """运行交互式模式"""
    try:
        from main import EnhancedRWAConsultingSystem
        
        print("Initializing Enhanced RWA Consultation System...")
        system = EnhancedRWAConsultingSystem()
        
        print("\nINTERACTIVE CONSULTATION MODE")
        print("=" * 100)
        print("Commands:")
        print("  - Enter your question directly")
        print("  - 'debate: [question]' for expert debate mode")
        print("  - 'quick: [question]' for quick consultation")
        print("  - 'help' for guidance")
        print("  - 'quit' or 'exit' to leave")
        print("=" * 100)
        
        session_count = 0
        
        while True:
            try:
                session_count += 1
                user_input = input(f"\n[Q{session_count}] Enter your RWA question: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nThank you for using RWA Consultation System!")
                    break
                    
                if user_input.lower() == 'help':
                    print_help()
                    continue
                
                # 解析命令
                if user_input.startswith('debate:'):
                    query = user_input[7:].strip()
                    mode = "debate"
                elif user_input.startswith('quick:'):
                    query = user_input[6:].strip()
                    mode = "quick"
                else:
                    query = user_input
                    mode = "enhanced"
                
                print(f"\nProcessing in {mode.upper()} mode...")
                
                if mode == "debate":
                    result = system.expert_debate_consult(query)
                elif mode == "quick":
                    result = system.quick_consult(query)
                else:
                    result = system.enhanced_consult(query)
                
                print(f"\nCONSULTATION RESULT [{mode.upper()}]:")
                print("=" * 100)
                print(result)
                print("=" * 100)
                
            except KeyboardInterrupt:
                print("\n\nSession interrupted. Thank you for using RWA Consultation System!")
                break
            except Exception as e:
                print(f"Error processing query: {e}")
                continue
        
        return True
        
    except Exception as e:
        print(f"Interactive mode failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主程序入口"""
    parser = argparse.ArgumentParser(
        description="RWA Intelligent Consultation System - 多Agent智能RWA咨询系统",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_rwa_consultant.py --query "Solar RWA issuance requirements"
  python run_rwa_consultant.py --query "Hong Kong regulations" --debate
  python run_rwa_consultant.py --query "Quick RWA info" --quick
  python run_rwa_consultant.py  # Interactive mode
        """
    )
    
    parser.add_argument(
        '--query', '-q',
        type=str,
        help='RWA consultation query (single query mode)'
    )
    
    parser.add_argument(
        '--debate', 
        action='store_true',
        help='Enable expert debate mode for comprehensive analysis'
    )
    
    parser.add_argument(
        '--quick',
        action='store_true', 
        help='Enable quick consultation mode for simple queries'
    )
    
    parser.add_argument(
        '--help-examples',
        action='store_true',
        help='Show usage examples and sample queries'
    )
    
    args = parser.parse_args()
    
    # 显示帮助示例
    if args.help_examples:
        print_help()
        return
    
    # 打印横幅
    print_banner()
    
    # 设置环境
    if not setup_environment():
        print("Please ensure openai_api_key.txt exists with your OpenAI API key")
        return
    
    try:
        # 确定运行模式
        if args.query:
            # 单次查询模式
            if args.debate and args.quick:
                print("Error: Cannot use both --debate and --quick simultaneously")
                return
                
            mode = "debate" if args.debate else "quick" if args.quick else "enhanced"
            success = run_single_query(args.query, mode)
            
        else:
            # 交互式模式
            if args.debate or args.quick:
                print("Note: --debate and --quick flags ignored in interactive mode")
                print("      Use 'debate: [question]' or 'quick: [question]' commands instead")
            
            success = run_interactive_mode()
        
        if not success:
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
