
from django.urls import path

from . import views
urlpatterns = [
   
    ### 카페 부가서비스페이지 (http://127.0.0.1:8000/je/service/cafe)
    path('service/다대선착장/', views.dadae),
    ### 카페 부가서비스페이지 (http://127.0.0.1:8000/je/service/cafe)
    path('service/cafe/', views.cafe),
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
