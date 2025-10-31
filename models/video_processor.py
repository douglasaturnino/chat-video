import time

import google.generativeai as genai
import streamlit as st


class VideoProcessor:
    """Responsável pela comunicação com a API do Gemini e processamento de vídeo."""

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def upload_video(self, video_path: str, display_name=None):
        """Faz upload do vídeo para a API do Gemini."""
        try:
            return genai.upload_file(
                path=video_path, display_name=display_name or "uploaded_video"
            )
        except Exception as e:
            st.error(f"Erro ao enviar vídeo: {str(e)}")
            return None

    def wait_for_file_processing(self, video_file):
        """Aguarda o processamento do vídeo pelo Gemini."""
        try:
            while video_file.state.name == "PROCESSING":
                time.sleep(2)
                video_file = genai.get_file(video_file.name)
            if video_file.state.name == "FAILED":
                raise ValueError("Falha no processamento do vídeo.")
            return video_file
        except Exception as e:
            st.error(f"Erro durante o processamento: {str(e)}")
            return None

    def chat_with_video(self, video_file, prompt: str):
        """Gera resposta baseada no conteúdo do vídeo e no prompt do usuário."""
        try:
            response = self.model.generate_content([video_file, prompt])
            return response.text
        except Exception as e:
            st.error(f"Erro ao gerar resposta: {str(e)}")
            return None
