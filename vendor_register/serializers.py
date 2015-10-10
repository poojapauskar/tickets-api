from rest_framework import serializers
import random
from random import randint
from vendor_register.models import Vendor_register, LANGUAGE_CHOICES, STYLE_CHOICES


class Vendor_registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_register
        fields = ('pk', 'firstname', 'lastname','email','phone','vendor_id')    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        # vendor_id = validated_data.pop('vendor_id')
        # barcode_string = validated_data.pop('barcode_string')
        # price = validated_data.pop('price')
        
        return Vendor_register.objects.create(**validated_data) 
    

