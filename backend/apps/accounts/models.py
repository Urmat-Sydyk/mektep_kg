from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.apps.lessons.models import Subject, Group


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, pin, password, **extra_fields):
        if not pin:
            raise ValueError('The given PIN must be set')
        self.pin = pin
        user = self.model(pin=pin, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    



class Teachers(AbstractUser):
    pin = models.BigIntegerField('ПИН', max_length=15)
    first_name = models.CharField('Фамилия', max_length=150, blank=True)
    middle_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Отчество', max_length=100, blank=True)
    avatar = models.ImageField('Фото', upload_to='teachers_images/', null=True, blank=True)
    is_active = models.BooleanField('Работает', default=False)
    POSITION_DIRECTOR = "director"
    POSITION_HEAD_FOSTER = "head_foster"
    POSITION_HEAD_EDUCATION = "head_education"
    POSITION_TEACHER = "teacher"
    POSITION_OTHER = "other"
    POSITION_STATUS = (
        (POSITION_DIRECTOR, "директор"),
        (POSITION_HEAD_FOSTER, "завуч по воспитательной работе"),
        (POSITION_HEAD_EDUCATION, "завуч по учебной части"),
        (POSITION_TEACHER, "преподаватель"),
        (POSITION_OTHER, "другое"),
    )
    position = models.CharField("Должность", max_length=30, choices=POSITION_STATUS, default=POSITION_OTHER)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='teachers')
    phone = models.IntegerField("Телефон", max_length=10)
    birthday = models.DateField("День рождения", blank=True)
    address = models.CharField("Адрес", max_length=250)


class Students(models.Model):
    pin = models.BigIntegerField('ПИН', max_length=15)
    first_name = models.CharField('Фамилия', max_length=150, blank=True)
    middle_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Отчество', max_length=100, blank=True)
    avatar = models.ImageField('Фото', upload_to='teachers_images/', null=True, blank=True)
    is_active = models.BooleanField('Работает', default=False)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="students")
    phone = models.IntegerField("Телефон ученика", max_length=10)
    birthday = models.DateField("День рождения", blank=True)
    address = models.CharField("Адрес", max_length=250)
    parent_phone = models.IntegerField("Телефон родителя", max_length=10)


