from django.shortcuts import render, redirect
from .models import *
import json

from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.views.generic import TemplateView, ListView

# Create your views here.
def show_map(request):
    buildings = Building.objects.all()
    buildings_js = json.dumps([building.to_json() for building in buildings])
    return render(request, 'home.html', {'buildings' : buildings_js})



def search_building(request):
    # 검색어 필터링 이후에 구현
    buildings = Building.objects.all()

    return render(request, 'search_building.html', {'buildings': buildings})

def building_detail(request, building_id):
    building = Building.objects.get(pk=building_id)
    reviews = Review.objects.filter(building_id=building_id) #filter는 쿼리셋 반환
    
    sum_rate = 0
    sum_host = 0
    sum_soundproof = 0
    sum_water_pressure = 0
    sum_new = 0

    if len(reviews) > 0:
      reviews_length=len(reviews)

      for review in reviews:
        sum_rate += review.rate
        sum_host += review.host
        sum_soundproof += review.soundproof
        sum_water_pressure += review.water_pressure
        sum_new += review.new
        
      average_rate = sum_rate/reviews_length
      average_host = sum_host/reviews_length
      average_soundproof = sum_soundproof /reviews_length
      average_water_pressure = sum_water_pressure/reviews_length
      average_new = sum_new /reviews_length
      
    else: 
      reviews_length = 0

      average_rate = 0
      average_host = 0
      average_soundproof = 0
      average_water_pressure = 0
      average_new = 0
    
    recent_reviews=reviews.order_by('-uploaded')[:3]


    return render(request, 'building_detail.html', {
      'building' : building, 
      'reviews' : reviews,
      'reviews_length': reviews_length,

      'average_rate': average_rate,
      'average_host': average_host,
      'average_soundproof': average_soundproof,
      'average_water_pressure': average_water_pressure,
      'average_new': average_new,

      'recent_reviews': recent_reviews,
      })

def review_list(request, building_id):
    building = Building.objects.get(pk=building_id)
    reviews = Review.objects.filter(building_id=building_id)

    return render(request, 'review_list.html', {'building': building, 'reviews': reviews})

def review_detail(request,  review_id):
    review = Review.objects.get(pk=review_id)

    return render(request, 'review_detail.html', {'review': review})


@login_required
def review_create(request, building_id):
    if not request.user.is_authenticated:
        return redirect('login')

    building = Building.objects.get(pk=building_id)
    conn_user = User.objects.get(email=request.user)
    
    # if building.count() > 0:
    if request.method == "POST":
      
      new_review = Review.objects.create(
        user_email = conn_user,
        building_id = building,
        host = request.POST['host'],
        soundproof = request.POST['soundproof'],
        water_pressure = request.POST['water_pressure'],
        new = request.POST['new'],
        memo = request.POST['memo'],
        rate = request.POST['rate']
      )

      return redirect('review_detail', new_review.pk)
    return render(request, 'review_create.html', {
      'building': building,
      'conn_user': conn_user})
    
    # else:
    #     if request.method == "POST":
    #         return redirect('home')
    #     return render(request, 'review_create.html', {'building': None})

class Search(TemplateView):
    template_name= 'search.html'

class Result(ListView):
    model = Building
    template_name = 'result.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Building.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        )
        return object_list