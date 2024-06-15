import streamlit as st

st.title("計數器範例")
if 'count' not in st.session_state:
    st.session_state.count = 0

#利用call_back的寫法
def increment_counter():
    st.session_state.count += 1

st.button("Increment",key='Increment',on_click=increment_counter)

    

st.write("Count=", st.session_state.count)