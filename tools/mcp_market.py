import requests


def get_market_price(asset: str) -> str:
    symbol = asset.upper()
    try:
        # 使用 CoinGecko 简单公共接口作为示例
        if symbol == "BTC":
            coin = "bitcoin"
        elif symbol == "ETH":
            coin = "ethereum"
        else:
            coin = symbol.lower()
        url = (
            "https://api.coingecko.com/api/v3/simple/price?ids="
            f"{coin}&vs_currencies=usd"
        )
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            price = data.get(coin, {}).get("usd")
            if price is not None:
                return f"{symbol} 当前价格：${price}"
        return "获取行情失败"
    except Exception as e:
        return f"获取行情失败：{e}"


