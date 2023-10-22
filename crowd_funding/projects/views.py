from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import messages
from django_ratelimit.decorators import ratelimit
from projects.models import Project, Comment, ReportedProject, ReportedComment ,Rating,Funding
from .forms import FundingForm



def create_project(request):
    pass



@login_required
def add_rating_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():

            rating = form.save(commit=False)
            rating.user = request.user
            rating.project = project
            rating.save()
            project.add_rate(rating.rate)

            return redirect('projects.show', project_id=project_id)
    else:
        form = RatingForm()

    return render(request, 'rate/add_rating.html', {'form': form, 'project': project})




def searchProject(request):
    searchedWord = request.GET.get('searchedWord', '')
    print(searchedWord)
    searchedProject = Project.objects.filter(title__icontains=searchedWord)
    return render(request, "proj/search_project_page.html", context={"projectsList": searchedProject, "searchedWord": searchedWord})





def ViewProject(request,id):  
    filteredProject = Project.objects.get(id=id)

    return render(request, 'proj/projectDetails.html', context={"project": filteredProject,})
 
 
 
@login_required
@ratelimit(key='user', rate='5/h', block=True)
def report_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.owner == request.user:
        raise PermissionDenied("You cannot report your own project.")

    if request.method == 'POST':
        reason = request.POST.get('reason', '')

        # Check if the user has already reported this project
        if ReportedProject.objects.filter(Q(user=request.user) & Q(project=project)).exists():
            return HttpResponseBadRequest("You have already reported this project.")

        ReportedProject.objects.create(user=request.user, project=project, reason=reason)

    return render(request, 'report_project.html', {'project': project})



@login_required
@ratelimit(key='user', rate='5/h', block=True)
def report_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author of the comment
    if comment.user == request.user:
        raise PermissionDenied("You cannot report your own comment.")

    if request.method == 'POST':
        reason = request.POST.get('reason', '')

        # Check if the user has already reported this comment
        if ReportedComment.objects.filter(Q(user=request.user) & Q(comment=comment)).exists():
            return HttpResponseBadRequest("You have already reported this comment.")

        ReportedComment.objects.create(user=request.user, comment=comment, reason=reason)

    return render(request, 'report_comment.html', {'comment': comment})







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