import os
import time
import certifi
from dotenv import load_dotenv

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

try:
  from groqflow import ChatGroq
except ImportError:
  print("Error: ChatGroq might not be part of the public groqflow library. Refer to groqflow documentation for usage instructions.")
  print("Consider using community libraries like transformers or rasa for chatbot functionalities.")
else:
  # Use the ChatGroq class here (if successful import)
  # ...
# Load environment variables
 load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
os.environ['SSL_CERT_FILE'] = certifi.where()

# Streamlit UI setup
st.title("Gemma Model Document Q&A")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-it")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    <context>
    Question: {input} 
    """
)

def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("./data")
        try:
            st.session_state.docs = st.session_state.loader.load()
        except Exception as e:
            st.error(f"Error loading documents: {e}")
            return
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

prompt1 = st.text_input("What do you want to ask from the documents?")

if st.button("Creating Vector Store"):
    with st.spinner("Loading documents and creating vector store..."):
        vector_embedding()
    st.write("Vector Store DB is Ready")

if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    with st.spinner("Getting the answer..."):
        start = time.process_time()
        response = retrieval_chain.invoke({'input': prompt1})
    st.write(response.get('answer', 'No response found.'))

    with st.expander("Document Similarity Matches"):
        for i, doc in enumerate(response.get("context", [])):
            st.write(doc.page_content)
            st.write("---------------------------------")



