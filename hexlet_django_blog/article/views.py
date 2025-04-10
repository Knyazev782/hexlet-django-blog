from django.shortcuts import render

def index(request):
    return render(request, 'articles/articles.html', context={
        'app_name': 'article',
    })