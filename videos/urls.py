from django.conf.urls import url
from . import views

app_name = 'videos'

urlpatterns = [
    url(r'^all/$',views.VideoList.as_view(),name='list'),
    url(r'^view/(?P<pk>\d+)/$',views.VideoDetail.as_view(),name='detail'),
    url(r'^podcasts/$',views.PodCastList.as_view(),name='podcast_list'),
]
