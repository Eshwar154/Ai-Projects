import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Verify API key
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY is not set. Please check your .env file.")
    exit(1)

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question using only the following context:

{context}

---

Question: {question}

Answer:
"""

def main():
    parser = argparse.ArgumentParser(description="Query data from a Chroma vector store.")
    parser.add_argument("query_text", type=str, help="The query text to search for in the database.")
    args = parser.parse_args()

    query_text = args.query_text

    try:
        embedding_function = OpenAIEmbeddings()
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    except Exception as e:
        print(f"Error initializing Chroma DB: {e}")
        exit(1)

    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if not results or results[0][1] < 0.7:
        print("Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", "Unknown") for doc, _ in results]
    formatted_response = f"Response: {response_text}\n\nSources:\n" + "\n".join(sources)
    print(formatted_response)

if __name__ == "__main__":
    main()
