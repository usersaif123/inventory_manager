from rest_framework import serializers
from .models import Item, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category._default_manager.all(), source='category', write_only=True
    )

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image', 'category', 'category_id']
