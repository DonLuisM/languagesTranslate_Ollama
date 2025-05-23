# :brain: _Traductor Multilingüe LLMs_ [V1](./streamlit_V1)
> [!IMPORTANT]
> _Para visualizar la Versión 2 del proyecto (README, archivos .py y mejoras), dirijase a la siguiente ruta [V2](./streamlit_v2)_

Este proyecto es una interfaz web con HMTL (Jinja2) y CSS que permite traducir entre idiomas modernos (Español, Inglés, Alemán, Francés, Italiano) y adicionalmente, conocer sobre la lengua indígena Arawak.
Utiliza modelos de lenguaje LLM como LLamA 3.1 a través de Ollama (Open Source), integrados con Flask, para generar traducciones precisas y culturalmente informadas.

### :dart: Características
- Traducción entre Arawak y otros idiomas modernos.
- Uso de LLMs para generación de texto con enfoque cultural.
- Diseño responsivo para móviles y tablets.
- Uso de streamlit para comparar diferentes respuestas de los modelos Ollama instalados.
- Optimización del modelo con herramientas de Prompt Engineering. 
- Preservación y revitalización lingüística.
  
### :rocket: Tecnologías usadas
- Python
- uv
- Ollama
- Flask
- HTML, CSS, JS
- Streamlit

### :framed_picture: Visualización de la aplicación

| Vista Web | Vista Móvil |
|-----------|-------------|
| ![webapp](./static/assets/appFront.jpg) | ![mobile](./static/assets/appMobile.jpg) |

| Vista Streamlit |
|------------------|
| ![st](./static/assets/appStreamlit.jpg) |
 
---
## :hammer_and_wrench: Configuración

### 1. Descargar Ollama y uv
- Ollama - [Download](https://ollama.com/)
- uv - [Terminal](https://docs.astral.sh/uv/#__tabbed_1_1)
> [!IMPORTANT]
> Para correr satisfactoriamente la aplicación y configuración debes contar con UV Python y Ollama (LLMs Open Source).

### 2. Instalar modelo de Ollama: [Llama3.1](https://ollama.com/library/llama3.1)
```bash
# Validar Ollama descargado
ollama

# Descargar modelos Llama3.1
ollama run llama3.1:8b-instruct-q5_K_M
```
> [!NOTE]
> Los modelos LLaMA 3.1 8B y 8B-Instruct-Q5_K_M tienen un tamaño de **_4.9 GB_** y **_5.7 GB_**, respectivamente.

### 3. Clona el repositorio e instalar dependencias
```bash
git clone https://github.com/DonLuisM/languagesTranslate_Ollama.git
cd languagesTranslate_Ollama

uv add
uv sync
```

### 4. Ejecutar la aplicación
```bash
uv run app.py
```

### 5. Ejecutar el streamlit para comparar respuestas
```bash
uv run streamlit run .\streamlit\app_st_cont.py   
```
---

### :scroll: Licencia
Licencia MIT – consulta el archivo [LICENSE](./LICENSE) para más detalles.

### :handshake: Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork del repositorio y enviar un pull request. ¡Todas las contribuciones son bienvenidas!

### :busts_in_silhouette: Autores:
- [@ingrid183](https://github.com/ingrid183)
- [@Juandiego001](https://github.com/Juandiego001)
- [@seba39399](https://github.com/seba39399)
- [@DonLuisM](https://github.com/DonLuisM)
