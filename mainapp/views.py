from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# mygjlist.html 처리
def mygjlist(request):
    return render(request,
                  'mainapp/mygjlist.html',
                  {})

# mypage.html 처리
def mypage(request):
    return render(request,
                  'mainapp/mypage.html',
                  {})

# hwsj.html 처리
def hwsj(request):
    return render(request,
                  'mainapp/hwsj.html',
                  {})

# signup.html 처리
def signup2(request):
    return render(request,
                  'mainapp/signup2.html',
                  {})

# signup.html 처리
def signup(request):
    return render(request,
                  'mainapp/signup.html',
                  {})

# login.html 처리
def login(request):
    return render(request,
                  'mainapp/login.html',
                  {})
    
# login.html 처리
def login2(request):
    return render(request,
                  'mainapp/login2.html',
                  {})

# imsi.html 처리
def imsi(request):
    return render(request,
                  'mainapp/imsi.html',
                  {})

# index.html 처리
def index(request):
    return render(request,
                  'mainapp/index.html',
                  {})
    