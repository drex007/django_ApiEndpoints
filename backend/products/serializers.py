from wsgiref.validate import validator
from rest_framework import serializers
from dataclasses import fields
from django import forms
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer( source= 'user',read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field = 'pk', read_only=True) #You can also use this instead of the get_url fxn 
    # title = serializers.CharField(validators = [validators.validate_title, validators.unique_product_title]) #Remobe this if you dont wanna use the validator.py file 
    class Meta:
        model = Product
        fields = ['owner','url','id','title', 'content', 
        'price','sale_price', 'my_discount',]

     #validate_<fieldname>
    # def validate_title(self,value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exist as a product name")
    #     return value

    #Function to get objects url
    # def get_url(self,obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-detail" #View_name,kwargs = {'pk': obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            None