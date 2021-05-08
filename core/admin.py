from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):

    date_hierarchy = 'date_joined'
    ordering = ['-date_joined']
    list_display = list(DjangoUserAdmin.list_display) + ['date_joined']


@admin.register(models.Post)
class PostsAdmin(admin.ModelAdmin):

    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_display = ['caption', 'user', 'created_at']
    search_fields = ['caption', 'user__username']
