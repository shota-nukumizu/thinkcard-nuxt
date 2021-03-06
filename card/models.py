from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify 

class TagModel(models.Model):
    name = models.CharField('タグ名', max_length=255)
    color = models.CharField('背景色', max_length=7, default='#000000')

    def __str__(self):
        return self.name

class ArticleModel(models.Model):
    title = models.CharField('タイトル', max_length=255)
    tag = models.ManyToManyField(TagModel, verbose_name='タグ')
    slug = models.SlugField('スラッグ', unique=True)
    main_text = MarkdownxField('本文')
    created_at = models.DateField('作成日', auto_now=True)

    class Color(models.TextChoices):
        WHITE = '#ffffff', '白'
        BLACK = '#000000', '黒'
    
    color = models.CharField(
        '文字色',
        max_length=7,
        choices=Color.choices,
        default='#ffffff'
    )

    def convert_markdown_to_html(self):
        return markdownify(self.main_text)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title