from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # many to one relation use foreign key

    def __str__(self):
        return self.title


def initData():
    user1 = User.objects.first()
    post_2 = Post(title='My doudou is the best',
                  content='Mon petit chéri grandit je l\'aime fort ce petit foufou', author=user1)
    post_2.save()
    #user1.post_set.create(title='blog 4',content='suite à suivre')



