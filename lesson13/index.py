import streamlit as st

st.subheader("BMI值計算--修改1")
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

if 'bmi_result' not in st.session_state:
    st.session_state.bmi_result = 0

#if 'height' not in st.session_state:
    #st.session_state.height = 100
#if 'weight' not in st.session_state:
    #st.session_state.weight = 30


with st.form('bmi form',border=False):
    height = st.slider(":green[選擇身高(cm)]",max_value=250,min_value=100,key="height")
    weight = st.number_input(":green[選擇體重(kg)]",max_value=200,min_value=30,key="weight")   
    txt=''
    if st.form_submit_button("BMI計算"):
        st.session_state.bmi_result = round( weight / ((height/100) ** 2),1 )            
        if st.session_state.bmi_result < 18.5:
            txt = "體重過輕"
        elif st.session_state.bmi_result < 24:
            txt = "正常範圍"
        elif st.session_state.bmi_result < 27:
            txt = "過重"
        elif st.session_state.bmi_result < 30:
            txt = "輕度肥胖"
        elif st.session_state.bmi_result < 35:
            txt = "中度肥胖"
        else:
            txt = "重度肥胖"

    
        
st.markdown(f'## :orange[{st.session_state.bmi_result}]')
st.markdown(f'#### :black[{txt}]')
   




