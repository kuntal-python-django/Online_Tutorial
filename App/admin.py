from django.contrib import admin
from django.contrib.auth.models import Group
from django.forms import Textarea
from .models import *

class CoursesUpdatedAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'id': 'project_update_textarea'})}
    }

class Courses_Custom(admin.ModelAdmin):
    search_fields = ['title','tag']
    list_display = ['id', 'title', 'tag']
    exclude = ['impression', 'created_at']
    ordering = ('id',)


admin.site.unregister(Group)
admin.site.register(Courses, Courses_Custom)
admin.site.register(Comments)
admin.site.register(Screenshots)
admin.site.register(CoverPhoto)
admin.site.register(ContactUs)
admin.site.register(Subscriber)
admin.site.register(BaseCMS)
admin.site.register(HomeCMS)
admin.site.register(Portfolio)
admin.site.register(CourseCMS)


