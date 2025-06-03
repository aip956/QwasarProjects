import requests


def warm_up_model(model="nomic-embed-text"):
    """
    Ensure the model is loaded before using it.
    """
    requests.post("http://localhost:11434/api/pull",json={
        "name": model
    })

# rag_engin calls this function to embed user's question during /ask API call and
# build_store.py calls it to embed documents during vector store building.
def get_embedding(text, model="nomic-embed-text"):
    # Ensure the model is loaded before making the request
    warm_up_model(model)

    # Send the text to the Ollama API to get the embedding
    response = requests.post("http://localhost:11434/api/embeddings", json={
        "model": model,
        "text": text
    })

    # Validate the response
    if response.status_code != 200 or 'embedding' not in response.json():
        raise Exception(f"Error: {response.status_code} - {response.text}")
    # Return the embedding from the response
    return response.json()['embedding']

