import requests


def warm_up_model(model="nomic-embed-text"):
    """
    Ensure the model is loaded before using it.
    """
    requests.post("http://localhost:11434/api/pull",json={
        "name": model
    })

def get_embedding(text, model="nomic-embed-text"):
    warm_up_model(model)
    response = requests.post("http://localhost:11434/api/embeddings", json={
        "model": model,
        "text": text
    })

    # Validate the response
    if response.status_code != 200 or 'embedding' not in response.json():
        raise Exception(f"Error: {response.status_code} - {response.text}")
    return response.json()['embedding']

