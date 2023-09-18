from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blogpost(models.Model):
    title = models.CharField(max_length=150, verbose_name='пост')
    slug = models.CharField(max_length=150, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blogpost/', verbose_name='превью (изображение)', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name="колличество просмотров")

    def __str__(self):
        return f'{self.title} {self.body}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('created_at',)