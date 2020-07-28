from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # {} 템플릿을 사용하기 위해 매개변수를 추가
    # {'posts': posts}
    return render(request, 'notebook/post_list.html', {'posts': posts})
