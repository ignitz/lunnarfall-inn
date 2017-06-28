from django.conf.urls import url, include
from . import views

app_name='lunnarfall'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
]
