from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^appointment/(?P<number>\d+)$', views.addAppointment),
    url(r'^appointment/update$', views.updateAppointment),
    url(r'^/appointment/delete/(?P<trip_id>\d+)$', views.deleteAppointment),
    url(r'^add$', views.addAppointment),
]