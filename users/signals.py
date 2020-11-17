from django.db.models.signals import post_save  # emet un signal qd on save un objet
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# qd un User est créer ( avec post_save) on appelle le fonction create profile qui créer un profile avec
# l'instance user créer avant
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
