from cgitb import lookup
from django.shortcuts import render
from rest_framework import generics, mixins,authentication
from .serializers import ProductSerializer
from . import serializers
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
 


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

    def get(self,request, *args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content= "COol stuffs"


product_listMixin_view = ProductMixinView.as_view()




class ProductCreateView(generics.CreateAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     def perform_create(self, serializer):
         instance = serializer.save()
         if instance.content is None:
             instance.content= instance.title

product_create_view = ProductCreateView.as_view()

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailView.as_view()


class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 
product_list_create_view = ProductListCreateView.as_view()

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateView.as_view()

class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    look_up = 'pk'
    
    def perform_destroy(self,instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyView.as_view()








# @api_view(['GET', 'POST'])
# def product_alt_view(request,pk=None, *args,**kwargs):
#     method = request.method
#     if method == 'GET': 
#         if pk is not None:
#             qs = get_object_or_404(Product, pk =pk)
#             data = ProductSerializer(qs, many=False).data
#             return Response(data)
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many= True).data
#             return Response(data)

#     if method == 'POST':
#         serializer = ProductSerializer(data= request.data)
#         if serializer.is_valid():
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None: 
#                 content= title
#             serializer.save(content=content)
#             return Response(serializer.data)
    
#         else:
#             return Response(serializer.errors)
