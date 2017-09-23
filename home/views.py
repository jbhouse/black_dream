from django.shortcuts import render
from django.views import generic
from posts.models import Post


class HomeView(generic.TemplateView):
    template_name = "home/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        self.posts = Post.objects.all().order_by('-created_at')
        context['posts'] = self.posts[:2]
        return context

class Contact(generic.TemplateView):
    template_name = "home/contact.html"
