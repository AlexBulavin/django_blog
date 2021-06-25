from django.forms import ModelForm
from .models import ArticleModel

class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ["title", "category", "author", "content"]
        # exclude = ["creation_date"] #Та же запись, что и fields = ["title", "category", "author", "content"] То есть исключаем из списка не нужный элемент, а все остальные будут включены.
