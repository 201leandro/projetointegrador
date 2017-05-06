from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home_capim, name="home_capim"),
    url(r'^sobre$', sobre_capim, name="sobre_capim"),
    url(r'^lista$', lista_capim, name="lista_capim"),
    url(r'^capim/(?P<id>\d+)$', item_capim, name="item_capim"),
]
