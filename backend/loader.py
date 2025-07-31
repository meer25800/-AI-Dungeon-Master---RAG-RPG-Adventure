import json
from pathlib import Path
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

DATA_DIR = Path("data/fetched/")

def json_to_documents(json_file: str, key_fields: list):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    docs = []
    for entry in data:
        content = "\n".join([f"{k.capitalize()}: {entry.get(k, '')}" for k in key_fields])
        docs.append(Document(page_content=content))
    return docs

def load_and_embed():
    all_docs = []
    all_docs += json_to_documents(DATA_DIR / "spells.json", ["name", "desc", "range", "duration", "level"])
    all_docs += json_to_documents(DATA_DIR / "monsters.json", ["name", "type", "alignment", "size"])
    all_docs += json_to_documents(DATA_DIR / "magicitems.json", ["name", "type", "desc"])

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(all_docs)

    vectordb = Chroma.from_documents(split_docs, OpenAIEmbeddings(), persist_directory="chroma_db")
    vectordb.persist()

if __name__ == "__main__":
    load_and_embed()