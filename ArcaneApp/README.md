# Welcome to My Arcane App

## Task
Build a Retrieval-Augmented Generation (RAG) API that connects to a local language model, retrieves relevant context from a small document set, and uses that context to generate more accurate answers to user questions.


## Description
This project addresses a core limitation of LLMs: their inability to access specific or up-to-date external knowledge. 

Imagine you're a company with confidential data. You want to use a language model, but you can't expose your data to public APIs. With RAG, you use a foundational LLM and augment it with your internal data . . . without retraining.

A RAG system resolves this by:

- Accepting a question through an API.
- Retrieving relevant context chunks from a vector database of documents.
- Sending both the question and retrieved context to an LLM.
- Returning the generated answer to the user via the API.

The app is built using 
- FastAPI for the API
- FAISS vector database for the vector store
- Ollama (Llama 3.2)
It also includes a simple API key security and logging. It's a functional, maintainable, and secure RAG prototype.

### Classes
#### main.py - API layer
- Defines the FastAPI server
- Defines POST/ask endpoint
- Accepts a JSON body with a question and api_key
- Uses the RagEngine to process the questions
- Returns an answer (or error message)
- This is the frontend API for the RAG app
#### rag_engine.py - Core logic (the brain)
- It embeds the quesiton
- Searches for relevant text chunks from FAISS
- Constructs a prompt using those retrieved texts
- Sends it to the local LLM
- Returns the model's final answer
- Combines retrieval and generation
#### vector_store.py - Document memory
- Handles the FAISS index and test storage
- Loads and saves the faiss.index (vector store)
- Loads and saves texts.pkl (raw source text chunks)
- Provides a .search(query_embedding) method to return relevant documents
- It's the document memory - optimized for fast vector search
#### embedder.py - Embedding engin
- Calls Ollama's nomic-embed-text model to turn text into vector embeddings
- Used for Document chunks (once, during setup)
- Used for User questions (every time you ask)
- This makes it possible to compare semantic similarity between text

#### loader.py - Document prep
- A utility script to load documents
- Loads text files from te documents/ folder
- Splits each document into managable chunkcs
- Returns a list of those chunks
- Used during the initial build to prepare text for embedding and storage

#### build_store.py - Index setup
- Setup script
- Loads text files (loader.py)
- Embeds the chunks (embedder.py)
- Saves the FAISS index + texts (vector_store.py)
- Need to run this once (whenever documents/ changes)

#### local_llm.py - LLM connector
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

Create a .env file to make Curl commands:

```
echo "API_SECRET_KEY=your-custom-secret" > .env
```

Add documents:

Place .txt files into the documents/folder (e.g.documents/birds.txt)
Run the provided embedding script to generate the vector store.
```
python3 build_store.py
```

Run the app:
```
uvicorn main:app --reload
```

## Usage
Send a POST request to the /ask endpoint with a JSON body:

```
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is LangChain?", "api_key": "your-custom-secret"}'
```

The API will:

- Validate your key
- Embed your question
- Retrieve top-k relevant document chunks
- Send context and question to the LLM
- Return a grounded, context-aware answer



## The Core Team
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
<br>
<span><i>Powered by FastAPI, FAISS/Chroma, and llama3.2:latest</i></span>


