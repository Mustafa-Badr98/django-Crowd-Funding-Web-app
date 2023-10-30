from django.shortcuts import render

from accounts.models import CustomUser
from projects.models import Project,Category,Rating,Comment,ReportedProject,ReportedComment,Funding
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from CustomAdmin.forms import UserForm,CategoryForm,ProjectForm

@login_required
def custom_admin_dashboard(request):
    if not request.user.is_admin:
        
        return render(request, 'error.html', {'message': 'You do not have permission to access this page.'})
   
    return render(request, 'custom_admin/dashboard.html')



@login_required
def admin_users(request):
    users=CustomUser.get_all_objects()
    return render(request, 'custom_admin/users/admin_users.html',context={'users': users})




@login_required
def admin_projects(request):
    projects=Project.get_all_objects()
    return render(request, 'custom_admin/projects/admin_projects.html',context={'projects': projects})

@login_required
def admin_categories(request):
    categories=Category.get_all_objects()
    return render(request, 'custom_admin/categories/admin_categories.html',context={'categories': categories})



@login_required
def admin_Rating(request):
    rates=Rating.get_all_objects()
    return render(request, 'custom_admin/projects/admin_rates.html',context={'rates': rates})

@login_required
def admin_Comments(request):
    comments=Comment.get_all_objects()
    return render(request, 'custom_admin/projects/admin_comments.html',context={'comments': comments})


@login_required
def admin_ReportedProjects(request):
    reportedProjects=ReportedProject.get_all_objects()
    return render(request, 'custom_admin/projects/admin_reported_projects.html',context={'reportedProjects': reportedProjects})

@login_required
def admin_ReportedComments(request):
    reportedComments=ReportedComment.get_all_objects()
    return render(request, 'custom_admin/projects/admin_reported_comments.html',context={'reportedComments': reportedComments})

@login_required
def admin_funds(request):
    funds=Funding.get_all_objects()
    return render(request, 'custom_admin/projects/admin_funds.html',context={'funds': funds})


@login_required
def admin_CreateUser(request): 
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,)
        if form.is_valid(): 
            
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user = form.save()  
            return redirect('custom_admin_users')  
    else:
        form = UserForm()
    return render(request, 'custom_admin/users/admin_user_create.html',context={'form': form})



@login_required
def admin_EditUser(request,id):
    user=CustomUser.objects.get(id = id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user = form.save()    
            return redirect('custom_admin_users')  
    else:
        form = UserForm(instance=user)
    
    return render(request, 'custom_admin/users/admin_user_edit.html',context={'form': form})



@login_required
def admin_DeleteUser(request,id):
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        
        user.delete()
        return redirect('custom_admin_users') 

    return render(request, 'custom_admin/users/admin_user_delete.html')









@login_required
def admin_CreateCategory(request): 
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid(): 
            
            category = form.save()  
            return redirect('custom_admin_categories')  
    else:
        form = CategoryForm()
    return render(request, 'custom_admin/categories/admin_category_create.html',context={'form': form})



@login_required
def admin_EditCategory(request,id):
    category=Category.objects.get(id = id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
        
            category = form.save()    
            return redirect('custom_admin_categories')  
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'custom_admin/categories/admin_category_edit.html',context={'form': form})



@login_required
def admin_DeleteCategory(request,id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        
        category.delete()
        return redirect('custom_admin_categories') 

    return render(request, 'custom_admin/categories/admin_category_delete.html')











@login_required
def admin_CreateProject(request): 
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid(): 
            
            project = form.save()  
            return redirect('custom_admin_projects')  
    else:
        form = ProjectForm()
    return render(request, 'custom_admin/projects/admin_project_create.html',context={'form': form})



@login_required
def admin_EditProject(request,id):
    project=Project.objects.get(id = id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
        
            project = form.save()    
            return redirect('custom_admin_projects')  
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'custom_admin/projects/admin_project_edit.html',context={'form': form})



@login_required
def admin_DeleteProject(request,id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        
        project.delete()
        return redirect('custom_admin_projects') 

    return render(request, 'custom_admin/projects/admin_project_delete.html')




