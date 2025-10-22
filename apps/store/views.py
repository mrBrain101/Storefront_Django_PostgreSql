from django.db.models import Count
from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product, Collection, OrderItem, Review
from .serializers import (ProductSerializer, CollectionSerializer, 
                          ReviewSerializer)
from .pagination import CustomPageNumberPagination


class CollectionViewSet(ModelViewSet):
    queryset = (Collection
                .objects
                .annotate(products_count=Count('products'))
                .all())
    serializer_class = CollectionSerializer
    
    def destroy(self, request : HttpRequest, *args, **kwargs) -> Response:
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({"error": ("Collection can't be deleted because "
                                       "it is associated with a product.")}, 
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        return super().destroy(request, *args, **kwargs)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'unit_price' : ['exact', 'gt', 'lt'], 
                        'collection' : ['exact']}
    ordering_fields = ['unit_price', 'last_update']
    pagination_class = CustomPageNumberPagination
    search_fields = ['title', 'description']


    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request : HttpRequest, *args, **kwargs) -> Response:
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({"error": ("Product can't be deleted because it"
                                       " is associated with an order item.")},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}