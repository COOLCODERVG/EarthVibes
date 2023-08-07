from django.db import models


# Create your models here.
class EventModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    date = models.DateField()
    zipcode = models.IntegerField()
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    description= models.CharField(max_length=1000)
    def __str__(self):
        return self.name