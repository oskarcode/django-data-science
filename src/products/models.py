from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Product(models.Model):
          name = models.CharField( max_length= 220)
          date = models.DateTimeField(auto_now_add=True)


          def __str__(self):
                    return str(self.name)


class Purchase(models.Model):
          product = models.ForeignKey(Product, on_delete=models.CASCADE)
          price = models.PositiveIntegerField()
          quantity = models.PositiveIntegerField()
          total_price = models.PositiveIntegerField(blank=True) # we leave it as blank, so that we can define a function and overwrite the value of total price later
          salesman = models.ForeignKey(User,on_delete=models.CASCADE)
          date = models.DateTimeField(default=timezone.now)

          def save(self,*args,**kwargs):
                    self.total_price = self.price * self.quantity
                    super().save(*args,**kwargs) # this will save the value to total_price
          
          def __str__(self):
                    return f'solled {self.product.name} - {self.quantity} item for {self.total_price}'