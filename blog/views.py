from django.shortcuts import render, redirect
from .forms import GuestbookForm
from .models import GuestbookEntry

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def article(request):
    return render(request, 'blog/article.html')

def guestbook(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = GuestbookForm()
    
    entries = GuestbookEntry.objects.filter(is_verified=True)
    return render(request, 'blog/guestbook.html', {'form': form, 'entries': entries})
