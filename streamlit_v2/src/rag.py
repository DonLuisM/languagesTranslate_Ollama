import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dictionary import all_docs


load_dotenv()


os.environ['LANGSMITH_TRACING'] = 'false'
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY') or ''


text_splitter = RecursiveCharacterTextSplitter( # Splitter de texto
    chunk_size=2000, 
    chunk_overlap=200, 
    add_start_index=True
)
embeddings = OllamaEmbeddings(model='nomic-embed-text') # Modelo de embeddings


def get_chroma_db():
    '''
    Obtener base de datos vectorial
    '''

    global embeddings

    return Chroma(
        collection_name='general',
        embedding_function=embeddings,
        persist_directory='./streamlit_v2/src/chroma_langchain_db', 
    )


def get_vectorial_default_db():
    '''
    Genera la base de datos vectorial con los documentos por defecto
    '''

    vector_store = get_chroma_db()
    vector_store.add_documents(documents=all_docs)
    return vector_store


def add_new_pdf(filepath):
    '''
    Agrega un nuevo PDF a la base de datos vectorial
    '''

    loader = PyPDFLoader(filepath)
    docs = loader.load()
    split_docs += docs
    all_splits = text_splitter.split_documents(split_docs)
    vector_store = get_chroma_db()
    vector_store.add_documents(documents=all_splits)
    return vector_store


def rag_user_input(vector_store: Chroma, user_input):
    '''
    Inserción de RAG en el query del usuario
    '''

    if user_input:
        results = vector_store.similarity_search_with_score(user_input)
        doc, score = results[0]
        return doc, score
    return None, None
