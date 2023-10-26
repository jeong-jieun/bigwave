### 행렬데이터 처리 라이브러리
import pandas as pd

### 지도 시각화에 사용하는 라이브러리
import folium
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


### 서비스 지도 시각화
class Service_Map_View:
    def __init__(self, ser_mar, ser_gu):
        self.sermap(ser_mar, ser_gu)

    def sermap(self, ser_mar, ser_gu):
        # 데이터 불러오기
        self.data = pd.read_excel('mainapp/mappy/항구 근처 가게.xlsx')

        # 데이터 필터링
        self.selected_data = self.data[(self.data['선착장'] == ser_mar) & (self.data['종류'] == ser_gu)]
        self.selected_data = self.selected_data.dropna(subset=['선착장위도', '선착장경도'])

        self.service_map = folium.Map(location=[self.selected_data['선착장위도'].mean(), self.selected_data['선착장경도'].mean()], zoom_start=16)

        # 회원 위치 마커 표시
        folium.Marker([self.selected_data['선착장위도'].mean(), self.selected_data['선착장경도'].mean()],
                      icon=folium.Icon(color='red', icon='home')
                      ).add_to(self.service_map)

        # 가게 마커 표시
        for j in range(len(self.selected_data)):
            service_name = self.selected_data.iloc[j, 0]
            service_gu = self.selected_data.iloc[j, 1]

            popup_html = "-"*69+"<br>"
            popup_html += f"<b>가게명:</b> {service_name}<br>"
            popup_html += f"<b>음식점 종류:</b> {service_gu}<br>"
            popup_html += "-"*69+"<br>"

            popup = folium.Popup(popup_html, max_width=250)
            folium.Marker([self.selected_data.iloc[j, 5], self.selected_data.iloc[j, 6],
                          ],
                          popup=popup, icon=folium.Icon(icon='plus')
                          ).add_to(self.service_map)
        
    # 지도맵 데이터를 HTML로 반환
    def getMap(self):
        return self.service_map._repr_html_()
        
        
        