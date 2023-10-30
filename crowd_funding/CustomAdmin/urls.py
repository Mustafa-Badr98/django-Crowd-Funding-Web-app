
from django.urls import include
from django.urls import path
from CustomAdmin.views import custom_admin_dashboard,admin_projects,admin_categories,admin_Rating,admin_Comments,admin_ReportedProjects,admin_ReportedComments
urlpatterns = [
    path('custom-admin/dashboard/', custom_admin_dashboard, name='custom_admin_dashboard'),
    path('custom-admin/projects/', admin_projects, name='custom_admin_projects'),
    path('custom-admin/categories/', admin_categories, name='custom_admin_categories'),
    path('custom-admin/rates/', admin_Rating, name='custom_admin_rates'),
    path('custom-admin/comments/', admin_Comments, name='custom_admin_comments'),
    path('custom-admin/reported_comments/', admin_ReportedComments, name='custom_admin_reported_comments'),
    path('custom-admin/reported_projects/', admin_ReportedProjects, name='custom_admin_reported_projects'),
   
   
]



