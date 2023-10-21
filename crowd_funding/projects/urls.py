from django.urls import path,include
from projects.views import create_project,add_rating_view,searchProject

urlpatterns=[
    path('create/',create_project,name='project.create'),
    path('<int:project_id>/rate/', add_rating_view, name='add_rating'),
    path('searched/',searchProject  ,name="project.search"),

]

