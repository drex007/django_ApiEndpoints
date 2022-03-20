from rest_framework import serializers
from dataclasses import fields
from django import forms
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['id','title', 'content', 
        'price','sale_price', 'my_discount']
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            None