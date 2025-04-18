from django.http import HttpResponse

def index(request, tags, article_id):
    return HttpResponse("Статья номер " + str(article_id) + ". Тег " + tags)