import streamlit as st

from utils.helpers import reset_chat


def render_sidebar_controls():
    """Renderiza os botões de controle da barra lateral (Clear / Reset)."""
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    with col2:
        if st.button("🔄 Reset All"):
            reset_chat()
            st.rerun()
