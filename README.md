# Taller: Laboratorio local de IA

**Título:** Laboratorio local de IA: Corre modelos con Python y Docker sin complicaciones  
**Duración estimada:** 2 a 2.5 horas  
**Objetivo:** Aprender a correr modelos de IA de manera local usando Docker Model Runner sin necesidad de configurar entornos complejos. Descubrirás cómo usar Docker para levantar un modelo de lenguaje en tu máquina, consultar su API y experimentar con IA de forma accesible y reproducible.

---

## 🔧 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**: esta es la herramienta principal. Incluye el motor de Docker que nos permitirá ejecutar contenedores.
- **Git**: útil para clonar repositorios con ejemplos.
- **Editor de texto**: Visual Studio Code o cualquier editor que te guste.

Además:
- Tener espacio libre en disco (~5GB) ya que algunos modelos ocupan bastante.
- Conexión a internet estable para descargar las imágenes y modelos.
- Familiaridad básica con la terminal o consola de comandos.

---

## 1. 🌟 Introducción al taller

### ¿Qué haremos hoy?
- Usarás Docker para correr un modelo de lenguaje natural localmente.
- Interactuarás con ese modelo desde tu máquina, sin necesidad de instalar librerías como Transformers o TensorFlow.
- Entenderás cómo funciona el archivo `model-runner.yaml` y cómo cambiar el modelo fácilmente.

### ¿Por qué usar Docker?
- Imagina que el modelo es como una app complicada de instalar. Docker te da una "cajita" lista para usar.
- Todo lo necesario (sistema, librerías, entorno) está empaquetado en un contenedor.
- Puedes compartir o mover esa "cajita" a cualquier máquina y funcionará igual.
- Te ahorra tiempo, evita errores de configuración y mantiene tu entorno limpio.

---

## 2. 🤖 ¿Qué es Docker Model Runner?

Docker Model Runner es una solución pensada para simplificar el uso de modelos de IA en contenedores. Está desarrollado por Docker y hace que correr modelos como LLaMA, Mistral, Gemma u otros, sea tan fácil como definir dos líneas en un archivo de configuración.

### ¿Cómo funciona?
- Lee el archivo `model-runner.yaml`.
- Según el modelo y backend definido (como `ollama`), descarga y configura automáticamente el contenedor correcto.
- Te expone una API tipo OpenAI que puedes consultar desde Python, cURL o tu navegador.

### ¿Qué es Ollama?
- Ollama es una tecnología que permite correr modelos LLM localmente, optimizados y fácilmente integrables.
- Docker Model Runner lo usa como backend por defecto para muchos modelos.

---

## 3. 📁 Clonar el repositorio de ejemplo

Usaremos un ejemplo compartido por Bret Fisher. Para empezar, abre la terminal y ejecuta:

```bash
git clone https://gist.github.com/BretFisher/aafd46eeb7acef2f5ef7d1ea70abe2ad model-runner-demo
cd model-runner-demo
```

Esto descargará el archivo `model-runner.yaml` que usaremos.

---

## 4. 📝 Explorar el archivo `model-runner.yaml`

Abre el archivo con tu editor:

```bash
code model-runner.yaml
```

Contenido típico:

```yaml
model: llama3
backend: ollama
```

- `model`: el nombre del modelo que quieres correr. En este caso, es `llama3`.
- `backend`: define cómo se corre el modelo. Aquí usamos `ollama`, que permite modelos LLM locales.

Este archivo actúa como la receta que Docker Model Runner va a leer.

---

## 5. 🐳 Ejecutar el modelo con Docker CLI

Ahora vamos a correr el modelo localmente con Docker:

```bash
docker run -it --rm \
  -v $(pwd)/model-runner.yaml:/etc/model-runner/model-runner.yaml \
  -p 11434:11434 \
  docker/model-runner
```

### ¿Qué hace cada parte?
- `docker run`: comando para iniciar un contenedor.
- `-it`: modo interactivo.
- `--rm`: borra el contenedor al salir.
- `-v`: monta tu archivo `model-runner.yaml` dentro del contenedor.
- `-p 11434:11434`: abre el puerto 11434 (el modelo corre ahí).
- `docker/model-runner`: imagen oficial que correrá el modelo por ti.

Cuando el modelo esté listo verás algo como:

```
Model loaded. Listening on :11434
```

Eso significa que ya puedes consultarlo desde tu máquina.

---

## 6. 🧪 Probar el modelo con cURL

Abre otra terminal (sin cerrar la que tiene Docker corriendo) y ejecuta:

```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "messages": [{"role": "user", "content": "¿Qué es la inteligencia artificial?"}]
}'
```

### ¿Qué hace esto?
- Le envía un mensaje al modelo usando la API.
- El modelo responde con una respuesta generada.

Verás una respuesta en formato JSON con el contenido del modelo, similar al estilo de OpenAI.

---

## 7. 🔁 Cambiar de modelo

Si quieres probar otro modelo:

1. Edita `model-runner.yaml`:

```yaml
model: mistral
backend: ollama
```

2. Vuelve a correr el comando de `docker run`.

**Consejo:** consulta modelos compatibles aquí 👉 [https://ollama.com/library](https://ollama.com/library)

---

## 8. 🐍 Usar Python para interactuar con el modelo

Si prefieres escribir un script en Python:

### Crea `chat.py` con este contenido:

```python
import requests

url = "http://localhost:11434/v1/chat/completions"
headers = {"Content-Type": "application/json"}
payload = {
    "model": "llama3",
    "messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Ejecutar:

```bash
python chat.py
```

Esto hace exactamente lo mismo que el `curl`, pero en tu propio código. ¡Listo para usar en apps reales!

---

## 9. ✅ Cierre del taller

### ¿Qué aprendimos?
- Cómo levantar un modelo de lenguaje local usando solo Docker.
- Cómo consultar su API local con `curl` y Python.
- Cómo cambiar el modelo editando un simple archivo YAML.

### ¿Qué podrías hacer ahora?
- Crear una pequeña app con FastAPI y conectarla al modelo.
- Usar modelos que respondan en español.
- Hacer un chatbot local sin conexión a internet usando tu propio modelo.

### Recursos útiles
- [Docker Model Runner Docs](https://docs.docker.com/ai/model-runner/)
- [Ollama Library](https://ollama.com/library)
- [Gist de Bret Fisher](https://gist.github.com/BretFisher/aafd46eeb7acef2f5ef7d1ea70abe2ad)

---

Gracias por ser parte de este taller 💫 ¡Ahora tienes un laboratorio de IA corriendo en tu máquina! 🧪🐳
