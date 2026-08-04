from pdf_assistant import config
from langchain_groq import ChatGroq


def get_llm():
    """ return a groq chat model """
    return ChatGroq(model=config.LLM_MODEL_NAME ,temperature=0)
