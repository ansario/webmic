from django.conf.urls import include, url


urlpatterns = [
    # Examples:
    url(r'^$', 'microscope.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
