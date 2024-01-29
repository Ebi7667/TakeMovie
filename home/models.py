from django.db import models
from django.utils.timezone import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Movies(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    entity_type=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    zhanr=models.CharField(max_length=20)
    running_time=models.CharField(max_length=10)
    photo=models.ImageField(default='A Dreamy World Wallpaper  (15).jpg')
    point=models.CharField(max_length=10)
    discription=models.TextField()
    limit_age=models.CharField(max_length=10)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    published=models.DateTimeField(default=datetime.now())
    def get_absolute_url(self):
        return reverse('frontend_Detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name