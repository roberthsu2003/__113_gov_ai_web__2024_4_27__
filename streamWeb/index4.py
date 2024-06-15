import streamlit as st
import time

placehoder = st.empty()

with placehoder:
    for seconds in range(5):
        st.write(f"{seconds} seconds have passed")
        time.sleep(1)
    
    st.write("😜 1 minute over!")

time.sleep(5)
placehoder.empty()
