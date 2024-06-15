import streamlit as st

if 'robert' not in st.session_state:
    st.session_state['robert'] = 30

st.session_state['robert']
st.session_state.robert = 50
st.session_state.robert
