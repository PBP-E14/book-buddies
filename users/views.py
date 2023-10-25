from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                return redirect('user_login')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_profile(request):
    return render(request, 'profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        user = request.user
        user.gender = request.POST.get('gender')
        user.birth_date = request.POST.get('birth_date')
        user.phone_number = request.POST.get('phone_number')
        user.address = request.POST.get('address')
        user.bio = request.POST.get('bio')
        user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})