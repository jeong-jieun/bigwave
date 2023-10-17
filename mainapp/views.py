from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

# Create your views here.

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
        mem_id =request.POST.get("mem_id", "")
        mem_pass =request.POST.get("mem_pass", "")
        
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
    