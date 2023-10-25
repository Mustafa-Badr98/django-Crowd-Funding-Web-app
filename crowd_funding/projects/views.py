from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Rating, Category
from .forms import ProjectForm
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import messages
from django_ratelimit.decorators import ratelimit
from django.urls import reverse
from projects.models import Project, Comment, ReportedProject, ReportedComment, Rating, Funding, Category
from .forms import ReportCommentForm, ReportProjectForm, CommentForm
from django.http import Http404


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.tag1='NEW'
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'projects/create.html', {'form': form})


def edit_project(request, id):
    project = Project.get_specific_object(id=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            url = reverse('projects.show', args=[id])
            return redirect(url)

    return render(request, 'projects/edit.html', {'form': form})


@login_required
def cancel_project(request, id):
    project = get_object_or_404(Project, id=id)
    fund_percentage = project.total_target * .25
    if request.method == 'POST':

        if project.current_fund < fund_percentage:
            if project.owner == request.user:
                project.delete()

    if project.current_fund >= fund_percentage:
        return render(request, 'projects/failure_cancel.html', {'project': project})

    return render(request, 'projects/cancel.html', {'project': project})


@login_required
def add_rating_view2(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':

        if 'submitRate' in request.POST:
            print(request.POST)
            rate_val = int(request.POST.get('stars'))
            rating = Rating()
            rating.user = request.user
            rating.project = project
            rating.rate_value = rate_val
            rating.save()
            project.add_rate(rating.rate_value)

        if 'editRate' in request.POST:
            print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            edited_rate = Rating.objects.get(user_id=request.user.id, project_id=project_id)
            old_rate = edited_rate.rate_value
            new_rate = int(request.POST.get('stars'))
            edited_rate.rate_value = new_rate
            edited_rate.save()
            project.edit_rate(new_rate, old_rate)
            # print(old_rate)
            # print(new_rate)
            # print(edited_rate.rate_value)

        url = reverse('projects.show', args=[project_id])
        return redirect(url, project_id=project_id)

    # return redirect('projectDetails.html', project_id=project_id)


@login_required
def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        print(request.POST)
        comment_val = request.POST.get('comment_text')
        comment = Comment()
        comment.user = request.user
        comment.project = project
        comment.comment_text = comment_val
        comment.save()

        url = reverse('projects.show', args=[project_id])
        return redirect(url, project_id=project_id)


def searchProject(request):
    searchedWord = request.GET.get('searchedWord', '')
    print(searchedWord)
    searchedProject = Project.objects.filter(title__icontains=searchedWord)
    return render(request, "proj/search_project_page.html",
                  context={"projectsList": searchedProject, "searchedWord": searchedWord})


def ViewProject(request, id):
    filteredProject = {}
    similar_projects = {}
    filteredRate = {}

    try:
        filteredProject = Project.objects.get(id=id)
        # similar_projects = Project.objects.filter(Category=filteredProject.Category).exclude(id=filteredProject.id)[:4]

        tags = [filteredProject.tag1, filteredProject.tag2, filteredProject.tag3, filteredProject.tag4]
        similar_projects = Project.objects.filter(
            Q(tag1__in=tags) | Q(tag2__in=tags) | Q(tag3__in=tags) | Q(tag4__in=tags)
        ).exclude(id=filteredProject.id).order_by('?')[:4]

        filteredRate = Rating.objects.get(user_id=request.user.id, project_id=filteredProject.id)


    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    except Rating.DoesNotExist:
        filteredRate = None

    commentForm = CommentForm()

    return render(request, 'proj/projectDetails.html', context={"project": filteredProject,
                                                                "comment_form": commentForm,
                                                                "rate": filteredRate,
                                                                'similarProjects': similar_projects,
                                                                })


class CategoryProjectsListView(ListView):
    model = Project
    template_name = 'proj/project_list_by_category.html'
    context_object_name = 'projects'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Project.objects.filter(Category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = get_object_or_404(Category, id=category_id)
        return context


@login_required
def report_project(request, id):
    project = get_object_or_404(Project, id=id)
    form = ReportProjectForm()

    if request.method == 'POST':
        form = ReportProjectForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.project = project
            report.user = request.user
            report.save()
            url = reverse('projects.show', args=[id])
            return redirect(url)

    return render(request, 'proj/report_project.html', {'form': form, 'project': project})


@login_required
def report_comment(request, comment_id, project_id):
    project = get_object_or_404(Project, id=project_id)
    comment = get_object_or_404(Comment, id=comment_id)
    form = ReportCommentForm()

    if request.method == 'POST':
        form = ReportCommentForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.project = project
            report.comment = comment
            report.user = request.user
            report.save()
            url = reverse('projects.show', args=[project_id])
            return redirect(url)

    return render(request, 'proj/report_comment.html', {'form': form, 'comment': comment})


@login_required
def fund_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        amount = int(request.POST.get('funds'))
        print(amount)

        funding = Funding.objects.create(user=request.user, project=project, amount=amount)

        project.current_fund += amount
        project.save()

        messages.success(request, f'Thank you for funding {project.title}!')
        url = reverse('projects.show', args=[project_id])
        return redirect(url, project_id=project_id)
