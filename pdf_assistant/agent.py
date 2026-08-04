from pdf_assistant  import config
from langchain.agents import create_agent



def create_pdf_agent(llm,tools):
    """ return a langchain agent that call tools to answer questions"""
    agent= create_agent(model=llm , tools=tools,system_prompt =config.SYSTEM_PROMPT)
    return agent