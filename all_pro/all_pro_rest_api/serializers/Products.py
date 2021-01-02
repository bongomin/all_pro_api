from rest_framework import serializers
from  ..models.Products import ProductsModel


class ProductsSerializer(serializers.Serializer):
    class Meta:
        model = ProductsModel
        fields = __all__
