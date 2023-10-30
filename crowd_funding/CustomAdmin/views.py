from django.shortcuts import render

from accounts.models import CustomUser
from projects.models import Project,Category,Rating,Comment,ReportedProject,ReportedComment,Funding
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from CustomAdmin.forms import UserForm,CategoryForm,ProjectForm,RateForm

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
    return render(request, 'custom_admin/rates/admin_rates.html',context={'rates': rates})

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
def admin_SearchUser(request):
   
    if request.method == 'POST':
        searched_word=request.POST.get('searched_word')
        search_field = request.POST.get('search_field', 'username') 
        print(searched_word)
        users = CustomUser.objects.all()
        
        

        if search_field == 'username':
            users = users.filter(username__icontains=searched_word)
        elif search_field == 'id':
            searchID=int(searched_word)
            users = users.filter(id=searchID)
        
        elif search_field == 'first_name':
            users = users.filter(first_name__icontains=searched_word)
        elif search_field == 'last_name':
            users = users.filter(last_name__icontains=searched_word)
        elif search_field == 'email':
            users = users.filter(email__icontains=searched_word)
       
        return render(request, 'custom_admin/users/admin_user_searched.html',context={'user_searched': users})

    return render(request, 'custom_admin/users/admin_users.html')


@login_required
def admin_SortUsers(request):
    

    if request.method == 'POST':
        sort_by=request.POST.get('sort_by')
        users_sorted=CustomUser.objects.all()

        if sort_by == 'username':
            users_sorted = CustomUser.objects.all().order_by('username')
        elif sort_by == 'is_active':
            users_sorted = CustomUser.objects.all().order_by('username')
        elif sort_by == 'id':
            users_sorted = CustomUser.objects.all().order_by('id')
        
        return render(request, 'custom_admin/users/admin_user_sorted.html',context={'user_sorted': users_sorted})
        

    return render(request, 'custom_admin/users/admin_users.html')





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
def admin_SearchCategory(request):
   
    if request.method == 'POST':
        searched_word=request.POST.get('searched_word')
        search_field = request.POST.get('search_field', 'id') 
        print(searched_word)
        category = Category.objects.all()

        if search_field == 'id':
            searchID=int(searched_word)
            category = category.filter(id=searchID)
        elif search_field == 'name':
            category = category.filter(name__icontains=searched_word)
        
       
        return render(request, 'custom_admin/categories/admin_categories_searched.html',context={'category_searched': category})

    return render(request, 'custom_admin/categories/admin_categories.html')







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




@login_required
def admin_SearchProjects(request):
   
    if request.method == 'POST':
        searched_word=request.POST.get('searched_word')
        search_field = request.POST.get('search_field', 'username') 
        
        
        projects=Project.objects.all()

        if search_field == 'title':
            projects = projects.filter(title__icontains=searched_word)
        elif search_field == 'id':
            searchID=int(searched_word)
            projects = projects.filter(id=searchID)
        
        elif search_field == 'Category':
            projects = projects.filter(Category__name__icontains=searched_word)
        elif search_field == 'owner':
            projects = projects.filter(owner__first_name__icontains=searched_word)
        elif search_field == 'average_rate':
            searchRate=int(searched_word)
            projects = projects.filter(average_rate=searchRate)
       
        return render(request, 'custom_admin/projects/admin_project_searched.html',context={'projects_searched': projects})

    return render(request, 'custom_admin/projects/admin_projects.html')


@login_required
def admin_SortProjects(request):
    
    if request.method == 'POST':
        sort_by=request.POST.get('sort_by')
        projects_sorted=Project.objects.all()

        if sort_by == 'title':
            projects_sorted = Project.objects.all().order_by('title')
        elif sort_by == 'Category':
            projects_sorted = Project.objects.all().order_by('Category')
        elif sort_by == 'id':
            projects_sorted = Project.objects.all().order_by('id')
        elif sort_by == 'average_rate_a':
            projects_sorted = Project.objects.all().order_by('average_rate')
        elif sort_by == 'average_rate_b':
            projects_sorted = Project.objects.all().order_by('-average_rate')    
        return render(request, 'custom_admin/projects/admin_project_sorted.html',context={'projects_sorted': projects_sorted})
        

    return render(request, 'custom_admin/projects/admin_projects.html')



















@login_required
def admin_CreateRate(request): 
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid(): 
            projectFromForm=form.cleaned_data['project']
            rateFromForm=form.cleaned_data['rate_value']
            project=Project.get_specific_object(id=projectFromForm.id)
            project.add_rate(rateFromForm)
            print("///////////////////////////////////")
            
            rate = form.save()  
            
            return redirect('custom_admin_rates')  
    else:
        form = RateForm()
    return render(request, 'custom_admin/rates/admin_rates_create.html',context={'form': form})



@login_required
def admin_EditRate(request,id):
    rate=Rating.objects.get(id = id)
    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            projectFromForm=form.cleaned_data['project']
            oldRate=projectFromForm.average_rate
            newRate=form.cleaned_data['rate_value']
            project=Project.get_specific_object(id=projectFromForm.id)
            project.edit_rate(newRate,oldRate)
            rate = form.save()    
            return redirect('custom_admin_rates')  
    else:
        form = RateForm(instance=rate)
    
    return render(request, 'custom_admin/rates/admin_rates_edit.html',context={'form': form})



@login_required
def admin_DeleteRate(request,id):
    rate = get_object_or_404(Rating, id=id)

    if request.method == 'POST':
        projectFromRate=rate.project
        
        oldRate=rate.rate_value
        project=Project.get_specific_object(id=projectFromRate.id)
        project.delete_rate(oldRate)
        
        rate.delete()
        return redirect('custom_admin_rates') 

    return render(request, 'custom_admin/rates/admin_rates_delete.html')






