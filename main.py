import os
import tempfile
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from models.video_processor import VideoProcessor
from views.chat_view import render_chat_interface
from views.footer_view import render_footer
from views.sidebar_controls import render_sidebar_controls
from views.sidebar_view import render_sidebar

st.set_page_config(
    page_title="Video RAG Com Gemini", page_icon="🎬", layout="wide"
)
load_dotenv()

for key in [
    "messages",
    "video_file",
    "video_processor",
    "video_name",
    "prompt",
]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "messages" else []

with st.sidebar:
    api_key, uploaded_file = render_sidebar()
    render_sidebar_controls()

if api_key and uploaded_file:
    if not st.session_state.video_processor:
        st.session_state.video_processor = VideoProcessor(api_key)

    vp = st.session_state.video_processor

    if st.session_state.video_name != uploaded_file.name:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=Path(uploaded_file.name).suffix
        ) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        with st.spinner("Uploading and processing video..."):
            video_file = vp.upload_video(tmp_path, uploaded_file.name)
            if video_file:
                processed = vp.wait_for_file_processing(video_file)
                if processed:
                    st.session_state.video_file = processed
                    st.session_state.video_name = uploaded_file.name
                    st.session_state.messages = []
                    st.success("✅ Video processed successfully!")

        os.unlink(tmp_path)

render_chat_interface(api_key)

render_footer()
