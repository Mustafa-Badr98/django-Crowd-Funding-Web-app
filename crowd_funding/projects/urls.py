from django.urls import path,include
from projects.views import create_project,add_rating_view,searchProject,edit_project

urlpatterns=[
    path('create/',create_project,name='project.create'),
    path('edit/<int:id>', edit_project, name='projects.edit'),

    path('<int:project_id>/rate/', add_rating_view, name='add_rating'),
    path('searched/',searchProject  ,name="project.search"),

]

