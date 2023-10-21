from django import forms
from projects.models import Rating,Project

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_value']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields=['title', 'details', 'Category','total_target','start_date','end_date','current_fund','num_of_ratings','total_rate','average_rate','tag1','tag2','tag3','tag4','image1','image2','image3','image4','main_image']
