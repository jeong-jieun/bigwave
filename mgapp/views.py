from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# index.html 처리
def temp2(request):
    return render(request,
                  'prc/temp2.html',
                  {})
def temp1(request):
    return render(request,
                  'prc/temp.html',
                  {})
def new(request):
    return render(request,
                  'prc/new.html',
                  {})
def nav_test(request):
    return render(request,
                  'prc/nav_index.html',
                  {})
def nav(request):
    return render(request,
                  'prc/nav_index2.html',
                  {})
def copy2(request):
    return render(request,
                  'prc/copy_2.html',
                  {})
def copy(request):
    return render(request,
                  'prc/copy.html',
                  {})
def index3(request):
    return render(request,
                  'prc/index.html',
                  {})
def about(request):
    return render(request,
                  'mgapp/about.html',
                  {})
def index(request):
    return render(request,
                  'mgapp/index.html',
                  {})
def index2(request):
    return render(request,
                  'mgapp/index2.html',
                  {})