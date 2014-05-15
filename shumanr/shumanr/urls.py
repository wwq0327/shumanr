from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

## media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
## urlpatterns += patterns('',
##         (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
##             {
##                 'document_root': settings.MEDIA_ROOT,
##                 }),
## )
