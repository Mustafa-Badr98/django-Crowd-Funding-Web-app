from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import  CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from .forms import AccountForm
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
