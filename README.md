# 📘 Laboratorio Local de IA con Python y Docker

## ✨ Objetivo del taller
Este laboratorio te guía paso a paso para ejecutar un modelo de lenguaje (LLM) localmente usando herramientas open source. Explorarás dos caminos:

- **Python (Streamlit y consola)**: Para quienes desean personalizar su experiencia o integrar con sus propios proyectos.
- **Open WebUI con Docker**: Una interfaz web estilo ChatGPT, rápida de levantar sin código.

---

## 🧰 Requisitos
- ✅ Python 3.9+ (ideal 3.10) con `llama-cpp-python` y `streamlit`
- ✅ Docker Desktop v4.40 o superior
- ✅ Terminal (macOS, Linux, Git Bash o PowerShell)
- ✅ Conexión inicial para descargar el modelo `.gguf`

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

## 🐍 Parte 1: Laboratorio en Python

### 1️⃣ Ejecutar en consola
```bash
python main.py
```
Selecciona un modelo `.gguf` y comienza a escribir tus prompts.

### 2️⃣ Ejecutar interfaz gráfica con Streamlit
```bash
streamlit run app.py
```

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

## 🪟 Guía para usuarios de Windows

### 🔧 Requisitos adicionales

1. ✅ Tener Python 3.10 instalado.
2. ✅ Actualiza pip:
   ```powershell
   python -m pip install --upgrade pip
   ```
3. ✅ Instala CMake:
   ```powershell
   pip install cmake
   ```

---

### 🔮 Crear y activar el entorno virtual

```powershell
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  # Solo si es necesario
.env\Scriptsctivate
```

---

### 📦 Instalar dependencias
```powershell
pip install llama-cpp-python==0.3.10 streamlit
```

---

### ▶️ Ejecutar el chatbot
```powershell
python main.py
# o
streamlit run app.py
```

---

## 🍎 Guía para usuarios de macOS

### 🔧 Requisitos adicionales

1. ✅ Tener Python 3.10+ instalado.
2. ✅ Tener Xcode Command Line Tools:
   ```bash
   xcode-select --install
   ```

---

### 🔮 Crear y activar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 Instalar dependencias
```bash
pip install --upgrade pip
pip install llama-cpp-python==0.3.10 streamlit
```

---

### ▶️ Ejecutar el chatbot
```bash
python3 main.py
# o
streamlit run app.py
```

---

## 🐳 Parte 2: Laboratorio Web con Docker y Open WebUI

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

## 🧼 Para detener Docker
```bash
Ctrl + C
docker compose down
```

---

## 💫 Créditos y agradecimientos

Gracias por ser parte de este taller de IA local 💻🐳  
¡Ahora tienes un laboratorio mágico de LLMs corriendo directamente en tu máquina! ✨


---

## ❗ Errores comunes y cómo solucionarlos

### 🔧 `ModuleNotFoundError: No module named 'llama_cpp'`

Esto significa que `llama-cpp-python` no está instalado correctamente. Solución:

1. Asegúrate de estar en tu entorno virtual:
   ```bash
   .\venv\Scripts\activate  # en Windows
   source venv/bin/activate   # en macOS/Linux
   ```

2. Instala el paquete:
   ```bash
   pip install llama-cpp-python
   ```

---

### ⚠️ Error de compilación: `error: command 'cmake' failed: None` o `Unknown compiler(s): [['cl'], ['gcc'], ['clang']]`

Esto indica que falta un compilador de C/C++ para compilar dependencias como `llama-cpp-python` o `pyarrow`.

#### ✅ En Windows:

- Instala `cmake` con:
  ```powershell
  pip install cmake
  ```

- Asegúrate de tener instalado **Visual C++ Build Tools**:
  - Descárgalos desde: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
  - Durante la instalación, selecciona:
    ```
    ✅ C++ build tools
    ✅ Windows 10 SDK
    ```

- Luego vuelve a intentar:
  ```powershell
  pip install llama-cpp-python==0.3.10
  ```

---

#### ✅ En macOS:

- Asegúrate de tener instaladas las herramientas de línea de comandos:
  ```bash
  xcode-select --install
  ```

- Luego ejecuta:
  ```bash
  pip install cmake
  pip install llama-cpp-python
  ```

---

¿Aún tienes problemas? Asegúrate de tener Python 3.10 instalado y crea un entorno limpio para evitar conflictos.

---

## 💬 ¿Te ayudó esta guía?

Si este laboratorio te sirvió, comparte tu experiencia y mejora este proyecto en [github.com/marisbotero](https://github.com/marisbotero) 💫


---

## ⚙️ Instalación de llama-cpp-python en Windows: dos caminos

### 🔮 Opción A: Instalar con `.whl` precompilado (recomendado para talleres)

Si no quieres instalar compiladores ni herramientas de desarrollo, puedes usar un archivo `.whl` ya compilado:

1. Ve a esta página oficial y confiable:
   👉 https://www.lfd.uci.edu/~gohlke/pythonlibs/#llama-cpp-python

2. Descarga el archivo que coincida con tu versión de Python. Por ejemplo:

   ```
   llama_cpp_python‑0.3.10‑cp310‑cp310‑win_amd64.whl
   ```

   (para Python 3.10 en Windows 64 bits)

3. Abre PowerShell y ve a la carpeta donde guardaste el archivo:
   ```powershell
   cd C:\Users\TU_USUARIO\Downloads
   pip install .\nombre_del_archivo.whl
   ```

✅ Esta es la forma más rápida y sin errores de instalar `llama-cpp-python` en Windows.

---

### 🛠️ Opción B: Instalar compiladores y compilar desde pip (para usuarios técnicos)

Si prefieres instalar todo desde cero con `pip`, necesitas un compilador de C/C++ y `cmake`.

1. Instala CMake:
   ```powershell
   pip install cmake
   ```

2. Instala Visual C++ Build Tools:
   👉 https://visualstudio.microsoft.com/visual-cpp-build-tools/

   Durante la instalación, asegúrate de marcar:
   ```
   ✅ C++ build tools
   ✅ Windows 10 SDK
   ```

3. Luego, instala llama-cpp-python normalmente:
   ```powershell
   pip install llama-cpp-python==0.3.10
   ```

❗ Esta opción es más pesada y puede causar errores si faltan componentes del sistema.

---

✅ **Recomendación general**: si solo quieres usar el laboratorio, la **Opción A (archivo `.whl`) es suficiente y más rápida**.


## 💫 Créditos y agradecimientos

Gracias por ser parte de este taller de IA local 💻🐳  
¡Ahora tienes un laboratorio mágico de LLMs corriendo directamente en tu máquina! ✨
