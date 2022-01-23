from rest_framework.serializers import ModelSerializer
from categories.serializer import CategorySerializer
from paragraphs.models import Paragraph
from .models import New

class ParagraphSerializer(ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'paragraph')

class NewSerializer(ModelSerializer):
    body = ParagraphSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = New
        fields = ('id', 'headline', 'lead', 'author', 'image', 'image_description', 'date', 'category', 'body')
