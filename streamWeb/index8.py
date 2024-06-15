import streamlit as st

with st.popover("open popover"):
    st.markdown("Hello World ⛹️‍♂️")
    name = st.text_input("What's your name?")

st.write("your name:",name)