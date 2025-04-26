from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

def create_vector_memory():
    embedding_model = OpenAIEmbeddings()
    docs = [Document(page_content="Initial context memory.")]
    vectorstore = FAISS.from_documents(docs, embedding_model)
    return vectorstore