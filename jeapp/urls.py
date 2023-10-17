
from django.urls import path

from . import views
urlpatterns = [
   
    ### 부가서비스페이지 (http://127.0.0.1:8000/je/service/cafe)
    path('service/cafe/', views.cafe),
    ### 부가서비스페이지 (http://127.0.0.1:8000/je/service/food)
    path('service/food/', views.food),
    ### 부가서비스페이지 (http://127.0.0.1:8000/je/service/tour)
    path('service/tour/', views.tour),
    ### 부가서비스페이지 (http://127.0.0.1:8000/je/service/traffic)
    path('service/traffic/', views.traffic),
    ### 스케줄 조회 페이지 (http://127.0.0.1:8000/je/schedule)
    path('schedule/', views.schedule),
    ### 결제버튼 클릭시 db저장 (http://127.0.0.1:8000/je/save_reservation)
    path('save_reservation/', views.save_reservation, name='save_reservation'),
    ### 부가서비스페이지 (http://127.0.0.1:8000/je/service)
    path('service/', views.service, name='search_action'),
    ### 로그인페이지 (http://127.0.0.1:8000/je/login)
    path('login/', views.login),
    ### 결제확인페이지 (http://127.0.0.1:8000/je/checkout)
    path('checkout/', views.checkout),
    # index 페이지(http://127.0.0.1:8000/je)
    path('', views.index),
    # # main 페이지(http://127.0.0.1:8000/)
    # path('', views.main),
]
