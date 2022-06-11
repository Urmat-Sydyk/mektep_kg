from django.db.models.signals import post_save


from backend.apps.accounts.models import User
from django.dispatch import receiver

from .models import StudentProfile, TeacherProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.ROLE_TEACHER:
            TeacherProfile.objects.create(user=instance)
        else:
            StudentProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.role == User.ROLE_TEACHER:
        instance.teacherprofile.save()
    else:
        instance.studentprofile.save()

