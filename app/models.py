from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
   
    imga = models.ImageField(upload_to= 'imges/')
    def __str__(self):
        return self.name

