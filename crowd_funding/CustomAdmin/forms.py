from django import forms
from accounts.models import CustomUser
from projects.models import Category,Project

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','password','phone_number',
              'birth_date','country','image','is_active'
                  ]



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description' ]
        



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','details','Category' ,'owner',
                  'total_target','num_of_ratings','total_rate',
                  'average_rate','main_image','image1','image2','image3','image4',
                  'tag1','tag2','tag3','tag4','start_date','end_date',
                  'is_featured'
                  ]

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields=['title', 'details', 'Category','total_target','start_date','image1','image2','image3','image4','main_image']

# class ReportCommentForm(forms.ModelForm):
#     class Meta:
#         model = ReportedComment
#         fields = ['reason']
#         labels = {'reason': 'Submit Your Report on Comment'}

# class ReportProjectForm(forms.ModelForm):
#     class Meta:
#         model = ReportedProject
#         fields = ['reason']
#         labels={'reason':'Submit Your Report'}



# class FundingForm(forms.ModelForm):
#     class Meta:
#         model = Funding
#         fields = ['amount']
# ad
       

        
        
        
         