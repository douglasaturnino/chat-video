import os

import streamlit as st

from utils.helpers import get_file_size_mb, is_video_file
from views.utils_view import display_video


def render_sidebar():
    """Renderiza a barra lateral de upload e configuração."""
    st.header("🔑 API Configuration")
    default_api_key = os.getenv("GEMINI_API_KEY", "")
    api_key = st.text_input(
        "Gemini API Key",
        value=default_api_key,
        type="password",
        help="Get your API key from https://aistudio.google.com/app/apikey",
    )

    st.markdown("---")
    st.header("📹 Upload Video")

    uploaded_file = st.file_uploader(
        "Choose a video file",
        type=["mp4", "avi", "mov", "mkv", "webm"],
    )

    if uploaded_file and not is_video_file(uploaded_file):
        st.error("Please upload a valid video file.")
        return api_key, None

    if uploaded_file:
        size_mb = get_file_size_mb(uploaded_file)
        st.info(f"File size: {size_mb:.2f} MB")
        if size_mb > 100:
            st.warning("Large files may take longer to process or may fail.")

        display_video(uploaded_file.getvalue(), uploaded_file.name)

    return api_key, uploaded_file
