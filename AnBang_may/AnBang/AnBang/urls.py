"""AnBang URL Configuration

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

from mainApp import views
from accountApp.views import logout


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.show_map, name='home'),
    path('search_building', views.search_building, name='search_building'),
    path('building_detail/<int:building_id>', views.building_detail, name='building_detail'),

    path('review_list/<int:building_id>', views.review_list, name='review_list'),
    path('review_detail/<int:review_id>', views.review_detail, name='review_detail'),
    path('review_create/<int:building_id>', views.review_create, name='review_create'),

    
    path('search', views.Search.as_view(), name='search'),
    path('result', views.Result.as_view(), name='result'),

    path('logout', logout, name='logout'),
    path('', include('allauth.urls')),
]
