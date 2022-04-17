from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Building(models.Model):
    
    address = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, blank=True)
    cctv = models.BooleanField(default=False)
    entrance = models.BooleanField(default=False)
    guard = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)



class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,default='')
    # pwd =
    name = models.CharField(max_length=10,blank=True)
    gender = models.CharField(max_length=1,blank=True)
    birth_year = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_date = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=30,blank=True)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Review(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    memo = models.TextField()
    uploaded = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=0)

    class Meta:
        ordering = ['uploaded']
        unique_together = (('user_id', 'building_id'),)

    


class Rating(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    host = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    soundproof = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    safety = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    water_pressure = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    new = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    lighting = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    insect = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)



class Comment(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    uploaded = models.DateField(default=timezone.now)

    

class Recomment(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    target_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    uploaded = models.DateField(default=timezone.now)


class Save(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user_id', 'building_id'),)