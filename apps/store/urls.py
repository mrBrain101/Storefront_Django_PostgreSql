from django.urls import path
from . import views

#URLConf - url config for an app
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail')
]