from django.conf.urls import url

from . views import home, produto, categoria

urlpatterns = [
    url(r'^$', home),
    url(r'^produto/(?P<id>\d+)/$', produto, name='produto'),
    url(r'^categoria/(?P<id>\d+)/$', categoria, name='categoria'),
]