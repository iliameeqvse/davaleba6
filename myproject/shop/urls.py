from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_shop, name='hello_shop'),
]
