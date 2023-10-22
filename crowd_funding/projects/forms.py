from django import forms
from projects.models import Rating,Funding

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_value']


class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = ['amount']