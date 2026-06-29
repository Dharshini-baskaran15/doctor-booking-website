from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def index_page(request):
    return render(request,'index.html')

def about_page(request):
     return render(request,'about.html')

def doctor_page(request):
    data = doctor.objects.all()
    a = data.count()
    print(a)
    return render(request, 'doctor.html', {'data': data})


def product_detail(request,id):
     d=doctor.objects.get(id=id)
     return render(request,'product_detail.html',{'d':d})

def success_page(request):
     return render(request,'success.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("index")

    return render(request, "signup.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")

