from django.shortcuts import render


def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')

def order_driver(request):
    return render(request, 'main/order_driver.html')

def order_success(request):
    return render(request, 'main/order_success.html')

def track_driver(request):
    return render(request, 'main/track_driver.html')

def index(request):
    return render(request, 'main/index.html')

def iDrive_view(request):
    return render(request, 'main/login.html')

def admin(request):
    return render(request, 'main/login.html')

