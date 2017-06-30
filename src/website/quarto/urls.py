from django.conf.urls import url
from . import views

app_name='quarto'

urlpatterns = [
    url(r'^$', views.QuartoIndexView.as_view(), name='index'),
    url(r'^quarto/(?P<pk>[0-9]+)/$', views.QuartoDetailView.as_view(), name='quarto_detail')
]
