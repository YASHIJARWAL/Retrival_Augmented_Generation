import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Rust RAG Assistant",
    layout="wide"
)

st.title("🦀 Rust Book RAG Assistant")

st.markdown(
    "Ask questions about Rust programming."
)

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


question = st.chat_input(
    "Ask a Rust question..."
)

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json={
                    "question": question
                }
            )

            data = response.json()

            answer = data["answer"]

            st.markdown(answer)

            if data["sources"]:
                st.markdown("---")
                st.subheader("Sources")

                for source in data["sources"]:
                    with st.expander(
                        f"Page {source['page']}"
                    ):
                        st.write(source["text"])

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })