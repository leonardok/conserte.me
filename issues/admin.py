from issues.models import Issue
from django.contrib import admin

class IssueAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'latitude', 'longitude')

admin.site.register(Issue, IssueAdmin)
