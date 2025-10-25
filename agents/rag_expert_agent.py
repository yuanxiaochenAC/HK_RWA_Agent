"""
RAG专家Agent - 专门负责查询本地文档数据库
"""
from typing import List, Dict
from openai import OpenAI
from rag.query_index import rag_search

class RAGExpertAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "RAG专家"
        self.description = "专门查询香港RWA监管文档、法规指引和政策文件"
    
    def search_documents(self, query: str) -> str:
        """在文档库中搜索相关信息"""
        try:
            # 首先进行RAG检索
            raw_results = rag_search(query, k=8)
            
            # 使用LLM提炼和总结检索结果
            refined_answer = self._refine_search_results(query, raw_results)
            return refined_answer
            
        except Exception as e:
            return f"文档查询出现错误：{str(e)}"
    
    def _refine_search_results(self, query: str, raw_results: str) -> str:
        """使用LLM提炼RAG检索结果"""
        system_prompt = """
你是香港RWA监管专家，请基于检索到的文档片段，为用户提供准确的监管信息。

任务：
1. 分析检索到的文档内容
2. 提取与用户问题相关的关键信息
3. 按重要性排序并结构化呈现
4. 指出信息来源（文档名称）
5. 如果信息不完整，明确说明

回答要求：
- 准确引用监管条款
- 突出重点要求和注意事项  
- 保持专业和客观
- 避免过度解读或猜测
"""
        
        user_content = f"""
用户问题：{query}

检索到的文档内容：
{raw_results}

请基于以上文档内容，提供专业的监管信息总结。
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.2,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"文档分析出现错误：{str(e)}\n\n原始检索结果：\n{raw_results}"
    
    def get_capabilities(self) -> List[str]:
        """返回该Agent的能力描述"""
        return [
            "查询香港稳定币监管法规",
            "检索RWA发行指引文件", 
            "查找合规要求和申请程序",
            "获取监管机构联系方式",
            "查询历史政策变更记录"
        ]


