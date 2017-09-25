from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.urls import reverse
from replies.forms import ReplyForm
from django.views import generic
from videos.models import Video
from posts.models import Post
from replies.models import Reply
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404,JsonResponse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class PodCastList(generic.ListView):
    model = Video
    template_name = 'videos/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        media_list = super().get_queryset().order_by('-created_at')
        video_list = []
        for x in media_list:
            if(x.is_video == False):
                video_list.append(x)
        context['video_list'] = video_list
        return context

class VideoList(generic.ListView):
    model = Video
    template_name = 'videos/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        media_list = super().get_queryset().order_by('-created_at')
        video_list = []
        for x in media_list:
            if(x.is_video == True):
                video_list.append(x)
        context['video_list'] = video_list
        return context

class VideoDisplay(generic.DetailView):
    model = Video
    template_name = 'videos/detail.html'
    def get_context_data(self, **kwargs):
        context = super(VideoDisplay, self).get_context_data(**kwargs)
        video = get_object_or_404(Video, pk=self.kwargs['pk'])
        self.video_replies = Video.objects.prefetch_related("video_replies").get(id=video.pk)
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        context['reply_form'] = ReplyForm()
        context['video_replies'] = self.video_replies.video_replies.all().order_by('-created_at')
        return context

class VideoDetail(View):
    def get(self, request, *args, **kwargs):
        view = VideoDisplay.as_view()
        return view(request, *args, **kwargs)
