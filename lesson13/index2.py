import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source
from source import Root
import pandas as pd


try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

    
    tableContainer = st.container(border=False)
    
    def area_change():
        sarea_name = st.session_state.sarea
        #st.write(sarea_name)        
        display_data = []
        for item in data:
            if item['行政區'] == sarea_name:
                display_data.append(item)
        #st.title("新北市youbike各行政區站點資料")
        st.subheader(sarea_name)
        col1, col2 = st.columns([3, 2])
        with col1:
            df1 = pd.DataFrame(display_data,
                            columns=['站點名稱','日期時間','總數','可借','可還'])
            st.dataframe(data=df1)

        with tableContainer:
            
                        
            
            df0 = pd.DataFrame(display_data,
                               columns=['站點名稱','總數'])
            
            st.scatter_chart(df0,
                             x='站點名稱',
                             y='總數',
                             color='#00ff00',
                             size='總數')
            

            df2 = pd.DataFrame(display_data,
                               columns=['站點名稱','總數','可借'])
            
            st.scatter_chart(df2,
                             x='站點名稱',
                             y='可借',
                             size='可借')
            
            df3 = pd.DataFrame(display_data,
                               columns=['站點名稱','總數','可還'])
            
            st.scatter_chart(df3,
                             x='站點名稱',
                             y='可還',
                             color='#ff0000',
                             size='可還')



    with st.sidebar:
        st.selectbox(":orange[請選擇行政區域:]",options=areas,on_change=area_change,key='sarea')
    
    
    

    





