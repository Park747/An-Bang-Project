"""An_Bang_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accountapp import views


urlpatterns = [
#관리자 페이지
    path('', views.index, name='index' ), #홈페이지
    path('signup/', views.signup, name='signup'), #회원가입 페이지
    path('login/', views.login, name='login'), #로그인 페이지
    path('logout/', views.logout, name='logout'), #로그아웃
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate")
]