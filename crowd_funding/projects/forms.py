from django import forms
from projects.models import Rating,Funding,ReportedComment,ReportedProject

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_value']



class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportedComment
        fields = ['reason']

class ReportProjectForm(forms.ModelForm):
    class Meta:
        model = ReportedProject
        fields = ['reason']





class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = ['amount']