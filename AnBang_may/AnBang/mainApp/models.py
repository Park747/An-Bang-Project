
# Create your models here.
from django.utils import timezone
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from accountApp.models import User

# Create your models here.
class Building(models.Model):
    address = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id' : self.pk,
            'address' : self.address,
            'name' : self.name,
            'latitude' : str(self.latitude),
            'longitude' : str(self.longitude) # Decimal type은 json으로 변환이 불가하다! str으로 바꿔서 전달해야 typeerror 발생 X. 더 알아보고 정리하자
        }


class Review(models.Model):
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, default=0)
    uploaded = models.DateTimeField(default=timezone.now)
   

    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    host = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    soundproof = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    water_pressure = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    new = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    memo = models.TextField()

    class Meta:
        ordering = ['uploaded']
        unique_together = (('user_email', 'building_id'),)
        

class Comment(models.Model):
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, default=0)
    content = models.TextField()
    uploaded = models.DateField(default=timezone.now)


class Pick(models.Model):
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, default=0)

    class Meta:
        unique_together = (('user_email', 'building_id'),)

    