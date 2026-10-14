from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def article(request):
    return render(request, 'blog/article.html')
