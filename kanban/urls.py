from django.conf.urls import url

from .views import drop, index, new_card

urlpatterns = [
    url(r'^new-card/$', new_card),
    url(r'^drop/$', drop),
    url(r'^$', index),
]
