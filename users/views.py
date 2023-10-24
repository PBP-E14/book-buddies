from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Redirect to the login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

