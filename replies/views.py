from django.shortcuts import render
from django.http import Http404,JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
from django.views import generic
from . import models
from replies.models import Reply
from posts.models import Post
from poetry.models import Poem
from videos.models import Video

# Create your views here.
def CreateReply(request):
    if request.method == "POST":
        response_data = {}
        if request.user.is_authenticated():
            sender = request.user
            replyId = request.POST.get('replyId')
        if request.POST.get('replyto') == 'post':
            post = get_object_or_404(Post, pk=replyId)
            new_reply = Reply.objects.create_post_reply(sender,post)
        elif request.POST.get('replyto') == 'poem':
            poem = get_object_or_404(Poem, pk=replyId)
            new_reply = Reply.objects.create_poem_reply(sender,poem)
        elif request.POST.get('replyto') == 'video':
            video = get_object_or_404(Video, pk=replyId)
            new_reply = Reply.objects.create_video_reply(sender,video)            
        text = request.POST.get('reply')
        new_reply.text = text
        new_reply.save()
        response_data['replyId'] = replyId
        response_data['sender_id'] = sender.pk
        response_data['text'] = new_reply.text
        response_data['id'] = new_reply.pk
        response_data['username'] = new_reply.user.username
        return JsonResponse(response_data)

def DeleteReply(request, **kwargs):
    response_data = {}
    reply = get_object_or_404(Reply, pk=kwargs['pk'])
    reply.delete()
    response_data['id'] = kwargs['pk']
    return JsonResponse(response_data)
