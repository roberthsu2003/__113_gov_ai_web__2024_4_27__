import streamlit as st

st.title("這是一個測試")
st.header("Header")
st.subheader("subHeader")
st.caption("caption")
st.divider()
st.markdown("## Hello! **_World_**")
st.markdown("### 步驟1")
st.markdown("### 步驟2")
st.code('''
import requests
from requests import Response

aqi_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
res:Response = requests.get(aqi_url)

if res.status_code == 200:
    print("下載成功")
else:
    print("下載失敗")
        ''')