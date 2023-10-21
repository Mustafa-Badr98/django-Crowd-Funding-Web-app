from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Rating
from .forms import RatingForm ,ProjectForm



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



