from django.shortcuts import redirect, reverse, render
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import  CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
# from django.db.models.query_utils import Q
# from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .forms import AccountForm, SetPasswordForm, PasswordResetForm
from .models import UserProfile




def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    print(account_activation_token.check_token(user, token))

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('registration_success')



def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    
    message = render_to_string("registration/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')



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

        activateEmail(self.request, user, form.cleaned_data.get('email'))
        return response
    


class ActivationRequiredView(TemplateView):
    template_name = 'registration/success.html'



class ActivationSuccessView(TemplateView):
    template_name = 'registration/activation_success.html'



class ActivationFailureView(TemplateView):
    template_name = 'registration/activation_failure.html'



def profile(request):
    url= reverse('profile_view')
    return  redirect(url)


# Decorator to ensure the user is logged in
class LoginRequiredMixin:
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile_view'

    def get_object(self, queryset=None):
        return self.request.user



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'accounts/profile_form.html'
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'image']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile_view')



class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('accounts.register')

    def get_object(self, queryset=None):
        return self.request.user




@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'accounts/password_change_confirm.html', {'form': form})