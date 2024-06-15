import streamlit as st


st.write("Inside the form")
slider_val = st.slider("Form slider")
checkbox_val = st.checkbox("Form checkbox")

    
st.write("slider", slider_val, "checkbox", checkbox_val)

