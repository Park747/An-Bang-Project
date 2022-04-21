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
from An_Bang_app import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 페이지
    path('', include('accountapp.urls')),
    path('google/', include('allauth.urls')),
    # path('building_create', views.building_create, name="building_create"), # 건물 추가 페이지
    # path('building_list', views.building_list, name='building_list'), #건물 목록 페이지
    # path('review_list/<str:building_address>', views.review_list, name='review_list'), #빌딩 디테일페이지에서 해당 빌딩의 리뷰 목록으로 이동 
    # path('building_detail/<str:building_address>', views.building_detail, name='building_detail'), #해당 빌딩의 디테일 페이지
    # path('review_detail/<int:review_id>', views.review_detail, name='review_detail'), #리뷰 작성, 리뷰 클릭시 리뷰디테일로 이동
    # path('review_create/<int:building_address>/<str:username>', views.review_create, name='review_create'), #건물 detail에서 리뷰 작성 버튼 클릭시 
# path('keyword_input', views.keyword_input, name='keyword_input'),
    ]
