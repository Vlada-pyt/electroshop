from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from provider.models import Supplier
from provider.permissions import IsEmployeeActive
from provider.serializers import FactorySerializer, FactoryUpdateSerializer


class SupplierCreateApiView(generics.CreateAPIView):
    serializer_class = FactorySerializer
    permission_classes = (IsEmployeeActive,)


class SupplierListApiView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = (IsEmployeeActive,)


class SupplierAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = Supplier
    serializer_class = FactoryUpdateSerializer
    permission_classes = (IsEmployeeActive,)

    def get_queryset(self):
        return Supplier.objects.all()


