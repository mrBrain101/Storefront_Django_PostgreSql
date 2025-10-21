from typing import Any, List, Tuple
from django.contrib import admin, messages
from django.db.models import Model, QuerySet, Count
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    custom_filter_1 = '<10'
    custom_filter_1_val = 'Low'

    def lookups(self, 
                request : HttpRequest, 
                model_admin : admin.ModelAdmin) -> List[Tuple[Any, str]]:
        return [(self.custom_filter_1, self.custom_filter_1_val)]
    
    def queryset(self, 
                 request : HttpRequest, 
                 queryset : QuerySet) -> QuerySet:
        if self.value() == self.custom_filter_1:
            return queryset.filter(inventory__lt=10)


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection : Model) -> int:
        url = reverse('admin:store_product_changelist')
        url += '?'
        url += urlencode({'collection__id' : str(collection.id)})
        return format_html('<a href="{}">{} Products<a>', 
                           url,
                           collection.products_count)
        
    def get_queryset(self, request : HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug' : ['title']
    }
    search_fields = ['title']
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 
                    'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product : Model) -> str:
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product : Model) -> str:
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    @admin.action(description='Clear inventory')
    def clear_inventory(self, 
                        request : HttpRequest, 
                        queryset : QuerySet) -> None:
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated!',
            messages.SUCCESS
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    search_help_text = 'Search customer by name'

    @admin.display(ordering='orders_count')
    def orders(self, customer : Model) -> str:
        url = reverse('admin:store_order_changelist')
        url += '?'
        url += urlencode({'customer__id' : str(customer.id)})
        return format_html('<a href="{}">{} Orders<a>', 
                           url, 
                           customer.orders_count)

    def get_queryset(self, request : HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


class OrderItemInline(admin.TabularInline):
    min_num = 1
    autocomplete_fields = ['product']
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    ordering = ['customer__first_name', 'customer__last_name']


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'customer']