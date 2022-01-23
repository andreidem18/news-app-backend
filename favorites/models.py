from django.db import models
from news.models import New
from users.models import User

class Favorite(models.Model):
    new = models.ForeignKey(New, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='favorites')
    rate = models.IntegerField()

    def __str__(self):
        return self.user
