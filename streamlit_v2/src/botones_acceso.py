import time

def palabraDia(st, create_prompt, llm, stream_text):
    """
    Función que actúa para que el modelo responda al presionar "palabra del día"
        Respuestas rápidas para mejorar la interactividad
    """
    st.session_state.palabraDia = 'Dame una palabra random en Arawak con su significado y uso en una oración.'
    prompt = create_prompt(st.session_state.palabraDia, st.session_state.language)

    st.session_state.message.append({"role": "user", "content": st.session_state.palabraDia})

    messages = [("system", prompt), ("human", st.session_state.palabraDia)]

    response = llm.invoke(messages)

    with st.chat_message("assistant", avatar=":material/network_intelligence:"):
        st.write_stream(stream_text(response.content))
        st.session_state.respuesta_palabraDia.append(response.content)
        
        st.session_state.message.append({"role": "assistant", "content": response.content})

def expliTribu(st, llm, stream_text):
    """
    Función que actúa como segundo botón, para conocer historia de la tribu
    """
    st.session_state.expliTribu = "Dame información sobre la tribu Arawak y su cultura."
    prompt = f"""Eres un experto antropólogo e historiador especializado en culturas indígenas de América. 
    Proporcióname una explicación clara, detallada y bien organizada sobre la tribu Arawak y su cultura. 
    Incluye información sobre su historia, ubicación geográfica, tradiciones, idioma, organización social, costumbres 
    y cualquier dato relevante que ayude a entender su importancia cultural y su legado actual.
    Estructura la respuesta en párrafos y usa un lenguaje accesible para un público general interesado en el tema.
    Cumpliendo lo que pide el usuario {st.session_state.expliTribu}
    """

    st.session_state.message.append({"role": "user", "content": st.session_state.expliTribu})

    messages = [("system", prompt), ("human", st.session_state.expliTribu)]

    with st.status(f"*Modelo pensando...*", expanded=True) as status:
        response = llm.invoke(messages)
        st.write("*🗒️ Buscando en NatGeographic...*")
        time.sleep(1)
        st.write("*:globe_with_meridians: Buscando en Google...*")
        time.sleep(1)
        st.write("*:chart_with_upwards_trend: Invirtiendo en Nvidia...*")
        time.sleep(1)
        st.write("*🧠 Generando respuesta sólida...*")
        time.sleep(1)
        status.update(label = "🤖 Búsqueda finalizada", expanded=False)

    if response: 
        with st.chat_message("assistant", avatar=":material/network_intelligence:"):
            st.write_stream(stream_text(response.content))
            st.session_state.respuesta_expliTribu.append(response.content)

            st.session_state.message.append({"role": "assistant", "content": response.content})

def adivinaPalabra(st, llm, stream_text):
    """
    Función que actúa como tercer botón para interactividad con el usuario y aprendizaje
    """
    st.session_state.adivinaPalabra = 'Dame un juego de opciones en donde tenga que Adivinar la palabra del Arawak.'
    prompt = f"""Partiendo del idioma del usuario {st.session_state.language}. Usa la información disponible en la base de datos vectorial (De momento usa tus conocimientos) y brinda toda tu respuesta en el idioma seleccionado por el usuario para ayudar a responder la siguiente consulta:
    Genera una palabra en Arawak con su significado y uso en una oración. Luego, proporciona varias opciones para que el usuario adivine cuál es la palabra correcta. Usa solo información que esté respaldada por los datos.
    """
    
    st.session_state.message.append({"role": "user", "content": st.session_state.adivinaPalabra})

    messages = [("system", prompt), ("human", st.session_state.adivinaPalabra)]

    response = llm.invoke(messages)

    with st.chat_message("assistant", avatar=":material/network_intelligence:"):
        st.write_stream(stream_text(response.content))
        st.session_state.respuesta_adivinaPalabra.append(response.content)

        st.session_state.message.append({"role": "assistant", "content": response.content})




""

