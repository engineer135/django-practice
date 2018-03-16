from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request) :
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# urls.py에서 설정한 r'^post/(?P<pk>\d+)/$' <pk> 이 부분의 이름을 동일하게 사용해야 한다.
# 장고가 pk 변수에 모든 값을 넣어 뷰로 전송하겠다는 의미임.
def post_detail(request, pk) :
    #Post.objet.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})