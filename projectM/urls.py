from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^project', views.project, name="project"),
    url(r'^addproject', views.addproject, name="addproject"),
    
]