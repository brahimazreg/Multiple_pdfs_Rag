from pdf_assistant.document_loader import load_document
from pdf_assistant.splitter import split_into_chunk  
from pdf_assistant.vector_store import save_vectore_store , build_vector_store,vector_store_exists,get_retriever
from pdf_assistant.llm import get_llm
from pdf_assistant.tools import create_search_tool
from pdf_assistant import config

from pdf_assistant.pipeline import build_pdf_assistant ,ask
def main():
    #documents = load_document([r"C:\test_cv\cv_test.pdf"])
    # ------- test oad_document.py -----------------
    
    
    """ print(f"Loaded {len(documents)} document pages")
    documents = load_document()
    print(documents[0].page_content)
    for doc in documents[:2]:
            print(doc.metadata)
            print(doc.page_content[:300])
            print("-" * 50)  """
    
    #--------     test splitter.py  ---------------
    #documents = load_document([r"C:\test_cv\cv_test.pdf"])
    """ documents = load_document()
    chunks=split_into_chunk(documents)
    print(f"we have {len(chunks)} : chunk")
    for i ,chunk in enumerate(chunks[:3], start=1) :
        print(f"chunk :{i}")
        print(chunk.page_content[:100])
        print("=" * 50)
        print() """

    #--------     vector_store.py  --------------- 
    #documents = load_document()
    #chunks=split_into_chunk(documents)
    #vectore_store =build_vector_store(chunks)
    #print(save_vectore_store(vectore_store, path=config.VECTORE_STORE_PATH))
    """ if(vector_store_exists(path=config.VECTORE_STORE_PATH)):
        print(" vectore store exist!!") """

    #--------   test   llm.py  --------------- 
    #print(get_llm())

    #--------  test Tools  --------------- 
"""     documents = load_document()
    chunks=split_into_chunk(documents)
    vector_store =build_vector_store(chunks)
    question="What is the official name of Belgium according to the Constitution?"
    retriever = get_retriever(vector_store, config.TOP_K_RESULTS)

    search_tool = create_search_tool(retriever)
    
    result = search_tool.invoke({
    "question": "What is the official name of Belgium according to the Constitution?"
    })

    print(result) """

# --------- test full rag ------
print("Building the pdf assistant ...")
agent = build_pdf_assistant()
print("Assistant is ready")
demo_question=[
"What is the official name of Belgium according to the Constitution?",
"How many regions are recognized by the Belgian Constitution?",
"What are the three Communities of Belgium?"
]
for question in demo_question:
    print("="*60)
    print("Question :" ,question)
    print("-"*60 )
    # debuggin
    


    # debuggin
    answer= ask(agent,question)
    print("answer:",answer)
    print("="*60)
    print()

if __name__ == "__main__":
    main()