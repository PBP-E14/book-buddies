import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.core import serializers
from django.core.serializers import serialize
from django.core.exceptions import ValidationError
from book.models import Book
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@login_required
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
    except Book.DoesNotExist:
        pass

    return redirect('user_profile')


@login_required
def filter_books(request):
    year_range = request.GET.get('selected_year_range', None)

    # Filter books based on the user's history_books
    user_books = request.user.history_books.all()

    if year_range is not None:
        start_year, end_year = map(int, year_range.split('-'))

        # Filter books that match the year range and are in the user's history_books
        filtered_books = Book.objects.filter(
            Q(year_publication__gte=start_year) &
            Q(year_publication__lte=end_year) &
            Q(pk__in=user_books)
        )
    else:
        # Display all books that are in the user's history_books
        filtered_books = user_books

    book_data = [
        {
            'title': book.title,
            'author': book.author,
            'publisher': book.publisher,
            'year': book.year_publication,
            'image_cover': book.image_cover
        }
        for book in filtered_books
    ]

    if not book_data:
        # If no books are found, return a message with the selected year range
        if year_range:
            message = f'No books found in the year range {year_range}.'
        else:
            message = 'No books found in your history.'

        messages.info(request, message) 
        return JsonResponse({'message': message, 'status': 'no_books'})

    return JsonResponse({'books': book_data, 'status': 'success'})

def show_json(request):
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def fetch_user_data(request):
    user = request.user

    user_data = serialize('json', [user], fields=('username', 'email', 'gender', 'birth_date', 'phone_number', 'address', 'bio', 'history_books'))

    return JsonResponse({'user_data': user_data})

@login_required
@csrf_exempt
def update_profile_flutter(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)

            # Update user profile
            user = request.user
            user.gender = data.get('gender', user.gender)  # Use existing value as default
            user.birth_date = data.get('birth_date', user.birth_date)
            user.phone_number = data.get('phone_number', user.phone_number)
            user.address = data.get('address', user.address)
            user.bio = data.get('bio', user.bio)
            user.save()

            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)