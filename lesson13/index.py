import streamlit as st

st.subheader("BMI值計算")
st.divider()
st.latex('BMI值計算公式:BMI = 體重(公斤) / 身高^2(公尺^2)')
st.latex('例如：一個52公斤的人，身高是155公分，則BMI為:')
st.markdown('<h6 style="color:blue;text-align:center">\
            52(公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>',
            unsafe_allow_html=True)

st.markdown('<h6 style="color:orange;text-align:center">體重正常範圍為 BMI = 18.5～24</h6>',
            unsafe_allow_html=True)

st.markdown('<hr style="border:0;margin:0 auto;width:80%;border-top:2px dotted blue">',
            unsafe_allow_html=True)

st.markdown('<h6 style="color:purple;text-align:center">快看看自己的BMI是否在理想範圍吧!</h6>',
            unsafe_allow_html=True)


