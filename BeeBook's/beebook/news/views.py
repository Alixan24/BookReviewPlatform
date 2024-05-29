from django.shortcuts import render # type: ignore
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, "news/news_home.html", {'news' :news})
