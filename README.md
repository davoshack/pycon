# 📘 Laboratorio Local de IA con Docker Model Runner

## ✨ Objetivo del taller
Este laboratorio te guía paso a paso para ejecutar un modelo de lenguaje (LLM) localmente usando Docker Model Runner, con dos interfaces posibles:

- **Open WebUI**: Una interfaz web estilo ChatGPT.
- **Python (Streamlit y consola)**: Para quienes desean personalizar su experiencia o integrar con sus propios proyectos.

---

## 🧰 Requisitos
- ✅ Docker Desktop v4.40 o superior
- ✅ Terminal (macOS, Linux, Git Bash o PowerShell)
- ✅ Conexión inicial para descargar el modelo `.gguf`
- ✅ Python 3.9+ con `llama-cpp-python` y `streamlit` para uso personalizado

---

## 🗂️ Estructura del proyecto

```
llama_lab/
├── app.py                # Chatbot en Streamlit
├── main.py               # Interfaz por consola con selección de modelo
├── requirements.txt      # Dependencias Python (llama-cpp-python, streamlit)
├── README.md             # Esta guía
├── LICENSE
├── .gitignore
└── models/               # Carpeta donde se guarda el modelo GGUF
```

---

## 🧪 Parte 1: Laboratorio Web con Docker y Open WebUI

### 🔹 Paso 1: Activar Docker Model Runner
```bash
docker desktop enable model-runner --no-tcp
```

### 🔹 Paso 2: Descargar un modelo ligero
```bash
docker model pull ai/gemma3-qat:1B-Q4_K_M
```

### 🔹 Paso 3: Crear el archivo `docker-compose.yaml`
```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OPENAI_API_BASE_URL=http://model-runner.docker.internal:80/engines/llama.cpp/v1
      - OPENAI_API_KEY=na
    volumes:
      - open-webui-data:/app/backend/data
    depends_on:
      - ai-runner

  ai-runner:
    provider:
      type: model
      options:
        model: ai/gemma3-qat:1B-Q4_K_M

volumes:
  open-webui-data:
```

### 🔹 Paso 4: Ejecutar el entorno
```bash
docker compose up
```

### 🔹 Paso 5: Abrir la interfaz en tu navegador
[http://localhost:3000](http://localhost:3000)

---

## 🐍 Parte 2: Laboratorio en Python (Opcional)

### 1️⃣ Ejecutar en consola
```bash
python main.py
```
Selecciona un modelo `.gguf` y comienza a escribir tus prompts.

### 2️⃣ Ejecutar interfaz gráfica con Streamlit
```bash
streamlit run app.py
```

Interactúa con el modelo local usando una interfaz estilo chat. Ideal para demos o personalización.

---

## 📦 Requisitos de Python

Instala dependencias con:

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:
```
llama-cpp-python==0.3.10
streamlit
```

---

## 🧼 Para detener Docker
```bash
Ctrl + C
docker compose down
```

---

## 💫 Créditos y agradecimientos

Gracias por ser parte de este taller de IA local 💻🐳  
¡Ahora tienes un laboratorio mágico de LLMs corriendo directamente en tu máquina! ✨
