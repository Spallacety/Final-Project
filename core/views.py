from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from .models import *
from django.utils import timezone
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status

class UserList(generics.ListAPIView):
  """
  get: Return a list of all the existing users.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-list'
  permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveAPIView):
  """
  get: Return the given user.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-detail'
  permission_classes = (permissions.IsAuthenticated,)

class EmployeeList(generics.ListAPIView):
  """
  get: Return a list of all the existing employees.
  """
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  name = 'employee-list'
  permission_classes = (permissions.IsAuthenticated,)

class EmployeeDetail(generics.RetrieveAPIView):
  """
  get: Return the given employee.
  """
  queryset = Employee.objects.all()
  serializer_class = EmployeeDetailSerializer
  name = 'employee-detail'
  permission_classes = (permissions.IsAuthenticated,)

class ClientList(generics.ListCreateAPIView):
  """
  get: Return a list of all the existing clients.
  post: Create a new client instance.
  """
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  name = 'client-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
  ordering_fields = ('name',)
  search_fields = ('name',)
  filter_fields = ('name',)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  get: Return the given client.
  delete: Delete the given client.
  put: Update the given client.
  patch: Update the given client.
  """
  queryset = Client.objects.all()
  serializer_class = ClientDetailSerializer
  name = 'client-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProductList(generics.ListCreateAPIView):
  """
  get: Return a list of all the existing products.
  post: Create a new product instance.
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  name = 'product-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
  ordering_fields = ('description',)
  search_fields = ('description',)
  filter_fields = ('description',)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  get: Return the given product.
  delete: Delete the given product.
  put: Update the given product.
  patch: Update the given product.
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  name = 'product-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SaleList(generics.ListCreateAPIView):
  """
  get: Return a list of all the existing sales.
  post: Create a new sale instance with atual date and auth user related employee.
  """
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer
  name = 'sale-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def perform_create(self, serializer):
    employee = Employee.objects.get(user=self.request.user)
    date = timezone.localdate()
    serializer.save(employee=employee, date=date)

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  get: Return the given sale.
  delete: Delete the given sale if belongs to the auth user related employee.
  """
  queryset = Sale.objects.all()
  serializer_class = SaleDetailSerializer
  name = 'sale-detail'
  http_method_names = ['get', 'delete', 'head', 'options']
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOnwerOrReadOnly,)

class SaleItemList(generics.ListCreateAPIView):
  """
  get: Return a list of all the existing sale items.
  post: Create a new sale item instance if sale belongs to the auth user related employee.
  """
  queryset = SaleItem.objects.all()
  serializer_class = SaleItemSerializer
  name = 'saleitem-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSaleOnwerOrReadOnly,)

  def create(self, request):
    serializer = SaleItemSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      if request.user != serializer.validated_data.get('sale').employee.user:
        content = {
          "detail": "You're not allowed to include items on this sale."
        }
        return Response(content, status=status.HTTP_403_FORBIDDEN)
      total_price = serializer.validated_data.get('product').price * serializer.validated_data.get('quantity')
      serializer.save(total_price=total_price)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleItemDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  get: Return the given sale item.
  delete: Delete the given sale item if sale belongs to the auth user related employee.
  """
  queryset = SaleItem.objects.all()
  serializer_class = SaleItemSerializer
  name = 'saleitem-detail'
  http_method_names = ['get', 'delete', 'head', 'options']
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSaleOnwerOrReadOnly,)

class APIRoot(generics.GenericAPIView):
  """
  get: Return a list of all the existing API routes.
  """
  def get(self, request):
    return Response({'employees': reverse(EmployeeList.name, request=request),
                     'clients': reverse(ClientList.name, request=request),
                     'sales': reverse(SaleList.name, request=request),
                     'products': reverse(ProductList.name, request=request),
                     'sale-items': reverse(SaleItemList.name, request=request)
                     })