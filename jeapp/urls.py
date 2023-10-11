
from django.urls import path

from . import views
urlpatterns = [

    ### 부가서비스페이지 (http://127.0.0.1:8000/je/booking)
    path('booking/', views.setbookingInsert),
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
