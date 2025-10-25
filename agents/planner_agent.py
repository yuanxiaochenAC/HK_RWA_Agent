from typing import List, Dict


def plan(query: str) -> List[Dict]:
    lowered = query.lower()
    tasks: List[Dict] = []

    # 简单路由：包含与监管、白皮书、要点等关键词 -> RAG
    rag_keywords = [
        "rwa",
        "白皮书",
        "监管",
        "合规",
        "政策",
        "香港",
        "stablecoin",
        "稳定币",
        "指引",
        "通告",
    ]

    if any(k in lowered for k in rag_keywords):
        tasks.append({"type": "rag", "query": query})

    # 市场价格关键词 -> 联网工具
    market_keywords = ["btc", "eth", "价格", "行情", "price", "symbol"]
    if any(k in lowered for k in market_keywords):
        # 默认识别BTC，简单解析
        symbol = "BTC"
        if "eth" in lowered:
            symbol = "ETH"
        tasks.append({"type": "market", "symbol": symbol})

    if not tasks:
        tasks.append({"type": "rag", "query": query})

    return tasks




