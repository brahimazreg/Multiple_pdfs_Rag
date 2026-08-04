from pdf_assistant import config
from langchain_community.document_loaders import PDFMinerLoader


def load_document(file_path=None):
    """Load PDF files and return a list of LangChain documents"""

    if file_path is None:
        file_path = config.DATA_FILE_PATH

    documents = []

    for pdf in file_path:
        loader = PDFMinerLoader(pdf)
        print(loader)
        documents.extend(loader.load())
    
    return documents

    
