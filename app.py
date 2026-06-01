import streamlit as st
import requests

st.title("AI Chatbot")

API_KEY = "sk-fewacxidgahuhnoiquukcpnzkphivveghopldyniqbxjnvtk"

with st.sidebar:
    st.subheader("设置")
    if st.button("清空对话"):
        st.session_state.messages = []
        st.rerun()
    st.caption("Powered by DeepSeek V3")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("输入你的问题..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = requests.post(
            "https://api.siliconflow.cn/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "deepseek-ai/DeepSeek-V3",
                "messages": st.session_state.messages
            }
        ).json()["choices"][0]["message"]["content"]
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
