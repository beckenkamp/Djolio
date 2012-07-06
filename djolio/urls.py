from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'djolio.views.404_handler'

from djolio.portfolio.models import Project
info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = patterns('',

    url(r'^$', 'django.views.generic.simple.redirect_to', {'url':'/work/'}, name='home'),
    url(r'^work/$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name="portfolio/projects_list.html"), name='work'),
    url(r'^work/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(info_dict, slug_field='slug'), name='work_detail'),

    #Teste para os templates de erro
    #url(r'^404testing/$', direct_to_template, {'template': '404.html'}),
    #url(r'^500testing/$', direct_to_template, {'template': '500.html'}),


    # Examples:
    # url(r'^$', 'djolio.views.home', name='home'),
    # url(r'^djolio/', include('djolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
