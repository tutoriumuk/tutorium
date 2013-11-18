from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^', include('mysite.freezer.freezer_url')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
