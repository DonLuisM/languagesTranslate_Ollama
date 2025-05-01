# :brain: _Traductor Multilingüe LLMs_
Este proyecto es una interfaz web con HMTL y CSS(Jinja2) que permite traducir entre idiomas modernos (Español, Inglés, Alemán, Francés, Italiano) y adicionalmente, conocer sobre la lengua indígena Arawak.
Utiliza modelos de lenguaje LLM como LLamA 3.1 a través de Ollama (Open Source), integrados con Flask, para generar traducciones precisas y culturalmente informadas.

### :dart: Características
- Traducción entre Arawak y otros idiomas modernos.
- Uso de LLMs para generación de texto con enfoque cultural.
- <!-- Agregar más -->
  
### :rocket: Tecnologías usadas
- Python
- uv
- Ollama
- Flask
- HTML, CSS, JS
- Streamlit

---
## :hammer_and_wrench: Configuración

### 1. Descargar Ollama y uv
- Ollama - [Download](https://ollama.com/)
- uv - [Terminal](https://docs.astral.sh/uv/#__tabbed_1_1)

### 2. Instalar modelo de Ollama: [Llama3.1](https://ollama.com/library/llama3.1)
```bash
# Validar Ollama descargado
ollama

# Descargar modelos Llama3.1
ollama run llama3.1:8b-instruct-q5_K_M
```
> [!NOTE]
> Los modelos LLaMA 3.1 8B y 8B-Instruct-Q5_0 tienen un tamaño de **_4.9 GB_** y **_5.6 GB_**, respectivamente.

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
