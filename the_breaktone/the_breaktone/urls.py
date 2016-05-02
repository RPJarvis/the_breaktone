from django.conf.urls import include, url
from django.contrib import admin
from the_breaktone_main import views

urlpatterns = [
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
]
