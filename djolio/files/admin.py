from django.contrib import admin
from djolio.files.models import Files

class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')

admin.site.register(Files, FilesAdmin)

