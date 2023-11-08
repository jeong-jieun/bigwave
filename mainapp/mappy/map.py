### 행렬데이터 처리 라이브러리
import pandas as pd

### 지도 시각화에 사용하는 라이브러리
import folium
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from folium import CustomIcon


### 서비스 지도 시각화
class Service_Map_View:
    def __init__(self, ser_mar, ser_gu, lat, lon):
        self.sermap(ser_mar, ser_gu, lat, lon)

    def sermap(self, ser_mar, ser_gu, lat, lon):
        # 데이터 불러오기
        self.data = pd.read_excel('mainapp/mappy/항구 근처 가게.xlsx')

        # 데이터 필터링
        self.selected_data = self.data[(self.data['선착장'] == ser_mar) & (self.data['종류'] == ser_gu)]
        self.selected_data = self.selected_data.dropna(subset=['선착장위도', '선착장경도'])

        self.service_map = folium.Map(location=[self.selected_data['선착장위도'].mean(), self.selected_data['선착장경도'].mean()], zoom_start=17)

        arr_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/arr.png', icon_size=(60, 60))
        
               
        # 선착장 위치 마커 표시
        folium.Marker([self.selected_data['선착장위도'].mean(), self.selected_data['선착장경도'].mean()],
                      icon=arr_icon 
                      ).add_to(self.service_map)
        
        user_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/user.png', icon_size=(60, 60))
               
         #회원 위치 마커 표시
        folium.Marker([lat, lon],
                      icon=user_icon 
                      ).add_to(self.service_map)

        # 가게 마커 표시
        for j in range(len(self.selected_data)):
            
            service_name = self.selected_data.iloc[j, 3]
            service_gu = self.selected_data.iloc[j, 1]
            service_distance = self.selected_data.iloc[j, 4]

            popup_html = "-"*40+"<br>"
            popup_html += f"<b>이름:</b> {service_name}<br>"
            popup_html += f"<b>선착장에서 거리:</b> {service_distance}<br>"
            popup_html += "-"*40+"<br>"
            
            

            popup = folium.Popup(popup_html, max_width=150)
            # 가게 종류에 따라 아이콘 선택
            if service_gu == '음식점':
                selected_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/ham.png', icon_size=(40, 40))
            elif service_gu == '카페':
                selected_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/cafe.png', icon_size=(40, 40))
            elif service_gu == '관광명소':
                selected_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/gk.png', icon_size=(40, 40))
            folium.Marker([self.selected_data.iloc[j, 5], self.selected_data.iloc[j, 6],
                          ],
                          popup=popup, icon=selected_icon 
                          ).add_to(self.service_map)
        
    # 지도맵 데이터를 HTML로 반환
    def getMap(self):
        return self.service_map._repr_html_()
        
        
        