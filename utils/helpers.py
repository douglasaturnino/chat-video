import mimetypes

import google.generativeai as genai
import streamlit as st


def is_video_file(file):
    """Verifica se o arquivo enviado é um vídeo."""
    if not file:
        return False
    mime_type, _ = mimetypes.guess_type(file.name)
    return mime_type and mime_type.startswith("video/")


def get_file_size_mb(file):
    """Retorna o tamanho do arquivo em MB."""
    return len(file.getvalue()) / (1024 * 1024)


def reset_chat():
    """Limpa o estado da sessão e remove arquivos do Gemini."""
    st.session_state.messages = []
    if "video_file" in st.session_state:
        try:
            genai.delete_file(st.session_state.video_file.name)
        except:
            pass
        del st.session_state.video_file
    for key in ["video_processor", "video_name"]:
        st.session_state.pop(key, None)
