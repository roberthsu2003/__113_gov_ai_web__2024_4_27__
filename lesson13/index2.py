import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source
from source import Root


try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

    st.title("台北市youbike各行政區站點資料")
    tableContainer = st.container(height=500,border=False)
    
    def area_change():
        sarea_name = st.session_state.sarea
        #st.write(sarea_name)        
        display_data = []
        for item in data:
            if item['行政區'] == sarea_name:
                display_data.append(item)
        with tableContainer:
            st.subheader(sarea_name)
            st.dataframe(data=display_data)



    with st.sidebar:
        st.selectbox(":orange[請選擇行政區域:]",options=areas,on_change=area_change,key='sarea')
    
    
    

    





