import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def build_index(source_dir: str = "data/docs", index_dir: str = "rag/faiss_index") -> None:
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs("rag", exist_ok=True)

    loader = DirectoryLoader(source_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vs = FAISS.from_documents(texts, embeddings)
    vs.save_local(index_dir)


if __name__ == "__main__":
    build_index()


