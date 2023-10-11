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
    
    ### mainapp (http://127.0.0.1:8000/hw/)
    path('hwsj/', views.hwsj),
    ### mainapp (http://127.0.0.1:8000/hw/)
    path('signup2/', views.signup2),
    ### mainapp (http://127.0.0.1:8000/hw/)
    path('signup/', views.signup),
    ### mainapp (http://127.0.0.1:8000/hw/)
    path('login/', views.login),
    ### mainapp (http://127.0.0.1:8000/hw/)
    path('login2/', views.login2),
    ### mainapp (http://127.0.0.1:8000/imsi/)
    path('imsi/', views.imsi),
    ### mainapp (http://127.0.0.1:8000/)
    path('', views.index),

]
