from pdf_assistant import config
from langchain_community.embeddings import JinaEmbeddings

def get_embedding_model():
    """ return the Jina embedding model"""
    embedding_model=JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
    return  embedding_model