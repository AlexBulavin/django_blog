from django.contrib import admin
from blog.models import ArticleModel

# Register your models here.
#admin.site.register(ArticleModel)

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date')