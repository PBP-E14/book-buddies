from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "gender",
            "birth_date",
            "phone_number",
            "address",
            "bio",
        ]
