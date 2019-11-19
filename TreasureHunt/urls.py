
from django.conf.urls import url
from . import api

urlpatterns = [
    # url('', api.index),
    url('rooms', api.rooms)
]
