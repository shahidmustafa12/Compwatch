from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from django.views.generic.simple import direct_to_template


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^login/$', 'compwatch.views.login_user'),
                       (r'^dashboard/$','compwatch.views.view_page'),
                       (r'^addnewcompany/$','compwatch.views.add_new'),
                       (r'^admin/(.*)', admin.site.root),
                       url (
        r'^$',
        direct_to_template,
        {'template': 'home.html'},
        name = 'home',
        ),
                       )

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                        )
   
                           
                       
