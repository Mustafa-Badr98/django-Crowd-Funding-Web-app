from django.contrib import admin

# Register your models here.
from projects.models import Project,Category,Rating,Comment,ReportedProject,ReportedComment

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(ReportedComment)
admin.site.register(ReportedProject)