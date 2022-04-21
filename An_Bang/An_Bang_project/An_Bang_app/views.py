# from django.shortcuts import render, redirect
# from .models import Building
# from .models import Review
# from .models import Rating
# from .models import Comment
# from .models import Recomment
# from .models import Save
# from .models import Profile
# import datetime

# # Create your views here.

# def review_create(request,building_address,username):
#     building = Building.objects.get(address=building_address)
#     user = Profile.objects.get(username=username)
#     if request == "POST":
#         user_id = user.username
#         building_id = building.address
#         memo = request.POST['memo']
#         uploaded = datetime.datetime.now()
#         like = request.POST['like']
#         new_review = Review.objects.create(
#             user_id = user_id, building_id = building_id,
#             memo = memo, uploaded = uploaded, like = like)
#         return redirect('review_detail', new_review.user_id)
#     return render(request,'review_create.html')

# def review_detail(request,review_id):
#     review = Review.objects.get(user_id=review_id)
#     return render(request, 'review_detail.html', {'review' : review})

# def review_list(request,building_address):
#     reviews = Review.objects.filter(building_id=building_address)
#     return render(request, 'review_list.html', {'reviews' : reviews})

# def building_create(request):
#     if request == "POST":
#         address = request.POST['address']
#         name = request.POST['name']
#         cctv = request.POST['cctv']
#         entrance = request.POST['entrance']
#         guard = request.POST['guard']
#         elevator = request.POST['elevator']
#         new_building = Building.objects.create(
#             address=address, name=name, cctv=cctv,
#             entrance=entrance, guard=guard, elevator=elevator,
#             guard=guard
#         )
#         return redirect('building_detail', new_building.address)

# def building_detail(request,building_address):
#     building = Building.objects.get(address=building_address)
#     reviews = Review.objects.filter(building_id=building_address)
#     return render(request, 'building_detail.html', {'building' : building , 'reviews' : reviews})

# def building_list(request):
#     buildings = Building.objects.order_by('name')
#     return render(request, 'building_list.html', {'buildings':buildings})
