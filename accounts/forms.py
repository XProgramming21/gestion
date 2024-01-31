from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateCommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["nom", "phone", "photo_profil", "email"]
