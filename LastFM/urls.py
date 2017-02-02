from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LastFM.views.home', name='home'),
    # url(r'^LastFM/', include('LastFM.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'principal.views.index', name="index"),
    url(r'^cargar/$', 'principal.views.cargar', name = "cargar"),
    url(r'^escuchas/$', 'principal.views.escuchas', name = "escuchas"),
    url(r'^recomendaciones/$', 'principal.views.recomendaciones', name = "recomendaciones"),
)
