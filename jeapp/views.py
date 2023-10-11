from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Marina, Schedule, Booking

# 결제하기 버튼 클릭시 DB에 저장시키기
def setbookingInsert(request):
    try:
        # book_no 생성
        now = datetime.now()
        book_no_format = now.strftime('%y%m%d%H%M')
        latest_booking = Booking.objects.filter(book_no__startswith=book_no_format).order_by('-book_no').first()
        if latest_booking:
            suffix = int(latest_booking.book_no[-2:]) + 1
            book_no = f"{book_no_format}{suffix:02}"
        else:
            book_no = f"{book_no_format}01"

        # 로그인한 사용자의 ID 가져오기
        # (이 예제에서는 `request.user`를 사용하였으나 실제 구현에 따라 다를 수 있습니다.)
        book_mem = request.user.id
        
        book_qty = request.POST.get("book_qty")
        book_price = request.POST.get("book_price")
        book_marina = request.POST.get("book_marina")
        book_arrival = request.POST.get("book_arrival")

        # 택시 번호는 index.html에서 받아오므로 다른 방법을 사용해야 합니다.
        # 예: session 또는 cookie 사용

        Booking.objects.create(
            book_no=book_no, book_mem=book_mem,
            book_qty=book_qty, book_price=book_price,
            book_marina=book_marina, book_arrival=book_arrival
            # book_taxi=book_taxi  # 택시 번호 추가 필요
        )
    except:
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1)
            </script>
        """
        return HttpResponse(msg)
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 저장되었습니다.');
            location.href='/je/'
        </script>
    """
    return HttpResponse(msg)
# def setbookingInsert(request):
#     try :
#         book_no = request.POST.get("book_no")
#         book_mem = request.POST.get("book_mem")
#         book_qty = request.POST.get("book_qty")
#         book_price = request.POST.get("book_price")
#         book_marina = request.POST.get("book_marina")
#         book_arrival = request.POST.get("book_arrival")
#         book_taxi = request.POST.get("book_taxi")
#         Booking.objects.create(book_no = book_no, book_mem = book_mem,
#                             book_qty = book_qty, book_price=book_price,
#                             book_marina=book_marina, book_arrival=book_arrival,
#                             book_taxi=book_taxi)
#     except :
#         msg = """
#             <script type='text/javascript'>
#                 alert('오류발생');
#                 history.go(-1)
#             </script>
#         """
#         return HttpResponse(msg)
#     msg = """
#         <script type='text/javascript'>
#             alert('정상적으로 저장되었습니다.');
#             location.href='/je/'
#         </script>
#     """
#     return HttpResponse(msg)



def service(request):
    marinas = Marina.objects.all()
    selected_option = request.POST.get('search_option', None)
    return render(request,
                  'jeapp/html/service.html',
                  {'marina_list': marinas,
                   'search_result': selected_option})

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
        
    # 선택한 출발지와 도착지에 해당하는 스케줄 검색
    schedules = Schedule.objects.filter(sch_marina=start, sch_arrival=end)
    return render(request,
                  'jeapp/index.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end})
    
# # main.html 처리(첫화면)
# def main(request):
#     return render(request,
#                   'jeapp/main.html',
#                   {})