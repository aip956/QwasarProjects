import requests

def ask_local_llm(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:3b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["resopnse"]