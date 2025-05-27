import requests

def ask_local_llm(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:2:latest",
            "prompt": prompt,
            "stream": False
        }
    )

    try:
        data = response.json()
    except Exception as e:
        raise ValueError(f"Failed to parse JSON response: {e}. Response text: {response.text}")
    # return response.json()["response"]


    # Print raw response for debugging
    print("Raw response:", data)
    if "response" not in data:
        raise ValueError("LLM failed to generate. Ollama returned: {data}")
    
    return data["response"]