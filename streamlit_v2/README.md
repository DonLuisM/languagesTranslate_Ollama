# :earth_americas: _LEXIWAK-BOT_

Este repositorio documenta el seguimiento en el desarrollo progresivo de LEXIWAK-BOT, un chatbot multilingüe diseñado para la preservación y revitalización de la lengua indígena Arawak, integrando traducción entre idiomas modernos (Español, Inglés, Alemán, Francés, Italiano) y el idioma ancestral Arawak.

Se presentan dos versiones principales:

- Versión 1: Punto de partida con funcionalidades básicas.
- Versión 2: Mejoras avanzadas que incluyen el uso de VectorDB, Recuperación Augmentada por Memoria (RAG), persistencia de memoria conversacional, embeddings semánticos y una interfaz de usuario más robusta e interactiva. Logrando destacar el compromiso en el desarrollo de un chatbot más avanzado y estructurado para preservar la lengua indígena Arawak.

Esta evolución refleja el compromiso en python y streamlit con la creación de un chatbot más estructurado, eficiente y culturalmente relevante.

### :information_source: Tabla de Contenidos
- [Características](#dart-características)
- [Tecnologías usadas](#rocket-tecnologías-usadas)
- [Visualización de la aplicación](#framed_picture-visualización-de-la-aplicación)
- [Configuración](#hammer_and_wrench-configuración)
- [Licencia](#scroll-licencia)
- [Contribuciones](#handshake-contribuciones)
- [Apoyo](#heart-apoyo)
- [Recursos](#books-recursos-lingüísticos-sobre-el-arawak)
- [Autores](#busts_in_silhouette-autores)

### :dart: Características
- Traducción entre Arawak y otros idiomas modernos.
- Uso de LLMs para generación de texto con enfoque cultural.
- Diseño modular para fácil manejo de las herramientas.
- Uso de streamlit como interfaz avanzada con caracteristicas esenciales para brindar servicios de chatbot de alta calidad.
- Uso de memoria conversacional para contexto continuo.
- Preservación y revitalización lingüística.
- Uso de código limpio y de calidad con apoyo de herramientas como Pylint.
  
### :rocket: Tecnologías usadas
- Python
- uv
- Ollama
- Streamlit
- LangChain

### :framed_picture: Visualización de la aplicación

| Vista de la interfaz | 
|-----------|
| ![Interfaz Completa](./data/Interfaz_box.jpg) |

| Vista Modelo cargando (status) |
|------------------|
| ![status Modelo](./data/Interfaz_waiting.jpg) |

| Validación de memoria y almacenamiento de chats |
|------------------|
| ![Vista Chat Avanzado](./data/Interfaz_memoria.jpg) |


## :hammer_and_wrench: Configuración

### 1. Descargar Ollama y uv
- Ollama - [Download](https://ollama.com/)
- uv - [Terminal](https://docs.astral.sh/uv/#__tabbed_1_1)
> [!IMPORTANT]
> Para correr satisfactoriamente la aplicación y configuración debes contar con UV Python y Ollama (LLMs Open Source).

### 2. Instalar modelo de Ollama:
```bash
# Validar Ollama descargado
ollama

# Descargar modelos qwen
ollama run qwen3:latest
```

### 3. Clona el repositorio e instalar dependencias
```bash
git clone https://github.com/DonLuisM/languagesTranslate_Ollama.git
cd languagesTranslate_Ollama

uv add
uv sync
```

### 4. Ejecutar la aplicación
```bash
uv run streamlit run .\streamlit_V2\src\chatbot_st_V2.py
```
---

### :scroll: Licencia
Licencia MIT – consulta el archivo [LICENSE](../LICENSE) para más detalles.

### :handshake: Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork del repositorio y enviar un pull request. ¡Todas las contribuciones son bienvenidas!

### :heart: Apoyo
Agradecemos tu apoyo, dandole una estrella al repositorio si es de tu agrado. Queremos llevar este proyecto a gran escala con entidades de preservación lingüística como museos, historiadores, entre otros. (⌒▽⌒)👍

### :books: Recursos lingüísticos sobre el Arawak
- [A Grammar Sketch and Lexicon of Arawak (Lokono Dian)]([https://www.ethnologue.com/subgroups/arawak](https://www.sil.org/system/files/reapdata/90/56/45/90564558109971050115741497077250122669/e_Books_30_Pet_Arawak_Suriname.pdf))
- [An Arawak English Dictionary with an English World List](https://tiboko.com/wp-content/uploads/2023/07/Arawak-English-Dictionary.pdf)
  
### :busts_in_silhouette: Autores:
- [@ingrid183](https://github.com/ingrid183)
- [@Juandiego001](https://github.com/Juandiego001)
- [@seba39399](https://github.com/seba39399)
- [@DonLuisM](https://github.com/DonLuisM)

