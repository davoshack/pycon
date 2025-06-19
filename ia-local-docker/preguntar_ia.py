import requests

url = "http://localhost:3000/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer na"
}

data = {
    "model": "llama.cpp",  
    "messages": [
        {"role": "system", "content": "Eres un asistente útil y simpático."},
        {"role": "user", "content": "¿Cuál es la capital de Colombia?"}
    ],
    "temperature": 0.7
}

response = requests.post(url, json=data, headers=headers)
print(response.json())