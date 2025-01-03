from django.db import models
from django.contrib.auth.models import AbstractUser


USERTYPE = (
    ('Customer' , 'Customer'),
    ('Supplier' , 'Supplier'),
    ('Admin' , 'Admin')
)

class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20 , choices=USERTYPE , null=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=2000 ,null=True)
    SKU = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    customerID = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    qty = models.IntegerField()
    productID = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
    
    def __str__(self):
        return self.CustomerID
    

class Order(models.Model):
    customerID = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    qty = models.IntegerField()
    productID = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
    
    def __str__(self):
        return self.CustomerID
    
    
class Invetory(models.Model):
    currentStock = models.IntegerField()
    productID = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
    location = models.CharField(max_length=100)
    lastUpdated = models.DateField(verbose_name="Last Updated",null=True)
    
    def __str__(self):
        return self.CustomerID
    
    

