from django.urls import path,include
from projects.views import create_project
urlpatterns=[
    path('create/',create_project,name='project.create'),



]