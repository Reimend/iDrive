from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.iDrive_view, name='iDrive'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('order_driver/', views.order_driver, name='order_driver'),
    path('order_success/', views.order_success, name='order_success'),
    path('track_driver/', views.track_driver, name='track_driver'),
]  

# path('iDrive', include ('iDrive_urls')), 
     
#     path('iDrive/', views.iDrive, name='iDrive'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login, name='login'),
#     path('order_driver/', views.order_driver, name='order_driver'),
#     path('order_success/', views.order_success, name='order_success'),
#     path('track_driver/', views.track_driver, name='track_driver'),