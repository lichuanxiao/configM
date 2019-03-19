from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^systemconfig', views.systemconfig),
    url(r'^editsystemconfig',views.editsystemconfig),
    url(r'^addsystemconfig',views.addsystemconfig),
]