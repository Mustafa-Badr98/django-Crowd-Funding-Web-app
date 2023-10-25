from django import forms
from projects.models import Rating,Project
from projects.models import Rating,Funding,ReportedComment,ReportedProject,Comment

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_value']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['title', 'details', 'Category','total_target','start_date','image1','image2','image3','image4','main_image']

class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportedComment
        fields = ['reason']
        labels = {'reason': 'Submit Your Report on Comment'}

class ReportProjectForm(forms.ModelForm):
    class Meta:
        model = ReportedProject
        fields = ['reason']
        labels={'reason':'Submit Your Report'}



# class FundingForm(forms.ModelForm):
#     class Meta:
#         model = Funding
#         fields = ['amount']
# ad
       

        
        
        
         
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']  
        labels = {
            'comment_text': 'Your Comment',
        }
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here',
                'style': 'color: #333; font-size: 14px; padding: 10px; height: 60px'
            }),
        }
