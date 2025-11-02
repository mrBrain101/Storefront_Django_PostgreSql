from django.urls import path
from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', 
                                              lookup='product')
products_router.register('reviews', views.ReviewViewSet, 
                         basename='product-reviews')

products_router.register('images', views.ProductImageViewSet, 
                         basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='carts-items')


def custom_api_root(request, format=None):
    return render(request, 'store/custom_root.html', {
        'endpoints': {
            'products': reverse('products-list', request=request, format=format),
            'collections': reverse('collection-list', request=request, format=format),
            'carts': reverse('cart-list', request=request, format=format),
            'customers': reverse('customer-list', request=request, format=format),
            'orders': reverse('orders-list', request=request, format=format)
        }
    })


urlpatterns = [path('', custom_api_root, name='custom-root')]
urlpatterns += router.urls + products_router.urls + carts_router.urls