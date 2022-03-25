from rest_framework import serializers
from products import validators

class UserInLineSerializer(serializers.Serializer):
   url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field = 'pk', read_only=True) #You can also use this instead of the get_url fxn 
   title = serializers.CharField(validators = [validators.validate_title, validators.unique_product_title]) #Remobe this if you dont wanna use the validator.py file 


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only = True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        user = obj
        my_products = user.product_set.all()
        return UserInLineSerializer(my_products, many=True, context=self.context).data