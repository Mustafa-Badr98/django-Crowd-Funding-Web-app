from django.urls import path,include
from projects.views import create_project,add_rating_view2,searchProject,ViewProject,add_comment

urlpatterns=[
    path('create/',create_project,name='project.create'),
    path('<int:project_id>/rate/', add_rating_view2, name='add_rating'),
    path('<int:project_id>/comment/', add_comment, name='add_comment'),
    path('searched/',searchProject  ,name="project.search"),
    path('view/<int:id>', ViewProject,name='projects.show'),

]

