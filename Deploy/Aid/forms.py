from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class FirstForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
