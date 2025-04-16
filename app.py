''' 
Adecuación del modelo Ollama para Flask
'''
from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

def generate_response(model, prompt_model):
    ''' 
    Función para generar la respuesta del modelo
    '''
    options = {
        "temperature": 0.2,
        "top_p": 0.9,
        "max_tokens": 50
    }

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "Eres un lingüista poliglota con profundo respeto a las lenguas indígenas. "
                        "Tienes experiencia en traducir con precisión entre arawak y otros idiomas: "
                        "español, inglés, portugués, francés y japonés."
                    )
                },
                {
                    "role": "user", 
                    "content": prompt_model
                },
            ],
            options=options
        )
        translation = response['message']['content']
        print(translation)
        return render_template('index.html', translation=translation)
    except KeyError as k:
        error = f"Error: {str(k)}"
        return render_template('index.html', error=error)
    except TypeError as t:
        error = f"Error: {str(t)}"
        return render_template('index.html', error=error)

def promptEngineering(model, prompt_model):
    '''
    Construcción del prompt especializado para el modelo
    '''
    prompt_engineering = f"""
    # Componentes del Prompt 
    A continuación tienes la siguiente estructura que debes seguir. No son variables, es una plantilla de promptEngineering para que cumplas. Procura estrictamente No usar asteriscos (**), markdown, encabezados ni títulos como "Párrafo 1", "Notas", etc. Separa los párrafos en saltos de líneas para que sea atractivo visualmente.

    1. persona = "Actúa como un lingüista multilingüe con profundo respeto por las lenguas indígenas. Traduces entre arawak, español, inglés, portugués, francés y japonés."

    2. instrucción = (
      "Traduce el texto que se te dará al idioma solicitado. Detecta automáticamente el idioma de origen si no se especifica. "
      "Detecta el idioma de origen y tradúcelo al idioma solicitado. Presenta la respuesta separada en párrafos según el formato indicado."
    )

    3. contexto = (
         "La traducción debe conservar el significado cultural, espiritual y lingüístico del arawak en caso de estar involucrado. "
         "Debe ser clara para hablantes indígenas que no manejan lenguas coloniales, y útil para estudiantes o investigadores que aprenden arawak. "
         "Para otros idiomas, asegúrate de mantener precisión gramatical y sentido contextual."
    )

    4. data_format = (
        "Primer párrafo: Traducción precisa al idioma solicitado. No uses comillas ni encabezados."
        "Segundo párrafo: Notas gramaticales o de estilo si son necesarias."
        "No uses asteriscos (**), markdown, encabezados ni títulos como "Párrafo 1", "Notas", etc."
        "Solo separa con un salto de línea entre párrafos."
    )

    5. audiencia = (
        "Diseñado para hablantes que desean entender otros idiomas, y para personas externas interesadas en aprender o traducir con respeto lenguas como el arawak."
    )

    6. tono = "El tono debe ser respetuoso, claro, culturalmente consciente y accesible."
    
    Aplica lo anterior al siguiente texto: {prompt_model}.

    Para la respuesta, procura usar una cantidad menor a 40 tokens. Cumple todos los ítems anteriores de forma estricta.
    """
    return generate_response(model, prompt_engineering)

@app.route('/')
def home():
    ''' 
    Página de inicio de la aplicación Traductor
    '''
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    ''' 
    Función para obtener la respuesta del modelo Ollama
    '''
    model = 'llama3.2'
    prompt = request.form['text']
    language = request.form.get('languages')

    if language not in ['ES', 'EN', 'PT', 'FR', 'JP']:
        error = "Tienes que seleccionar un idioma. Intenta de nuevo."
        return render_template('index.html', error=error)

    prompt_model = f"Traduce el texto: '{prompt}' al siguiente idioma: '{language}'."
    print(prompt_model)
    return promptEngineering(model, prompt_model)

@app.route('/about')
def about():
    ''' 
    Página de información sobre Arawak
    '''
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
