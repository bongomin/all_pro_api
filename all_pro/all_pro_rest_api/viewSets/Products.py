from rest_framework import viewsets
from ..models.Products import ProductsModel
from ..serializers.Products import ProductsSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer



