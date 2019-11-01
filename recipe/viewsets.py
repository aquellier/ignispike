from rest_framework import viewsets
from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework.decorators import action

from .models import Recipe
from .serializers import RecipeSerializer
# from .serializers import RecipePicSerializer
import pdb

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    # pdb.set_trace()
    # @action(
    #     detail=True,
    #     methods=['PUT'],
    #     serializer_class=RecipePicSerializer,
    #     parser_classes=[parsers.MultiPartParser],
    # )
    # def picture(self, request, pk):
    #     obj = self.get_object()
    #     serializer = self.serializer_class(obj, data=request.data,
    #                                        partial=True)
    #     pdb.set_trace()
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data, status=200)
    #     return response.Response(serializer.errors,
    #                              status.HTTP_400_BAD_REQUEST)
