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
    '''
    Función para inicializar el estado de la conversación y memoria del bot
    '''
    if 'chats' not in st.session_state:
        st.session_state.chats = {}

    if 'chat_actual' not in st.session_state or st.session_state.chat_actual not in st.session_state.chats:
        chat_id = str(uuid.uuid4())[:8]
        bienvenida = {
            "role": "assistant",
            "content": """
            Bienvenido humano, soy LEXIWAK tu asistente de traducción con conocimientos en la lengua indígena Arawak. 
            \n\n ¿Deseas aprender una palabra en Arawak?
            """
        }
        st.session_state.chats[chat_id] = {
            "memory": ConversationBufferMemory(memory_key="chat_history", input_key="input", return_messages=True),
            "historial": [bienvenida],
            "nombre": f"Chat #{len(st.session_state.chats) + 1}"
        }
        st.session_state.chat_actual = chat_id
        st.session_state.message = [bienvenida]

def get_chat_actual():
    '''
    Función para obtener el chat actual del usuario
    '''
    return st.session_state.chats[st.session_state.chat_actual]