from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, EventRegistration
from .services.user_service import update_user_points

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create UserProfile when a new User is created."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=EventRegistration)
def award_registration_points(sender, instance, created, **kwargs):
    """Award points when user registers for an event."""
    if created:
        update_user_points(instance.user, 10)