# Generated by Django 3.2.9 on 2022-06-15 14:31

import backend.apps.accounts.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.SmallIntegerField(choices=[(0, 'Учитель'), (1, 'Студент')], default=1, verbose_name='Роль')),
                ('pin', models.CharField(max_length=15, unique=True, verbose_name='ПИН')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='teachers_images/', verbose_name='Фото')),
                ('is_active', models.BooleanField(default=False, verbose_name='Работает')),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='Телефон')),
                ('birthday', models.DateField(null=True, verbose_name='День рождения')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', backend.apps.accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_phone', models.CharField(max_length=10, verbose_name='Телефон родителя')),
            ],
            options={
                'verbose_name': 'Профиль ученика',
                'verbose_name_plural': 'Профили учеников',
            },
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('director', 'директор'), ('head_foster', 'завуч по воспитательной работе'), ('head_education', 'завуч по учебной части'), ('teacher', 'преподаватель'), ('other', 'другое')], default='other', max_length=30, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Профиль преподавателя',
                'verbose_name_plural': 'Профили преподавателей',
            },
        ),
    ]
