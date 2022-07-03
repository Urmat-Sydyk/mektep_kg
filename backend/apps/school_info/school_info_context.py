from backend.apps.school_info.models import SchoolInfo, SocialLink


def get_school_info_context(request):
    school_info = SchoolInfo.objects.get(id=1)
    socials = SocialLink.objects.all()
    context = {
        'school_info': school_info,
        'socials': socials
    }
    return context
