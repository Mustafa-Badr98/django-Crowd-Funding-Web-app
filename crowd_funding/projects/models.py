# from django.db import models
# # from taggit.managers import TaggableManager
# from django.contrib.auth.models import User 

# # Create your models here.
# class Category(models.Model):
#     name=models.CharField(max_length=255)


#     def __str__(self):
#         return f"{self.name}"
    



# class Project(models.Model):
#         title=models.CharField(max_length=100)
#         details=models.TextField(max_length=255)
#         category=models.ForeignKey(Category,on_delete=models.CASCADE)
#         start_time=models.DateField(auto_now=False, auto_now_add=False)
#         end_time=models.DateField(auto_now=False, auto_now_add=False)


from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# from users.models import CustomUser
# from category.models import Category

# Create your models here.

import os

def get_image_path(instance, filename):
    # Constructing the file path based on owner's ID
    owner_id = str(instance.owner.id)
    project_id = str(instance.id)
    
    base_filename, file_extension = os.path.splitext(filename)
    return f'projects/images/owner{owner_id}/project{project_id}/{base_filename}{file_extension}'


class Project(models.Model):
    HOT = 'hot'
    NEW = 'new'
    TOP = 'top'
    BEST = 'best'
    ENDING_SOON = 'endingsoon'

    TAG_CHOICES = [
        (HOT, 'Hot'),
        (NEW, 'New'),
        (TOP, 'Top'),
        (BEST, 'Best'),
        (ENDING_SOON, 'Ending Soon'),
    ]
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField(max_length=200, null=True, blank=True)
    # Category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    
    image1=models.ImageField(upload_to=get_image_path, null=True, blank=True)
    image2=models.ImageField(upload_to=get_image_path, null=True, blank=True)
    image3=models.ImageField(upload_to=get_image_path, null=True, blank=True)
    image4=models.ImageField(upload_to=get_image_path, null=True, blank=True)
    main_image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    total_target=models.FloatField()
    current_fund=models.FloatField()
    # rate = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],default=0)
    # num_of_ratings=models.PositiveIntegerField(default=0)
    # average_rate=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],default=1)
   
    tag1 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag2 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag3 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag4 = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    
    start_date=models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def _str_(self):
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
    
    def add_rate(self, new_rate):   
        self.rate += new_rate
        self.num_of_ratings += 1
        self.average_rate = self.rate / self.num_of_ratings
        rounded_average_rate = round(self.average_rate, 2)
        self.average_rate=rounded_average_rate
        self.save()
        
    
    def get_main_image_url(self):
        return f'/media/{self.main_image}' if self.main_image else None


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