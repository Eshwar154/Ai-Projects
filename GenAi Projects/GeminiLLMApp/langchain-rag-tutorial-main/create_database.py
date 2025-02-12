from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    print("Error: OpenAI API key is missing. Ensure it is set in the .env file.")
    exit(1)

CHROMA_PATH = "chroma"
DATA_PATH = "data/books"

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    if not documents:
        print("No documents to process. Exiting.")
        return

    chunks = split_text(documents)
    if not chunks:
        print("No chunks generated. Exiting.")
        return

    save_to_chroma(chunks)

def load_documents():
    if not os.path.exists(DATA_PATH):
        print(f"Error: The directory '{DATA_PATH}' does not exist.")
        exit(1)

    if not os.listdir(DATA_PATH):
        print(f"Error: The directory '{DATA_PATH}' is empty.")
        exit(1)

    try:
        loader = DirectoryLoader(DATA_PATH, glob="*.md")
        documents = loader.load()
        print(f"Loaded {len(documents)} documents from {DATA_PATH}.")
        return documents
    except Exception as e:
        print(f"Error loading documents: {e}")
        exit(1)

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    if len(chunks) > 10:
        document = chunks[10]
        print("Sample chunk content:")
        print(document.page_content)
        print("Metadata:", document.metadata)

    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        confirm = input(f"Directory '{CHROMA_PATH}' already exists. Rebuild database? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Aborting operation.")
            exit(1)
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()

