from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
  name = models.CharField(max_length=128)
  user = models.OneToOneField(User, related_name='user')
  salary = models.FloatField()

  def __str__(self):
    return self.name

class Client(models.Model):
  name = models.CharField(max_length=128)
  address = models.CharField(max_length=256)
  phone = models.CharField(max_length=16)

  def __str__(self):
    return self.name

class Product(models.Model):
  description = models.CharField(max_length=128)
  price = models.FloatField()

  def __str__(self):
    return self.description

class Sale(models.Model):
  employee = models.ForeignKey(Employee, related_name="sales", on_delete=models.CASCADE)
  client = models.ForeignKey(Client, related_name="shoppings", on_delete=models.CASCADE)
  date = models.DateField()

  def __str__(self):
    return "Sale to %s" % (self.client.name)

class SaleItem(models.Model):
  sale = models.ForeignKey(Sale, related_name="items", on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name="sold", on_delete=models.CASCADE)
  quantity = models.IntegerField()
  total_price = models.FloatField()

  def __str__(self):
    return "%d %s at $%.2f" %(self.quantity, self.product.description, self.total_price)