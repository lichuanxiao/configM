from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^systemconfig', views.systemconfig, name='systemconfig'),
    url(r'^editsystemconfig/([0-9]+)/$',views.editsystemconfig, name='editsystemconfig'),
    url(r'^delsystemconfig/([0-9]+)/$',views.delsystemconfig, name='delsystemconfig'),
    url(r'^addsystemconfig',views.addsystemconfig, name='addsystemconfig'),
    url(r'^repo', views.repo, name='repo'),
    url(r'^addrepo', views.addrepo, name='addrepo'),
    url(r'^searchrepo', views.searchrepo, name='searchrepo'),  
    url(r'^importrepo', views.importrepo, name='importrepo'),
]