import streamlit as st
from backend.rag_pipeline import get_rag_chain
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.rag_pipeline import get_rag_chain

st.set_page_config(page_title="🧙 AI Dungeon Master", layout="wide")
st.title("🧙 AI Dungeon Master - RAG RPG Adventure")

rag_chain = get_rag_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Your next move, adventurer...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = rag_chain.run(user_input)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})