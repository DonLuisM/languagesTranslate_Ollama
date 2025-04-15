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
                        "Tienes experiencia en traducir con precisión entre arawak y otros idiomas:" 
                        "español,inglés,portugués,francés y japonés.")
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
    promptEngineering = f"""
    Con la información obtenida del {prompt_model}, cumple las siguientes funciones/abarca los componentes
    # Componentes del Prompt (No tengas en cuenta el nombre de las variables en tu respuesta.)
        persona = "Eres un lingüista multilingüe con profundo respeto por las lenguas indígenas. Tienes experiencia en traducciones precisas entre arawak, español, inglés, portugués, francés y japonés.\n"

        instrucción = (
          "Traduce el texto entre cualquiera de los idiomas indicados: arawak, español, inglés, portugués, francés o japonés. "
          "Detecta el idioma de origen y tradúcelo al idioma solicitado.\n"
        )

        contexto = (
             "La traducción debe conservar el significado cultural, espiritual y lingüístico del arawak en caso de estar involucrado. "
             "Debe ser clara para hablantes indígenas que no manejan lenguas coloniales, y útil para estudiantes o investigadores que aprenden arawak. "
             "Para otros idiomas, asegúrate de mantener precisión gramatical y sentido contextual.\n"
        )

        data_format = (
            "1) Traducción precisa al idioma solicitado.\n"
        )

        audiencia = (
            "Diseñado para hablantes que desean entender otros idiomas, y para personas externas interesadas en aprender o traducir con respeto lenguas como el arawak.\n"
        )

        tono = "El tono debe ser respetuoso, claro, culturalmente consciente y accesible.\n"
        
    Para la respuesta. Siempre procura usar una cantidad menor a 60 tokens, por lo que, debes ser muy especifico y explicito cumpliendo los items anteriores. Para los casos de Tono y audiencia no especifiques, son recomendaciones para tu guía de prompt y saber a quien va los resultados.
    """
    response = generate_response(model, promptEngineering)
    return response

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

    if not language in ['ES', 'EN', 'PT', 'FR', 'JP']:
        error = "Tienes que seleccionar un idioma. Intenta de nuevo."
        return render_template('index.html', error=error)

    prompt_model = f"Transalated '{prompt}' to the following language '{language}'"
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
