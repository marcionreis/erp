from django.conf.urls import url

from . views import home, produto

urlpatterns = [
    url(r'^$', home),
    url(r'^produto/(?P<id>\d+)/$', produto, name='produto'),
]