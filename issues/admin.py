from issues.models import Issue, State, City
from django.contrib import admin

class IssueAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'latitude', 'longitude')

admin.site.register(Issue, IssueAdmin)
admin.site.register(State)
admin.site.register(City)
