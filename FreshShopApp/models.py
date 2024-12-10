from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class productModel(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='Images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Product'

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,unique=True)

    def __str__(self):
        return f"{self.user.first_name} - Profile"

class cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(productModel,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)