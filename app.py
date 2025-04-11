''' 
Adecuación del modelo Ollama para Flask
'''
from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

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

    prompt_model = f"Transalated {prompt} to the following language {language}"
    print(prompt_model)

    # prompt para modelo. Tener en cuenta:
    #     ES = Español
    #     EN - Ingles
    #     PT - Portugues
    #     FR - Frances
    #     JP - Japones

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user', 
                    'content': prompt
                }
            ]
        )

        translation = response['message']['content']
        return render_template('index.html', translation=translation)
    except KeyError as k:
        error = f"Error: {str(k)}"
        return render_template('index.html', error=error)
    except TypeError as t:
        error = f"Error: {str(t)}"
        return render_template('index.html', error=error)

@app.route('/about')
def about():
    ''' 
    Página de información sobre Arawak
    '''
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
