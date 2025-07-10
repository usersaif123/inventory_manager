from codecs import ignore_errors
from rest_framework import viewsets
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # type: ignore
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()   # type: ignore
    serializer_class = CategorySerializer
