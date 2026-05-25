from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginForm

def login_view(request:HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('projects:list')
            form.add_error(None, 'Invalide email or password')
            
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request:HttpRequest):
    if request.method == 'POST':
        logout(request)
        return redirect('users:login')
    return render(request, 'users/logout.html')
