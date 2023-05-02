
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers





urlpatterns = [
    path("admin/", admin.site.urls),
    path("eshop/", include("provider.urls")),
    # path("elshop/factory", FactoryViewSet.as_view({'get': 'list'})),
    # path("elshop/retail", RetailViewSet.as_view({'get': 'list'})),
    # path("elshop/entrep", EntrepreneurViewSet.as_view({'get': 'list'})),
]


