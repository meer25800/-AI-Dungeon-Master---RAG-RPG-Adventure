from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

def get_rag_chain():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)