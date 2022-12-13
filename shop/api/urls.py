from django.urls import path
from .views import *


urlpatterns = [
    path('products/', index, name="index"),
    path('products/<int:id>/', detail, name="detail"),
]
