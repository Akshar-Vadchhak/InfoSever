from django.db import models
from django.utils import timezone, timesince

# Create your models here. 

class Info(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='infos/')
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    adress = models.TextField()
    NativePlace = models.CharField(max_length=100)
    occuppation = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    description = models.TextField()
    addDate = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.name