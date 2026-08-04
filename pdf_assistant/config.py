import os
from dotenv import load_dotenv

from pathlib import Path



load_dotenv()

# environment variables
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
JINA_API_KEY=os.getenv("JINA_API_KEY")

# Define the path for the file and vectore store
# PDF files
DATA_DIR = Path("data")
DATA_FILE_PATH = list(DATA_DIR.glob("*.pdf"))
""" DATA_FILE_PATH = [
    os.path.join("data", "BelgianConstitution.pdf"),
    os.path.join("data", "Constitution_BillOfRights.pdf"),
] """

VECTORE_STORE_PATH= os.path.join("data","faiss_index")

# Models : LLM and Embedding
LLM_MODEL_NAME="openai/gpt-oss-120b"
#LLM_MODEL_NAME="meta-llama/llama-4-scout-17b-16e-instruct"
#LLM_MODEL_NAME="llama-3.1-8b-instant"
EMBEDDING_MODEL_NAME="jina-embeddings-v5-text-small"

# Chunk : text splitting configuration
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# Retreival resuls
TOP_K_RESULTS=3

#System instructions
SYSTEM_PROMPT="""
    You are a helpful assistant that answers questions using the uploaded PDF documents.

    Always use the document search tool when the answer may be found in the PDFs.

    If the information is not in the documents, say you do not have enough information.
"""
# Chek api keys

def check_api_keys()->None:
    """Stop early with a clear message if a required key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY . Please add it to your .env file. ")
    if not JINA_API_KEY:
            raise ValueError("Missing JINA_API_KEY:. Please add it to your .env file. ")