from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from accounts.models import CustomUser
import os
from django.utils.translation import gettext_lazy as _
# from users.models import CustomUser
# from category.models import Category






class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
    
    def category_show_url(self):
        return  reverse('category.show',args=[self.id])

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()
    
    

              
class Project(models.Model):
    HOT = 'Hot'
    NEW = 'New'
    TOP = 'Top'
    BEST = 'Best'
    ENDING_SOON = 'EndingSoon'

    TAG_CHOICES = [
        (HOT, 'Hot'),
        (NEW, 'New'),
        (TOP, 'Top'),
        (BEST, 'Best'),
        (ENDING_SOON, 'Ending Soon'),
    ]
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField(max_length=200, null=True, blank=True)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    
    total_target=models.FloatField()
    current_fund=models.FloatField(default=0)
    num_of_ratings = models.PositiveIntegerField(default=0)
    total_rate = models.IntegerField(default=0)
    average_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)

    is_featured = models.BooleanField(_("Is Featured"), default=False)
    image1=models.ImageField(upload_to="projects/images/", null=True, blank=True)
    image2=models.ImageField(upload_to="projects/images/", null=True, blank=True)
    image3=models.ImageField(upload_to="projects/images/", null=True, blank=True)
    image4=models.ImageField(upload_to="projects/images/", null=True, blank=True)
    main_image = models.ImageField(upload_to="projects/images/", null=True, blank=True)
    tag1 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag2 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag3 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag4 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    
    start_date=models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"
    
    
    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timezone.timedelta(days=365 * 2)
        super().save(*args, **kwargs)


    def get_image1_url(self):
        return  f'/media/{self.image1}'
    
    def get_image2_url(self):
        return  f'/media/{self.image2}'
    
    def get_image3_url(self):
        return  f'/media/{self.image3}'
    
    def get_image4_url(self):
        return  f'/media/{self.image4}'
    
    
    def get_main_image_url(self):
        return f'/media/{self.main_image}' if self.main_image else None
    
    
    def get_all_imagesArray(self):
        projectImages=[]
        if(self.main_image):
            projectImages.append(self.get_main_image_url)
        if(self.image1):    
            projectImages.append(self.get_image1_url)
        if(self.image2):    
            projectImages.append(self.get_image2_url)
        if(self.image3):
            projectImages.append(self.get_image3_url)
        if(self.image4):
            projectImages.append(self.get_image4_url)
        return projectImages
    
    
    def get_all_tags(self):
        projectTags=[]
        if(self.tag1):
            projectTags.append(self.tag1)
        if(self.tag2):    
            projectTags.append(self.tag2)
        if(self.tag3):    
            projectTags.append(self.tag3)
        if(self.tag4):
            projectTags.append(self.tag4)
        return projectTags
        
    def add_rate(self, new_rate):   
        self.total_rate += new_rate
        self.num_of_ratings += 1
        self.average_rate = self.total_rate / self.num_of_ratings
        rounded_average_rate = round(self.average_rate, 2)
        self.average_rate=rounded_average_rate
        self.save()
        
    def edit_rate(self, new_rate,old_rate):   
        self.total_rate -= old_rate
        self.total_rate += new_rate
        self.average_rate = self.total_rate / self.num_of_ratings
        rounded_average_rate = round(self.average_rate, 2)
        self.average_rate=rounded_average_rate
        self.save()    
        
    def get_edit_url(self):
        return  reverse('projects.edit',args=[self.id])

    def get_show_url(self):
        return  reverse('projects.show',args=[self.id])

    def get_delete_url(self):
        return  reverse('projects.delete',args=[self.id])

    @classmethod
    def get_all_objects(cls):
        # return cls.objects.filter(id__gt=1)
        return cls.objects.all()
    @classmethod
    def get_specific_object(cls,id):
        return cls.objects.get(id=id)
    
    def add_rate(self, new_rate):
       
        self.total_rate += new_rate
        self.num_of_ratings += 1

        if self.num_of_ratings > 0:
            self.average_rate = self.total_rate / self.num_of_ratings
            self.average_rate = round(self.average_rate, 2)

        self.save()
        
    def get_all_ratings(self):
        return self.ratings.all()    
        
    def get_all_comments(self):
        return self.comments.all()    
        



class Rating(models.Model):
    class RateValue(models.IntegerChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='ratings')
    rate_value = models.IntegerField(choices=RateValue.choices,default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'project') 
    
    
    def __str__(self):
        return f"{self.user} rated {self.project} with {self.rate_value} stars"    
    
    
    
    
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='comments')
    comment_text = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # class Meta:
    #     unique_together = ('user', 'project')    
        
        
    def __str__(self):
        return f"{self.user} commented on  {self.project}"        
    
    


class ReportedProject(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reason = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"user : {self.user} Reported Project: {self.project.title}"

class ReportedComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user} Reported Comment: {self.comment.id}"
    
    
    

class Funding(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} funded {self.project.title} - {self.amount}"    