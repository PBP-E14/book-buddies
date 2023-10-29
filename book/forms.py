from django.forms import ModelForm
from .models import RequestBook


class RequestBookForm(ModelForm):
    class Meta:
        model = RequestBook
        fields = ["title", "author", "publisher", "year_publication", "image_cover"]
