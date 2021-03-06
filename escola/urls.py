from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from escola import views


urlpatterns = [
    url(r'^api/classes/$',views.ClasseList.as_view()),
    url(r'^api/classes/(?P<pk>[0-9]+)/$', views.ClasseView.as_view()),
    url(r'^api/classes/create/$', views.ClasseCreate.as_view()),

    url(r'^api/componentes/$',views.ComponenteList.as_view()),
    url(r'^api/componentes/(?P<pk>[0-9]+)/$', views.ComponenteView.as_view()),
    url(r'^api/componentes/create/$', views.ComponenteCreate.as_view()),

    url(r'^api/departamentos/$',views.DepartamentoList.as_view()),
    url(r'^api/departamentos/(?P<pk>[0-9]+)/$', views.DepartamentoView.as_view()),
    url(r'^api/departamentos/create/$', views.DepartamentoCreate.as_view()),

    url(r'^api/cadernetas/$',views.CadernetaList.as_view()),
    url(r'^api/cadernetas/(?P<pk>[0-9]+)/$', views.CadernetaView.as_view()),
    url(r'^api/cadernetas/create/$', views.CadernetaCreate.as_view()),

    url(r'^classes/$', views.ClasseViewHTML.as_view(), name='classes'),
    url(r'^classes/(?P<pk>[0-9]+)/$', views.ClasseDetail.as_view(), name='classe-detail'),

    url(r'^departamentos/$', views.DepartamentoViewHTML.as_view(), name='departamentos'),

    url(r'^professores/$', views.ProfessorViewHTML.as_view(), name='professores'),
    url(r'^alunos/$', views.AlunoViewHTML.as_view(), name='alunos'),
    url(r'^componentes/(?P<pk>[0-9]+)/$', views.ComponenteDetail.as_view(), name='componente-detail'),
    url(r'^componentes/novo/$', views.ComponenteNew.as_view(), name='componente_new'),
    url(r'^classes/novo/$', views.ClasseNew.as_view(), name='classe_new'),
    url(r'^cadernetas/$', views.CadernetaViewHTML.as_view(), name='cadernetas'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
