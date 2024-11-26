from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    specifications = models.TextField(max_length=1000 , default="Available")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.DecimalField(max_digits=2,default=3,decimal_places=1)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name}, {self.city}"



