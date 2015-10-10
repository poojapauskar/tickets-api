from rest_framework import serializers
import random
from random import randint
from decode.models import Decode, LANGUAGE_CHOICES, STYLE_CHOICES
from barcode.models import Barcode, LANGUAGE_CHOICES, STYLE_CHOICES


class DecodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decode
        fields = ('barcode','ref_no','vendor_id','price')    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #Decode.objects.create(**validated_data)
        # vendor_id = validated_data.pop('vendor_id')
        # barcode_string = validated_data.pop('barcode_string')
        # price = validated_data.pop('price')
        
        #price= Barcode.objects.filter(barcode=validated_data.get(u'barcode'),ref_no=validated_data.get(u'ref_no')).values('price')
        #vendor_id= Barcode.objects.filter(barcode=validated_data.get(u'barcode'),ref_no=validated_data.get(u'ref_no')).values('vendor_id')

        if Barcode.objects.filter(barcode=validated_data.get(u'barcode'),ref_no=validated_data.get(u'ref_no')).exists():
            obj=Barcode.objects.get(barcode=validated_data.get(u'barcode'),ref_no=validated_data.get(u'ref_no'))
            return Decode.objects.create(barcode=validated_data.get(u'barcode'),ref_no=validated_data.get(u'ref_no'),vendor_id=obj.vendor_id,price=obj.price)
        #Decode.objects.filter(barcode=validated_data.get(u'barcode')).update(price=price)
        #Decode.objects.filter(barcode=validated_data.get(u'barcode')).update(vendor_id=vendor_id)
        #Barcode.objects.filter(barcode=validated_data.get(u'barcode'))
        #validated_data.get(u'barcode')

        
            
        
        return validated_data

