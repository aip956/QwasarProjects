# Welcome to My Arcane App

## Task
Build a Retrieval-Augmented Generation (RAG) API that connects to a local language model, retrieves relevant context from a small document set, and uses that context to generate more accurate answers to user questions.


## Description
This project addresses a core limitation of LLMs: their inability to access specific or up-to-date external knowledge. 

Imagine you are a company who wants to use an LLM. However, your work is confidential, so you don't want the publically available LLM to be trained on your data. You could obtain an LLM as a foundation, and then augment it with your confidential information. This is fundamentally what a RAG system does.

A RAG system resolves this by:

- Receiving a question through an API.
- Retrieving relevant context chunks from a vector database of documents.
- Sending both the question and retrieved context to an LLM.
- Returning the generated answer to the user via the API.

The app is built using FastAPI, integrates with a vector store (FAISS or ChromaDB), and connects to either OpenAI’s GPT-4 or a local LLaMA 2 instance. It includes basic API key security and simple logging. The goal is a functional, maintainable, and secure RAG prototype.

### Classes
#### main.py
- FastAPI web server
- Defines POST/ask endpoint
- Accepts a JSON body with a question and api_key
- Uses the RagEngine to process the questions
- Returns an answer (or error message)
- This is the frontend API for the RAG app
#### rag_engine.py
- Core logic of the app; the brain
- it embeds the quesiton using an embedder
- Searches for relevant text chunks from FAISS
- Constructs a prompt using those retrieved texts
- sends it to the local LLM
- Returns the model's final answer
- Combines retrieval and generation
#### vector_store.py
- Handles the FAISS index and test storage
- Loads and saves the faiss.index (vector store)
- Loads and saves texts.pkl (raw source text chunks)
- Provides a .search(query_embedding) method to return relevant documents
- It's the document memory - optimized for fast vector search

#### embedder.py
- Embedding tool
- Calls Ollama's nomic-embed-text model to turn text into vector embeddings
- Used for Document chunks (once, during setup)
- Used for User questions (every time you ask)
- This makes it possible to compare semantic similarity between text

#### loader.py
- A utility script to load documents
- Loads text files from te documents/ folder
- Splits each document into managable chunkcs
Returns a list of those chunks
- Used during the initial build to prepare text for embedding and storage

#### build_store.py
-  Setup script
- Loads text files (loader.py)
- Embeds the chunks (embedder.py)
- Saves teh FAISS index + texts (vector_store.py)
- Need to run this onec (whenever documents/ changes)

#### local_llm.py
- Sends the final prompt to Ollama
- Taks to locall llama3 model via HTTP
- Returns the LLM's output text
- Used by the rag_engine.py to do the generation step

### Runtime Flow
1. Main calls the rag_engine.ask(. . . )
2. Rag_engine.py 
- embeds the question,
- searches for top relevant docs in FAISS
- builds a prompt like:</br>
```Context: [matching document text]```</br>
```Question: [your question]```   
- Sends this prompt to local_llm.py (Ollama)
3. LLM generates an answer using the retrieved text
4. main.py returns that answer as the HTTP response

## Installation
Clone the repository:
```
git clone https://github.com/your-username/arcane-rag-app.git
cd arcane-rag-app
```


Install dependencies:


Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your environment variables in a .env file to make Curl commands:

```
API_SECRET_KEY=your-custom-secret
```

Prepare documents:

Place your 50–100 documents in a documents/ folder.

Run the provided embedding script to generate the vector store.

Run the app:

uvicorn main:app --reload
Usage
Send a POST request to the /ask endpoint with a JSON body:
```
{
  "question": "What is RAG architecture?",
  "api_key": "your-custom-secret"
}
```

The API will:

Validate your key

Embed your question

Retrieve top-k relevant document chunks

Send context and question to the LLM

Return a grounded, context-aware answer

You can test it using Postman or curl:

```
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is LangChain?", "api_key": "your-custom-secret"}'
```

## The Core Team
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
<br>
<span><i>Powered by FastAPI, FAISS/Chroma, and OpenAI or LLaMA 2</i></span>


lsof -i :8000
kill -9 (PID)

uvicorn main:app

curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is retrieval-augmented generation?",
    "api_key": "llm_secret_key"
  }'
