from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from datetime import datetime
from blog.models import ArticleModel
from django.utils import timezone
from blog.forms import ArticleForm


# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse('Welcome to my blog!')

    def post(self, request):
        return HttpResponse('[POST] Posted blog!')


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, 'articles.html', {'articles': articles, 'forms': ArticleForm()})

    def post(self, request):
        # title = request.POST['title'] #Должно соответствовать атрибуту name кажого объекта
        # category = request.POST['category']
        # author = request.POST['author']
        # content = request.POST['content']
        form = ArticleForm(request.POST)  # Тот же результат, что и в предыдущих строках.
        form.instance.creation_date = datetime.now(tz=timezone.utc)
        form.save()
        # ArticleModel.objects.create(title=title, category=category, author=author, content=content, creation_date=datetime.now(tz=timezone.utc))

        return redirect('/blog/articles')


class ArticleDetails(View):
    def get(self, request, id):
        try:
            article_detail = ArticleModel.objects.get(id=id)
            return render(request, 'article_details.html', {'article': article_detail})

        except ArticleModel.DoesNotExist:
            return HttpResponseNotFound()


