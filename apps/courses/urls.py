from django.conf.urls import url
from . import views      
     # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^courses/destroy/(?P<number>\d+)$', views.destroy),
    url(r'^courses/(?P<number>\d+)/delete$', views.delete)

  ]