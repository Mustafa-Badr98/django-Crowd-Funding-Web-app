from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import uuid
from .phonevalid import phone_validator



from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True, validators=[phone_validator])
    image = models.ImageField(blank=True, null=True)
    activation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    activation_token_created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)


    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='customuser_set',  # Change this line
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
            Permission,
            verbose_name=_('user permissions'),
            blank=True,
            help_text=_('Specific permissions for this user.'),
            related_name='customuser_set',  # Change this line
            related_query_name='user',
        )

    def get_image_url(self):
        return f'/media/{self.image}'


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True)
    username= models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, blank=True, null=True, validators=[phone_validator])
    image = models.ImageField(upload_to='accounts/images/', blank=True, null=True)
    activation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    activation_token_created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def get_image_url(self):
        return f'/media/{self.image}'

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




