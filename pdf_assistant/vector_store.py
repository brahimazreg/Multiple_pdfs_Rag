from pdf_assistant import config
from pdf_assistant.embedding import get_embedding_model
import os
from langchain_community.vectorstores import FAISS

# buil a vector store
def build_vector_store(chunks):
    """ Embed each chunk and build a searchable Faiss index in memory"""
    embedding_model = get_embedding_model()
    vector_store=FAISS.from_documents(chunks,embedding_model)
    return vector_store


# save the vecor store
def save_vectore_store(vector_store,path:str=config.VECTORE_STORE_PATH)-> str:
    """ Store the vector stor in VECTORE_STORE_PATH"""
    vector_store.save_local(path)
    return "Vector store successfully saved"

# load a vector store
def load_vector_store(path:str=config.VECTORE_STORE_PATH):
    """ Load the vector store """
    embedding_model = get_embedding_model()
    return FAISS.load_local(path,embedding_model,allow_dangerous_deserialization=True)

# check if a vector exist
def vector_store_exists(path:str=config.VECTORE_STORE_PATH)-> bool:
    """ check if the vector store exist"""
    return os.path.exists(os.path.join(path,"index.faiss"))

# get a reriever
def get_retriever(vector_store,k:int=config.TOP_K_RESULTS):
    """ turn the vector store into retriever"""
    return vector_store.as_retriever(search_kwargs={"k":k})