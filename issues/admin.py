from issues.models import Issue, State, City, Photo
from django.contrib import admin

class IssueAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public', 'enable_comments', 'latitude', 'longitude')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('issue', 'name', 'photo_thumb', 'is_public')

admin.site.register(Issue, IssueAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Photo, PhotoAdmin)
