import openai

# Configura el endpoint local
openai.api_base = "http://localhost:12434/v1"
openai.api_key = "not-needed"  # No se requiere API key para el Model Runner

response = openai.ChatCompletion.create(
    model="llama2",  # Usa el modelo que hayas cargado, ej: ai/smollm2:360M-Q4_K_M
    messages=[
        {"role": "system", "content": "Eres un asistente útil"},
        {"role": "user", "content": "¿Qué es Docker Model Runner?"}
    ],
    temperature=0.7,
)

print(response['choices'][0]['message']['content'])
