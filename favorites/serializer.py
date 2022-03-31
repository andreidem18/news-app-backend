from rest_framework.serializers import ModelSerializer
from news.serializer import NewsSerializer
from .models import Favorite

class FavoriteSerializer(ModelSerializer):
    news = NewsSerializer(read_only=True)
    class Meta:
        model = Favorite
        fields = ('id', 'rate', 'news')
