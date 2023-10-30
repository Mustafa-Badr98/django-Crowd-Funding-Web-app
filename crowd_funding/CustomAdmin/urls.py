
from django.urls import include
from django.urls import path
from CustomAdmin.views import custom_admin_dashboard,admin_projects,admin_categories,admin_Rating,admin_Comments,admin_ReportedProjects
from CustomAdmin.views import admin_ReportedComments,admin_funds,admin_users,admin_EditUser,admin_CreateUser,admin_SearchUser,admin_SortUsers
from CustomAdmin.views import admin_DeleteUser,admin_CreateCategory,admin_EditCategory,admin_DeleteCategory
from CustomAdmin.views import admin_CreateProject,admin_EditProject,admin_DeleteProject
from CustomAdmin.views import admin_CreateRate,admin_EditRate,admin_DeleteRate

urlpatterns = [
    
    path('custom-admin/dashboard/', custom_admin_dashboard, name='custom_admin_dashboard'),
    
    
    path('custom-admin/users/', admin_users, name='custom_admin_users'),
    path('custom-admin/create_user/', admin_CreateUser, name='custom_admin_user_create'),
    path('custom-admin/edit_user/<int:id>', admin_EditUser, name='custom_admin_user_edit'),
    path('custom-admin/delete_user/<int:id>', admin_DeleteUser, name='custom_admin_user_delete'),
    path('custom-admin/search_user/', admin_SearchUser, name='custom_admin_user_search'),
    path('custom-admin/sort_user/', admin_SortUsers, name='custom_admin_user_sort'),
    
    
    path('custom-admin/categories/', admin_categories, name='custom_admin_categories'),
    path('custom-admin/create_categories/', admin_CreateCategory, name='custom_admin_categories_create'),
    path('custom-admin/edit_categories/<int:id>', admin_EditCategory, name='custom_admin_categories_edit'),
    path('custom-admin/delete_categories/<int:id>', admin_DeleteCategory, name='custom_admin_categories_delete'),


    path('custom-admin/projects/', admin_projects, name='custom_admin_projects'),
    path('custom-admin/create_project/', admin_CreateProject, name='custom_admin_project_create'),
    path('custom-admin/edit_project/<int:id>', admin_EditProject, name='custom_admin_project_edit'),
    path('custom-admin/delete_project/<int:id>', admin_DeleteProject, name='custom_admin_project_delete'),


    path('custom-admin/rates/', admin_Rating, name='custom_admin_rates'),
    path('custom-admin/create_rate/', admin_CreateRate, name='custom_admin_rate_create'),
    path('custom-admin/edit_rate/<int:id>', admin_EditRate, name='custom_admin_rate_edit'),
    path('custom-admin/delete_rate/<int:id>', admin_DeleteRate, name='custom_admin_rate_delete'),

    
    path('custom-admin/comments/', admin_Comments, name='custom_admin_comments'),
    path('custom-admin/reported_comments/', admin_ReportedComments, name='custom_admin_reported_comments'),
    path('custom-admin/reported_projects/', admin_ReportedProjects, name='custom_admin_reported_projects'),
    path('custom-admin/funds/', admin_funds, name='custom_admin_funds'),
   
   
]



