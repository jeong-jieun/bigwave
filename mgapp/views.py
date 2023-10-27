from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Marina, Schedule, Booking, Boo_sch, Boo_mem
from datetime import datetime
# Create your views here.


# index.html 처리
def chat(request):
    return render(request,
                  'mgapp/chatbot.html',
                  {})
def logout(request):
    
    ### 로그아웃 처리는 session 딕셔너리의 key를 없애주면 됩니다
    # - 딕셔너리에서 모든 정보 삭제하는 함수 : flush()
    request.session.flush()
    msg = """
            <script type='text/javascript'>
                alert('로그아웃 되었습니다.');
                location.href = '/mg/home/';
            </script>
        """
    
    return HttpResponse(msg)
def booking(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = Boo_mem.objects.filter(boo_mem1=mem_id).first()


    # DB에서 선택한 스케줄 정보 조회

    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        qty = request.POST.get('qty', '')

    elif request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        qty = request.GET.get('qty', '')

    return render(request,
                  'mgapp/booking.html',
                  {'boo_mem' : boo_mem,})
    
def login(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = Boo_sch.objects.get(book_mem=mem_id)
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
                   'qty' : qty,
                    "mem_id": mem_id,
                    "boo_mem": boo_mem,})
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
def temptemp(request):
    return render(request,
                  'mgapp/temptemp.html',
                  {})
def index_t(request):
    return render(request,
                  'mgapp/index_test.html',
                  {})
def service(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = None
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
    if mem_id is not None:
        boo_mem = Boo_mem.objects.filter(boo_mem1=mem_id).first()        
    return render(request,
                  'mgapp/service.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                    "mem_id": mem_id,
                    "boo_mem": boo_mem,})
def index(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = None
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
    if mem_id is not None:
        boo_mem = Boo_mem.objects.filter(boo_mem1=mem_id).first()        
    return render(request,
                  'mgapp/index.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                    "mem_id": mem_id,
                    "boo_mem": boo_mem,})
def index2(request):
    return render(request,
                  'mgapp/index2.html',
                  {})
def test(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = None
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    
    if mem_id is not None:
        boo_mem = Boo_sch.objects.filter(book_mem=mem_id).first()    
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
                   'qty' : qty,
                   'boo_mem': boo_mem,})
def save2_reservation(request):
    try:
        mem_id = request.session.get('ses_mem_id', None)
        # 예약번호 생성
        now = datetime.now()
        book_no_format = now.strftime('%y%m%d%H%M')
        latest_booking = Booking.objects.filter(book_no__startswith=book_no_format).order_by('-book_no').first()
        if latest_booking:
            suffix = int(str(latest_booking.book_no)[-2:]) + 1
            book_no = f"{book_no_format}{suffix:02}"
        else:
            book_no = f"{book_no_format}01"

        # 로그인한 사용자의 ID 가져오기 (이 예제에서는 `request.user.id`를 사용하였으나 실제 구현에 따라 다를 수 있습니다.)
        # book_mem = 'abc001'
        book_qty = int(request.POST.get("book_qty"))  # 정수형으로 변환
        book_price = book_qty * 20000  # 예약금액 계산
        book_schedule = int(request.POST.get("selected_schedule")) # 예약 스케줄 번호

        # Booking 모델에 데이터 저장
        Booking.objects.create(
            book_no=book_no,
            book_mem=mem_id,
            book_qty=book_qty,
            book_price=book_price,
            book_schedule=book_schedule
        )
        msg = """
                <script type='text/javascript'>
                    alert('정상적으로 저장되었습니다.');
                    location.href='/mg/home/'
                </script>
            """
        return HttpResponse(msg)

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        return HttpResponse(error_msg)
    
def check(request):
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    selected_qty = request.GET.get('qty')
    selected_schedule_id = request.GET.get('selected_schedule')

    # DB에서 선택한 스케줄 정보 조회
    selected_schedule = Schedule.objects.get(sch_no=selected_schedule_id)
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
                  'mgapp/check.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                   'qty' : qty,
                   'selected_qty': selected_qty,
                   'selected_schedule_id': selected_schedule_id,
                   'selected_schedule': selected_schedule,})