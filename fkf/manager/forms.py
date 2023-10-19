from django import forms
from .models import County, Academy, Player


class CountyForm(forms.ModelForm):
    class Meta:
        model = County
        fields = ["name", "admin", "password"]


class AcademyForm(forms.ModelForm):
    class Meta:
        model = Academy
        fields = ["county", "name", "admin", "password"]


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["academy", "name", "picture"]
