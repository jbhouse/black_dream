from django.shortcuts import render
from posts.models import Post
from photo_gallery.models import Photo
from django.views import generic

# Create your views here.
class PhotoList(generic.ListView):
    model = Photo
    template_name = 'photo_gallery/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        self.photos = Photo.objects.all().order_by('-created_at')
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        context['photo_list'] = super().get_queryset().order_by('-created_at')
        return context
