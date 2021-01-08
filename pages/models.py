from django.db import models

# Create your models here.

class home(models.Model):
    picture= models.ImageField()
    name= models.CharField(max_length=100)
    description= models.TextField()
    address= models.CharField(max_length=50)
    bedroom_number= models.IntegerField()


    def __str__(self):
        return self.name
    
