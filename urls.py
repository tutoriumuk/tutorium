from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import password_reset, password_reset_done, password_change, password_change_done
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('tutorium.freezer.freezer_url')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.urls')),
	#url(r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
	#url(r'^account/register/$', 'django_test.views.register_user'),
	#url(r'^account/register_success/$', 'django_test.views.register_success'),
)

urlpatterns += patterns('',
  (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
  (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
  (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
  (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
  (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)

#from django.contrib.restful_model_views.restful_urls import get_restful_patterns
#urlpatterns += get_restful_patterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


# url(r'^$', 'tutorium.views.home', name='home'),
    # url(r'^tutorium/', include('tutorium.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#)
