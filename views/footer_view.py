import streamlit as st


def render_footer():
    """Renderiza o rodapé da aplicação."""
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align:center;color:#666;'>
            Built with ❤️ using Gemini API and Streamlit |
            <a href='https://ai.google.dev/gemini-api/docs/video-understanding' target='_blank'>
            Learn more about Gemini Video API</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
