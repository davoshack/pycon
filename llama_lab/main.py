import os
from llama_cpp import Llama

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")


def list_models():
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
    models = [f for f in os.listdir(MODELS_DIR) if f.endswith(".gguf")]
    return models


def select_model():
    models = list_models()
    if not models:
        print(f"No se encontraron modelos en {MODELS_DIR}. Por favor, descarga un modelo GGUF y colócalo allí.")
        exit(1)
    print("Modelos disponibles:")
    for idx, model in enumerate(models):
        print(f"  [{idx+1}] {model}")
    while True:
        choice = input(f"Selecciona un modelo [1-{len(models)}]: ")
        if choice.isdigit() and 1 <= int(choice) <= len(models):
            return os.path.join(MODELS_DIR, models[int(choice)-1])
        else:
            print("Opción inválida. Intenta de nuevo.")


def main():
    print("\n=== Laboratorio Local de Modelos de Lenguaje ===\n")
    model_path = select_model()
    print(f"\nCargando modelo: {model_path}\nEsto puede tardar unos segundos...")
    llm = Llama(model_path=model_path, n_ctx=2048)
    print("\n¡Modelo cargado! Puedes comenzar a escribir tus preguntas. Escribe 'salir' para terminar.\n")
    while True:
        prompt = input("Tú: ")
        if prompt.strip().lower() == "salir":
            print("Hasta luego!")
            break
        response = llm(prompt, max_tokens=256, stop=["\n", "Tú:"])
        print("Modelo:", response["choices"][0]["text"].strip())


if __name__ == "__main__":
    main()
