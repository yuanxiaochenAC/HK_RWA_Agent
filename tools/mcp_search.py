"""
Google搜索和Web搜索工具
使用多个搜索引擎获取最新的在线信息
"""
import requests
from typing import List, Dict, Optional
import json

def search_web(query: str, num_results: int = 5) -> List[Dict[str, str]]:
    """
    使用多种方式进行网络搜索
    
    Args:
        query: 搜索查询
        num_results: 返回结果数量
        
    Returns:
        搜索结果列表，每个结果包含title, url, snippet
    """
    results = []
    
    # 方法1: 使用DuckDuckGo搜索（无需API key）
    try:
        from ddgs import DDGS
        
        print(f"  [Search] Searching web for: {query}")
        
        with DDGS() as ddgs:
            search_results = list(ddgs.text(query, max_results=num_results))
            
            for result in search_results:
                results.append({
                    'title': result.get('title', ''),
                    'url': result.get('href', ''),
                    'snippet': result.get('body', '')
                })
        
        print(f"  [Search] Found {len(results)} results")
        return results
        
    except ImportError:
        print("  [Search] DDGS library not installed, trying alternative...")
    except Exception as e:
        print(f"  [Search] DDGS search failed: {str(e)}")
    
    # 方法2: 使用Google搜索（备用方案，需要googlesearch-python）
    try:
        from googlesearch import search as google_search
        
        print(f"  [Search] Using Google search for: {query}")
        
        search_urls = list(google_search(query, num_results=num_results, lang='en'))
        
        for url in search_urls[:num_results]:
            results.append({
                'title': url,
                'url': url,
                'snippet': ''
            })
        
        print(f"  [Search] Found {len(results)} results")
        return results
        
    except ImportError:
        print("  [Search] Google search library not installed")
    except Exception as e:
        print(f"  [Search] Google search failed: {str(e)}")
    
    # 方法3: 使用SerpAPI（如果配置了API key）
    try:
        import os
        serpapi_key = os.getenv('SERPAPI_KEY')
        
        if serpapi_key:
            print(f"  [Search] Using SerpAPI for: {query}")
            
            url = "https://serpapi.com/search"
            params = {
                "q": query,
                "api_key": serpapi_key,
                "num": num_results,
                "engine": "google"
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                organic_results = data.get('organic_results', [])
                
                for result in organic_results[:num_results]:
                    results.append({
                        'title': result.get('title', ''),
                        'url': result.get('link', ''),
                        'snippet': result.get('snippet', '')
                    })
                
                print(f"  [Search] Found {len(results)} results")
                return results
    except Exception as e:
        print(f"  [Search] SerpAPI search failed: {str(e)}")
    
    # 如果所有方法都失败，返回模拟结果
    if not results:
        print("  [Search] All search methods failed, using fallback")
        results = [{
            'title': 'Search functionality requires additional setup',
            'url': '',
            'snippet': 'To enable real-time web search, please install: pip install duckduckgo-search'
        }]
    
    return results


def search_news(query: str, num_results: int = 5) -> List[Dict[str, str]]:
    """
    搜索新闻内容
    
    Args:
        query: 搜索查询
        num_results: 返回结果数量
        
    Returns:
        新闻结果列表
    """
    try:
        from ddgs import DDGS
        
        print(f"  [News Search] Searching news for: {query}")
        
        with DDGS() as ddgs:
            news_results = list(ddgs.news(query, max_results=num_results))
            
            results = []
            for result in news_results:
                results.append({
                    'title': result.get('title', ''),
                    'url': result.get('url', ''),
                    'snippet': result.get('body', ''),
                    'date': result.get('date', ''),
                    'source': result.get('source', '')
                })
            
            print(f"  [News Search] Found {len(results)} news items")
            return results
            
    except Exception as e:
        print(f"  [News Search] Failed: {str(e)}")
        return search_web(f"{query} news", num_results)


def search_rwa_info(topic: str) -> str:
    """
    搜索RWA相关信息的专用函数
    
    Args:
        topic: RWA相关主题
        
    Returns:
        格式化的搜索结果摘要
    """
    # 优化搜索查询
    search_query = f"Hong Kong RWA {topic} regulation 2025"
    
    results = search_web(search_query, num_results=5)
    
    if not results or (len(results) == 1 and 'requires additional setup' in results[0]['snippet']):
        return "Web search is not currently available. Please install search dependencies."
    
    # 格式化结果
    summary = f"Web Search Results for '{topic}':\n\n"
    
    for i, result in enumerate(results, 1):
        summary += f"{i}. {result['title']}\n"
        if result['snippet']:
            summary += f"   {result['snippet']}\n"
        if result['url']:
            summary += f"   Source: {result['url']}\n"
        summary += "\n"
    
    return summary


def search_regulatory_updates(jurisdiction: str = "Hong Kong") -> str:
    """
    搜索最新的监管更新
    
    Args:
        jurisdiction: 司法管辖区
        
    Returns:
        监管更新摘要
    """
    query = f"{jurisdiction} financial regulation updates 2025"
    
    results = search_news(query, num_results=5)
    
    if not results:
        results = search_web(query, num_results=5)
    
    summary = f"Latest Regulatory Updates - {jurisdiction}:\n\n"
    
    for i, result in enumerate(results, 1):
        summary += f"{i}. {result['title']}\n"
        if result.get('date'):
            summary += f"   Date: {result['date']}\n"
        if result['snippet']:
            summary += f"   {result['snippet']}\n"
        if result['url']:
            summary += f"   Source: {result['url']}\n"
        summary += "\n"
    
    return summary


if __name__ == "__main__":
    # 测试搜索功能
    print("Testing web search functionality...\n")
    
    # 测试1: 基本搜索
    print("Test 1: Basic search")
    results = search_web("Hong Kong RWA regulations", num_results=3)
    for r in results:
        print(f"  - {r['title']}")
    
    print("\n" + "="*60 + "\n")
    
    # 测试2: RWA信息搜索
    print("Test 2: RWA information search")
    info = search_rwa_info("stablecoin licensing")
    print(info[:500] + "...")
    
    print("\n" + "="*60 + "\n")
    
    # 测试3: 监管更新搜索
    print("Test 3: Regulatory updates")
    updates = search_regulatory_updates("Hong Kong")
    print(updates[:500] + "...")

