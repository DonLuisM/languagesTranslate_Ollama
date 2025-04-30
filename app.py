''' 
Adecuación del modelo Ollama para Flask
'''
from flask import Flask, render_template, request
import ollama
from prompt_eng import create_prompt
import markdown

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
                        "Español, Inglés, Alemán, Francés e Italiano."
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
        translation = markdown.markdown(translation)
        print(translation)
        return render_template('index.html', translation=translation)
    except KeyError as k:
        error = f"Error: {str(k)}"
        return render_template('index.html', error=error)
    except TypeError as t:
        error = f"Error: {str(t)}"
        return render_template('index.html', error=error)

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
    model = 'llama3.1:8b-instruct-q5_K_M'
    prompt = request.form['text']
    language = request.form.get('languages')

    if language not in ['Español', 'Inglés', 'Alemán', 'Francés', 'Italiano', 'Arawak']:
        error = "Tienes que seleccionar un idioma. Intenta de nuevo."
        return render_template('index.html', error=error)

    prompt_model = f"Traduce el texto: '{prompt}' al siguiente idioma: '{language}'."
    print(prompt_model)
    return create_prompt(model, prompt_model, language)

@app.route('/about')
def about():
    ''' 
    Página de información sobre Arawak
    '''
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
