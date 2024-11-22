from django.contrib import admin
from .models import Task, GoogleOAuthSettings

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_date', 'updated_date')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('created_date', 'updated_date')

@admin.register(GoogleOAuthSettings)
class GoogleOAuthSettingsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'created_date', 'updated_date')