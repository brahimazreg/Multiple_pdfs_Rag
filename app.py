"""Streamlit chat app for the Belgian constitution.

Run with:  streamlit run app.py
"""

import streamlit as st
import os
from PIL import Image
from pathlib import Path

from pdf_assistant.pipeline import build_pdf_assistant ,ask

def main():
    BASE_DIR = Path(__file__).parent
    icon = Image.open(BASE_DIR / "data" / "imagepdf.png")
    col1, col2 = st.columns([1, 5])

    with col1:
        st.image(icon, width=90)

    with col2:
        st.title("Chat with multiple PDFs :books:")
        st.caption("Ask me questions")
    #  handle side bare    
    DATA_DIR = Path(r"C:\Users\brahi\Desktop\Multiple_pdfs_Rag\data")
    DATA_DIR.mkdir(exist_ok=True)

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
        process = st.button("Process")

        if process:
            if uploaded_file is not None:
                file_path = DATA_DIR / uploaded_file.name

                # Save the uploaded PDF
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                st.success(f"'{uploaded_file.name}' has been added to the data folder.")
            else:
                st.warning("Please upload a PDF first.")
            # end handle side bare

    @st.cache_resource(show_spinner="Setting up the assistant (only happens once)...")
    def get_agent():
        return build_pdf_assistant()


    agent = get_agent()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show the past conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get a new question from the user
    question = st.chat_input("Ask a question ...")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask(agent, question)
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()
