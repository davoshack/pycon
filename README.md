# Taller: Laboratorio local de IA

**Título:** Laboratorio local de IA: Corre modelos con Python y Docker sin complicaciones  
**Duración estimada:** 2 a 2.5 horas  
**Objetivo:** Aprender a correr modelos de IA de manera local usando Docker Model Runner sin necesidad de configurar entornos complejos.

---

## 🔧 Requisitos previos

- Tener instalado:
  - Docker Desktop (con Docker Compose v2)
  - Git
  - VSCode u otro editor de texto
- Clonar el repositorio base del taller (se proporcionará al inicio)

---

## 1. Introducción al taller

### Objetivo general
Correr modelos de lenguaje de manera local usando contenedores Docker con configuraciones simples.

### ¿Por qué Docker para IA?
- Evitas problemas de instalación de dependencias.
- Entornos reproducibles y portables.
- Ideal para pruebas, demos y despliegues.

---

## 2. ¿Qué es Docker Model Runner?

- Proyecto oficial de Docker para correr modelos LLM en contenedores.
- Permite definir el modelo y configuración en un archivo `model-runner.yaml`.
- Compatible con OpenAI, Hugging Face, Ollama y más.

### Recursos:
- [Documentación oficial](https://docs.docker.com/ai/model-runner/)
- [Gist de Bret Fisher](https://gist.github.com/BretFisher/aafd46eeb7acef2f5ef7d1ea70abe2ad)

---

## 3. Primer modelo: Demo de texto con Docker Compose

### Paso a paso:

```bash
# 1. Clonar el gist de Bret Fisher
git clone https://gist.github.com/BretFisher/aafd46eeb7acef2f5ef7d1ea70abe2ad model-runner-demo
cd model-runner-demo

# 2. Explora el archivo model-runner.yaml
code model-runner.yaml

# 3. Levanta el servicio
docker compose up

# 4. Probar con curl
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
  "model": "llama3",
  "messages": [{"role": "user", "content": "¿Cuál es la capital de Colombia?"}]
}'
```

---

## 4. ¿Qué pasa por dentro?

- El contenedor descarga y levanta el modelo `llama3` usando Ollama.
- Docker Model Runner actúa como orquestador del modelo.
- Se expone un endpoint OpenAI compatible en `localhost:11434`.

---

## 5. Crea tu propio model-runner.yaml

### Ejercicio:
- Edita `model-runner.yaml` para usar otro modelo disponible en Ollama o Hugging Face.
- Ejemplo de cambio:
```yaml
model: mistral
backend: ollama
```

- Vuelve a correr el contenedor y valida que funcione.

---

## 6. Bonus: Integra con una app Python

### Archivos extra:
- `app.py` con FastAPI
- `docker-compose.override.yml` para correr ambos servicios

### Prueba local
```bash
docker compose -f docker-compose.yml -f docker-compose.override.yml up
```

---
