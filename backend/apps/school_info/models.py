from django.db import models

# Create your models here.


class SchoolInfo(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    email = models.EmailField('Email')
    link = models.CharField(max_length=100, verbose_name='Ссылка')
    name = models.CharField(max_length=255, verbose_name='Название')
    slogan = models.CharField(max_length=255, verbose_name='Слоган')
    logo = models.ImageField('Лого', upload_to='school_info/')
    background_image = models.ImageField('Фон', upload_to='school_info/')
    work_time = models.CharField(max_length=255, verbose_name='Рабочее время')
    founded = models.DateField('Основан')
    about_us = models.TextField(verbose_name='О нас')
    our_history = models.TextField(verbose_name='Наша история')
    school_image = models.ImageField('Лого', upload_to='school_info/')

    class Meta:
        verbose_name = 'Информация о школе'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Названия')
    image = models.ImageField('Изображение', upload_to='courses/')
    price = models.CharField(verbose_name='Цена', max_length=10)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Названия')
    image = models.ImageField('Изображение', upload_to='services/')
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    title = models.CharField(max_length=255, verbose_name='Названия')
    icon = models.ImageField('Изображение', upload_to='icons/')
    link = models.CharField(max_length=100, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name='Названия')
    image = models.ImageField('Изображение', upload_to='gallery/')
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Галерея'

    def __str__(self):
        return self.title


class Message(models.Model):
    sender_name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField('Email')
    title = models.CharField(max_length=255, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст обращения')
    phone = models.CharField("Телефон", max_length=10, null=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return self.title
