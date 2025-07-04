import streamlit as st

st.set_page_config(page_title="Chatbot Conversacional", page_icon="💬", layout="centered")
st.markdown("""
    <style>
    .chat-bubble {
        border-radius: 1.2em;
        padding: 0.7em 1.2em;
        margin-bottom: 0.4em;
        max-width: 80%;
        font-size: 1.1em;
        line-height: 1.5em;
        display: inline-block;
    }
    .bot {
        background: #f0f2f6;
        color: #222;
        border: 1px solid #e6e6e6;
        margin-right: auto;
    }
    .user {
        background: #007bff;
        color: #fff;
        border: 1px solid #007bff;
        margin-left: auto;
    }
    .chat-container {
        min-height: 300px;
        margin-bottom: 1em;
        padding: 1em 0.5em;
        background: #fafbfc;
        border-radius: 1em;
        box-shadow: 0 2px 12px #0001;
    }
    .input-row {
        display: flex;
        gap: 0.5em;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Chatbot Conversacional")

# Botón para limpiar chat
if st.button("🧹 Limpiar conversación"):
    st.session_state['messages'] = []
    st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()

# Inicializar historial
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Mostrar historial en burbujas
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.markdown(f'<div class="chat-bubble user">🧑‍💻 <b>Tú:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble bot">🤖 <b>Bot:</b> {msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Entrada de usuario en una fila
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("", placeholder="Escribe tu mensaje y presiona Enviar...", key="input")
with col2:
    send_clicked = st.button("Enviar", use_container_width=True)

if send_clicked and user_input:
    st.session_state['messages'].append({'role': 'user', 'content': user_input})

    import os
    from llama_cpp import Llama

    MODEL_PATH = "models/llama-2-7b-chat.Q2_K.gguf"  # Cambia por el nombre de tu modelo si es diferente
    if not os.path.exists(MODEL_PATH):
        bot_response = "⚠️ Modelo no encontrado. Por favor, guarda tu modelo GGUF en la carpeta 'models'."
    else:
        import sys
        print('DEBUG: Antes de crear Llama', file=sys.stderr)
        if 'llm' not in st.session_state:
            st.session_state['llm'] = Llama(model_path=MODEL_PATH)
        print('DEBUG: Llama cargado', file=sys.stderr)
        llm = st.session_state['llm']
        prompt = user_input
        print(f'DEBUG: Prompt: {prompt}', file=sys.stderr)
        try:
            output = llm(prompt, max_tokens=128, stop=None, echo=False)
            print(f'DEBUG: Output: {output}', file=sys.stderr)
            bot_response = output['choices'][0]['text'].strip() if 'choices' in output and output['choices'] else '(Sin respuesta)'
        except Exception as e:
            print(f'DEBUG: Error llamando al modelo: {e}', file=sys.stderr)
            bot_response = f'(Error llamando al modelo: {e})'
    st.session_state['messages'].append({'role': 'bot', 'content': bot_response})
    print('DEBUG: Antes de rerun', file=sys.stderr)
    st.rerun()

