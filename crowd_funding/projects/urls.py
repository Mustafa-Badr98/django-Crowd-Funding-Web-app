from django.urls import path,include
from projects.views import searchProject,edit_project
from projects.views import create_project,add_rating_view2,searchProject,ViewProject,add_comment,fund_project,CategoryProjectsListView,cancel_project,report_project,report_comment

urlpatterns=[
    path('create/',create_project,name='project.create'),
    path('edit/<int:id>', edit_project, name='projects.edit'),
    path('<int:project_id>/rate/', add_rating_view2, name='add_rating'),
    path('<int:project_id>/comment/', add_comment, name='add_comment'),
    path('searched/',searchProject  ,name="project.search"),
    path('viewProject/<int:id>', ViewProject,name='projects.show'),
    path('fund/<int:project_id>', fund_project,name='project_add_fund'),
    path('viewCategory/<int:category_id>', CategoryProjectsListView.as_view(),name='category.show'),
    path('cancel/<int:id>', cancel_project, name='projects.cancel'),
    path('report/<int:id>',report_project, name='projects.report'),
    path('report_comment/<int:project_id>/<int:comment_id>', report_comment, name='projects.report.comment'),

]

