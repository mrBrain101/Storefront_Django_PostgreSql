from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Count, Sum
from ..store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.
def say_hello(request) -> HttpResponse:
    queryset = Product.objects.all()
    
    return render(request, 'hello.html', 
                  {'name' : 'Django',
                   'product': queryset})