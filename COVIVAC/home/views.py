from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as logmeout, authenticate
# Create your views here.
def index(request):
    total =20
    daily =9
    context = {
        "tn":total,
        "dn":daily
    }
    return render(request, 'index.html', context)

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            # login(request)
            auth_login(request, user)
            print(user)
            return redirect("/loggedview")
        else:
            return render(request, "login.html")
    return render(request, 'login.html')
    
def logout(request):
    logmeout(request)
    return render(request, 'index.html')
def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = username
        password = request.POST.get('password')
        # firstname = request.POST.get('firstname')
        # lastname = request.POST.get('lastname')
        user = User.objects.create_user(username, email, password)
        # user.last_name= lastname
        # user.first_name= firstname
        
    return render(request, 'register.html')

def loggedview(request):
    return render(request, 'loggedinview.html')
