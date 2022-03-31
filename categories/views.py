from rest_framework.decorators import api_view, permission_classes
from .models import Category
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serialized = CategorySerializer(categories, many=True)
    return Response(status=status.HTTP_200_OK, data=serialized.data)
