import streamlit as st


def render_footer():
    """Renderiza o rodapé da aplicação."""
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align:center;color:#666;'>
            <a href='https://ai.google.dev/gemini-api/docs/video-understanding' target='_blank'>
            Saiba mais sobre a API de vídeo Gemini.</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
