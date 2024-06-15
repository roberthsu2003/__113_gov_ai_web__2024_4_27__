import streamlit as st


# with notation
with st.sidebar:
    with st.form("abc"):
        selected_value = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
            )
        radio_value = st.radio(
            "Choose a shipping method",
            ("Standard(5-15 days)","Express(2-3 days)")
            )
        
        st.form_submit_button("確定")
    
st.write(selected_value, radio_value)
