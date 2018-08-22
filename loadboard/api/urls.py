from django.conf.urls import include, url
from django.urls import path

from . import views
from .v1.urls import urlpatterns as v1_urls

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^v1/', include(v1_urls)),
]
