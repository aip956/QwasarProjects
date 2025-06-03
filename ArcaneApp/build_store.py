from rag_engine import build_vector_store

# Build and save the FAISS vector store
# Via rag_engine.py, it calls VectorStore.add() in vector_store.py
build_vector_store()