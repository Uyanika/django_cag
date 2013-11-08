from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:



from django.contrib import admin
admin.autodiscover()
import autocomplete_light
autocomplete_light.autodiscover()
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
    url(r'^calculate_route/','geocode.views.calculate_route'),
    url(r'^calculate_directions/','geocode.views.calculate_directions' ),
    url(r'calculate_route_directions/','geocode.views.calculate_route_directions'),
    url(r'merhaba/','geocode.views.merhaba'),
    url(r'ara/', 'geocode.views.ara'),
    url(r'^autocomplete/', include('autocomplete_light.urls'))

)
