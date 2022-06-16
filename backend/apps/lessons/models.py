
from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class StudentGroup(models.Model):
    name = models.CharField(max_length=10, verbose_name='Класс')
    teacher = models.ForeignKey('accounts.User', on_delete=models.PROTECT, verbose_name='Преподаватель', limit_choices_to={'role': False})

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.name


class RoomNumber(models.Model):
    name = models.CharField(max_length=15, verbose_name='Номер кабинета')

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self):
        return self.name


class ShiftNumber(models.Model):
    name = models.CharField(max_length=100, verbose_name='Смена')

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return self.name


class LessonTime(models.Model):
    number = models.CharField(verbose_name='Номер Урока', max_length=20)
    shift = models.ForeignKey(
        ShiftNumber,
        verbose_name='Смена',
        on_delete=models.CASCADE
    )
    start = models.TimeField(verbose_name='Начало урока')
    end = models.TimeField(verbose_name='Конец урока')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.start} - {self.end}'


class TimeTable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет', related_name='subject_time')
    student_group = models.ForeignKey(
        StudentGroup,
        on_delete=models.CASCADE,
        verbose_name='Класс'
    )
    teacher = models.ForeignKey(
        'accounts.User',
        on_delete=models.PROTECT,
        verbose_name='Преподаватель',
        limit_choices_to={'role': False}
    )
    WEEKS_MONDAY = '1'
    WEEKS_TUESDAY = '2'
    WEEKS_WEDNESDAY = '3'
    WEEKS_THURSDAY = '4'
    WEEKS_FRIDAY = '5'
    WEEKS_SATURDAY = '6'
    WEEKS = (
        (WEEKS_MONDAY, 'Понедельник'),
        (WEEKS_TUESDAY, 'Вторник'),
        (WEEKS_WEDNESDAY, 'Среда'),
        (WEEKS_THURSDAY, 'Четверг'),
        (WEEKS_FRIDAY, 'Пятница'),
        (WEEKS_SATURDAY, 'Суббота')
    )
    weeks = models.CharField('День недели', max_length=30, choices=WEEKS, default=WEEKS_MONDAY)
    room = models.ForeignKey(RoomNumber, on_delete=models.PROTECT, verbose_name='Кабинет')
    lesson = models.ForeignKey(LessonTime, on_delete=models.CASCADE, verbose_name='Номер урока', related_name='lesson_time')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return self.weeks


class Grade(models.Model):
    value = models.FloatField(max_length=5, verbose_name='Оценка')
    student = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        limit_choices_to={'role': True},
        verbose_name='Ученик',
        related_name='student_grade'
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    grade_date = models.DateField(verbose_name='Дата')
    teacher = models.ForeignKey(
        'accounts.User',
        on_delete=models.PROTECT,
        verbose_name='Преподаватель',
        limit_choices_to={'role': False},
        related_name='teacher_grade'
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


