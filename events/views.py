from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404,JsonResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from events.models import Event
from posts.models import Post
# Create your views here.
class EventList(generic.ListView):
    model = Event
    template_name = 'events/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['event_list'] = super().get_queryset().order_by('-created_at')
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        return context

class EventDisplay(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_context_data(self, **kwargs):
        context = super(EventDisplay, self).get_context_data(**kwargs)
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        return context

class EventDetail(View):
    def get(self, request, *args, **kwargs):
        view = EventDisplay.as_view()
        return view(request, *args, **kwargs)
