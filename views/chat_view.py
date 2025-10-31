import time

import streamlit as st


def render_chat_interface(api_key):
    """Renderiza a interface principal de chat."""
    st.title("🎬 Video RAG with Gemini")
    st.markdown("Upload a video and chat with it using Google's Gemini AI!")

    if not api_key:
        st.info("👈 Please enter your Gemini API key in the sidebar.")
        return
    if not st.session_state.get("video_file"):
        st.info(
            "👈 Please upload a video file in the sidebar to start chatting."
        )
        return

    st.success(f"✅ Ready to chat about: **{st.session_state.video_name}**")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if len(st.session_state.messages) == 0:
        st.markdown("### 💡 Example questions:")
        examples = [
            "What is happening in this video?",
            "Summarize the main events",
            "Describe the people and objects you see",
            "What actions are taking place?",
        ]
        cols = st.columns(2)
        for i, text in enumerate(examples):
            with cols[i % 2]:
                if st.button(f"💬 {text}", key=f"ex_{i}"):
                    st.session_state.messages.append(
                        {"role": "user", "content": text}
                    )
                    st.rerun()

    if prompt := st.chat_input("Ask a question about your video..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Analyzing video..."):
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
                st.error("Failed to generate response. Please try again.")
