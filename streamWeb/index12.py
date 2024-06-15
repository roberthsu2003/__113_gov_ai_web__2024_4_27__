import streamlit as st

st.title("計數器範例")
count = 0

increment = st.button("Increment")
if increment:
    count += 1

st.write("Count=", count)