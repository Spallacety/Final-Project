from django.conf.urls import url
from .views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Final Project API')

urlpatterns = [
  url(r'^$', APIRoot.as_view(), name='root'),
  url(r'^users/$', UserList.as_view(), name=UserList.name),
  url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name=UserDetail.name),
  url(r'^employees/$', EmployeeList.as_view(), name=EmployeeList.name),
  url(r'^employee/(?P<pk>[0-9]+)/$', EmployeeDetail.as_view(), name=EmployeeDetail.name),
  url(r'^clients/$', ClientList.as_view(), name=ClientList.name),
  url(r'^client/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name=ClientDetail.name),
  url(r'^sales/$', SaleList.as_view(), name=SaleList.name),
  url(r'^sale/(?P<pk>[0-9]+)/$', SaleDetail.as_view(), name=SaleDetail.name),
  url(r'^sale-items/$', SaleItemList.as_view(), name=SaleItemList.name),
  url(r'^sale-item/(?P<pk>[0-9]+)/$', SaleItemDetail.as_view(), name=SaleItemDetail.name),
  url(r'^products/$', ProductList.as_view(), name=ProductList.name),
  url(r'^product/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name=ProductDetail.name),
  url(r'^swagger/$', schema_view, name='swagger'),
]