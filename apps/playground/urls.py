from django.urls import path
from . import views

#URLConf - url config for an app
urlpatterns = [
    path('hello/', views.say_hello),
]