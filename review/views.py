from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from review.forms import ReviewForm
from django.urls import reverse
from review.models import Review
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from users.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
def show_review(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, "show_review.html", context)

def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return HttpResponseRedirect(reverse('show_review'))

    context = {'form': form}
    return render(request, "create_review.html", context)

def get_review_json(request):
    reviews = Review.objects.all()
    return HttpResponse(serializers.serialize('json', reviews))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        review = request.POST.get("review")

        new_review = Review(title=title, review=review)
        new_review.user = request.user
        new_review.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_user(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize('json', users))