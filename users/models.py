from django.db import models
from django.contrib.auth.models import User


# one to one relation  user has 1 profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='pics')

    def __str__(self):
        return f'{self.user.username} Profile'
