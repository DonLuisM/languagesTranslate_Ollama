"""
Funciones que manejan la lógica de los botones de acceso rápido en la aplicación Streamlit
"""
import time
import streamlit as st

def mostrar_status(llm, messages):
    """
    Muestra el estado del proceso mientras el modelo genera una respuesta
    """
    with st.status("*Modelo pensando...*", expanded=True) as status:
        response = llm.invoke(messages)
        st.write("*🗒️ Buscando en NatGeographic...*")
        time.sleep(1)
        st.write("*:globe_with_meridians: Buscando en Google...*")
        time.sleep(1)
        st.write("*:chart_with_upwards_trend: Invirtiendo en Nvidia...*")
        time.sleep(1)
        st.write("*🧠 Generando respuesta sólida...*")
        time.sleep(1)
        status.update(label="🤖 Búsqueda finalizada", expanded=False)
    return response

def palabra_dia(create_prompt, llm, stream_text):
    """
    Responde al botón 'Palabra del día' mostrando una palabra en Arawak con su significado
    """
    st.session_state.palabraDia = (
        "Dame una palabra random en Arawak con su significado y uso en una oración."
    )
    prompt = create_prompt(st.session_state.palabraDia, st.session_state.language)
    st.session_state.message.append({"role": "user", "content": st.session_state.palabraDia})

    messages = [("system", prompt), ("human", st.session_state.palabraDia)]
    response = mostrar_status(llm, messages)

    with st.chat_message("assistant", avatar=":material/translate:"):
        st.write_stream(stream_text(response.content))
        st.session_state.respuesta_palabraDia.append(response.content)
        st.session_state.message.append({"role": "assistant", "content": response.content})

def explicar_tribu(llm, stream_text):
    """
    Responde al botón para obtener información sobre la tribu Arawak
    """
    st.session_state.expliTribu = "Dame información sobre la tribu Arawak y su cultura."

    prompt = (
        f"""Eres un experto antropólogo e historiador
        especializado en culturas indígenas de América.
        Proporcióname una explicación clara, detallada y bien organizada sobre la tribu Arawak y su cultura.
        Incluye historia, ubicación geográfica, tradiciones, idioma, organización social y legado actual.
        Usa lenguaje accesible y párrafos bien estructurados.
        Consulta del usuario: {st.session_state.expliTribu}"""
    )

    st.session_state.message.append({"role": "user", "content": st.session_state.expliTribu})
    messages = [("system", prompt), ("human", st.session_state.expliTribu)]
    response = mostrar_status(llm, messages)

    if response:
        with st.chat_message("assistant", avatar=":material/translate:"):
            st.write_stream(stream_text(response.content))
            st.session_state.respuesta_expliTribu.append(response.content)
            st.session_state.message.append({"role": "assistant", "content": response.content})

def adivinar_palabra(llm, stream_text):
    """
    Responde al botón de juego para adivinar palabras en Arawak
    """
    st.session_state.adivinaPalabra = (
        "Dame un juego de opciones en donde tenga que Adivinar la palabra del Arawak."
    )

    prompt = (
        f"""Partiendo del idioma del usuario {st.session_state.language}.
        Genera una palabra en Arawak con su significado y uso en una oración.
        Luego, proporciona varias opciones para que el usuario adivine la palabra correcta.
        Usa solo información respaldada por datos."""
    )

    st.session_state.message.append({"role": "user", "content": st.session_state.adivinaPalabra})
    messages = [("system", prompt), ("human", st.session_state.adivinaPalabra)]
    response = mostrar_status(llm, messages)

    with st.chat_message("assistant", avatar=":material/translate:"):
        st.write_stream(stream_text(response.content))
        st.session_state.respuesta_adivinaPalabra.append(response.content)
        st.session_state.message.append({"role": "assistant", "content": response.content})
