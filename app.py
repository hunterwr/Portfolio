import streamlit as st

# Title and Description
st.title("My Streamlit App")
st.write("Welcome to my app!")

# Input and Output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")