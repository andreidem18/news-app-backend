from django.db import models
from news.models import News
from users.models import User

class Favorite(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='favorites')
    rate = models.IntegerField()

    def __str__(self):
        return self.user
