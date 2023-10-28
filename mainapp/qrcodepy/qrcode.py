import folium
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import mysql.connector
import qrcode
from io import BytesIO

class Qrcode:
    def __init__(self, mem_id, sch_marina, book_qty, book_price, sch_arrival, sch_stime, sch_etime):
        self.mem_id = mem_id
        self.sch_marina = sch_marina
        self.book_qty = book_qty
        self.book_price = book_price
        self.sch_arrival = sch_arrival
        self.sch_stime = sch_stime
        self.sch_etime = sch_etime

    def generate_qr_code(self):
        # QR 코드 데이터 생성
        qr_data = f"예약 ID: {self.mem_id}\n" \
                  f"출발지: {self.sch_marina}\n" \
                  f"예약 인원: {self.book_qty}\n" \
                  f"결제 금액: {self.book_price}\n" \
                  f"도착지: {self.sch_arrival}\n" \
                  f"출발 시간: {self.sch_stime}\n" \
                  f"하차 시간: {self.sch_etime}"

        # QR 코드 이미지 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # QR 코드 이미지를 BytesIO 객체에 저장
        qr_bytes_io = BytesIO()
        img.save(qr_bytes_io, format="PNG")
        qr_bytes_io.seek(0)

        return qr_bytes_io

    def get_html(self):
        qr_bytes_io = self.generate_qr_code()
        qr_data = qr_bytes_io.read()
        qr_base64 = base64.b64encode(qr_data).decode("utf-8")
        return f'<img src="data:image/png;base64,{qr_base64}"/>'
        