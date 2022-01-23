from rest_framework.decorators import api_view, permission_classes
from .serializer import NewSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import New
from rest_framework.serializers import ModelSerializer
from favorites.models import Favorite
from favorites.serializer import FavoriteSerializer



headline = openapi.Parameter('headline__icontains', openapi.IN_QUERY, description="filter by headline", type=openapi.TYPE_STRING)
category = openapi.Parameter('category', openapi.IN_QUERY, description="filter by category", type=openapi.TYPE_INTEGER)


@permission_classes([IsAuthenticated])
@swagger_auto_schema(methods=['get'], manual_parameters=[headline, category])
@api_view(['GET'])
def news(request):
    data = dict()
    if request.query_params:
        for k, v in request.query_params.items():
            print(k)
            data[k] = v
    news = New.objects.filter(**data)
    serialized = NewSerializer(news, many=True)
    return Response(status=status.HTTP_200_OK, data = serialized.data)


@api_view(['GET'])
def new_detail(request, id):
    new = New.objects.get(id=id)
    serialized = NewSerializer(new)
    return Response(status=status.HTTP_200_OK, data = serialized.data)


class AddToFavorite(ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('new', 'rate')


@swagger_auto_schema(methods=['post'], request_body=AddToFavorite)
@api_view(['POST'])
def add_to_favorite(request):
    user = request.user
    new = New.objects.get(id=request.data['new'])
    favorite = Favorite.objects.create(user=user, new=new, rate=request.data['rate'])
    serialized = FavoriteSerializer(favorite)
    return Response(status=status.HTTP_200_OK, data = serialized.data)
