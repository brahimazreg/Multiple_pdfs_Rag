from pdf_assistant.document_loader import load_document


def main():
    from pdf_assistant.document_loader import load_document

    docs = load_document()

    for doc in docs:
        print(doc.metadata["source"])
        print(doc.page_content[:200])
        print("=" * 50)


if __name__ == "__main__":
    main()