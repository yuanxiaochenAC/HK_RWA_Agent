from typing import Dict

from rag.query_index import rag_search
from tools.mcp_market import get_market_price


def execute(task: Dict) -> str:
    task_type = task.get("type")
    if task_type == "rag":
        query = task.get("query", "")
        return rag_search(query)
    if task_type == "market":
        symbol = task.get("symbol", "BTC")
        return get_market_price(symbol)
    return "未知任务类型"




