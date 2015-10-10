from barcode.models import Barcode
from barcode.serializers import BarcodeSerializer
from rest_framework import generics


class BarcodeList(generics.ListCreateAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer


class BarcodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer