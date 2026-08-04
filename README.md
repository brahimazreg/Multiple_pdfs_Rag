
# 📚 MultiPDF Chat App

![MultiPDF Chat App](data/PDF-LangChain.jpg)

## 📖 Introduction

The **MultiPDF Chat App** is an AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload and chat with multiple PDF documents using natural language.

Instead of manually searching through lengthy documents, users can simply ask questions, and the application retrieves the most relevant content from the PDFs before generating an accurate response using a Large Language Model (LLM).

The application only answers questions based on the uploaded documents, helping reduce hallucinations and improving answer reliability.

---

## ✨ Features

- 📄 Upload and process multiple PDF files
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering
- 💬 Interactive chat interface with Streamlit
- ⚡ Fast inference using Groq LLMs
- 🧠 Retrieval-Augmented Generation (RAG)
- 📦 Modular project structure
- 🐳 Docker support

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| LangChain | LLM Orchestration |
| Groq API | Large Language Model |
| HuggingFace Embeddings | Text Embeddings |
| FAISS | Vector Database |
| PyPDF | PDF Processing |
| Docker | Containerization |

---

# 📂 Project Structure

```
Multiple_pdfs_Rag/
│
├── data/
│   └── PDF-LangChain.jpg
│
├── pdf_assistant/
│   ├── agent.py
│   ├── config.py
│   ├── document_loader.py
│   ├── embedding.py
│   ├── llm.py
│   ├── pipeline.py
│   ├── splitter.py
│   ├── tools.py
│   └── vector_store.py
│
├── testing/
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# ⚙️ How It Works

The application follows the Retrieval-Augmented Generation (RAG) pipeline:

```
PDF Files
     │
     ▼
Document Loader
     │
     ▼
Text Splitter
     │
     ▼
Embeddings
     │
     ▼
Vector Database (ChromaDB)
     │
     ▼
Retriever
     │
     ▼
LangGraph Agent
     │
     ▼
Groq LLM
     │
     ▼
Generated Answer
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Multiple_pdfs_Rag.git

cd Multiple_pdfs_Rag
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running the Application

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 💬 Example Questions

After uploading your PDFs, you can ask questions such as:

- What is the project deadline?
- Who attended the meeting?
- Summarize this document.
- What technologies were selected?
- Explain the introduction.
- What are the key findings?
- Who is responsible for the API?
- List all action items.

---

# 📚 Project Modules

### `document_loader.py`

Loads PDF documents.

### `splitter.py`

Splits documents into manageable chunks.

### `embedding.py`

Generates vector embeddings using HuggingFace models.

### `vector_store.py`

Stores embeddings in ChromaDB.

### `tools.py`

Defines retrieval tools used by the LangGraph agent.

### `llm.py`

Initializes the Groq language model.

### `agent.py`

Creates the LangChain agent.

### `pipeline.py`

Coordinates retrieval and response generation.

### `app.py`

Provides the Streamlit user interface.

---

# 🚀 RAG Workflow

1. Upload one or more PDF files.
2. Extract text from PDFs.
3. Split text into chunks.
4. Generate embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve the most relevant chunks.
7. Send context to the Groq LLM.
8. Generate an answer grounded in the uploaded documents.

---

# 📸 Application Screenshot

Replace the image below with your application screenshot.

```markdown
![Application Screenshot](data/app.png)
```

---

# 🐳 Docker

Build the Docker image

```bash
docker build -t multipdf-chat .
```

Run the container

```bash
docker run -p 8501:8501 multipdf-chat
```

---

# 📈 Future Improvements

- Conversation memory
- Source citation for answers
- PDF highlighting
- Support for Word and PowerPoint files
- User authentication
- Persistent vector database
- Multiple LLM providers
- Chat history export

---

# 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.