import faiss
import numpy as np
import pickle

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []


    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)
        
    def search(self, query_embedding, k=5):
        D, I = self.index.search(np.array([query_embedding]).astype("float32"), k)
        return [self.texts[i] for i in I[0]]
    
    def save(self):
        faiss.write_index(self.index, "fiass.index")
        with open("texts.pkl", "wb") as f:
            pickle.dump(self.texts, f)

    def load(self):
        self.index = faiss.read_index("faiss.index")
        with open("texts.pkl", "rb") as f:
            self.texts = pickle.load(f)


