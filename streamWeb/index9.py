import streamlit as st

# Object notation
selected_value = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# with notation
with st.sidebar:
    radio_value = st.radio(
        "Choose a shipping method",
        ("Standard(5-15 days)","Express(2-3 days)")
        )
    
st.write(selected_value, radio_value)
