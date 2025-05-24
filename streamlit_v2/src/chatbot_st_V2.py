import time
import os
import sys
import ollama
import uuid
import streamlit as st
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from streamlit_V1.prompt_st import create_prompt
from persistencia_memoria import init_chats, get_chat_actual, promptHistorial
from botones_acceso import palabraDia, expliTribu, adivinaPalabra

# * ------------ Funciones -----------
def stream_text(text):
    '''
    Función para hacer lograr el correcto funcionamiento del st.write_stream 
    '''
    for word in text:
        yield word
        time.sleep(0.022)
  
def clc_chat_history():
    '''
    Función para limpiar el historial a partir del botón
    '''
    st.session_state.message = [{
        "role": "assistant",
        "content": """
        Bienvenido humano, soy LEXIWAK tu asistente de traducción con conocimientos en la lengua indígena Arawak. 
        \n\n ¿Deseas aprender una palabra en Arawak?"""
    }]
    st.session_state.language = "Español"
    st.session_state.respuesta_palabraDia = []
    st.session_state.respuesta_expliTribu = []
    st.session_state.respuesta_adivinaPalabra = []
     
def clc_history():
    '''
    Función para limpiar el historial o carpetas de chats
    '''
    st.session_state.message = [{
        "role": "assistant",
        "content": "Bienvenido humano, soy LEXIWAK tu asistente de traducción con conocimientos en la lengua indígena Arawak. \n\n ¿Deseas aprender una palabra en Arawak?"
    }]
    st.session_state.chats = {}
    st.session_state.chat_actual = None
    st.toast("Historial limpiado. Crea un nuevo chat para continuar.")
    st.session_state.respuesta_palabraDia = []
    st.session_state.respuesta_expliTribu = []
    st.session_state.respuesta_adivinaPalabra = []
    
def list_models():
    '''
    Función para enlistar los modelos de ollama locales
    '''
    models_running = ollama.list()['models']
    available_models = [model["model"] for model in models_running]
    return available_models

lista = list_models()

def roles():
    '''
    Función para definir los roles del usuario y asistente
    '''
    for message in st.session_state.message:
        role = message.get("role", "")
        content = message.get("content", "")

        if role == "user":
            with st.chat_message("user", avatar=":material/emoji_people:"):
                st.write(content)
        elif role == "assistant":
            with st.chat_message("assistant", avatar=":material/translate:"):
                st.write(content)

# * --------------------------------------------------------
st.set_page_config(page_title="LEXIWAK-BOT", page_icon="🌎")

init_chats()

if "message" not in st.session_state:
    st.session_state.message = [{
        "role": "assistant", 
        "content": """
        Bienvenido humano, soy LEXIWAK tu asistente de traducción con conocimientos en la lengua indígena Arawak. 
        \n\n ¿Deseas aprender una palabra en Arawak?
        """
    }]

if "language" not in st.session_state:
    st.session_state.language = "Español"
    
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "respuesta_palabraDia" not in st.session_state:
    st.session_state.respuesta_palabraDia = []

if "respuesta_expliTribu" not in st.session_state:
    st.session_state.respuesta_expliTribu = []

if "respuesta_adivinaPalabra" not in st.session_state:
    st.session_state.respuesta_adivinaPalabra = []

# * Configuración barra lateral (Configuración parámetros)
roles()

