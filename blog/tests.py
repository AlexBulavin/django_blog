from django.test import TestCase
from blog.models import ArticleModel
from django.utils import timezone
from datetime import datetime

# Create your tests here.
class ArticleTest(TestCase):
    def test_article_created_success(self):
        #Записываем тестовую статью в БД
        ArticleModel.objects.create(title='Test article', category='Test category', author='Test Author', content='Test Content', creation_date=datetime.now(tz=timezone.utc))
        #Извлекаем тестовую статью из БД
        article = ArticleModel.objects.get(title='Test article')
        #Сравниваем извлечённые данные с ожидаемыми
        self.assertEqual(article.category, 'Test category')
        self.assertEqual(article.author, 'Test Author')
        self.assertEqual(article.content, 'Test Content')


class BlogPagesTest(TestCase):
    def test_home_page_content(self):
        res = self.client.get('/blog/')
        self.assertEqual(res.content, b'Welcome to my blog!') #Добавили b перед 'Welcome to my blog!' потому, что со страницы home.html
        #получаем байты, а не строку.
