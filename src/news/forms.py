from django import forms
from .models import Favorite


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = "__all__"

    description = forms.CharField(required=False)
    title = forms.CharField(required=False)
    url = forms.URLField(required=False)
    author = forms.CharField(required=False)
    published_at = forms.DateTimeField(required=False)
