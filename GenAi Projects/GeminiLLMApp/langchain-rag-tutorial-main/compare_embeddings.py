from sentence_transformers import SentenceTransformer
import numpy as np

def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

def main():
    # Initialize the SentenceTransformer model
    model_name = "all-MiniLM-L6-v2"  # A lightweight and efficient model
    model = SentenceTransformer(model_name)

    # Words to compare
    word1 = "apple"
    word2 = "iphone"

    # Generate embeddings
    vec1 = model.encode(word1)
    vec2 = model.encode(word2)

    # Display embedding information
    print(f"Vector for '{word1}': {vec1}")
    print(f"Vector for '{word2}': {vec2}")
    print(f"Vector length: {len(vec1)}")

    # Compute cosine similarity
    similarity = cosine_similarity(vec1, vec2)
    print(f"Cosine similarity between '{word1}' and '{word2}': {similarity:.4f}")

if __name__ == "__main__":
    main()

