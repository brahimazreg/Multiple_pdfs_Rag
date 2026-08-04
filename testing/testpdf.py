from pdf_assistant.vector_store import get_retriever,build_vector_store
from pdf_assistant import config
from pdf_assistant.document_loader import load_document
from pdf_assistant.splitter import split_into_chunk  
from pdf_assistant.vector_store import save_vectore_store , build_vector_store,vector_store_exists,get_retriever
from pdf_assistant.llm import get_llm
from pdf_assistant.tools import create_search_tool
from pdf_assistant import config

def main():
    """ llm=get_llm()
    
    documents = load_document()
    chunks=split_into_chunk(documents)
    vector_store =build_vector_store(chunks)
    retriever=get_retriever(vector_store,config.TOP_K_RESULTS)
    docs = retriever.invoke("Bob")

    print("Retrieved:", len(docs))

    for i, doc in enumerate(docs):
        print(f"\n----- {i+1} -----")
        print("Source:", doc.metadata.get("source"))
        print(doc.page_content[:300])
 """
    # ------------------------------
from pdf_assistant.document_loader import load_document
from pdf_assistant.splitter import split_into_chunk
from pdf_assistant.vector_store import build_vector_store, get_retriever

documents = load_document()
chunks = split_into_chunk(documents)

vector_store = build_vector_store(chunks)
retriever = get_retriever(vector_store, 5)

docs = retriever.invoke("Who is the customer?")

print("Retrieved:", len(docs))

for doc in docs:
    print("--------------------------------")
    print(doc.metadata["source"])
    print(doc.page_content[:500])
    

if __name__ == "__main__":
    main()