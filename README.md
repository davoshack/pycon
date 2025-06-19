
# 📘 Laboratorio Local de IA con Docker Model Runner

## ✨ Objetivo del taller

Este laboratorio guía paso a paso cómo ejecutar un modelo de lenguaje local (LLM) usando [Docker Model Runner](https://docs.docker.com/ai/model-runner/) y Open WebUI, sin necesidad de conexión a Internet ni acceso a la API de OpenAI.

---

## 🧰 Requisitos

- ✅ Docker Desktop v4.40 o superior instalado
- ✅ Terminal (macOS, Linux o Git Bash/PowerShell en Windows)
- ✅ Conexión inicial a Internet para descargar el modelo (solo la primera vez)

---

## 📁 Estructura del proyecto

```
ia-local-docker/
├── docker-compose.yaml       # Archivo para levantar el modelo y WebUI
├── preguntar_ia.py           # (opcional) Script en Python para usar la API local
├── README.md                 # Esta guía
└── notas/
    └── comandos.txt          # Historial de comandos ejecutados
```

---

## 🧪 Paso a paso del laboratorio

### 🔹 Paso 1: Activar Docker Model Runner

```bash
docker desktop enable model-runner --no-tcp
```

---

### 🔹 Paso 2: Descargar el modelo

```bash
docker model pull ai/gemma3-qat:1B-Q4_K_M
```

---

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

---

### 🔹 Paso 4: Levantar el entorno

```bash
docker compose up
```

---

### 🔹 Paso 5: Acceder a la interfaz

Abre [http://localhost:3000](http://localhost:3000) en tu navegador.

---

### 🐍 Paso 6: (Opcional) Usar el modelo desde Python

*(Este paso se realizará más adelante.)*

---

### 🧼 Para detener todo:

```bash
Ctrl + C
docker compose down
```

Gracias por ser parte de este taller 💫 ¡Ahora tienes un laboratorio de IA corriendo en tu máquina! 🧪🐳
