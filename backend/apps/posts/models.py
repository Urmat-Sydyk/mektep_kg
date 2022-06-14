from django.db import models

# Create your models here.
from backend.apps.accounts.models import User
from backend.apps.lessons.models import StudentGroup


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', limit_choices_to={'role': False})
    group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT, verbose_name='Класс')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
