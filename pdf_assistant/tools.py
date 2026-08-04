from pdf_assistant import config
from langchain.tools import tool

def create_search_tool(retriever):
    """ return @tool function that search the constitution informations"""
    @tool
    def search_documents(question:str) -> str:
        """
        Search all uploaded PDF documents.

        Use this tool whenever the user asks about information
        contained in the uploaded documents.
        This includes names, dates, invoices, CVs, contracts,
        articles, skills, and any other PDF content.
        """
        docs = retriever.invoke(question)
        return "\n\n".join(doc.page_content for doc in docs)

    return search_documents




