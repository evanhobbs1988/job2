from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add_job$', views.add_job, name = 'add_job'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^delete_job$', views.delete_job, name = 'delete_job'),
    url(r'^delete_job2$', views.delete_job2, name = 'delete_job2')
]
