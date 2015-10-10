from rest_framework import serializers
import random
from random import randint
from barcode.models import Barcode, LANGUAGE_CHOICES, STYLE_CHOICES


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
#I"ll be generating code39 barcodes, others are available
from reportlab.graphics.barcode import code39

class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ('pk', 'vendor_id', 'price','barcode','ref_no')    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #Barcode.objects.create(**validated_data)
        # vendor_id = validated_data.pop('vendor_id')
        # barcode_string = validated_data.pop('barcode_string')
        # price = validated_data.pop('price')
        
        barcode_string=str(random.randint(100000, 999999))
        ref_string=str(random.randint(100, 999))

        ref_no =validated_data.get(u'vendor_id').replace(validated_data.get(u'vendor_id')[:3], '')+""+ref_string
        barcode=barcode_string
        #Barcode.objects.filter(vendor_id=validated_data.get(u'vendor_id')).update(ref_no=validated_data.get(u'vendor_id').replace(validated_data.get(u'vendor_id')[:3], '')+""+ref_string)
        #Barcode.objects.filter(vendor_id=validated_data.get(u'vendor_id')).update(barcode=barcode_string)
        

        objects= Barcode.objects.create(vendor_id=validated_data.get(u'vendor_id'),price=validated_data.get(u'price'),barcode=barcode,ref_no=ref_no)

        # generate a canvas (A4 in this case, size doesn"t really matter)
        c=canvas.Canvas("/tmp/barcode.pdf",pagesize=A4)
        # create a barcode object
        # (is not displayed yet)
        # The encode text is "123456789"
        # barHeight encodes how high the bars will be
        # barWidth encodes how wide the "narrowest" barcode unit is
        barcode=code39.Extended39(barcode_string,barWidth=0.5*mm,barHeight=20*mm)
        # drawOn puts the barcode on the canvas at the specified coordinates
        barcode.drawOn(c,100*mm,100*mm)

        c.drawString(100, 100, validated_data.get(u'vendor_id').replace(validated_data.get(u'vendor_id')[:3], '')+""+ref_string)
        # now create the actual PDF
        c.showPage()
        c.save()



       
        return objects
