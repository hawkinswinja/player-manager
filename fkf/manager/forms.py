from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import County, Academy, Player, Admin


class AddUser(UserCreationForm):
    class Meta:
        model = Admin
        fields = ["name", "role"]


class CountyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = County
        fields = ["name", "password"]


class AcademyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Academy
        fields = ["county", "name", "password"]


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["academy", "name", "picture"]
