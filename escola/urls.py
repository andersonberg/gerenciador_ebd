from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from escola import views


urlpatterns = [
    url(r'^classes/$',views.ClasseList.as_view()),
    url(r'^classe/(?P<pk>[0-9]+)/$', views.ClasseRetrieve.as_view()),
    url(r'^classe/create/$', views.ClasseCreate.as_view()),
    url(r'^classe/update/(?P<pk>[0-9]+)/$', views.ClasseUpdate.as_view()),
    url(r'^classe/delete/(?P<pk>[0-9]+)/$', views.ClasseDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
