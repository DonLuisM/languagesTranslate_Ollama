from langchain_ollama import ChatOllama
import streamlit as st
import ollama
from prompt_st import create_prompt

def list_models():
    models_running = ollama.list()['models']
    available_models = [model["model"] for model in models_running]
    return available_models

lista = list_models()

st.title('Ollama Comparativo Modelos Traductor')
st.write('Comparando distintas salidas de los modelos como traductores')

# Inicializar estado de sesión
if 'historial' not in st.session_state:
    st.session_state.historial = []

with st.sidebar:
    st.write('## Configuración de Parámetros')
    st.session_state.temperature = st.slider(
        'Temperatura',
        min_value=0.0,
        max_value=1.0,
        value=0.2,
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

# Mostrar modelos disponibles
st.write(f"### Modelos activos ({len(lista)}):")
st.write(lista)

language = st.selectbox(
    "A qué idioma deseas traducir?",
    ("Español", "Inglés", "Alemán", "Francés", "Italiano", "Arawak"),
)

user_input = st.chat_input('Escribe o pega el texto aquí')

if user_input:
    # Mostrar pregunta en un contenedor principal
    with st.container():
        with st.chat_message("user"):
            st.write(user_input)
        st.divider()

    # Crear contenedores en tabs dinámicas según cantidad de modelos
    tabs = st.tabs([model_name for model_name in lista])
    
    # Procesar cada modelo en paralelo
    for idx, model_name in enumerate(lista):
        with tabs[idx]:
            st.write(f"**Modelo:** `{model_name}`")
            
            try:
                # Configurar modelo específico
                llm = ChatOllama(
                    model=model_name,
                    temperature=st.session_state.temperature,
                    top_p=st.session_state.top_p,
                    top_k=st.session_state.top_k,
                    num_predict=st.session_state.max_tokens
                )
                
                prompt = create_prompt(model_name, user_input, language)
                messages = [
                    ("system", prompt),
                    ("human", user_input)
                ]
                
                # Generar y mostrar respuesta
                with st.spinner(f"*Pensando con {model_name}...*"):
                    response = llm.invoke(messages)
                    
                    st.write("**Respuesta:**")
                    st.write(response.content)
                    
                    # Metadata de la respuesta
                    st.caption(f"""
                    **Detalles Técnicos:**
                    - Tokens usados: {response.response_metadata['eval_count']}
                    - Tiempo respuesta: {response.response_metadata['total_duration'] / 1e9:.2f}s
                    - Modelo preciso: {response.response_metadata['model']}
                    """)
                    
                    # Guardar en historial
                    st.session_state.historial.append({
                        "modelo": model_name,
                        "pregunta": user_input,
                        "respuesta": response.content,
                        "metadata": response.response_metadata
                    })
                    
            except Exception as e:
                st.error(f"Error en {model_name}: {str(e)}")

# Sección de historial (opcional)
with st.expander("Ver historial completo"):
    for entry in st.session_state.historial:
        st.write(f"**Modelo:** {entry['modelo']}")
        st.write(f"**Pregunta:** {entry['pregunta']}")
        st.write(f"**Respuesta:** {entry['respuesta']}")
        st.divider()