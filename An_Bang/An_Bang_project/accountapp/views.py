from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from An_Bang_app.models import Profile
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
            auth.login(request,user)
            return redirect('index')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
