from django.contrib import admin

from .models import Learning, Tag


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


class LearningAdmin(admin.ModelAdmin):
    list_display = ['learning_title', 'status']
    ordering = ['learning_title']
    actions = [make_published]

admin.site.register(Learning, LearningAdmin)
admin.site.register(Tag)
