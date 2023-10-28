from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import Wishlist  # Import your Product model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from book.models import Book

# Create your views here.
def show_wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlists': wishlists,
    }

    return render(request, "show_wishlist.html", context)

@csrf_exempt
def remove_wishlist(request, wishlist_id):
    if request.method == 'DELETE':
        wishlist = Wishlist.objects.get(pk=wishlist_id)
        wishlist.user = request.user
        wishlist.delete()
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()

def get_wishlist(request):
    product_wishlist = Wishlist.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_wishlist))

@csrf_exempt
def create_ajax(request, book_id):
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

        wishlist_item = Wishlist(user=request.user,book=book)
        wishlist_item.save()

        return JsonResponse({'message': 'Book added to the wishlist'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)