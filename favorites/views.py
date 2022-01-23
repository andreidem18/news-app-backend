from django.shortcuts import render
from rest_framework.decorators import api_view
from favorites.models import Favorite
from favorites.serializer import FavoriteSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.serializers import ModelSerializer

@api_view(['GET'])
def get_favorites(request):
    user = request.user
    serialized = FavoriteSerializer(user.favorites, many=True)
    return Response(status=status.HTTP_200_OK, data=serialized.data)

@api_view(['DELETE'])
def remove_favorite(request, id):
    Favorite.objects.get(id=id).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class RateSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('rate',)

@swagger_auto_schema(methods=['put'], request_body=RateSerializer)
@api_view(['PUT'])
def change_rate(request, id):
    favorite = Favorite.objects.get(id=id)
    favorite.rate = request.data['rate']
    favorite.save()
    serialized = FavoriteSerializer(favorite)
    return Response(status=status.HTTP_200_OK, data=serialized.data)
