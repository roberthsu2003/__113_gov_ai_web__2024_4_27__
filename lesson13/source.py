import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st

class Site(BaseModel):
    站點名稱:str = Field(alias="sna")
    行政區:str = Field(alias="sarea")
    日期時間:str = Field(alias='mday')
    地址:str = Field(alias='ar')
    總數:int = Field(alias='tot')
    可借:int = Field(alias='sbi')
    可還:int = Field(alias='bemp')
    狀態:bool = Field(alias='act')
    緯度:float = Field(alias='lat')
    經度:float = Field(alias='lng')

    @field_validator('站點名稱',mode='before')
    @classmethod
    def abc(cls,value):
        return value.split('_')[-1]
    
    @field_validator('日期時間',mode='before')
    @classmethod
    def abcd(cls,value):
        return f'{value[:4]}-{value[4:6]}-{value[6:8]} {value[8:10]}:{value[10:12]}:{value[12:]}'
    
    @field_serializer('狀態')
    def abce(self,value):
        if value:
            return "營業中"
        else:
            return "維護中"
        
class Root(RootModel):
    root:list[Site]


@st.cache_data
def download_youbike()->str:
    youbike_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=2000'
    try:
        response = requests.get(youbike_url)
    except Exception as e:
        print(e)
    else:
        return response.text