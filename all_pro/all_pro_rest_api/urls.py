
from django.urls import include, path
from rest_framework import routers
from .viewSets.Products import ProductsViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)


urlpatterns = [
    # thsi helps to fetch the endpoints of the routers
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
