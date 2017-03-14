from django.conf.urls import url

from .views import drop, index

urlpatterns = [
    url(r'^drop/$', drop),
    url(r'^$', index),
]
