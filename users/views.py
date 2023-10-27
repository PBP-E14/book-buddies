from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from book.models import Book
from .models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        bio = request.POST.get('bio', '')

        errors = {}

        # Validate data 
        if User.objects.filter(username=username).exists():
            errors['username'] = ['Username already exists.']

        if User.objects.filter(email=email).exists():
            errors['email'] = ['Email already in use.']

        if password1 != password2:
            errors['password'] = ['Passwords do not match.']

        try:
            validate_password(password1)
        except ValidationError as e:
            errors['password'] = list(e)

        if not errors:
            # Create the user
            user = User.objects.create_user(
                username=username, 
                email=email, 
                password=password1,
                gender=gender,
                birth_date=birth_date,
                phone_number=phone_number,
                address=address,
                bio=bio,
            )
            user.save()

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                return redirect('user_login')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': errors})

    return render(request, 'register.html')


def user_profile(request):
    user = request.user
    user.birth_date_str = user.birth_date.strftime('%Y-%m-%d') if user.birth_date else ''
    user_books = request.user.history_books.all()
    context = {
        'user': user,
        'user_books': user_books,
    }
    return render(request, 'profile.html', context)

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

def delete_book(request, book_id):
    user = request.user
    try:
        book = get_object_or_404(Book, id=book_id)
        user.history_books.remove(book)
        return HttpResponseRedirect(reverse('profile')) 
    except Book.DoesNotExist:
        return HttpResponseRedirect(reverse('profile'))  