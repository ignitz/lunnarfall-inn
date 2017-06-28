from django.conf.urls import url
from . import views

app_name='pessoa'

urlpatterns = [
    url(r'^$', views.PessoaIndexView.as_view(), name='index'),
    url(r'^cliente/$', views.ClienteIndexView.as_view(), name='cliente_index'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetailView.as_view(), name='detail'),
    url(r'^funcionario/$', views.FuncionarioIndexView.as_view(), name='funcionario_index'),
    url(r'^funcionario/(?P<pk>[0-9]+)/$', views.FuncionarioDetailView.as_view(), name='detail'),
]
