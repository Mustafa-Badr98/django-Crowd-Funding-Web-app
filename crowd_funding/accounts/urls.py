from django.urls import include
from django.urls import path
from accounts.views import AccountCreateView, ProfileDetailView, ProfileUpdateView, ProfileDeleteView,ActivationSuccessView, ActivationFailureView, ActivationRequiredView, profile, activate, password_change, password_reset_request, passwordResetConfirm
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', AccountCreateView.as_view(), name='accounts.register'),
    path('register/success', ActivationRequiredView.as_view(), name='activation.required'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('activation/success/', ActivationSuccessView.as_view(), name='registration_success'),
    path('activation/failure/', ActivationFailureView.as_view(), name='registration_failure'),
    path('profile/', profile, name='accounts.profile'),
    path('profile/view/', ProfileDetailView.as_view(), name='profile_view'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path("password/change", password_change, name="password_change"),
    path("password_reset", password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', passwordResetConfirm, name='password_reset_confirm'),

]
