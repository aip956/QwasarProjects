from loader import load_documents
from embedder import get_embedding
from vector_store import VectorStore

def build_vector_store():
    docs = load_documents()
    embddings = [get_embedding(chunk) for chunk in docs]
    store = VectorStore(dim=len(embddings[0]))
    store.add(embddings, docs)
    store.save()
    return store

def answer_question(question, store):
    query_embedding = get_embedding(question)
    top_chunks = store.search(query_embedding, k=5)
    return "\n".join(top_chunks)


    """
    Build a vector store from text documents in the specified folder.
    
    Args:
        folder_path (str): The path to the folder containing text files.
        dim (int): The dimension of the embeddings.
        
    Returns:
        VectorStore: An instance of VectorStore containing the embeddings and texts.
    """
    documents = load_documents(folder_path)
    vector_store = VectorStore(dim)
    
    embeddings = []
    for text in documents:
        embedding = get_embedding(text)
        embeddings.append(embedding)
    
    vector_store.add(embeddings, documents)
    vector_store.save()
    
    return vector_store