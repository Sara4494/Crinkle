
from .models import Menu
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate

def home(request):
    data = Menu.objects.all()
    name = None
    if 'search' in request.GET:
        name = request.GET['search']
        if name:
            data = data.filter(name__icontains=name)

    return render(request ,'home.html' , {'data':data})

def services(request):
    return render(request, "services.html")
def portfolio(request):
    return render(request,"portfolio.html")
 

def register(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST['name']
        email = request.POST['mail']
        password = request.POST['pass']
        password_confirm = request.POST['pass-confirm']

       
        if password != password_confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
 
        user = User.objects.create_user(username=username, email=email, password=password)
 
        login(request, user)
 
        return redirect('home')   
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email_mobile = request.POST['mail']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=email_mobile, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            # Redirect to home or any other page
            return redirect('home')  # Adjust the URL as needed
        else:
            # Authentication failed, handle accordingly (e.g., show an error message)
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

