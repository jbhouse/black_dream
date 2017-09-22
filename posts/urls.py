from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^all/$',views.PostList.as_view(),name='list'),
    url(r'^view/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='detail'),
]
