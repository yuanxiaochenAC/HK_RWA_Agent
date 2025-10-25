import requests


def get_eth_block_number() -> str:
    try:
        # 例：使用 Cloudflare Ethereum Gateway 的公开 JSON-RPC
        url = "https://cloudflare-eth.com"
        payload = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
        resp = requests.post(url, json=payload, timeout=10)
        if resp.status_code == 200:
            result = resp.json().get("result")
            if result:
                height = int(result, 16)
                return f"以太坊当前区块高度：{height}"
        return "获取区块信息失败"
    except Exception as e:
        return f"获取区块信息失败：{e}"




