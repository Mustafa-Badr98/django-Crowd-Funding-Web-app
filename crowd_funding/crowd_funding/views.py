from django.views.generic import TemplateView
from projects.models import Project,Rating,Category


class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['all_projects'] = Project.objects.all()[:10]
        context['latest_projects'] = Project.objects.order_by('-created_at')[:5]
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:5]
        context['hightest_rated_projects'] = Project.objects.order_by('-average_rate')[:5]
        context['categories']=Category.objects.all()
       
        
        

        return context  


    
