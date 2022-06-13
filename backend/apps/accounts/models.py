from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.apps.lessons.models import Subject, StudentGroup


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, pin=None, password=None, **extra_fields):
        if not pin:
            raise ValueError('The given PIN must be set')
        user = self.model(pin=pin, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pin, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(pin, password, **extra_fields)



# if user.role == User.ROLE_STUDENT:

class User(AbstractUser):
    ROLE_TEACHER = 0
    ROLE_STUDENT = 1
    ROLES = (
        (ROLE_TEACHER, "Учитель"),
        (ROLE_STUDENT, "Студент"),
    )
    username = None
    role = models.SmallIntegerField("Роль", choices=ROLES, default=ROLE_STUDENT)
    pin = models.CharField('ПИН', max_length=15, unique=True)
    email = models.EmailField("Email")
    first_name = models.CharField('Фамилия', max_length=150, blank=True)
    middle_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Отчество', max_length=100, blank=True)
    avatar = models.ImageField('Фото', upload_to='teachers_images/', null=True, blank=True)
    is_active = models.BooleanField('Работает', default=False)
    phone = models.CharField("Телефон", max_length=10, null=True)
    birthday = models.DateField("День рождения", null=True)
    address = models.CharField("Адрес", max_length=250, null=True)

    USERNAME_FIELD = 'pin'
    REQUIRED_FIELDS = []

    objects = UserManager()


class TeacherProfile(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    position = models.CharField("Должность", max_length=30, choices=POSITION_STATUS, default=POSITION_OTHER)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='teachers')


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    student_group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT, related_name="students", null=True)
    parent_phone = models.CharField("Телефон родителя", max_length=10)
