from django.urls import path
from admin_dashboard.views import admin_home, users_list, AccountCreateView, user_delete, user_edit, categories_list, projects_list

urlpatterns = [
    path('admin_home/', admin_home, name='admin_home'),
    path('users_list/', users_list, name='users_list'),
    path('user_create/', AccountCreateView.as_view(), name='user_create'),
    path('user_edit/<int:id>/', user_edit, name='user_edit'),
    path('user_delete/<int:id>/', user_delete, name='user_delete'),
    path('categories_list/', categories_list, name='categories_list'),
    path('projects_list/', projects_list, name='projects_list'),
    
]
