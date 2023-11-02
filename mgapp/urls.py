"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
### include : 각 앱에서 관리하는 urls.py 호출 시 사용
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    ### about (http://127.0.0.1:8000/mg/chat/)
    path('chat/', views.chat),
    ### about (http://127.0.0.1:8000/mg/login/)
    path('booking/', views.booking),
    ### about (http://127.0.0.1:8000/mg/logout/)
    path('logout/', views.logout),
    ### about (http://127.0.0.1:8000/mg/login/)
    path('login/', views.login),
    ### about (http://127.0.0.1:8000/mg/temp2/)
    path('temp2/', views.temp2),
    ### about (http://127.0.0.1:8000/mg/temp1/)
    path('temp1/', views.temp1),
    ### about (http://127.0.0.1:8000/mg/new/)
    path('new/', views.new),
    ### about (http://127.0.0.1:8000/mg/nav_test/)
    path('nav_test/', views.nav_test),
    ### about (http://127.0.0.1:8000/mg/nav/)
    path('nav/', views.nav),
    ### copy2 (http://127.0.0.1:8000/mg/copy2/)
    path('copy2/', views.copy2),
    ### about (http://127.0.0.1:8000/mg/copy/)
    path('copy/', views.copy),
    ### about (http://127.0.0.1:8000/mg/about/)
    path('index3/', views.index3),
    ### about (http://127.0.0.1:8000/mg/about/)
    path('about/', views.about),
    ### mainapp (http://127.0.0.1:8000/mg/home/)
    path('index_test/', views.index_t),
    ### mainapp (http://127.0.0.1:8000/mg/home/)
    path('service/', views.service),
    ### mainapp (http://127.0.0.1:8000/mg/home/)
    path('home/', views.index),
    ### mainapp (http://127.0.0.1:8000/mg/home2/)
    path('home2/', views.index2),
    ### mainapp (http://127.0.0.1:8000/mg/test/)
    path('test/', views.test),
    ### mainapp (http://127.0.0.1:8000/mg/check/)
    path('check/', views.check),
    ### mainapp (http://127.0.0.1:8000/mg/check/)
    path('temp3/', views.temptemp),
    ### mainapp (http://127.0.0.1:8000/mg/save2/)
    path('save2/', views.save2_reservation, name='save2_reservation'),
    
    
    
    ## 아래 경로는 종민이 추가한거임
    path('chatbot_frame/', views.chatbot_frame),
]
    

