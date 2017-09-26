from django.conf.urls import url
from . import views

app_name = 'events'

urlpatterns = [
    url(r'^all/$',views.EventList.as_view(),name='list'),
    url(r'^view/(?P<pk>\d+)/$',views.EventDetail.as_view(),name='detail'),
]
