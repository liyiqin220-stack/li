from django.shortcuts import render, redirect
from .forms import GuestbookForm
from .models import GuestbookEntry

# 作业3：博客页面
def index(request):
    return render(request, 'blog/index.html') # 如果你的首页不叫这个，请把名字改对

def about(request):
    return render(request, 'blog/about.html')

def article(request):
    return render(request, 'blog/article.html')

# 作业4：留言簿视图（包含老师要求的审核逻辑）
def guestbook(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = GuestbookForm()
    
    # 核心：只显示审核通过的留言
    entries = GuestbookEntry.objects.filter(is_verified=True)
    return render(request, 'blog/guestbook.html', {'form': form, 'entries': entries})
