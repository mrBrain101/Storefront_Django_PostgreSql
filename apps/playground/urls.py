from django.urls import path
from .views import HelloView

#URLConf - url config for an app

urlpatterns = [
    path('', HelloView.as_view(), name='hello'),
]