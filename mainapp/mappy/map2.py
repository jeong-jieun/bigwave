### 행렬데이터 처리 라이브러리
import pandas as pd

### 지도 시각화에 사용하는 라이브러리
import folium
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from folium import CustomIcon


### 서비스 지도 시각화
class Marina_Map_View:
    def __init__(self):
        self.sermap()

    def sermap(self):
        # 데이터 불러오기
        self.data = pd.read_excel('mainapp/mappy/선착장 위경도.xlsx')

        # 데이터 필터링

        self.marina_map = folium.Map(location=[self.data['선착장위도'].mean(), self.data['선착장경도'].mean()], zoom_start=13)
        
        #bus_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/bus.png', icon_size=(60, 60))
               
        # 회원 위치 마커 표시
        #folium.Marker([self.lat, self.lon],
                      #icon=bus_icon 
                      #).add_to(self.service_map)

        # 가게 마커 표시
        for j in range(len(self.data)):
            marina_name = self.data.iloc[j, 0]

            popup_html = "-"*50+"<br>"
            popup_html += f"<b>이름:</b> {marina_name}<br>"
            popup_html += "-"*50+"<br>"
            
            

            popup = folium.Popup(popup_html, max_width=250)
            # 가게 종류에 따라 아이콘 선택
            arr_icon = CustomIcon(icon_image='mainapp/static/mainapp/img/arr.png', icon_size=(50, 50))
                
            # 선착장 위치 마커 표시
            folium.Marker([self.data.iloc[j, 1], self.data.iloc[j, 2],
                          ],
                          popup=popup, icon=arr_icon 
                          ).add_to(self.marina_map)
        
    # 지도맵 데이터를 HTML로 반환
    def getMap(self):
        return self.marina_map._repr_html_()
        
        
        