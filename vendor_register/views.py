from vendor_register.models import Vendor_register
from vendor_register.serializers import Vendor_registerSerializer
from rest_framework import generics


class Vendor_registerList(generics.ListCreateAPIView):
    queryset = Vendor_register.objects.all()
    serializer_class = Vendor_registerSerializer


class Vendor_registerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor_register.objects.all()
    serializer_class = Vendor_registerSerializer