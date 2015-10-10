from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from barcode import views

urlpatterns = [
    url(r'^barcode/$', views.BarcodeList.as_view()),
    url(r'^barcode/(?P<pk>[0-9]+)/$', views.BarcodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)