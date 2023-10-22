from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Rating
from .forms import RatingForm ,ProjectForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from django.http import HttpResponseBadRequest,HttpResponseRedirect 
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import messages
from django_ratelimit.decorators import ratelimit
from django.urls import reverse 
from projects.models import Project, Comment, ReportedProject, ReportedComment ,Rating,Funding
from .forms import FundingForm,ReportCommentForm, ReportProjectForm,CommentForm
from django.http import Http404


def create_project(request):
   
    form=ProjectForm()
    if request.method == 'POST':
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
          


    return render(request, 'projects/create.html', {'form': form})



def edit_project(request,id):
    project=Project.get_specific_object(id=id)
    form=ProjectForm(instance=project)
    if request.method == 'POST':
        form=ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'projects/edit.html', {'form':form})
          


@login_required
def add_rating_view2(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        
        if 'submitRate' in request.POST:
            print(request.POST)
            rate_val=int(request.POST.get('stars'))
            rating = Rating()
            rating.user = request.user
            rating.project = project
            rating.rate_value=rate_val
            rating.save()
            project.add_rate(rating.rate_value)
        
        
        if 'editRate' in request.POST:
            print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            edited_rate=Rating.objects.get(user_id=request.user.id,project_id=project_id)
            old_rate=edited_rate.rate_value
            new_rate=int(request.POST.get('stars'))
            edited_rate.rate_value=new_rate
            edited_rate.save()
            project.edit_rate(new_rate,old_rate)
            # print(old_rate)
            # print(new_rate)
            # print(edited_rate.rate_value)
            
       
        url = reverse('projects.show',args=[project_id])
        return redirect(url, project_id=project_id)
        
    
    # return redirect('projectDetails.html', project_id=project_id)
        




@login_required
def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        
        print(request.POST)
        comment_val=request.POST.get('comment_text')
        comment = Comment()
        comment.user=request.user
        comment.project=project
        comment.comment_text=comment_val
        comment.save()
        
        url = reverse('projects.show',args=[project_id])
        return redirect(url, project_id=project_id)





def searchProject(request):
    searchedWord = request.GET.get('searchedWord', '')
    print(searchedWord)
    searchedProject = Project.objects.filter(title__icontains=searchedWord)
    return render(request, "proj/search_project_page.html", context={"projectsList": searchedProject, "searchedWord": searchedWord})





def ViewProject(request,id):  
    filteredProject = {}
    similar_projects = {}
    filteredRate={}
    
    try:
        filteredProject = Project.objects.get(id=id)
        similar_projects = Project.objects.filter(Category=filteredProject.Category).exclude(id=filteredProject.id)[:4]
        filteredRate=Rating.objects.get(user_id=request.user.id,project_id=filteredProject.id)
    
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    except Rating.DoesNotExist:
        filteredRate = None
        
    
    commentForm=CommentForm()
    return render(request, 'proj/projectDetails.html', context={"project": filteredProject,"comment_form":commentForm,"rate":filteredRate,'similarProjects':similar_projects})
 
 
 

@login_required
def report_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ReportProjectForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']

            # Create a ReportedProject instance
            reported_project = ReportedProject.objects.create(user=request.user, project=project, reason=reason)
            reported_project.save()

            messages.success(request, 'Project reported successfully.')
            return redirect('projects.show', project_id=project.id)
    else:
        form = ReportProjectForm()

    return render(request, 'proj/report_project.html', {'project': project, 'form': form})



@login_required
def report_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = ReportCommentForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']

            # Create a ReportedComment instance
            reported_comment = ReportedComment.objects.create(user=request.user, comment=comment, reason=reason)
            reported_comment.save()

            messages.success(request, 'Comment reported successfully.')
            return redirect('projects.show', project_id=comment.project.id)
    else:
        form = ReportCommentForm()

    return render(request, 'proj/report_comment.html', {'comment': comment, 'report_comment_form': form})







@login_required
def fund_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = FundingForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']

            # Create a funding record
            funding = Funding.objects.create(user=request.user, project=project, amount=amount)

            # Update the current_fund of the project
            project.current_fund += amount
            project.save()

            messages.success(request, f'Thank you for funding {project.title}!')
            return redirect('project_detail', project_id=project.id)
    else:
        form = FundingForm()

    return render(request, 'fund_project.html', {'project': project, 'form': form})
