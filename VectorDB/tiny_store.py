# Tutorial from https://dev.to/vivekalhat/building-a-tiny-vector-store-from-scratch-59ep
import os
import sys
import warnings
import ollama
import numpy as np # efficient numerical ops and storing multi-dimensional arrays
from sentence_transformers import SentenceTransformer #Embeddings generation; text to vectors
from helpers import cosine_similarity

"""
Tiny, in-memory vector store called Pixie
1. Store document embeddings
2. Perform similarity searches
"""

warnings.filterwarnings("ignore")

class Pixie:
    # Initialize Pixie with an embedder

    def __init__(self, embedder) -> None:
        self.store: np.ndarray = None # holds our document embeddings as a NumPy array
        self.embedder: SentenceTransformer = embedder # Hold embedding model that we'll use to convert docs and queries to vectors


    # Ingesting docs
    def from_docs(self, docs):
        self.docs = np.array(docs)
        self.store = self.embedder.encode(self.docs)
        return f"Ingested {len(docs)} documents"

    # Perform similarity search
    def similarity_search(self, query,top_k=3):
        matches = list()
        q_embedding = self.embedder.encode(query)
        top_k_indices = cosine_similarity(self.store, q_embedding, top_k)
        for i in top_k_indices:
            matches.append(self.docs[i])
        return matches
    
    # Cosine similarity
    def cosine_similarity(store_embeddings, query_embedding, top_k):
        dot_product = np.dot(store_embeddings, query_embedding)
        magnitude_a = np.linalg.norm(store_embeddings, axis = 1)
        magnitude_b = np.linalg.norm(query_embedding)
        similarity = dot_product / (magnitude_a * magnitude_b)
        sim = np.argsort(similarity)
        top_k_indices = sim[::-1][:top_k]
        return top_k_indices
    
    # Function for generating an answer using Llama model
    def generate_answer(prompt):
        response = ollama.chat(
            model="llama3",
            options={"temperature": 0.7},
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    
    # Creating an instance of the SentenceTransformer model
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    # Reading the space battle text document and ingesting it into Pixie
    with open("example/spacebattle.txt") as f:
        content = f.read()
        ingested = pixie.from_docs(content.split("\n\n"))
        print(ingested)

    # RAG systems's prompt format
    PROMPT = """
    User has asked you the following question and you need to answer it based on the below provided context. 
    If you don't find any answer in the given context, just say 'I don't have an answer for that'. 
    In the final answer, do not add "according to the context or as per the context". 
    You can be creative while using the context to generate the final answer. DO NOT just share the context as it is.

    CONTEXT: {0}
    QUESTION: {1}

    ANSWER HERE:
    """

    # Main loop for querying
    while True:
        query = input("\nAsk anything: ")
        if len(query) == 0:
            print("Ask a question to continue . . .")
            quit()
        
        if query == "/bye":
            quit()

        # Search similar matches for query in the embedding store
        similarities = pixie.similarity_search(query, top_k=5)
        print(f"query: {query}, top {len(similarities)} matched results:\n")

        print("-" * 5, "Matched Dcouments Start", "-" * 5)
        for match in similarities:
            print(f"{match}\n")
        print("-" * 5, "Matched Documents End", "-" * 5)

        context = ",".join(similarities)
        answer = generate_answer(prompt=PROMPT.format(context, query))
        print("\n\nQuestion: {0}\nAnswer: {1}".format(query, answer))

        continue
    


