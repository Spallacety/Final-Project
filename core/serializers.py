from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username',)

class EmployeeSerializer(serializers.ModelSerializer):
  user = UserSerializer()

  class Meta:
    model = Employee
    fields = ('url', 'name', 'user', 'salary',)

class EmployeeDetailSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  sales = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sale-detail')

  class Meta:
    model = Employee
    fields = ('url', 'name', 'user', 'salary', 'sales',)

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = ('url', 'name', 'address', 'phone',)

class ClientDetailSerializer(serializers.ModelSerializer):
  shoppings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sale-detail')

  class Meta:
    model = Client
    fields = ('url', 'name', 'address', 'phone', 'shoppings')

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('url', 'description', 'price',)

class SaleSerializer(serializers.ModelSerializer):
  employee = serializers.SlugRelatedField(read_only=True, slug_field='name')
  client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')
  date = serializers.ReadOnlyField()

  class Meta:
    model = Sale
    fields = ('url', 'employee', 'client', 'date',)

class SaleDetailSerializer(serializers.ModelSerializer):
  employee = serializers.SlugRelatedField(read_only=True, slug_field='name')
  client = serializers.SlugRelatedField(read_only=True, slug_field='name')
  date = serializers.ReadOnlyField()
  items = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='saleitem-detail')

  class Meta:
    model = Sale
    fields = ('url', 'employee', 'client', 'date', 'items',)

class SaleItemSerializer(serializers.ModelSerializer):
  sale = serializers.HyperlinkedRelatedField(queryset=Sale.objects.all(), view_name='sale-detail')
  product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='description')
  total_price = serializers.ReadOnlyField()

  class Meta:
    model = SaleItem
    fields = ('url', 'sale', 'product', 'quantity', 'total_price',)