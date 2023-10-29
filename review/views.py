from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from review.forms import ReviewForm
from django.urls import reverse
from review.models import Review
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_review(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, "show_review.html", context)

def get_review_id(request, select_option):
    if select_option == 1:
        reviews = Review.objects.all()
    elif select_option == 2:
        reviews = Review.objects.filter(user=request.user)
    else:
        reviews = Review.objects.all() 
    return HttpResponse(serializers.serialize('json', reviews))

@csrf_exempt
@login_required
def add_review_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        review = request.POST.get("review")

        new_review = Review(title=title, review=review)
        new_review.user = request.user
        new_review.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_user_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize('json', users))