from django.contrib import admin
from djolio.portfolio.models import Project, Medium, Client

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Medium)
admin.site.register(Client)

