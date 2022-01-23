from rest_framework.serializers import ModelSerializer
from news.serializer import NewSerializer
from .models import Favorite

class FavoriteSerializer(ModelSerializer):
    new = NewSerializer(read_only=True)
    class Meta:
        model = Favorite
        fields = ('id', 'rate', 'new')
