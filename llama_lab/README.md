# Laboratorio Local de Modelos de Lenguaje con llama-cpp-python

Este laboratorio te permite ejecutar modelos de lenguaje (LLM) localmente en tu PC con Windows, usando Python y la librería `llama-cpp-python`, sin necesidad de internet, Docker o APIs externas.

## Requisitos
- Python 3.8 o superior
- Windows 10/11

## Instalación

### Windows
1. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

### macOS / Linux
1. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Descarga de modelo compatible
Debes descargar un modelo compatible en formato GGUF. Ejemplo:
- [TheBloke/Llama-2-7B-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-GGUF)
- [TheBloke/Mistral-7B-Instruct-v0.2-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

Descarga el archivo `.gguf` (por ejemplo, `llama-2-7b.Q4_K_M.gguf`) y colócalo en la carpeta `models` dentro de este proyecto.

## Uso
Ejecuta el script principal:
```sh
python main.py
```

Sigue las instrucciones en pantalla para interactuar con el modelo desde la línea de comandos.

## Créditos
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
