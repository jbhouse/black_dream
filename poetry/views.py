from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from replies.forms import ReplyForm
from django.views import generic
from poetry.models import Poem
from replies.models import Reply
# from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404,JsonResponse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class PoemList(generic.ListView):
    model = Poem
    template_name = 'poetry/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['poem_list'] = super().get_queryset().order_by('-created_at')
        print(context['poem_list'])
        return context

class PoemDisplay(generic.DetailView):
    model = Poem
    template_name = 'poetry/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PoemDisplay, self).get_context_data(**kwargs)
        poem = get_object_or_404(Poem, pk=self.kwargs['pk'])
        self.poem_replies = Poem.objects.prefetch_related("poem_replies").get(id=poem.pk)
        context['reply_form'] = ReplyForm()
        print(self.poem_replies)
        context['poem_replies'] = self.poem_replies.poem_replies.all().order_by('-created_at')
        return context

class PoemDetail(View):
    def get(self, request, *args, **kwargs):
        view = PoemDisplay.as_view()
        return view(request, *args, **kwargs)
