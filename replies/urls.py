from django.conf.urls import url
from . import views

app_name = 'replies'

urlpatterns = [
    url(r'^create/$',views.CreateReply,name='create'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteReply,name='delete'),
]
