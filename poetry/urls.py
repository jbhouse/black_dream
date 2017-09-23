from django.conf.urls import url
from . import views

app_name = 'poems'

urlpatterns = [
    url(r'^all/$',views.PoemList.as_view(),name='list'),
    url(r'^view/(?P<pk>\d+)/$',views.PoemDetail.as_view(),name='detail'),
]
