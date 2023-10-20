from django import forms
from projects.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_value']
