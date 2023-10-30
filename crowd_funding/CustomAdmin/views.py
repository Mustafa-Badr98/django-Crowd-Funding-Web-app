from django.shortcuts import render

from accounts.models import CustomUser
from projects.models import Project,Category,Rating,Comment,ReportedProject,ReportedComment,Funding
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from CustomAdmin.forms import UserForm,CategoryForm

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
    category = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        
        category.delete()
        return redirect('custom_admin_categories') 

    return render(request, 'custom_admin/categories/admin_category_delete.html')







# def is_admin(user):
#     return user.is_staff


# @user_passes_test(is_admin)
# def admin_home(request):
#     return render(request, 'custom_admin/admin_home.html')


# def categories_list(request):
#     categories = Category.objects.all()
#     return render(request, 'custom_admin/categories_list.html', context={'categories': categories})


# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'custom_admin/tags_list.html', context={'tags': tags})


# def category_create(request):
#     category_form = CategoryForm(request.POST, request.FILES)
#     if request.method == "POST":
#         if category_form.is_valid():
#             category_form.save()
#             return redirect('categories_list')
#     return render(request, 'custom_admin/category_create.html', context={'category_form': category_form})


# def tag_create(request):
#     tag_form = TagForm(request.POST, request.FILES)
#     if request.method == "POST":
#         if tag_form.is_valid():
#             tag_form.save()
#             return redirect('tags_list')
#     return render(request, 'custom_admin/tag_create.html', context={'tag_form': tag_form})


# def category_edit(request, id):
#     category_to_edit = get_object_or_404(Category, id=id)
#     if request.method == 'POST':
#         category_form = CategoryForm(
#             request.POST, request.FILES, instance=category_to_edit)
#         if category_form.is_valid():
#             category_form.save()
#             return redirect('categories_list')
#     else:
#         category_form = CategoryForm(instance=category_to_edit)
#     return render(request, 'custom_admin/category_edit.html', context={'category_form': category_form})


# def category_delete(request, id):
#     category_to_delete = get_object_or_404(Category, id=id)
#     if request.method == 'POST':
#         category_to_delete.delete()
#         return redirect('categories_list')
#     return render(request, 'custom_admin/category_delete.html')


# def tag_edit(request, id):
#     tag_to_edit = get_object_or_404(Tag, id=id)
#     if request.method == 'POST':
#         tag_form = TagForm(request.POST, request.FILES, instance=tag_to_edit)
#         if tag_form.is_valid():
#             tag_form.save()
#             return redirect('tags_list')
#     else:
#         tag_form = TagForm(instance=tag_to_edit)
#     return render(request, 'custom_admin/tag_edit.html', context={'tag_form': tag_form})


# def tag_delete(request, id):
#     tag_to_delete = get_object_or_404(Tag, id=id)
#     if request.method == 'POST':
#         tag_to_delete.delete()
#         return redirect('tags_list')
#     return render(request, 'custom_admin/tag_delete.html')


# @user_passes_test(is_admin)
# def donation(request):
#     donations = Donation.objects.all()
#     return render(request, 'custom_admin/donation.html', context={"donations": donations})


# @user_passes_test(is_admin)
# def edit_donation(request, pk):
#     donation = get_object_or_404(Donation, pk=pk)

#     if request.method == 'POST':
#         form = DonationForm(request.POST, instance=donation)
#         if form.is_valid():
#             form.save()
#             return redirect('donation')
#     else:
#         form = DonationForm(instance=donation)

#     return render(request, 'custom_admin/edit_donation.html', {'form': form})


# @user_passes_test(is_admin)
# def delete_donation(request, pk):
#     donation = get_object_or_404(Donation, pk=pk)

#     if request.method == 'POST':
#         donation.delete()
#         return redirect('donation')

#     return render(request, 'custom_admin/delete_donation.html', {'donation': donation})


# @user_passes_test(is_admin)
# def create_donation(request):
#     if request.method == 'POST':
#         form = DonationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('donation')
#     else:
#         form = DonationForm()

#     return render(request, 'custom_admin/create_donation.html', {'form': form})


# @user_passes_test(is_admin)
# def report(request):
#     reports = Report.objects.all()
#     return render(request, 'custom_admin/report.html', context={"reports": reports})


# @user_passes_test(is_admin)
# def edit_report(request, pk):
#     report = get_object_or_404(Report, pk=pk)

#     if request.method == 'POST':
#         form = ReportForm(request.POST, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('report')
#     else:
#         form = ReportForm(instance=report)

#     return render(request, 'custom_admin/edit_report.html', {'form': form})


# @user_passes_test(is_admin)
# def delete_report(request, pk):
#     report = get_object_or_404(Report, pk=pk)

#     if request.method == 'POST':
#         report.delete()
#         return redirect('report')

#     return render(request, 'custom_admin/delete_report.html', {'report': report})


# @user_passes_test(is_admin)
# def create_report(request):
#     if request.method == 'POST':
#         form = ReportForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('report')
#     else:
#         form = ReportForm()

#     return render(request, 'custom_admin/create_report.html', {'form': form})
