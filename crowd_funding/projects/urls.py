from django.urls import path,include
from projects.views import searchProject,edit_project
from projects.views import create_project,add_rating_view2,searchProject,ViewProject,add_comment,fund_project

urlpatterns=[
    path('create/',create_project,name='project.create'),
    path('edit/<int:id>', edit_project, name='projects.edit'),
    path('<int:project_id>/rate/', add_rating_view2, name='add_rating'),
    path('<int:project_id>/comment/', add_comment, name='add_comment'),
    path('searched/',searchProject  ,name="project.search"),
    path('view/<int:id>', ViewProject,name='projects.show'),
    path('fund/<int:project_id>', fund_project,name='project_add_fund'),

]

