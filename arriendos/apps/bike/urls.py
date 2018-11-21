from django.conf.urls import url

from apps.bike.views import index_bike

urlpatterns = [
    url(r'^index$', index_bike)
]