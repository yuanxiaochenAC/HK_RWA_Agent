"""
联网研究员Agent - 负责获取最新的市场和政策信息
集成Google搜索和实时网络数据
"""
from typing import List, Dict, Optional
import requests
from openai import OpenAI
from tools.mcp_market import get_market_price
from tools.mcp_chain import get_eth_block_number
from tools.mcp_search import search_web, search_news, search_rwa_info, search_regulatory_updates

class WebResearcherAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "联网研究员"
        self.description = "查询最新政策、市场数据、新闻动态和实时信息"
    
    def research_topic(self, query: str) -> str:
        """根据查询主题进行联网研究"""
        # 分析查询类型
        research_plan = self._analyze_research_needs(query)
        
        results = []
        
        # 执行不同类型的查询
        if research_plan.get("need_market_data"):
            market_data = self._get_market_information(query)
            if market_data:
                results.append(f"【市场数据】\n{market_data}")
        
        if research_plan.get("need_blockchain_data"):
            blockchain_data = self._get_blockchain_information()
            if blockchain_data:
                results.append(f"【区块链数据】\n{blockchain_data}")
        
        # 新增：网络搜索功能
        if research_plan.get("need_web_search"):
            web_results = self._perform_web_search(query)
            if web_results:
                results.append(f"【网络搜索结果】\n{web_results}")
        
        if research_plan.get("need_news_research"):
            news_summary = self._get_regulatory_news(query)
            results.append(f"【监管动态】\n{news_summary}")
        
        # 整合研究结果
        if results:
            return "\n\n".join(results)
        else:
            return "未找到相关的最新信息"
    
    def _analyze_research_needs(self, query: str) -> Dict[str, bool]:
        """分析查询需要哪些类型的联网研究"""
        query_lower = query.lower()
        
        return {
            "need_market_data": any(keyword in query_lower for keyword in 
                                  ["价格", "市值", "btc", "eth", "价", "行情", "汇率", "price", "market"]),
            "need_blockchain_data": any(keyword in query_lower for keyword in 
                                      ["区块", "链上", "以太坊", "交易", "智能合约", "blockchain", "ethereum"]),
            "need_web_search": any(keyword in query_lower for keyword in
                                 ["最新", "latest", "recent", "news", "update", "新闻", "政策"]),
            "need_news_research": True  # 默认都需要政策研究
        }
    
    def _get_market_information(self, query: str) -> Optional[str]:
        """获取市场数据信息"""
        try:
            results = []
            
            # 检查是否询问特定币种
            if "btc" in query.lower() or "比特币" in query:
                btc_price = get_market_price("BTC")
                results.append(btc_price)
            
            if "eth" in query.lower() or "以太坊" in query:
                eth_price = get_market_price("ETH")
                results.append(eth_price)
            
            # 如果没有特定币种，提供BTC作为参考
            if not results:
                btc_price = get_market_price("BTC")
                results.append(f"加密货币市场参考：{btc_price}")
            
            return "\n".join(results)
        except Exception as e:
            return f"市场数据获取失败：{str(e)}"
    
    def _get_blockchain_information(self) -> Optional[str]:
        """获取区块链相关信息"""
        try:
            block_info = get_eth_block_number()
            return block_info
        except Exception as e:
            return f"区块链数据获取失败：{str(e)}"
    
    def _perform_web_search(self, query: str) -> str:
        """执行实时网络搜索"""
        try:
            print(f"\n[Web Researcher] Performing web search for: {query}")
            
            # 优化RWA相关查询
            if any(keyword in query.lower() for keyword in ['rwa', 'tokenization', 'stablecoin', 'hong kong']):
                results = search_rwa_info(query)
            else:
                results = search_web(query, num_results=5)
                
                # 格式化搜索结果
                if isinstance(results, list):
                    formatted_results = ""
                    for i, result in enumerate(results, 1):
                        formatted_results += f"{i}. {result.get('title', 'No title')}\n"
                        if result.get('snippet'):
                            formatted_results += f"   {result['snippet']}\n"
                        if result.get('url'):
                            formatted_results += f"   URL: {result['url']}\n"
                        formatted_results += "\n"
                    results = formatted_results
            
            return results
            
        except Exception as e:
            return f"Web search failed: {str(e)}\nNote: To enable web search, install: pip install duckduckgo-search"
    
    def _get_regulatory_news(self, query: str) -> str:
        """获取监管新闻和更新"""
        try:
            print(f"\n[Web Researcher] Searching regulatory news for: {query}")
            
            # 尝试获取最新监管更新
            news_results = search_regulatory_updates("Hong Kong")
            
            if news_results and "requires additional setup" not in news_results.lower():
                return news_results
            
            # 如果网络搜索不可用，回退到LLM分析
            return self._simulate_policy_analysis(query)
            
        except Exception as e:
            print(f"[Web Researcher] News search failed: {str(e)}")
            return self._simulate_policy_analysis(query)
    
    def _simulate_policy_analysis(self, query: str) -> str:
        """基于LLM的政策分析（备用方案）"""
        system_prompt = """
You are a financial policy research expert. Provide latest policy trend analysis based on the query.

Focus on:
1. Hong Kong financial regulation trends
2. RWA and stablecoin regulatory developments
3. Potential policy impacts
4. Note that this is analysis based on known information

Provide concise but professional policy summary.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Query: {query}"}
                ],
                temperature=0.3,
                max_tokens=800
            )
            
            analysis = response.choices[0].message.content
            disclaimer = "\n\nNote: The above analysis is based on known policies and trends. For the latest official updates, please check the Hong Kong Monetary Authority website."
            
            return analysis + disclaimer
            
        except Exception as e:
            return f"Policy analysis failed: {str(e)}"
    
    def get_capabilities(self) -> List[str]:
        """返回该Agent的能力描述"""
        return [
            "Real-time web search (Google/DuckDuckGo)",
            "Latest regulatory news and updates",
            "Cryptocurrency market prices",
            "Blockchain network status",
            "Policy trend analysis",
            "Financial data and exchange rates"
        ]
