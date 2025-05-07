import streamlit as st
from voz import transcrever_audio_arquivo

st.title("🎙️ Transcrição de Áudio com Avelyn")

arquivo_audio = st.file_uploader("Envie um áudio .wav", type=["wav"])

if arquivo_audio:
    with open("temp_audio.wav", "wb") as f:
        f.write(arquivo_audio.read())

    with st.spinner("Transcrevendo..."):
        try:
            texto = transcrever_audio_arquivo("temp_audio.wav")
            st.success("🧾 Transcrição:")
            st.write(texto)
        except Exception as e:
            st.error(f"Erro: {e}")
