from pdf_assistant import config
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_into_chunk(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = text_splitter.split_documents(documents)
    
    
    return chunks