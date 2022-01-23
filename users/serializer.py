from rest_framework.serializers import ModelSerializer
from favorites.serializer import FavoriteSerializer
from .models import User

class UserSerializer(ModelSerializer):
    favorites = FavoriteSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'favorites')
        
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
