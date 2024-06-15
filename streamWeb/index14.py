import streamlit as st

st.title("計數器範例")
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button("Increment")
if increment:
    st.session_state.count += 1

st.write("Count=", st.session_state.count)