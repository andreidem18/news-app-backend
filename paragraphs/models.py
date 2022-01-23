from django.db import models
from news.models import New

class Paragraph(models.Model):
    paragraph = models.TextField()
    new = models.ForeignKey(New, on_delete=models.SET_NULL, null=True, related_name='body')
    
    def __str__(self):
        return self.paragraph
