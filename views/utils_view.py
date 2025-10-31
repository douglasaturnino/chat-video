import streamlit as st


def display_video(video_bytes, video_name):
    """Exibe o vídeo carregado na interface."""
    st.markdown(f"### 🎬 {video_name}")
    st.video(video_bytes)
