from django.contrib import admin
from .models import Building
from .models import Profile
from .models import Review
from .models import Rating
from .models import Comment
from .models import Recomment
from .models import Save
# Register your models here.
admin.site.register(Building)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Recomment)
admin.site.register(Save)
