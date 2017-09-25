"""black_dream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from home.views import HomeView,Contact
from photo_gallery.views import PhotoList

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^photos/$', PhotoList.as_view(), name='photos'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^videos/',include('videos.urls',namespace='videos')),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^poems/',include('poetry.urls',namespace='poems')),
    url(r'^replies/',include('replies.urls',namespace='replies')),
]
