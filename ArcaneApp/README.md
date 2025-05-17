#### Welcome to My Arcane App

###
Task
Build a Retrieval-Augmented Generation (RAG) API that connects to a local or cloud-based language model, retrieves relevant context from a small document set, and uses that context to generate more accurate answers to user questions.


Description
This project addresses a core limitation of LLMs: their inability to access specific or up-to-date external knowledge. A RAG system resolves this by:

Receiving a question through an API.

Retrieving relevant context chunks from a vector database of documents.

Sending both the question and retrieved context to an LLM.

Returning the generated answer to the user via the API.

The app is built using FastAPI, integrates with a vector store (FAISS or ChromaDB), and connects to either OpenAI’s GPT-4 or a local LLaMA 2 instance. It includes basic API key security and simple logging. The goal is a functional, maintainable, and secure RAG prototype.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/arcane-rag-app.git
cd arcane-rag-app
Install dependencies:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Add your environment variables in a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your-api-key
API_SECRET_KEY=your-custom-secret
Prepare documents:

Place your 50–100 documents in a documents/ folder.

Run the provided embedding script to generate the vector store.

Run the app:

bash
Copy
Edit
uvicorn main:app --reload
Usage
Send a POST request to the /ask endpoint with a JSON body:

json
Copy
Edit
{
  "question": "What is RAG architecture?",
  "api_key": "your-custom-secret"
}
The API will:

Validate your key

Embed your question

Retrieve top-k relevant document chunks

Send context and question to the LLM

Return a grounded, context-aware answer

You can test it using Postman or curl:

bash
Copy
Edit
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is LangChain?", "api_key": "your-custom-secret"}'
The Core Team
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
<br>
<span><i>Powered by FastAPI, FAISS/Chroma, and OpenAI or LLaMA 2</i></span>

