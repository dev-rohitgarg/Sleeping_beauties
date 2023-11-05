from django.shortcuts import render
import connect

var = {'hello':connect.b}

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html', var)