from django.db import models
from news.models import News

class Paragraph(models.Model):
    paragraph = models.TextField()
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='body')
    
    def __str__(self):
        return self.paragraph
