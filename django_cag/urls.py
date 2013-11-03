from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_cag.views.home', name='home'),
    # url(r'^django_cag/', include('django_cag.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'geocode.views.index'),
    url(r'^contact/$', 'mysite.views.contact'),

    url(r'^search/', 'geocode.views.search'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calculate_route/','geocode.views.calculate_route')
)
