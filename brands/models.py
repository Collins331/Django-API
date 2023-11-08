from django.db import models

# Create your models here.
#
class Cloths(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    gender = models.CharField(max_length=50, default='Both')
    image = models.ImageField(default='clothes.png')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300, default='No description available')

    def __str__(self):
        return '%s %s' % (self.name, self.price)