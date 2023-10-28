import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')
