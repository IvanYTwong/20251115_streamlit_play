import streamlit as st
import openai

st.title("💬 MyChatGPT")

msg = st.chat_input("Ask me anything")

if msg:
    with st.chat_message("user"):
        st.write(msg)

    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":msg}]
    )

    answer = resp.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)
