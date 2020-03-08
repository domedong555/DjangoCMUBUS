from django.db import models

# Create your models here.
class Mask(models.Model):
    name = models.CharField(max_length=50)
    des = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name
