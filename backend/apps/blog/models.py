from django.db import models
from apps.users.models import User

# News
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    image = models.FileField(upload_to='news_images/', verbose_name='Картинка', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Название', null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.text[0:10]}...'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'