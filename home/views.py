from django.shortcuts import render
from django.views import View
from blog.models.article_models import Article


def home(request):
    artigos = Article.objects.filter(status=Article.PUBLISHED)

    return render(request, 'home/home.html', {'artigos': artigos})
