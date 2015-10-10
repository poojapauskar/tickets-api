from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from vendor_register import views

urlpatterns = [
    url(r'^vendor_register/$', views.Vendor_registerList.as_view()),
    url(r'^vendor_register/(?P<pk>[0-9]+)/$', views.Vendor_registerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)