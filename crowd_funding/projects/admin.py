from django.contrib import admin

# Register your models here.
from projects.models import Project,Category,Rating

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Rating)