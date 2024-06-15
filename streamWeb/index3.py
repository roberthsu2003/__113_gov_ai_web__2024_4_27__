import streamlit as st
import numpy as np

with st.container(border=True):
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50,3))

st.write("This is outside the container")