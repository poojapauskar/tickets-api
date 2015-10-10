from decode.models import Decode
from decode.serializers import DecodeSerializer
from rest_framework import generics


class DecodeList(generics.ListCreateAPIView):
    queryset = Decode.objects.all()
    serializer_class = DecodeSerializer

