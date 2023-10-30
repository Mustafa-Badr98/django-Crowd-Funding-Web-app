from django.shortcuts import render, redirect, get_object_or_404
from admin_dashboard.forms import UserChangeForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import user_passes_test
from accounts.models import UserProfile, CustomUser
from django.views.generic.edit import  CreateView
from django.urls import reverse_lazy



def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin)
def admin_home(request):
    total_users = CustomUser.objects.all().count()
    counts = {
        'total_users': total_users,
    }
    return render(request, 'admin_dashboard/admin_home.html', counts)


@user_passes_test(is_admin)
def users_list(request):
    total_users = CustomUser.objects.all().count()
    users = CustomUser.objects.all()
    return render(request, 'admin_dashboard/users/users_list.html', context={'users': users, 'total_users': total_users})

class AccountCreateView(CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return response
    

@user_passes_test(is_admin)
def user_edit(request, id):
    user_to_edit = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, request.FILES, instance=user_to_edit)
        if user_form.is_valid():
            user_form.save()
            return redirect('users_list')
    else:
        user_form = UserChangeForm(instance=user_to_edit)
    return render(request, 'admin_dashboard/users/user_edit.html', context={'user_form': user_form})


@user_passes_test(is_admin)
def user_delete(request, id):
    user_to_delete = get_object_or_404(CustomUser, id=id)
    if user_to_delete == request.user:
        return redirect('users_list')
    elif request.method == 'POST':
        user_to_delete.delete()
        return redirect('users_list')
    return render(request, 'admin_dashboard/users/user_delete.html')
