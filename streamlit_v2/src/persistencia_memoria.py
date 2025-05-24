from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
import uuid
import streamlit as st

promptHistorial = PromptTemplate.from_template("""
Historial de conversación:
{chat_history}

Usuario: {input}
Asistente:
""")

def init_chats():

    if "chat_actual" not in st.session_state:
        chat_id = str(uuid.uuid4())[:8]
        st.session_state.chats[chat_id] = {
            "memory": ConversationBufferMemory(memory_key="chat_history", input_key="input", return_messages=True),
            "historial": [],
            "nombre": f"Chat #{len(st.session_state.chats) + 1}"
        }
        st.session_state.chat_actual = chat_id

def get_chat_actual():
    return st.session_state.chats[st.session_state.chat_actual]