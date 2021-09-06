from django.shortcuts import render

from .models import Post


def index(request):
    a = 1
    latest = Post.objects.order_by('-pub_date')[:10]
    # That's correct way to use render func
    return render(request, "index.html", {"posts": latest}) 
    