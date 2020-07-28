from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def post_list(request):
    # return render(request, 'notebook/index.html', {})
    return render(request, 'notebook/post_list.html', {})
