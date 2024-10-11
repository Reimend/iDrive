from django.urls import path
from . import views

urlpatterns = [
    

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('order_driver/', views.order_driver, name='order_driver'),
    path('order_success/', views.order_success, name='order_success'),
    path('track_driver/', views.track_driver, name='track_driver'),
]
