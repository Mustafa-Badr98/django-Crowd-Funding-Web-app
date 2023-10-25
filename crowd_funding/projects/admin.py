from django.contrib import admin
from .models import Category, Project, Rating, Comment, ReportedProject, ReportedComment, Funding



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'Category', 'owner', 'total_target',
        'current_fund', 'num_of_ratings', 'total_rate', 'average_rate',
        'is_featured', 'start_date', 'end_date', 'created_at', 'updated_at'
    )
    search_fields = ('title', 'details', 'owner__email', 'Category__name')
    ordering = ('-created_at',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'rate_value')
    search_fields = ('user__email', 'project__title')
    ordering = ('-project__created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'comment_text')
    search_fields = ('user__email', 'project__title')
    ordering = ('-project__created_at',)


@admin.register(ReportedProject)
class ReportedProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'reason')
    search_fields = ('user__email', 'project__title')
    ordering = ('-project__created_at',)

@admin.register(ReportedComment)
class ReportedCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'reason')
    search_fields = ('user__email', 'comment__project__title')
    ordering = ('-comment__project__created_at',)


@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'amount', 'transaction_date')
    search_fields = ('user__email', 'project__title')
    ordering = ('-project__created_at',)
