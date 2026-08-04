from pdf_assistant.config import *
from pdf_assistant.tools import create_search_tool
from pdf_assistant.llm import get_llm
from pdf_assistant.vector_store import *
from pdf_assistant.document_loader import load_document
from pdf_assistant.splitter import split_into_chunk 
from pdf_assistant.agent import  create_pdf_agent


def build_vectore_store_for_document(file_path=None):
    if file_path is None:
        file_path = config.DATA_FILE_PATH
    print("Rebuilding vector store...")
    documents = load_document()
    chunks = split_into_chunk(documents)
    vector_store = build_vector_store(chunks)
    save_vectore_store(vector_store, path=config.VECTORE_STORE_PATH)

    return vector_store


    # Build an AI agent
def build_pdf_assistant(file_path:str=config.DATA_FILE_PATH):
    """ Build the full rag agent ready to answer question"""
    check_api_keys()

    vector_store=build_vectore_store_for_document(file_path)
    retriever = get_retriever(vector_store, config.TOP_K_RESULTS)    
    search_tool = create_search_tool(retriever)

    llm=get_llm()
    agent=create_pdf_agent(llm,[search_tool])
    # debug
    response = llm.invoke("Say hello")
    print(response.content)
    # debug
    return agent

def ask(agent,question:str)-> str:
    """ Ask the agent a question and return its final answer as plain text"""


    response = agent.invoke(
        {"messages":[{
            "role":"user","content":question
        }]}
   
    )
    return response["messages"][-1].content