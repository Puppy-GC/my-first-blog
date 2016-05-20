from django.shortcuts import render
from django.utils import timezone
from .models import Post
import steam_api
channelname ={'channel': 'etozhemad'}
data_from_stream = steam_api.data_twitch['stream']
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data = data_from_stream
    return render(request, 'blog/post_list.html', {'data': data})

# def twitch(requsest):
#     data = {'data': 'etozhemad'}
#     return render(request, 'blog/post_list.html', {'data', data} )