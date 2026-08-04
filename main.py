from pdf_assistant.document_loader import load_document
from pdf_assistant.splitter import split_into_chunk  
from pdf_assistant.vector_store import save_vectore_store , build_vector_store,vector_store_exists,get_retriever
from pdf_assistant.llm import get_llm
from pdf_assistant.tools import create_search_tool
from pdf_assistant import config

from pdf_assistant.pipeline import build_pdf_assistant ,ask
def main():

    # --------- test full rag ------
    print("Building the pdf assistant ...")
    agent = build_pdf_assistant()
    print("Assistant is ready")
    demo_question=[
    "What does Article 1 of the Belgian Constitution state?",
    "Where is the seat of the federal government?",
    "What languages are recognized in Belgium?",
    "Who I am ?"
    ]
    for question in demo_question:
        print("="*60)
        print("Question :" ,question)
        print("-"*60 )
        answer= ask(agent,question)
        print("answer:",answer)
        print("="*60)
        print()

if __name__ == "__main__":
    main()