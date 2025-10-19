from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from apps.store.admin import ProductAdmin
from apps.store.models import Product
from apps.tags.models import TaggedItem

# Register your models here.
class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)