from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'/mysite/edriver/register.html')
def login_view(request):
    return render(request,'/mysite/edriver/login.html')
def order_driver(request):
    return render(request,'/mysite/edriver/order_driver.html')
def order_success(request):
    return render(request,'/mysite/edriver/order_success.html')
def track_driver(request):
    return render(request,'/mysite/edriver/track_driver.html')
def index(request):
    return render(request,'/mysite/edriver/index.html')
def iDrive_view(request):
    # Your view logic here
    return render(request, 'main/login.html')   
def admin(request):
    # Your view logic here
    return render(request, 'main/login.html')    