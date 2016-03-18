from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'microscope.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^slide/(?P<pk>[0-9]+)/$', 'microscope.views.slide', name="slide"),
    url(r'^admin/', include(admin.site.urls)),
]
