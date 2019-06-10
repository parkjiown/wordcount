from django.shortcuts import render
from .models import Login

# Create your views here.
def login(request):
    return render(request, "login/test.html")

def check(request):
    user_id = request.GET.get('Your ID')
    user_pwd = request.GET.get('PassWord')
    user_infos = Login.objects.all()

    for user_info in user_infos :
        if (user_info.id == user_id and user_info.pwd == user_pwd) :
            text = "로그인 성공"
            break
        else :
            text = "로그인 실패"
        
    context = {'text' : text}

    return render(request, "login/check.html", context)
    