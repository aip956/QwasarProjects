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
    



