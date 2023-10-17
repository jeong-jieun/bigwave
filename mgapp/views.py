from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Marina, Schedule, Booking
from datetime import datetime
# Create your views here.


# index.html 처리
def booking(request):
    return render(request,
                  'mgapp/booking.html',
                  {})
def login(request):
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        qty = request.POST.get('qty', '')
        schedules = Schedule.objects.filter(sch_marina=start, sch_arrival=end)
    elif request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        qty = request.GET.get('qty', '')
        schedules = Schedule.objects.filter(sch_marina=start, sch_arrival=end)
    return render(request,
                  'mgapp/index_login.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                   'qty' : qty})
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
def index_t(request):
    return render(request,
                  'mgapp/index_test.html',
                  {})
def index(request):
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        
    return render(request,
                  'mgapp/index.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end})
def index2(request):
    return render(request,
                  'mgapp/index2.html',
                  {})
def test(request):
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        qty = request.POST.get('qty', '')
        schedules = Schedule.objects.filter(sch_marina=start, sch_arrival=end)
    elif request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        qty = request.GET.get('qty', '')
        schedules = Schedule.objects.filter(sch_marina=start, sch_arrival=end)
    return render(request,
                  'mgapp/index_test.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                   'qty' : qty})