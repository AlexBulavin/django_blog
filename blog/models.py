from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    #Создали мета класс для отображения заголовков элементов БД в пользовательской форме
    class Meta:
        ordering = ('creation_date',)
        verbose_name = ('Article title')
        verbose_name_plural = ('Article titles')

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField()

#Делаем отображение элементов (заголовков постов) в админке БД нативным, как назвал пользователь, а не в виде индексов БД
    def __str__(self):
        return self.title
