from rest_framework import serializers
from provider.models import Factory, Retail, Entrepreneur


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['id', 'title', 'email', 'country', 'city', 'street', 'building', 'product_name', 'product_model',
                  'date_created', 'debts', 'time_created']


class FactoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['id', 'title', 'email', 'country', 'city', 'street', 'building', 'product_name', 'product_model',
                  'date_created', 'debts', 'time_created']
        read_only_fields = ['debts']


class RetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = '__all__'


class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'
