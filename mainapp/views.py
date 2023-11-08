from django.shortcuts import render
from django.http import HttpResponse

from .models import Member, Booking, Schedule, Boo_sch, Marina, Boo_mem, Service

# 시각화 보여주는 라이브러리
from mainapp.mappy.map import Service_Map_View

import json
from django.http import JsonResponse

# Create your views here.

# mypage.html 처리
def mypage(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = Member.objects.get(mem_id=mem_id)

    return render(request, 'mainapp/signup.html', {
        "mem_id": mem_id,
        "boo_mem": boo_mem,
    })

def mygjlist(request):
    mem_id = request.session.get('ses_mem_id', None)
    boo_mem = Boo_sch.objects.get(book_mem=mem_id)

    return render(request, 'mainapp/mygjlist.html', {
        "mem_id": mem_id,
        "boo_mem": boo_mem,
    })
    
### signupafter 회원가입 후 페이지
def signupafter(request):
    try :
        mem_id = request.POST.get("mem_id", "")
        mem_pass = request.POST.get("mem_pass", "")
        mem_name = request.POST.get("mem_name", "")
        mem_mail = request.POST.get("mem_mail", "")
        mem_mail2 = request.POST.get("mem_mail2", "")
        mem_regno1 = request.POST.get("mem_regno1", "")
        mem_hp = request.POST.get("mem_hp", "")
        mem_add1 = request.POST.get("mem_add1", "")
        mem_add2 = request.POST.get("mem_add2", "")
        mem_add3 = request.POST.get("mem_add3", "")

        
        Member.objects.create(mem_id=mem_id,
                            mem_pass=mem_pass,
                            mem_name=mem_name,
                            mem_regno1=mem_regno1,
                            mem_mail=mem_mail +"@"+ mem_mail2,
                            mem_add1=mem_add1 + mem_add2,
                            mem_add2=mem_add3,
                            mem_hp=mem_hp
                            )
         
    except Exception as e:
        print("오류가 발생했습니다:", str(e))
        import traceback
        traceback.print_exc()
        msg = """
            <script type='text/javascript'>
                alert('오류가 발생했습니다. 정보를 확인하고 다시 시도하세요.');
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
    
    msg = """
            <script type='text/javascript'>
                alert('{}님 가입을 축하드립니다.');
                location.href = '/login2/';
            </script>
        """.format(mem_name)
        
    return HttpResponse(msg)

### idcheck 회원가입 아이디 중복 체크 페이지
def idcheck(request):
    mem_id = request.GET.get("mem_id", "")
    try :
        mem = Member.objects.get(mem_id = mem_id)
    except :
        mem = None
        
    if mem is None : 
        msg = """
                <script type="text/javascript">
                    alert('{}는 사용가능한 아이디입니다.');
                    history.go(-1);
                </script>
        """.format(mem_id)
        
    else :
        msg = """
                <script type="text/javascript">
                    alert('{}는 중복된 아이디입니다.');
                    history.go(-1);
                </script>
        """.format(mem_id)
    
    return HttpResponse(msg)

### loginafter 로그인 후 페이지
def loginafter(request):
    try:
        mem_id = request.POST.get("mem_id", "")
        mem_pass = request.POST.get("mem_pass", "")
        
        # Get the member based on mem_id
        try:
            mem = Member.objects.get(mem_id=mem_id)
        except Member.DoesNotExist:
            msg = """
                <script type="text/javascript">
                    alert('해당 아이디는 존재하지 않습니다. 다시 입력해주세요!');
                    history.go(-1);
                </script>
            """ 
            return HttpResponse(msg)
        
        # Check if the password matches
        if mem.mem_pass == mem_pass:
            msg = f"""
                <script type="text/javascript">
                    alert('{mem.mem_name}님 정상적으로 로그인 되었습니다.');
                    location.href='/';
                </script>
            """
            request.session["ses_mem_id"] = mem_id
            request.session["ses_mem_name"] = mem.mem_name
        else:
            msg = """
                <script type="text/javascript">
                    alert('아이디와 비밀번호가 일치하지 않습니다. 다시 입력해주세요!');
                    history.go(-1);
                </script>
            """
        return HttpResponse(msg)
    
    except Exception as e:
        print("An error occurred:", str(e))
        import traceback
        traceback.print_exc()
        msg = """
            <script type="text/javascript">
                alert('An error occurred. Please try again later.');
                history.go(-1);
            </script>
        """ 
        return HttpResponse(msg)
    
### logout 로그아웃 처리하기
def logout(request):
    
    ### 로그아웃 처리는 session 딕셔너리의 key를 없애주면 됩니다
    # - 딕셔너리에서 모든 정보 삭제하는 함수 : flush()
    request.session.flush()
    msg = """
            <script type='text/javascript'>
                alert('로그아웃 되었습니다.');
                location.href = '/';
            </script>
        """
    
    return HttpResponse(msg)

# hwsj.html 처리
def hwsj(request):
    service = Service.objects.all()
    print("================>>\n", service, "\n<<================")
    print("222222222222222222222222")
    test_df = ["test_df-data"]
    
    df_list = []
    df_list2 = []
    df_list3 = []
    df_list4 = []
    df_list5 = []
    
    for i in range(0, len(service)) :
        df_list.append({"ser_mar" : service[i].ser_mar})
        df_list2.append({"ser_gu" : service[i].ser_gu})
        df_list3.append({"ser_distance" : service[i].ser_distance})
        df_list4.append({"ser_lat" : service[i].ser_lat})
        df_list5.append({"ser_lon" : service[i].ser_lon})
    
    
    contexts = {"df_list":df_list,
                "df_list2":df_list2,
                "df_list3":df_list3,
                "df_list4":df_list4,
                "df_list5":df_list5,
                "test_df" : test_df}
    
    return JsonResponse(contexts)
    

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
def geo(request):
    latitude = request.GET.get("latitude")
    
    return render(request,
                  'mainapp/imsi.html',
                  {"latitude":latitude,})

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

# main.html 처리
def main(request):
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
                  'mainapp/main.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                    "mem_id": mem_id,
                    "boo_mem": boo_mem,})

# imsi.html 처리
def imsi(request):

    return render(request,
                  'mainapp/imsi.html',
                  {})

# index.html 처리
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
                  'mainapp/index.html',
                  {"mem_list" : mem_list,
                   'schedule': schedules,
                   'marina_list': marinas,
                   'selected_start': start,
                   'selected_end': end,
                    "mem_id": mem_id,
                    "boo_mem": boo_mem,})
    
# naver_login.html 처리
def naver_login(request):
  
    return render(request,
                  'mainapp/naver_login.html',
                  {})
    
### loginafter 로그인 후 페이지
def naver_login_after(request):
    if request.method == 'POST':
        mem_id = request.POST.get("id", "")
        mem_name = request.POST.get("name", "")
        
        # 이후 필요한 작업 수행
        request.session["ses_mem_id"] = mem_id
        request.session["ses_mem_name"] = mem_name
        
        msg = f"""
        <script type="text/javascript">
            alert('{mem_id} {mem_name}님 정상적으로 로그인 되었습니다.');
            location.href='/';
        </script>
        """
        return HttpResponse(msg)
    
    
    
    