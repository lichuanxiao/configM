from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^systemconfig', views.createproject),
]