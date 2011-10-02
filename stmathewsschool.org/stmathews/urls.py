from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'portal.views.index'),
    (r'^info/$', 'portal.views.info'),
    (r'^students/(?P<student_id>\d+)$', 'portal.views.students'),
    (r'^teachers/$', 'portal.views.teachers'),
    (r'^donate/$', 'portal.views.donate'),
    # Example:
    # (r'^stmatthews/', include('stmatthews.foo.urls')),
    
    #this is to serve static files
    #"""(r'^base/(?P<path>.*)$', 'django.views.static.serve',
    #{'document_root': '/home/david/Active/StMatthews/code/src/static'}),"""
                       
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
    
)
