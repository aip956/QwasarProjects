import requests

def get_embedding(text, model="nomic-embed-text"):
    response = requests.post("http://localhost:11434/api/embddings", json={

    })

    # Validate the response
    if response.status_code != 200 or 'embedding' not in response.json():
        raise Exception(f"Error: {response.status_code} - {response.text}")
    return response.json()['embedding']

