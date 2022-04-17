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
from django.urls import path
from accountapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index' ),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('home', views.home, name='home'),
    # path('keyword_input', views.keyword_input, name='keyword_input'),
    # path('building_list', views.building_list, name='building_list'),
    # path('review_list', views.review_list, name='review_list'),
    # path('building_detail<int:building_id>', views.building_detail, name='building_detail'),
    # path('review_detail/<int:review_id>', views.review_detail, name='review_detail'),
    # path('review_create', views.review_create, name='review_create'),
]
