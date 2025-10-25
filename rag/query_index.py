import os
from typing import List

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


INDEX_DIR = "rag/faiss_index"


def _load_index() -> FAISS:
    if not os.path.isdir(INDEX_DIR):
        raise RuntimeError("RAG 索引未构建。请先运行 python rag/build_index.py")
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)


def rag_search(query: str, k: int = 5) -> str:
    vs = _load_index()
    docs: List = vs.similarity_search(query, k=k)
    if not docs:
        return "未检索到相关内容"
    snippets = []
    for i, d in enumerate(docs, 1):
        meta = d.metadata or {}
        source = meta.get("source", "unknown")
        snippets.append(f"[片段{i}] 来源: {source}\n{d.page_content.strip()}")
    return "\n\n".join(snippets)




