from loader import load_documents
from embedder import get_embedding
from vector_store import VectorStore

def build_vector_store():
    docs = load_documents() # Calls load_documents() in loader.py to load documents from the data directory
    if not docs:
        raise ValueError("No documents found to build the vector store.")   
        return
    
    embeddings = [get_embedding(chunk) for chunk in docs]
    if not embeddings:
        raise ValueError("No embeddings generated from the documents.")
        return
    

    store = VectorStore(dim=len(embeddings[0]))
    store.add(embeddings, docs)
    store.save()
    return store

def answer_question(question, store):
    # Get embedding from embedder.py; it then sends the question to Ollama's nomic-embed-text model
    query_embedding = get_embedding(question) 

    # store.search() calls VectorStore.search in vectorer_store.py
    top_chunks = store.search(query_embedding, k=5)

    # Sends received context chunks back to the main.py file
    return "\n".join(top_chunks)


