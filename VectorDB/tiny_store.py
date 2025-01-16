# Tutorial from https://dev.to/vivekalhat/building-a-tiny-vector-store-from-scratch-59ep

import numpy as np # efficient numerical ops and storing multi-dimensional arrays
from sentence_transformers import SentenceTransformer #Embeddings generation; text to vectors
from helpers import cosine_similarity

"""
Tiny, in-memory vector store called Pixie
1. Store document embeddings
2. Perform similarity searches
"""
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
    
            

