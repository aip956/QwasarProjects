from loader import load_documents
from embedder import get_embedding
from vector_store import VectorStore

def build_vector_store():
    docs = load_documents()
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
    query_embedding = get_embedding(question)
    top_chunks = store.search(query_embedding, k=5)
    return "\n".join(top_chunks)


