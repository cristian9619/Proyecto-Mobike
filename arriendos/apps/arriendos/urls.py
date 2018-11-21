from django.conf.urls import url, include
from apps.arriendos.views import index

urlpatterns = [
    url(r'^Arriendo$', index),
]