from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from escola import views


urlpatterns = [
    url(r'^classes/$',views.ClasseList.as_view()),
    url(r'^classes/(?P<pk>[0-9]+)/$', views.ClasseView.as_view()),
    url(r'^classes/create/$', views.ClasseCreate.as_view()),

    url(r'^componentes/$',views.ComponenteList.as_view()),
    url(r'^componentes/(?P<pk>[0-9]+)/$', views.ComponenteView.as_view()),
    url(r'^componentes/create/$', views.ComponenteCreate.as_view()),

    url(r'^departamentos/$',views.DepartamentoList.as_view()),
    url(r'^departamentos/(?P<pk>[0-9]+)/$', views.DepartamentoView.as_view()),
    url(r'^departamentos/create/$', views.DepartamentoCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
