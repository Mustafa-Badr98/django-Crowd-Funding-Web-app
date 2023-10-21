
from django.urls import include
from django.urls import path
from accounts.views import profile, AccountCreateView
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', AccountCreateView.as_view(), name='accounts.register'),
   
]
