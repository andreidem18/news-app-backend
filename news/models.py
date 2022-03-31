from django.db import models
from categories.models import Category

class News(models.Model):
    headline = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    lead = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    image = models.TextField()
    image_description = models.TextField()

    def __str__(self):
        return self.headline
