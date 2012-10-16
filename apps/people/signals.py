from django.conf import settings

def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a profile."""
    from people.models import Profile
    if created:
        Profile(user = instance).save()
