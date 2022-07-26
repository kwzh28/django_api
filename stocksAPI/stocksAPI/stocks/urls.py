from django.conf.urls import url

from . import views

urlpatterns = [
    url('stocks', views.index, name='index'),
]