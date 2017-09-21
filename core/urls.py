from django.conf.urls import url
from .views import *
from django.contrib.auth import views

urlpatterns = [
  url(r'^$', index, name='index'),
  url(r'^employees/$', employees, name='employees'),
  url(r'^clients/$', clients, name='clients'),

  url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
  url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name='logout'),
]