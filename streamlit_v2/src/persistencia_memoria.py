from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
import streamlit as st
import uuid

# Crear prompt
# prompt = PromptTemplate.from_template("""
# Historial de conversación:
# {chat_history}

# Usuario: {input}
# Asistente:
# """)

def init_chats(session_state):
    """
    
    """
    if "chats" not in session_state:
        session_state.chats = {}

    if "chat_actual" not in session_state:
        chat_id = str(uuid.uuid4())[:8]
        session_state.chats[chat_id] = {
            "memory": ConversationBufferMemory(memory_key="chat_history", input_key="input", return_messages=True),
            "historial": [],
            "nombre": "Chat"
        }
        session_state.chat_actual = chat_id
    
# Sidebar: seleccionar o crear chats
# with st.sidebar:
#     st.title("💬 Chats")
#     # Lista de chats
#     for cid, chat in st.session_state.chats.items():
#         if st.button(chat["nombre"], key=cid):
#             st.session_state.chat_actual = cid

#     if st.button("Nuevo Chat Ji"):
#         new_id = str(uuid.uuid4())[:8]
#         st.session_state.chats[new_id] = {
#             "memory": ConversationBufferMemory(memory_key="chat_history", input_key="input", return_messages=True),
#             "historial": [],
#             "nombre": f"Chat {len(st.session_state.chats)+1}"
#         }
#         st.session_state.chat_actual = new_id

#     st.write("---")
#     st.write("📌 Chat activo:", st.session_state.chats[st.session_state.chat_actual]["nombre"])

# # Configuración modelo
# llm = ChatOllama(
#     model="qwen3:latest",
#     temperature=0.4,
#     num_predict=256,
# )

# # Obtener memoria e historial del chat actual
# chat = st.session_state.chats[st.session_state.chat_actual]
# memory = chat["memory"]
# historial = chat["historial"]

# # Mostrar historial en pantalla
# st.title(chat["nombre"])
# for mensaje in historial:
#     with st.chat_message(mensaje["role"]):
#         st.write(mensaje["content"])

# # Input del usuario
# user_input = st.chat_input("Escribe algo...")

# if user_input:
#     historial.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.write(user_input)

#     chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
#     with st.spinner("Pensando..."):
#         try:
#             result = chain.invoke({"input": user_input})
#             respuesta = result["text"]
#             historial.append({"role": "assistant", "content": respuesta})

#             with st.chat_message("assistant"):
#                 st.write(respuesta)
#         except Exception as e:
#             st.error(f"❌ Error: {e}")
