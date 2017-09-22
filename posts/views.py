from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden
# from replies.forms import ReplyForm
from django.views import generic
from posts.models import Post
from replies.models import Reply
from braces.views import SelectRelatedMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404,JsonResponse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = super().get_queryset().order_by('-created_at')
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
