from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def user_logout (request):
    auth.logout(request)
    return render(request,'login.html')


def create_user(request):
    # Your code to create a new user goes here
    return render(request, 'Register.html')


def user_login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Login")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username__iexact=name).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email__iexact=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=name, password=password, first_name=first_name, last_name=last_name, email=email)
                auth.login(request, user)  # Log in the user after registration if needed
                messages.success(request, "User created successfully")
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

    return render(request, "Register.html")
