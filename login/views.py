from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import auth, messages


# Create your views here.

def login(r):
    if not r.user.is_authenticated:
        if r.method == 'POST':
            username = r.POST['username']
            password = r.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(r, user)
                messages.success(r, "Successful")
                return redirect('dashboard/')
            else:
                messages.error(r, "User not found")
        return render(r, 'login.html')
    else:
        return redirect('dashboard/')


def dashbaord(r):
    if r.user.is_authenticated:
        return render(r, 'dashboard-admin.html')
    else:
        return redirect('login/')


def logout(r):
    auth.logout(r)
    messages.success(r, "Logout Successfull")
    return redirect('login/')
