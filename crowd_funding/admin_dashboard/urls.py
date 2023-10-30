from django.urls import path
from admin_dashboard.views import admin_home, users_list, AccountCreateView, user_delete, user_edit, categories_list, projects_list, comments_list, fundings_list, ratings_list, reported_comments_list,reported_projects_list

urlpatterns = [
    path('admin_home/', admin_home, name='admin_home'),
    path('users_list/', users_list, name='users_list'),
    path('user_create/', AccountCreateView.as_view(), name='user_create'),
    path('user_edit/<int:id>/', user_edit, name='user_edit'),
    path('user_delete/<int:id>/', user_delete, name='user_delete'),
    path('categories_list/', categories_list, name='categories_list'),
    path('projects_list/', projects_list, name='projects_list'),
    path('comments_list/', comments_list, name='comments_list'),
    path('fundings_list/', fundings_list, name='fundings_list'),
    path('ratings_list/', ratings_list, name='ratings_list'),
    path('reported_comments_list/', reported_comments_list, name='reported_comments_list'),
    path('reported_projects_list/', reported_projects_list, name='reported_projects_list'),
    
]
