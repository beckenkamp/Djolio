from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from djolio.portfolio.models import Project

info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = patterns('',

    url(r'^work/$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name="portfolio/projects_list.html")),
    url(r'^work/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(info_dict, slug_field='slug')),

    # Examples:
    # url(r'^$', 'djolio.views.home', name='home'),
    # url(r'^djolio/', include('djolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
