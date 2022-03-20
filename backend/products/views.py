from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from . import serializers
from .models import Product

class ProductCreateView(generics.CreateAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

product_create_view = ProductCreateView.as_view()

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailView.as_view()