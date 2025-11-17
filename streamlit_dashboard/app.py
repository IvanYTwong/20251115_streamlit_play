import streamlit as st

# Sidebar inputs
st.sidebar.title("Settings")

# 选择数字范围
number = st.sidebar.slider("Pick a number", 1, 100, 50)

# 显示到主画面
st.title("Streamlit Dashboard Demo")
st.write(f"You picked: {number}")
