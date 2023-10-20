from django.urls import path,include
from projects.views import create_project,add_rating_view

urlpatterns=[
    path('create/',create_project,name='project.create'),
    path('projects/<int:project_id>/rate/', add_rating_view, name='add_rating'),


]

