from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from An_Bang_app.models import Profile
#SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"]
            )
            name = request.POST["name"]
            gender = request.POST["gender"]
            birth_year = request.POST["birth_year"]
            birth_month = request.POST["birth_month"]
            birth_date = request.POST["birth_date"]
            phone = request.POST["phone"]
            email = request.POST["email"]
            profile = Profile(username=user, name=name, gender=gender, 
            birth_year=birth_year, birth_month=birth_month, birth_date=birth_date,
            phone=phone, email=email)
            profile.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('activation_email.html',{
                'user' : user,
                'domain' : current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user),
            })
            mail_title = "안암동 방리뷰 : An-Bang 계정 활성화 확인 이메일입니다."
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            # auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend' )
            return redirect('index')
        else:
            return render(request, 'login.html' , {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    else:
        return render(request, 'index.html', {'error' : '계정 활성화 오류'})
    return

