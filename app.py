import streamlit as st

# App title
st.title("My First Streamlit App")

# Simple text
st.write("Hello, Streamlit! 👋")

# A slider
age = st.slider("How old are you?", 0, 100, 25)
st.write("You selected:", age)

# A text input
name = st.text_input("What's your name?", "Ivan")
st.write("Nice to meet you,", name)

hobby = st.selectbox(
    "What is your favorite hobby?",
    ["Reading", "Coding", "Gaming", "Travel", "Sports"]
)
st.write("Your hobby is:", hobby)
