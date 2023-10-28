from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from review.forms import ReviewForm
from django.urls import reverse
from review.models import Review
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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

