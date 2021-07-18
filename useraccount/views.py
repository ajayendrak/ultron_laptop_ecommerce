from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages



# Create your views here.

# testing user details: username=ajay, password=ajay@1234

def loginUser(request):
    if request.method=='POST':
        # Check if user enterd correct credentials
        username=request.POST.get('username')
        password=request.POST.get('pswd')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('/')
            
            # A backend authenticated the credentials
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def sign_up(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exist')
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist')
                print('email taken')
            else:
                u_info = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                u_info.save()
                messages.success(request, 'You have registered account successfully!')
                return redirect('/login')
        else:
            messages.warning(request, 'Password is incorrect')
    return render(request, 'signup.html')