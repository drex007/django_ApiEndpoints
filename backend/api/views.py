from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request, *args,**kwargs):
#     data= request.data
#     instance= Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#         # data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price 
#     # return JsonResponse(data)
#     return Response(data)

@api_view(['POST'])
def api_home(request, *args,**kwargs):
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)

    else:
         return Response(serializer.errors)