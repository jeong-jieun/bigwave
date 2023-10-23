
from django.urls import path

from . import views
urlpatterns = [
    
    # main페이지
    path('test/', views.test),
    # main페이지
    path('main/', views.main),
    # 서비스 페이지 상세보기 처리
    path('service_detail/', views.service_detail, name='service_detail'),
    ### 서비스(교통) 조회 페이지 (http://127.0.0.1:8000/je/schedule/traffic)
    path('schedule/traffic/', views.traffic),
    ### 스케줄 조회 페이지 (http://127.0.0.1:8000/je/schedule)
    path('schedule/', views.schedule),
    ### 결제버튼 클릭시 db저장 (http://127.0.0.1:8000/je/save_reservation)
    path('save_reservation/', views.save_reservation, name='save_reservation'),
    ### 서비스페이지 (http://127.0.0.1:8000/je/service)
    path('service/', views.service, name='search_action'),
    ### 로그인페이지 (http://127.0.0.1:8000/je/login)
    path('login/', views.login),
    ### 결제확인페이지 (http://127.0.0.1:8000/je/checkout)
    path('checkout/', views.checkout),
    # index 페이지(http://127.0.0.1:8000/je)
    path('', views.index),
    
    
    # # main 페이지(http://127.0.0.1:8000/)
    # path('', views.main),
    path('service/jong/', views.jong),
]
