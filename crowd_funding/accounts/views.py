from django.views.generic.edit import  CreateView
from django.urls import reverse_lazy
from .forms import AccountForm
from .models import UserProfile

# create new user ?
class AccountCreateView(CreateView):
    form_class = AccountForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('activation.required')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # login(self.request, self.object)
        return response
    
