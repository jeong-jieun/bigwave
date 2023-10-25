from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Marina, Schedule, Booking, Service, Traffic
from datetime import datetime


# test.html
def test(request):
    service = Service.objects.all()
    selected_service_type = request.POST.get('service_type', '')
    services = Service.objects.filter(ser_gu=selected_service_type)
    return render(request,
                  'jeapp/html/test.html',
                  {'service' : service,
                   'services' : services})
# main.html
def main(request):
    return render(request,
                  'jeapp/html/main.html',
                  {})
# map.html
def map(request):
    marinas = Marina.objects.all()
    services = Service.objects.all()
    
    selected_mar = request.POST.get('search_option', None)
    selected_service_type = request.POST.get('service_type', '음식점')  # 기본값 설정

    # 필터링된 서비스 가져오기
    if selected_mar:
        if selected_service_type in ['음식점', '카페', '관광명소', '교통정보']:
            filtered_services = services.filter(ser_mar=selected_mar, ser_gu=selected_service_type)
        else:
            # 선택한 `ser_mar` 및 `ser_gu`가 없거나 올바르지 않은 경우, 모든 음식점 정보 반환
            filtered_services = services.filter(ser_mar=selected_mar, ser_gu='음식점')
    else:
        # 선택한 `ser_mar` 및 `ser_gu`가 없는 경우, 모든 음식점 정보 반환
        filtered_services = services.filter(ser_mar=selected_mar, ser_gu='음식점')

    return render(request, 'jeapp/html/map.html', {
        'marina_list': marinas,
        'service': services,
        'search_result': selected_mar,
        'services': filtered_services,
        'selected_service_type': selected_service_type,
    })


# 서비스 상세보기
def service_detail(request, marina, service_type, service_name):
    # 데이터베이스에서 해당 정보와 관련된 데이터를 가져옵니다.
    service = Service.objects.get(ser_mar=marina, ser_gu=service_type, ser_nm=service_name)
    # 데이터를 템플릿으로 전달합니다.
    return render(request, 'jeapp/html/service_detail.html', {'service': service})


# 부가서비스
def traffic(request):
    marinas = Marina.objects.all()
    selected_option = request.POST.get('search_option', None)
    return render(request, 
                  'jeapp/html/traffic.html',
                  {'marina_list': marinas,
                   'search_result': selected_option})


 # 서비스
def service(request):
    marinas = Marina.objects.all()
    service = Service.objects.all()
    selected_mar = request.POST.get('search_option', None) 
    selected_service_type = request.POST.get('service_type', '')  # Default is '음식점'

    filtered_services = Service.objects.filter(ser_mar=selected_mar, ser_gu=selected_service_type)
    
    return render(request,
                  'jeapp/html/service.html',
                  {'marina_list': marinas,
                   'service' : service,
                   'search_result': selected_mar,
                   'services': filtered_services,
                   'selected_service_type': selected_service_type})
    
 # 서비스_first
def fservice(request):
    marinas = Marina.objects.all()
    service = Service.objects.all()
    selected_mar = request.POST.get('search_option', None) 
    selected_service_type = request.POST.get('service_type', '')  # Default is '음식점'

    filtered_services = Service.objects.filter(ser_mar=selected_mar, ser_gu=selected_service_type)
    
    return render(request,
                  'jeapp/html/service.html',
                  {'marina_list': marinas,
                   'service' : service,
                   'search_result': selected_mar,
                   'services': filtered_services,
                   'selected_service_type': selected_service_type})


# 메인페이지에서 조회하기 버튼 클릭시 스케줄 조회 페이지 보여주기
def schedule(request):
    schedules = []
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
    return render(request, 'jeapp/html/schedule.html', {'qty' : qty,
                                                        'schedule': schedules})

# 결제하기 버튼 클릭시 DB에 저장시키기
def save_reservation(request):
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
        # book_mem = request.user.id
        book_mem = mem_id
        book_qty = int(request.POST.get("book_qty"))  # 정수형으로 변환
        book_price = book_qty * 20000  # 예약금액 계산
        book_schedule = int(request.POST.get("selected_schedule")) # 예약 스케줄 번호

        # Booking 모델에 데이터 저장
        Booking.objects.create(
            book_no=book_no,
            book_mem=book_mem,
            book_qty=book_qty,
            book_price=book_price,
            book_schedule=book_schedule
        )
        msg = """
                <script type='text/javascript'>
                    alert('정상적으로 저장되었습니다.');
                    location.href='/je/'
                </script>
            """
        return HttpResponse(msg)

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        return HttpResponse(error_msg)

    
# def setbookingInsert(request):
    # try:
    #     # book_no 생성
    #     now = datetime.now()
    #     book_no_format = now.strftime('%y%m%d%H%M')
    #     latest_booking = Booking.objects.filter(book_no__startswith=book_no_format).order_by('-book_no').first()
    #     if latest_booking:
    #         suffix = int(latest_booking.book_no[-2:]) + 1
    #         book_no = f"{book_no_format}{suffix:02}"
    #     else:
    #         book_no = f"{book_no_format}01"

    #     # 로그인한 사용자의 ID 가져오기
    #     # (이 예제에서는 `request.user`를 사용하였으나 실제 구현에 따라 다를 수 있습니다.)
    #     book_mem = request.user.id
        
    #     book_qty = request.POST.get("book_qty")
    #     book_price = request.POST.get("book_price")
    #     book_marina = request.POST.get("book_marina")
    #     book_arrival = request.POST.get("book_arrival")

    #     Booking.objects.create(
    #         book_no=book_no, book_mem=book_mem,
    #         book_qty=book_qty, book_price=book_price,
    #         book_marina=book_marina, book_arrival=book_arrival
    #         # book_taxi=book_taxi  # 택시 번호 추가 필요
    #     )
    # except:
    #     msg = """
    #         <script type='text/javascript'>
    #             alert('오류발생');
    #             history.go(-1)
    #         </script>
    #     """
    #     return HttpResponse(msg)
    # msg = """
    #     <script type='text/javascript'>
    #         alert('정상적으로 저장되었습니다.');
    #         location.href='/je/'
    #     </script>
    # """
    # return HttpResponse(msg)


def login(request):
    return render(request, 
                  'jeapp/html/login.html',
                  {})


# checkout.html 처리
def checkout(request):
    selected_qty = request.GET.get('qty')
    selected_schedule_id = request.GET.get('selected_schedule')

    # DB에서 선택한 스케줄 정보 조회
    selected_schedule = Schedule.objects.get(sch_no=selected_schedule_id)

    return render(request, 
                  'jeapp/html/checkout.html',
                  {'selected_qty': selected_qty,
                   'selected_schedule_id': selected_schedule_id,
                   'selected_schedule': selected_schedule,
                  })
    
# index.html 처리
def index(request):
    schedules = []
    mem_list = Member.objects.all()
    marinas = Marina.objects.all()
    start, end = None, None
    
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        
    return render(request,
                  'jeapp/index.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end})
    
def jong(request):
    return render(request, 
                  'jeapp/html/jong.html',
                  {})   
    
    
# # main.html 처리(첫화면)
# def main(request):
#     return render(request,
#                   'jeapp/main.html',
#                   {})