with st.sidebar:
    st.title('🤖 Configuración LEXIWAK')

    left, right = st.columns(2)
    if left.button('Nuevo chat', icon="🗒️", use_container_width=True, on_click=clc_chat_history):
        new_id = str(uuid.uuid4())[:8]
        bienvenida = {
            "role": "assistant",
            "content": """
            Bienvenido humano, soy LEXIWAK tu asistente de traducción con conocimientos en la lengua indígena Arawak. 
            \n\n ¿Deseas aprender una palabra en Arawak?
            """
        }
        st.session_state.chat_actual = new_id
        st.session_state.chats[new_id] = {
            "memory": ConversationBufferMemory(memory_key="chat_history", input_key="input", return_messages=True),
            "historial": [bienvenida],
        }
        st.session_state.message = [bienvenida]
        st.session_state.nuevo_chat_id = new_id
        st.toast("✅ Nuevo chat iniciado.")

    with right.popover("Config.", icon="⚙️"):
        st.session_state.model = st.selectbox(
            'Elije el modelo', 
            lista
        )
        st.session_state.temperature = st.slider(
            'Temperatura',
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1
        )
        st.session_state.top_p = st.slider(
            'Top P',
            min_value=0.0,
            max_value=1.0,
            value=0.9,
            step=0.1
        )
        st.session_state.top_k = st.slider(
            'Top K',
            min_value=0,
            max_value=100,
            value=50,
            step=1
        )
        st.session_state.max_tokens = st.slider(
            'Max Tokens',
            min_value=1,
            max_value=4096,
            value=256,
            step=1
        )
        st.info("Docs: selecciona el archivo al lado izquierdo en el navegador lateral.\n\n Imgs: selecciona el logo de clip **(En proceso de prueba)**", icon=":material/help:", width="stretch")

    st.divider()

    st.session_state.language = st.selectbox(
        "A qué idioma deseas traducir?", 
        ("Español", "Inglés", "Alemán", "Francés", "Italiano", "Arawak")
    )
    
    with st.form("Sube tu archivo", clear_on_submit=True):
        upload_file = st.file_uploader(
            "Sube tu archivo PDF",
            accept_multiple_files=False,
            type = ['pdf'],
        )

        submitted_file = st.form_submit_button("Subir archivo")

        if submitted_file and upload_file is not None:
            st.write(f"Archivo subido: *{upload_file.name}*")

            filepath = os.path.join("data/", upload_file.name)
            with open(filepath, "wb") as f:
                f.write(upload_file.getbuffer())

            with st.spinner("*Leyendo documento...*"):
                # vector = rag_function(filepath)
                # st.session_state.pdf_vector = vector
                # st.session_state.pdf_loaded = True
                st.success("Cargado con éxito")

    st.divider()

    if not st.button("Limpiar historial", icon="🖌️", on_click=clc_history):
        st.info(f"Nuevo chat creado: {st.session_state.nuevo_chat_id}")

    for chat_id in st.session_state.chats:
        if st.button(f"🗂️ Chat {chat_id}",  use_container_width=True, key=chat_id):
            st.session_state.chat_actual = chat_id
            st.session_state.message = st.session_state.chats[chat_id]["historial"].copy()
            st.toast(f"📂 Cargado chat {chat_id}")


# * Configuración del user_input y respuesta del modelo
modeloLLM = st.session_state.model

llm = ChatOllama(model=modeloLLM)

user_input = st.chat_input(
    'Escribe que deseas saber del documento',
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)

# * Configuración de los botones de rápido acceso
if user_input is None:
    cols = st.columns(3)

    if cols[0].button("📘 Conoce la palabra del día en Arawak", use_container_width=True):
        palabraDia(st, create_prompt, llm, stream_text)
    
    if cols[1].button("🌎 Explicame acerca de la tribu Arawak", use_container_width=True):
        expliTribu(st, llm, stream_text)
    
    if cols[2].button("❓Adivina la siguiente palabra del Arawak", use_container_width=True):
        adivinaPalabra(st, llm, stream_text)

# * Configuración del texto de entrada para usuario
# * Procesar entrada del usuario con memoria

# Obtener el chat actual (memoria e historial)
chat = get_chat_actual()
memory = chat["memory"]
historial = chat["historial"]

if user_input and user_input.text:
    with st.chat_message("user", avatar=":material/emoji_people:"):
        st.write(user_input.text)
  
    historial.append({"role": "user", "content": user_input.text})
    st.session_state.message.append({"role": "user", "content": user_input.text})

    try:
        # * Configurar modelo con parámetros actuales
        llm = ChatOllama(
            model=st.session_state.model,
            temperature=st.session_state.temperature,
            top_p=st.session_state.top_p,
            top_k=st.session_state.top_k,
            num_predict=st.session_state.max_tokens
        )

        # * Usar prompt con memoria de conversación
        chain = LLMChain(llm=llm, prompt=promptHistorial, memory=memory)

        # * Mensajes de carga
        with st.status(f"*Modelo {st.session_state.model} pensando...*", expanded=True) as status:
            response = chain.invoke({"input": user_input.text})["text"]
            
            st.write("*🗒️ Procesando información...*")
            time.sleep(1)
            st.write("*:bar_chart: Buscando en la Base de Datos...*")
            time.sleep(1)
            st.write("*🍕 Pidiendo pizza...*")
            time.sleep(1)
            st.write("*📲 Llamando a Siri...*")
            time.sleep(1)
            st.write("*:chart_with_upwards_trend: Buscando relaciones...*")
            time.sleep(1)
            st.write("*🧠 Generando respuesta sólida...*")
            time.sleep(1)
            status.update(label="🤖 Respuesta generada", expanded=False)

        if response:
            with st.chat_message("assistant", avatar=":material/translate:"):
                st.write_stream(stream_text(response))
                
            historial.append({"role": "assistant", "content": response})
            st.session_state.message.append({"role": "assistant", "content": response})
            
    except Exception as e:
        st.error(f"Error en {st.session_state.model}: {str(e)}")
