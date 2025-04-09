''' 
Adecuación del modelo Ollama para Flask
'''
from flask import Flask, jsonify, render_template, request
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
    # language = request.form['languages']

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
        return translation
    except KeyError as k:
        return jsonify({'error': str(k)}), 500
    except TypeError as t:
        return jsonify({'error': str(t)}), 500
    
@app.route('/about')
def about():
    ''' 
    Página de información sobre Arawak
    '''
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
