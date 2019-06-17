from django.shortcuts import render
from django.utils import timezone
from.models import Post


def education(request):
    return render(request,'blog/Educational.html')

def main(request):
    return render(request, 'blog/huh.html')

def login(request):
    return render(request, 'blog/log.html')

def gallery1(request):
    return render(request, 'blog/gallery1.html')

def artist(request):
    return render(request, 'blog/Artists.html')

def styleh(request):
    return render(request, 'blog/styleh.html')

def nova(request):
    return render(request, 'blog/nova.html')

def markers(request):
    return render(request, 'blog/marker.html')

def acryl(request):
    return render(request, 'blog/acr.html')

def wc(request):
    return render(request, 'blog/akva.html')

def graphics(request):
    return render(request, 'blog/graph.html')
