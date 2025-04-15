from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

CHROMA_PATH = "chroma_index"
DOCS_PATH = "./agile_docs/"

def create_vector_store():
    loader = UnstructuredFileLoader(DOCS_PATH)
    docs = loader.load()
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=CHROMA_PATH)
    vectordb.persist()

def answer_question_from_documents(question: str) -> str:
    vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings())
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)
    return qa_chain.run(question)