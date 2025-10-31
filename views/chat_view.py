import time

import streamlit as st


def render_chat_interface(api_key):
    """Renderiza a interface principal de chat."""
    st.title("🎬 Video RAG Com Gemini")
    st.markdown(
        "Faça o upload de um vídeo e converse com ele usando a IA Gemini do Google!"
    )

    if not api_key:
        st.info(
            "👈 Por favor, insira sua chave de API do Gemini na barra lateral."
        )
        return
    if not st.session_state.get("video_file"):
        st.info(
            "👈 Faça o upload de um arquivo de vídeo na barra lateral para iniciar o bate-papo."
        )
        return

    st.success(
        f"✅ Já pode conversar sobre: **{st.session_state.video_name}**"
    )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if len(st.session_state.messages) == 0:
        st.markdown("### 💡 Exemplos de perguntas:")
        examples = [
            "O que está acontecendo neste vídeo?",
            "Resuma os principais eventos",
            "Descreva as pessoas e os objetos que você vê",
            "Que ações estão ocorrendo?",
        ]
        cols = st.columns(2)
        for i, text in enumerate(examples):
            with cols[i % 2]:
                if st.button(f"💬 {text}", key=f"ex_{i}"):
                    st.session_state.messages.append(
                        {"role": "user", "content": text}
                    )
                    st.session_state["prompt"] = text
                    st.rerun()

    if (
        prompt := st.chat_input("Faça uma pergunta sobre o seu vídeo...")
        or st.session_state["prompt"]
    ):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Analisando o vídeo..."):
                vp = st.session_state.video_processor
                response = vp.chat_with_video(
                    st.session_state.video_file, prompt
                )

            if response:
                full_response = ""
                for chunk in response.split():
                    full_response += chunk + " "
                    message_placeholder.markdown(full_response + "▌")
                    time.sleep(0.02)
                message_placeholder.markdown(full_response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            else:
                st.error("Não foi possível gerar resposta. Tente novamente.")
