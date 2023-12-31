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
    # - http://127.0.0.1:8000/mem_delete/
    path('mem_delete/', views.mem_delete),
    # - http://127.0.0.1:8000/mem_update/
    path('mem_update/', views.mem_update),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('geo/', views.geo),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('naver_login_after/', views.naver_login_after),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('naver_login/', views.naver_login),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('main/', views.main),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('logout/', views.logout),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('signupafter/', views.signupafter),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('idcheck/', views.idcheck),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('loginafter/', views.loginafter),
    ### mainapp (http://127.0.0.1:8000/mygjlist/)
    path('mygjlist/', views.mygjlist),
    ### mainapp (http://127.0.0.1:8000/mypage/)
    path('signup/', views.mypage),
    ### mainapp (http://127.0.0.1:8000/hwsj/)
    path('hwsj/', views.hwsj),
    ### mainapp (http://127.0.0.1:8000/signup2/)
    path('signup2/', views.signup2),
    ### mainapp (http://127.0.0.1:8000/signup/)
    path('signup/', views.signup),
    ### mainapp (http://127.0.0.1:8000/login/)
    path('login/', views.login),
    ### mainapp (http://127.0.0.1:8000/login2/)
    path('login2/', views.login2),
    ### mainapp (http://127.0.0.1:8000/imsi/)
    path('imsi/', views.imsi, name='search_action'),
    ### mainapp (http://127.0.0.1:8000/)
    path('2/', views.index2),
    ### mainapp (http://127.0.0.1:8000/)
    path('', views.index),

]
