from django.urls import path, include
# from rest_framework.routers import SimpleRouter
# from provider.views import FactoryViewSet, RetailViewSet, EntrepreneurViewSet, SupplierViewSet
from provider.views import SupplierCreateApiView, SupplierListApiView, SupplierAPIView

urlpatterns = [
    path('create', SupplierCreateApiView.as_view(), name='create-supplier'),
    path('list', SupplierListApiView.as_view(), name='supplier-list'),
    path('supplier/<int:pk>', SupplierAPIView.as_view(), name='supplier')]
