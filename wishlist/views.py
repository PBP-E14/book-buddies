import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import Wishlist  # Import your Product model
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='')
def show_wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlists': wishlists,
    }

    return render(request, "main.html", context)

def show_info(request):
    context = {}