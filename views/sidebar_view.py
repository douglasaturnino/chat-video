import os

import streamlit as st

from utils.helpers import get_file_size_mb, is_video_file
from views.utils_view import display_video


def render_sidebar():
    """Renderiza a barra lateral de upload e configuração."""
    st.header("🔑 Configuração da API")
    default_api_key = None
    api_key = st.text_input(
        "Gemini API Key",
        value=default_api_key,
        type="password",
        help="Como conseguir a API https://aistudio.google.com/app/apikey",
    )

    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "")

    st.markdown("---")
    st.header("📹 Upload Video")

    uploaded_file = st.file_uploader(
        "Escolha um vídeo no formato",
        type=["mp4", "avi", "mov", "mkv", "webm"],
    )

    if uploaded_file and not is_video_file(uploaded_file):
        st.error("Por favor, envie um vídeo válido.")
        return api_key, None

    if uploaded_file:
        size_mb = get_file_size_mb(uploaded_file)
        st.info(f"Tamanho do arquivo: {size_mb:.2f} MB")
        if size_mb > 100:
            st.warning(
                "Arquivos grandes podem demorar mais para serem processados ​​ou podem apresentar falhas."
            )

        display_video(uploaded_file.getvalue(), uploaded_file.name)

    return api_key, uploaded_file
